#!/usr/bin/env python3
"""
Agent Detection System
Scans codebase to determine which agents should be enabled.
"""

import os
import json
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import Counter
import subprocess


class AgentDetector:
    """Detects relevant agents based on codebase analysis."""

    # Always enabled for ANY codebase
    DEFAULT_AGENTS = [
        "data-agent",
        "logic-agent",
        "test-agent",
        "security-agent",
        "infra-agent",
        "doc-agent"
    ]

    # Patterns that trigger optional agents
    OPTIONAL_AGENT_TRIGGERS = {
        "performance-agent": {
            "file_patterns": ["*/api/*", "*/backend/*", "*/pipeline/*"],
            "file_types": [".go", ".rs", ".cpp"],
            "keywords": ["performance", "optimization", "profiling", "benchmark"],
            "min_files": 10,
            "description": "Detected API/backend services or performance-critical code"
        },
        "refactor-agent": {
            "indicators": ["high_duplication", "large_files", "complex_functions"],
            "min_files": 50,
            "description": "Detected mature codebase that could benefit from refactoring"
        },
        "observability-agent": {
            "file_patterns": ["*/logging/*", "*/monitoring/*", "*/metrics/*"],
            "keywords": ["logger", "metrics", "trace", "span", "observability"],
            "frameworks": ["prometheus", "datadog", "newrelic", "sentry"],
            "description": "Detected observability or distributed systems patterns"
        },
        "research-agent": {
            "tech_indicators": ["ml", "ai", "pytorch", "tensorflow", "transformers"],
            "min_deps": 20,
            "description": "Detected fast-moving tech stack (AI/ML)"
        },
        "devex-agent": {
            "indicators": ["multiple_contributors", "active_prs"],
            "min_contributors": 3,
            "description": "Detected team-scale repository"
        },
        "ux-accessibility-agent": {
            "file_patterns": ["*/components/*", "*/ui/*", "*/pages/*"],
            "frameworks": ["react", "vue", "angular", "svelte"],
            "file_types": [".jsx", ".tsx", ".vue"],
            "description": "Detected frontend/UI project"
        },
        "error-handling-agent": {
            "indicators": ["production_code", "error_patterns"],
            "keywords": ["try", "catch", "error", "exception", "handle"],
            "description": "Detected production codebase"
        },
        "dependency-agent": {
            "files": ["package.json", "requirements.txt", "Cargo.toml", "go.mod", "Gemfile"],
            "min_deps": 10,
            "description": "Detected package manager with dependencies"
        },
        "build-agent": {
            "files": [".github/workflows", ".gitlab-ci.yml", "Jenkinsfile", ".circleci"],
            "keywords": ["ci", "cd", "pipeline", "workflow"],
            "description": "Detected CI/CD pipelines"
        },
        "cost-agent": {
            "file_patterns": ["*/cloud/*", "*/aws/*", "*/gcp/*", "*/azure/*"],
            "files": ["serverless.yml", "lambda", "function"],
            "keywords": ["serverless", "lambda", "cloud", "aws", "gcp"],
            "description": "Detected cloud/serverless infrastructure"
        },
        "knowledge-agent": {
            "indicators": ["active_docs", "wiki"],
            "file_patterns": ["*/docs/*", "*/wiki/*"],
            "description": "Detected documentation system"
        },
        "ethics-compliance-agent": {
            "keywords": ["gdpr", "hipaa", "pci", "compliance", "privacy", "regulation"],
            "file_patterns": ["*/compliance/*", "*/legal/*"],
            "description": "Detected compliance requirements"
        },
        "benchmark-agent": {
            "file_patterns": ["*/benchmark/*", "*/perf/*"],
            "keywords": ["benchmark", "performance", "profiling"],
            "description": "Detected benchmark or performance testing"
        },
        "security-redteam-agent": {
            "indicators": ["customer_facing", "public_api"],
            "keywords": ["api", "endpoint", "public", "external"],
            "description": "Detected customer-facing or public services"
        }
    }

    def __init__(self, repo_path: str):
        self.repo_path = Path(repo_path).resolve()
        self.detected_languages = Counter()
        self.detected_frameworks = set()
        self.detected_patterns = set()
        self.file_count = 0
        self.line_count = 0
        self.contributors = 0

    def detect(self) -> Tuple[List[str], Dict[str, str]]:
        """
        Detect which agents should be enabled.

        Returns:
            Tuple of (enabled_agents, reasons)
        """
        print("🔍 Scanning codebase for agent requirements...")

        # Run all detection methods
        self._detect_languages()
        self._detect_frameworks()
        self._detect_patterns()
        self._detect_structure()
        self._detect_git_activity()

        # Start with default agents
        enabled_agents = self.DEFAULT_AGENTS.copy()
        reasons = {
            agent: "Default agent (enabled for all codebases)"
            for agent in self.DEFAULT_AGENTS
        }

        # Check each optional agent
        for agent, triggers in self.OPTIONAL_AGENT_TRIGGERS.items():
            should_enable, reason = self._should_enable_agent(agent, triggers)
            if should_enable:
                enabled_agents.append(agent)
                reasons[agent] = reason

        return enabled_agents, reasons

    def _detect_languages(self):
        """Detect programming languages used."""
        extensions = {
            ".py": "Python",
            ".js": "JavaScript",
            ".ts": "TypeScript",
            ".jsx": "React",
            ".tsx": "React TypeScript",
            ".java": "Java",
            ".go": "Go",
            ".rs": "Rust",
            ".rb": "Ruby",
            ".php": "PHP",
            ".cpp": "C++",
            ".c": "C",
            ".cs": "C#",
            ".swift": "Swift",
            ".kt": "Kotlin"
        }

        for ext, lang in extensions.items():
            files = list(self.repo_path.rglob(f"*{ext}"))
            if files:
                self.detected_languages[lang] += len(files)

    def _detect_frameworks(self):
        """Detect frameworks and libraries used."""
        # Check package files
        checks = {
            "package.json": self._check_package_json,
            "requirements.txt": self._check_requirements_txt,
            "Gemfile": self._check_gemfile,
            "go.mod": self._check_go_mod,
            "Cargo.toml": self._check_cargo_toml,
            "composer.json": self._check_composer_json
        }

        for filename, check_func in checks.items():
            file_path = self.repo_path / filename
            if file_path.exists():
                check_func(file_path)

    def _check_package_json(self, file_path: Path):
        """Check Node.js dependencies."""
        try:
            with open(file_path) as f:
                data = json.load(f)

            deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}

            framework_indicators = {
                "react": "react", "vue": "vue", "angular": "@angular",
                "express": "express", "next": "next", "nest": "@nestjs",
                "fastify": "fastify", "koa": "koa"
            }

            for fw, indicator in framework_indicators.items():
                if any(indicator in dep for dep in deps):
                    self.detected_frameworks.add(fw)

        except Exception:
            pass

    def _check_requirements_txt(self, file_path: Path):
        """Check Python dependencies."""
        try:
            with open(file_path) as f:
                deps = f.read().lower()

            framework_indicators = [
                "django", "flask", "fastapi", "pytorch", "tensorflow",
                "pandas", "numpy", "scikit", "keras", "transformers"
            ]

            for fw in framework_indicators:
                if fw in deps:
                    self.detected_frameworks.add(fw)

        except Exception:
            pass

    def _check_gemfile(self, file_path: Path):
        """Check Ruby dependencies."""
        try:
            with open(file_path) as f:
                deps = f.read().lower()

            if "rails" in deps:
                self.detected_frameworks.add("rails")
            if "sinatra" in deps:
                self.detected_frameworks.add("sinatra")

        except Exception:
            pass

    def _check_go_mod(self, file_path: Path):
        """Check Go dependencies."""
        try:
            with open(file_path) as f:
                deps = f.read().lower()

            framework_indicators = ["gin", "echo", "fiber", "gorilla"]

            for fw in framework_indicators:
                if fw in deps:
                    self.detected_frameworks.add(fw)

        except Exception:
            pass

    def _check_cargo_toml(self, file_path: Path):
        """Check Rust dependencies."""
        try:
            with open(file_path) as f:
                deps = f.read().lower()

            framework_indicators = ["actix", "rocket", "warp", "tokio"]

            for fw in framework_indicators:
                if fw in deps:
                    self.detected_frameworks.add(fw)

        except Exception:
            pass

    def _check_composer_json(self, file_path: Path):
        """Check PHP dependencies."""
        try:
            with open(file_path) as f:
                data = json.load(f)

            deps = {**data.get("require", {}), **data.get("require-dev", {})}

            if "laravel/framework" in deps:
                self.detected_frameworks.add("laravel")
            if "symfony/symfony" in deps:
                self.detected_frameworks.add("symfony")

        except Exception:
            pass

    def _detect_patterns(self):
        """Detect code patterns and keywords."""
        # Search for specific patterns
        patterns_to_check = [
            ("api", ["*/api/*", "*/routes/*", "*/endpoints/*"]),
            ("database", ["*/models/*", "*/db/*", "*/database/*"]),
            ("testing", ["*/tests/*", "*/test/*", "*/__tests__/*"]),
            ("frontend", ["*/components/*", "*/views/*", "*/pages/*"]),
            ("ml", ["*/models/*", "*/training/*", "*/inference/*"])
        ]

        for pattern_name, paths in patterns_to_check:
            for path_pattern in paths:
                if list(self.repo_path.glob(path_pattern)):
                    self.detected_patterns.add(pattern_name)
                    break

    def _detect_structure(self):
        """Detect repository structure metrics."""
        # Count files and lines
        for file_path in self.repo_path.rglob("*"):
            if file_path.is_file() and not self._should_ignore(file_path):
                self.file_count += 1

                # Try to count lines
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        self.line_count += sum(1 for _ in f)
                except Exception:
                    pass

    def _detect_git_activity(self):
        """Detect Git repository activity."""
        try:
            # Get contributor count
            result = subprocess.run(
                ["git", "log", "--format=%ae"],
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                timeout=5
            )

            if result.returncode == 0:
                emails = set(result.stdout.strip().split('\n'))
                self.contributors = len(emails)

        except Exception:
            pass

    def _should_ignore(self, file_path: Path) -> bool:
        """Check if file should be ignored."""
        ignore_patterns = [
            ".git", "node_modules", "__pycache__", ".pytest_cache",
            "venv", "env", ".venv", "dist", "build", ".next",
            ".cache", "coverage", ".DS_Store"
        ]

        return any(pattern in str(file_path) for pattern in ignore_patterns)

    def _should_enable_agent(
        self, agent: str, triggers: Dict
    ) -> Tuple[bool, str]:
        """Determine if an agent should be enabled based on triggers."""

        # Check file patterns
        if "file_patterns" in triggers:
            for pattern in triggers["file_patterns"]:
                if list(self.repo_path.glob(pattern)):
                    return True, triggers.get("description", "Pattern match")

        # Check file types
        if "file_types" in triggers:
            for ext in triggers["file_types"]:
                if list(self.repo_path.rglob(f"*{ext}")):
                    return True, triggers.get("description", "File type match")

        # Check specific files
        if "files" in triggers:
            for filename in triggers["files"]:
                file_path = self.repo_path / filename
                if file_path.exists() or list(self.repo_path.rglob(filename)):
                    return True, triggers.get("description", "Required file found")

        # Check frameworks
        if "frameworks" in triggers:
            if any(fw in self.detected_frameworks for fw in triggers["frameworks"]):
                return True, triggers.get("description", "Framework detected")

        # Check keywords in codebase
        if "keywords" in triggers:
            # This is a simplified check - in production, you'd scan file contents
            # For now, just check if framework/pattern suggests keywords
            for keyword in triggers["keywords"]:
                if keyword in str(self.detected_frameworks).lower():
                    return True, triggers.get("description", "Keyword match")

        # Check tech indicators
        if "tech_indicators" in triggers:
            if any(tech in str(self.detected_frameworks).lower()
                   for tech in triggers["tech_indicators"]):
                return True, triggers.get("description", "Tech stack match")

        # Check minimum file count
        if "min_files" in triggers:
            if self.file_count >= triggers["min_files"]:
                # Additional validation for specific triggers
                if agent == "refactor-agent":
                    return True, "Large codebase detected (refactoring recommended)"

        # Check minimum contributors
        if "min_contributors" in triggers:
            if self.contributors >= triggers["min_contributors"]:
                return True, triggers.get("description", "Team repository")

        # Check custom indicators
        if "indicators" in triggers:
            indicators = triggers["indicators"]

            if "production_code" in indicators:
                # Check for production indicators
                if (self.repo_path / "Dockerfile").exists() or \
                   (self.repo_path / ".github" / "workflows").exists():
                    return True, triggers.get("description", "Production code")

            if "customer_facing" in indicators or "public_api" in indicators:
                # Check for API indicators
                if "api" in self.detected_patterns:
                    return True, triggers.get("description", "Public API detected")

            if "multiple_contributors" in indicators:
                if self.contributors >= 3:
                    return True, triggers.get("description", "Team repository")

        return False, ""

    def generate_report(
        self, enabled_agents: List[str], reasons: Dict[str, str]
    ) -> str:
        """Generate detection report."""
        report = ["🔍 Codebase Analysis Report", "=" * 50, ""]

        # Languages
        report.append("📝 Languages Detected:")
        for lang, count in self.detected_languages.most_common():
            report.append(f"  - {lang}: {count} files")
        report.append("")

        # Frameworks
        if self.detected_frameworks:
            report.append("🛠️  Frameworks Detected:")
            for fw in sorted(self.detected_frameworks):
                report.append(f"  - {fw}")
            report.append("")

        # Patterns
        if self.detected_patterns:
            report.append("🔎 Patterns Detected:")
            for pattern in sorted(self.detected_patterns):
                report.append(f"  - {pattern}")
            report.append("")

        # Metrics
        report.append("📊 Repository Metrics:")
        report.append(f"  - Files: {self.file_count}")
        report.append(f"  - Lines: {self.line_count:,}")
        report.append(f"  - Contributors: {self.contributors}")
        report.append("")

        # Enabled agents
        report.append("🤖 Enabled Agents:")
        report.append("")

        # Default agents
        report.append("  Default Agents (always enabled):")
        for agent in self.DEFAULT_AGENTS:
            report.append(f"    ✅ {agent}")
        report.append("")

        # Optional agents
        optional = [a for a in enabled_agents if a not in self.DEFAULT_AGENTS]
        if optional:
            report.append("  Optional Agents (detected):")
            for agent in optional:
                report.append(f"    ✅ {agent}")
                report.append(f"       → {reasons.get(agent, 'N/A')}")
        report.append("")

        # Suggested agents (not auto-enabled)
        report.append("  💡 Agents you might want to consider:")
        all_optional = set(self.OPTIONAL_AGENT_TRIGGERS.keys())
        not_enabled = all_optional - set(optional)
        for agent in sorted(not_enabled):
            desc = self.OPTIONAL_AGENT_TRIGGERS[agent].get("description", "")
            report.append(f"    ⭕ {agent}")
            if desc:
                report.append(f"       → {desc}")
        report.append("")

        return "\n".join(report)


def main():
    """CLI for agent detection."""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python agent_detector.py <repo_path>")
        sys.exit(1)

    repo_path = sys.argv[1]
    detector = AgentDetector(repo_path)

    enabled_agents, reasons = detector.detect()
    report = detector.generate_report(enabled_agents, reasons)

    print(report)

    # Output JSON for programmatic use
    if "--json" in sys.argv:
        output = {
            "enabled_agents": enabled_agents,
            "reasons": reasons,
            "languages": dict(detector.detected_languages),
            "frameworks": list(detector.detected_frameworks),
            "patterns": list(detector.detected_patterns),
            "metrics": {
                "files": detector.file_count,
                "lines": detector.line_count,
                "contributors": detector.contributors
            }
        }
        print("\n" + json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
