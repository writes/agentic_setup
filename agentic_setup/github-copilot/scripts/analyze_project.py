#!/usr/bin/env python3
"""
Project Analyzer for GitHub Copilot Agent Setup
Scans codebase to detect languages, frameworks, and patterns.
Recommends which agents to enable for optimal Copilot performance.
"""

import os
import json
from pathlib import Path
from typing import Dict, List, Tuple
from collections import Counter


class CopilotProjectAnalyzer:
    """Analyze project for GitHub Copilot agent configuration."""

    def __init__(self, repo_path: str):
        self.repo_path = Path(repo_path).resolve()
        self.detected_languages = Counter()
        self.detected_frameworks = set()
        self.detected_patterns = set()
        self.file_count = 0

    def analyze(self) -> Dict:
        """Run complete project analysis."""
        print("🔍 Analyzing project for GitHub Copilot Agent setup...")

        self._detect_languages()
        self._detect_frameworks()
        self._detect_patterns()

        recommended_agents = self._recommend_agents()

        analysis = {
            "project_path": str(self.repo_path),
            "languages": dict(self.detected_languages),
            "frameworks": list(self.detected_frameworks),
            "patterns": list(self.detected_patterns),
            "file_count": self.file_count,
            "recommended_agents": recommended_agents
        }

        # Save analysis
        output_dir = self.repo_path / ".copilot"
        output_dir.mkdir(exist_ok=True)

        output_file = output_dir / "analysis.json"
        with open(output_file, 'w') as f:
            json.dump(analysis, f, indent=2)

        self._print_report(analysis)

        return analysis

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
            ".php": "PHP"
        }

        for ext, lang in extensions.items():
            files = list(self.repo_path.rglob(f"*{ext}"))
            if files:
                self.detected_languages[lang] += len(files)
                self.file_count += len(files)

    def _detect_frameworks(self):
        """Detect frameworks and libraries."""
        # Check package files
        checks = [
            ("package.json", self._check_package_json),
            ("requirements.txt", self._check_requirements),
            ("Gemfile", self._check_gemfile),
            ("go.mod", self._check_go_mod)
        ]

        for filename, check_func in checks:
            file_path = self.repo_path / filename
            if file_path.exists():
                check_func(file_path)

    def _check_package_json(self, file_path: Path):
        """Check Node.js dependencies."""
        try:
            with open(file_path) as f:
                data = json.load(f)

            deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}

            frameworks = {
                "react": "React", "vue": "Vue", "angular": "@angular",
                "express": "Express", "fastify": "Fastify",
                "next": "Next.js", "nest": "NestJS"
            }

            for key, name in frameworks.items():
                if any(key in dep for dep in deps):
                    self.detected_frameworks.add(name)
        except Exception:
            pass

    def _check_requirements(self, file_path: Path):
        """Check Python dependencies."""
        try:
            with open(file_path) as f:
                deps = f.read().lower()

            frameworks = ["django", "flask", "fastapi", "pytorch", "tensorflow"]

            for fw in frameworks:
                if fw in deps:
                    self.detected_frameworks.add(fw.title())
        except Exception:
            pass

    def _check_gemfile(self, file_path: Path):
        """Check Ruby dependencies."""
        try:
            with open(file_path) as f:
                deps = f.read().lower()

            if "rails" in deps:
                self.detected_frameworks.add("Rails")
        except Exception:
            pass

    def _check_go_mod(self, file_path: Path):
        """Check Go dependencies."""
        try:
            with open(file_path) as f:
                deps = f.read().lower()

            frameworks = ["gin", "echo", "fiber"]

            for fw in frameworks:
                if fw in deps:
                    self.detected_frameworks.add(fw.title())
        except Exception:
            pass

    def _detect_patterns(self):
        """Detect project patterns."""
        patterns_to_check = [
            ("api", ["*/api/*", "*/routes/*", "*/endpoints/*"]),
            ("frontend", ["*/components/*", "*/views/*", "*/pages/*"]),
            ("tests", ["*/tests/*", "*/test/*", "*/__tests__/*"]),
            ("database", ["*/models/*", "*/db/*", "*/migrations/*"]),
            ("ci_cd", [".github/workflows/*", ".gitlab-ci.yml"]),
            ("docker", ["Dockerfile", "docker-compose.yml"])
        ]

        for pattern_name, paths in patterns_to_check:
            for path_pattern in paths:
                if list(self.repo_path.glob(path_pattern)):
                    self.detected_patterns.add(pattern_name)
                    break

    def _recommend_agents(self) -> Dict[str, List[str]]:
        """Recommend agents based on detection."""
        # Core agents (always enabled)
        core_agents = [
            "Security Agent",
            "Logic Agent",
            "Test Agent",
            "Doc Agent",
            "Data Agent",
            "Infrastructure Agent"
        ]

        optional_agents = []

        # Performance Agent for APIs and performance-critical code
        if ("api" in self.detected_patterns or
            "backend" in str(self.repo_path).lower() or
            any(fw in self.detected_frameworks for fw in ["FastAPI", "Flask", "Express", "Fastify"])):
            optional_agents.append("Performance Agent")

        # Refactor Agent for mature codebases
        if self.file_count > 50:
            optional_agents.append("Refactor Agent")

        # Observability Agent for distributed systems
        if ("api" in self.detected_patterns and "docker" in self.detected_patterns) or \
           any(fw in str(self.detected_frameworks) for fw in ["prometheus", "datadog"]):
            optional_agents.append("Observability Agent")

        # Research Agent for fast-moving tech (AI/ML)
        if any(fw in self.detected_frameworks for fw in ["Pytorch", "Tensorflow", "Transformers"]):
            optional_agents.append("Research Agent")

        # DevEx Agent for team repositories
        if self._is_team_repo():
            optional_agents.append("DevEx Agent")

        # UX/Accessibility Agent for frontends
        if "frontend" in self.detected_patterns or \
           any(fw in self.detected_frameworks for fw in ["React", "Vue", "Angular", "Next.js"]):
            optional_agents.append("UX/Accessibility Agent")

        # Error Handling Agent for production code
        if self.file_count > 20:
            optional_agents.append("Error Handling Agent")

        # Dependency Agent for projects with package managers
        dep_files = ["package.json", "requirements.txt", "Cargo.toml", "go.mod", "Gemfile"]
        if any((self.repo_path / f).exists() for f in dep_files):
            optional_agents.append("Dependency Agent")

        # Build/CI Agent for projects with CI/CD
        if "ci_cd" in self.detected_patterns:
            optional_agents.append("Build Agent")

        # Cost Agent for cloud/serverless projects
        cloud_indicators = ["serverless.yml", "lambda", ".aws", "terraform"]
        if any((self.repo_path / f).exists() for f in cloud_indicators) or \
           "serverless" in str(self.detected_frameworks).lower():
            optional_agents.append("Cost Optimization Agent")

        # Knowledge Agent for projects with active docs
        docs_paths = ["docs/", "wiki/", "documentation/"]
        if any((self.repo_path / d).exists() for d in docs_paths):
            optional_agents.append("Knowledge Agent")

        # Ethics/Compliance Agent for regulated industries
        compliance_keywords = ["compliance", "hipaa", "gdpr", "legal"]
        if any((self.repo_path / d).exists() for d in compliance_keywords):
            optional_agents.append("Ethics & Compliance Agent")

        # Benchmark Agent for performance testing
        if "benchmark" in str(self.detected_patterns).lower():
            optional_agents.append("Benchmark Agent")

        # Security Red Team Agent for public-facing services
        if "api" in self.detected_patterns:
            optional_agents.append("Security Red Team Agent")

        return {
            "core": core_agents,
            "optional": optional_agents
        }

    def _is_team_repo(self) -> bool:
        """Check if this is a team repository."""
        try:
            import subprocess
            result = subprocess.run(
                ["git", "shortlog", "-sn"],
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                timeout=5
            )
            contributors = len(result.stdout.strip().split("\n"))
            return contributors >= 3
        except Exception:
            return False

    def _print_report(self, analysis: Dict):
        """Print analysis report."""
        print("\n" + "="*50)
        print("🔍 Project Analysis Complete")
        print("="*50)

        print("\n📝 Languages Detected:")
        for lang, count in self.detected_languages.most_common():
            print(f"  - {lang}: {count} files")

        if self.detected_frameworks:
            print("\n🛠️  Frameworks Detected:")
            for fw in sorted(self.detected_frameworks):
                print(f"  - {fw}")

        if self.detected_patterns:
            print("\n🔎 Patterns Detected:")
            for pattern in sorted(self.detected_patterns):
                print(f"  - {pattern}")

        print("\n🤖 Recommended Agents:")
        print("\n  Core Agents (always enabled):")
        for agent in analysis["recommended_agents"]["core"]:
            print(f"    ✅ {agent}")

        if analysis["recommended_agents"]["optional"]:
            print("\n  Optional Agents (detected):")
            for agent in analysis["recommended_agents"]["optional"]:
                print(f"    ✅ {agent}")

        print(f"\n📁 Analysis saved to: .copilot/analysis.json")
        print("\nNext step: Run setup_copilot_agents.py to install configuration")


def main():
    """CLI entry point."""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python analyze_project.py <repo_path>")
        sys.exit(1)

    repo_path = sys.argv[1]
    analyzer = CopilotProjectAnalyzer(repo_path)
    analyzer.analyze()


if __name__ == "__main__":
    main()
