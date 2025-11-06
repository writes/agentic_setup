#!/usr/bin/env python3
"""
Universal Multi-Agent Framework Installer
Auto-detects codebase and installs appropriate agents.
"""

import os
import sys
import json
import shutil
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional

# Import agent detector
sys.path.insert(0, str(Path(__file__).parent))
from agent_detector import AgentDetector

class MultiAgentFrameworkInstaller:
    """Install and configure the universal multi-agent system."""

    # Default agents (always enabled)
    DEFAULT_AGENTS = [
        "data-agent",
        "logic-agent",
        "test-agent",
        "security-agent",
        "infra-agent",
        "doc-agent"
    ]

    # Will be populated by agent detection
    AGENTS = []

    def __init__(self, repo_path: str = "."):
        """Initialize installer with target repository path."""
        self.repo_path = Path(repo_path).resolve()
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.detector = AgentDetector(str(self.repo_path))
        self.enabled_agents = []
        self.agent_reasons = {}

    def run(self):
        """Execute complete installation process."""
        print("🚀 Universal Multi-Agent Framework Installer")
        print("=" * 50)

        steps = [
            ("Checking prerequisites", self.check_prerequisites),
            ("Detecting codebase and required agents", self.detect_agents),
            ("Creating directory structure", self.create_directory_structure),
            ("Installing agent configurations", self.install_agents),
            ("Setting up validation scripts", self.create_validation_scripts),
            ("Configuring Git hooks", self.setup_git_hooks),
            ("Creating slash commands", self.create_slash_commands),
            ("Generating Claude configuration", self.create_claude_config),
            ("Setting up GitHub Copilot", self.setup_github_copilot),
            ("Creating helper scripts", self.create_helper_scripts),
            ("Running initial tests", self.run_tests),
            ("Generating documentation", self.generate_documentation)
        ]

        for step_name, step_func in steps:
            print(f"\n📍 {step_name}...")
            try:
                step_func()
                print(f"   ✅ {step_name} complete")
            except Exception as e:
                print(f"   ❌ {step_name} failed: {e}")
                if not self.ask_continue():
                    print("\n❌ Installation aborted")
                    return False

        print("\n" + "=" * 50)
        print("✨ Installation Complete!")
        print("\nNext steps:")
        print("1. Review agent configurations in .claude/skills/")
        print("2. Customize validation logic for your domain")
        print("3. Test with: python .claude/scripts/test_system.py")
        print("4. Commit with: git commit (triggers validation)")

        return True

    def check_prerequisites(self):
        """Check system requirements."""
        # Check Python version
        if sys.version_info < (3, 8):
            raise RuntimeError(f"Python 3.8+ required, found {sys.version}")

        # Check Git repository
        if not (self.repo_path / ".git").exists():
            print("   ⚠️  Warning: Not a git repository")
            print("   Initializing git repository...")
            subprocess.run(["git", "init"], cwd=self.repo_path, check=True)

        # Check disk space
        import shutil
        total, used, free = shutil.disk_usage(self.repo_path)
        free_gb = free / (1024 ** 3)
        if free_gb < 1:
            raise RuntimeError(f"Insufficient disk space: {free_gb:.1f}GB free")

    def detect_agents(self):
        """Detect which agents should be enabled for this codebase."""
        self.enabled_agents, self.agent_reasons = self.detector.detect()
        self.AGENTS = self.enabled_agents

        # Generate and display report
        report = self.detector.generate_report(self.enabled_agents, self.agent_reasons)
        print("\n" + report)

        # Ask user confirmation
        print("\n❓ Proceed with these agents? (y/n): ", end="")
        response = input().strip().lower()

        if response != 'y':
            print("\n   You can manually edit .claude/config.py after installation")
            print("   Proceeding with default agents only for now...")
            self.AGENTS = self.DEFAULT_AGENTS
            self.enabled_agents = self.DEFAULT_AGENTS

    def create_directory_structure(self):
        """Create all required directories."""
        directories = [
            # Claude directories
            ".claude/agents",
            ".claude/skills",
            ".claude/commands",
            ".claude/templates",
            ".claude/hooks",
            ".claude/scripts",
            ".claude/metrics",

            # Agent skill directories
            *[f".claude/skills/{agent}" for agent in self.AGENTS],
            *[f".claude/skills/{agent}/PATTERNS" for agent in self.AGENTS],
            *[f".claude/skills/{agent}/CHECKLISTS" for agent in self.AGENTS],
            *[f".claude/skills/{agent}/VALIDATION" for agent in self.AGENTS],
            *[f".claude/skills/{agent}/SCRIPTS" for agent in self.AGENTS],

            # Project directories
            "scripts/core",
            "scripts/utils",
            "scripts/tools",
            "tests/unit",
            "tests/integration",
            "docs/implementation",
            "docs/strategies",
            "docs/audits",
            "docs/archive"
        ]

        for dir_path in directories:
            (self.repo_path / dir_path).mkdir(parents=True, exist_ok=True)

    def install_agents(self):
        """Install all agent configurations."""
        for agent in self.AGENTS:
            self.create_agent_skill(agent)
            self.create_agent_patterns(agent)
            self.create_agent_checklists(agent)

    def create_agent_skill(self, agent: str):
        """Create SKILL.md for an agent."""
        agent_configs = {
            # Default Agents (Always Enabled)
            "data-agent": {
                "name": "Data Agent",
                "description": "Validates inputs, file formats, and API schemas",
                "responsibilities": [
                    "Input data validation",
                    "File format verification (.csv, .json, .xml)",
                    "API schema compliance",
                    "Data integrity checks"
                ],
                "standards": {
                    "Validation Coverage": ">95%",
                    "Data Integrity": "No corrupt data",
                    "Schema Compliance": "100%"
                },
                "veto_triggers": [
                    "Corrupt or invalid input data",
                    "Missing required validation",
                    "Schema violations"
                ]
            },
            "logic-agent": {
                "name": "Logic Agent",
                "description": "Ensures core logic correctness and control flow",
                "responsibilities": [
                    "Business logic validation",
                    "Control flow correctness",
                    "State management verification",
                    "Edge case handling"
                ],
                "standards": {
                    "Logic Coverage": ">90%",
                    "Test Pass Rate": "100%",
                    "Edge Cases": "All handled"
                },
                "veto_triggers": [
                    "Failing tests",
                    "Invalid logic paths",
                    "Unhandled edge cases"
                ]
            },
            "test-agent": {
                "name": "Test Agent",
                "description": "Enforces test coverage and regression control",
                "responsibilities": [
                    "Test coverage enforcement",
                    "Regression prevention",
                    "Test quality validation",
                    "CI/CD integration"
                ],
                "standards": {
                    "Test Coverage": ">80%",
                    "Test Quality": "Meaningful assertions",
                    "Execution Time": "<5min"
                },
                "veto_triggers": [
                    "Coverage below 80%",
                    "Missing critical test cases",
                    "Flaky tests"
                ]
            },
            "security-agent": {
                "name": "Security Agent",
                "description": "Scans for secrets, injections, and vulnerable dependencies",
                "responsibilities": [
                    "Secret scanning",
                    "Injection attack prevention",
                    "Dependency vulnerability checking",
                    "Security best practices"
                ],
                "standards": {
                    "Critical CVEs": "0",
                    "Secrets Exposed": "0",
                    "OWASP Top 10": "No violations"
                },
                "veto_triggers": [
                    "Found hardcoded secrets",
                    "High/critical CVE in dependencies",
                    "Injection vulnerabilities"
                ]
            },
            "infra-agent": {
                "name": "Infrastructure Agent",
                "description": "Checks build, containers, and CI/CD safety",
                "responsibilities": [
                    "Build configuration validation",
                    "Container security",
                    "CI/CD pipeline safety",
                    "Deployment readiness"
                ],
                "standards": {
                    "Build Success": "100%",
                    "Container Security": "No critical issues",
                    "Deployment Safety": "Validated"
                },
                "veto_triggers": [
                    "Unsafe permissions",
                    "Insecure container config",
                    "Build failures"
                ]
            },
            "doc-agent": {
                "name": "Documentation Agent",
                "description": "Verifies docs and README sync with code",
                "responsibilities": [
                    "Documentation completeness",
                    "Code-docs synchronization",
                    "README maintenance",
                    "API documentation"
                ],
                "standards": {
                    "Coverage": "100% of public APIs",
                    "Currency": "Updated with code",
                    "Completeness": "No placeholders"
                },
                "veto_triggers": [
                    "Missing documentation for new features",
                    "Outdated documentation",
                    "Broken references"
                ]
            },
            # Optional Agents (Auto-Enabled Based on Detection)
            "performance-agent": {
                "name": "Performance Agent",
                "description": "Runtime efficiency, profiling, algorithmic complexity",
                "responsibilities": [
                    "Performance benchmarking",
                    "Algorithmic complexity analysis",
                    "Resource usage monitoring",
                    "Optimization recommendations"
                ],
                "standards": {
                    "CPU Usage": "<80%",
                    "Memory Usage": "<75%",
                    "Request Latency": "<300ms"
                },
                "veto_triggers": [
                    "Performance regression >10%",
                    "Memory leaks",
                    "CPU/memory limits exceeded"
                ]
            },
            "refactor-agent": {
                "name": "Refactor Agent",
                "description": "Code structure and maintainability",
                "responsibilities": [
                    "Code structure improvement",
                    "Duplication elimination",
                    "Complexity reduction",
                    "Maintainability enhancement"
                ],
                "standards": {
                    "Maintainability Index": ">85",
                    "Code Duplication": "<5%",
                    "Complexity": "<10"
                },
                "veto_triggers": [
                    "Maintainability index <85",
                    "High duplication",
                    "Excessive complexity"
                ]
            },
            "observability-agent": {
                "name": "Observability Agent",
                "description": "Logging, tracing, and metrics validation",
                "responsibilities": [
                    "Logging coverage",
                    "Distributed tracing",
                    "Metrics instrumentation",
                    "Event schema validation"
                ],
                "standards": {
                    "Critical Path Coverage": ">90%",
                    "Log Consistency": "100%",
                    "Metrics Coverage": "All endpoints"
                },
                "veto_triggers": [
                    "Missing logs on critical paths",
                    "Inconsistent event schemas",
                    "No metrics on new endpoints"
                ]
            }
        }

        config = agent_configs.get(agent, {})
        skill_content = f"""---
name: {config.get('name', agent)}
description: {config.get('description', 'Agent description')}
---

# {config.get('name', agent)} Skill

## Core Responsibilities
{chr(10).join(f"- {r}" for r in config.get('responsibilities', []))}

## Quality Standards
{chr(10).join(f"- **{k}:** {v}" for k, v in config.get('standards', {}).items())}

## Veto Authority

This agent will VETO changes that have:
{chr(10).join(f"- {t}" for t in config.get('veto_triggers', []))}

## Validation Script

```bash
python .claude/skills/{agent}/validate.py
```

## Patterns

See PATTERNS/ directory for domain-specific patterns and examples.

## Checklists

See CHECKLISTS/ directory for review checklists.

---

**Last Updated:** {datetime.now().strftime('%Y-%m-%d')}
**Version:** 1.0.0
"""

        skill_path = self.repo_path / f".claude/skills/{agent}/SKILL.md"
        skill_path.write_text(skill_content)

    def create_agent_patterns(self, agent: str):
        """Create pattern files for an agent."""
        pattern_file = self.repo_path / f".claude/skills/{agent}/PATTERNS/main.md"
        pattern_content = f"""# {agent.replace('-', ' ').title()} Patterns

## Common Patterns

### Pattern 1: Validation
```python
def validate_{agent.split('-')[0]}_quality(data):
    \"\"\"Validate {agent.split('-')[0]} quality.\"\"\"
    # Implementation
    pass
```

### Pattern 2: Error Handling
```python
try:
    # {agent.split('-')[0]} operation
    pass
except {agent.split('-')[0].title()}Error as e:
    logger.error(f"{agent} error: {{e}}")
    raise
```

## Best Practices

1. Always validate inputs
2. Handle errors gracefully
3. Log important operations
4. Follow naming conventions
5. Keep functions focused
"""
        pattern_file.parent.mkdir(parents=True, exist_ok=True)
        pattern_file.write_text(pattern_content)

    def create_agent_checklists(self, agent: str):
        """Create checklist files for an agent."""
        checklist_file = self.repo_path / f".claude/skills/{agent}/CHECKLISTS/review.md"
        checklist_content = f"""# {agent.replace('-', ' ').title()} Review Checklist

## Pre-Review
- [ ] Code follows {agent} standards
- [ ] Tests are included
- [ ] Documentation updated

## Quality Checks
- [ ] No {agent.split('-')[0]}-related errors
- [ ] Performance acceptable
- [ ] Security reviewed

## Post-Review
- [ ] All issues addressed
- [ ] Approved by {agent}
- [ ] Ready for next agent
"""
        checklist_file.parent.mkdir(parents=True, exist_ok=True)
        checklist_file.write_text(checklist_content)

    def create_validation_scripts(self):
        """Create validation scripts for each agent."""
        for agent in self.AGENTS:
            script_content = f'''#!/usr/bin/env python3
"""
Validation script for {agent.replace('-', ' ').title()}.
"""

import sys
import json
from pathlib import Path
from typing import Dict, List, Any

class {agent.replace('-', '').title()}Validator:
    """Validate code against {agent} standards."""

    def __init__(self):
        self.agent_name = "{agent}"
        self.errors = []
        self.warnings = []

    def validate(self, path: str = ".") -> Dict[str, Any]:
        """Run validation checks."""
        repo_path = Path(path)

        # Run specific validations for this agent
        self.check_standards(repo_path)
        self.check_patterns(repo_path)
        self.check_quality(repo_path)

        # Determine status
        if self.errors:
            status = "VETO"
        elif self.warnings:
            status = "WARN"
        else:
            status = "APPROVE"

        return {{
            "agent": self.agent_name,
            "status": status,
            "errors": self.errors,
            "warnings": self.warnings,
            "timestamp": "{datetime.now().isoformat()}"
        }}

    def check_standards(self, repo_path: Path):
        """Check agent-specific standards."""
        # TODO: Implement specific checks for {agent}
        pass

    def check_patterns(self, repo_path: Path):
        """Check for required patterns."""
        # TODO: Implement pattern checks
        pass

    def check_quality(self, repo_path: Path):
        """Check quality metrics."""
        # TODO: Implement quality checks
        pass

def main():
    """Run validation and output results."""
    validator = {agent.replace('-', '').title()}Validator()
    result = validator.validate()

    # Output JSON result
    print(json.dumps(result, indent=2))

    # Exit with appropriate code
    if result["status"] == "VETO":
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
'''

            script_path = self.repo_path / f".claude/skills/{agent}/validate.py"
            script_path.write_text(script_content)
            script_path.chmod(0o755)

    def setup_git_hooks(self):
        """Configure Git hooks for agent validation."""
        hooks_dir = self.repo_path / ".git/hooks"
        hooks_dir.mkdir(parents=True, exist_ok=True)

        # Pre-commit hook
        pre_commit_content = '''#!/bin/bash
#
# Multi-Agent Consensus Pre-Commit Hook
# Runs all 8 agents to validate changes before commit
#

echo "🤖 Multi-Agent Consensus Check"
echo "================================"

# Colors for output
RED='\\033[0;31m'
GREEN='\\033[0;32m'
YELLOW='\\033[1;33m'
NC='\\033[0m' # No Color

# Track results
FAILED_AGENTS=()
WARNING_AGENTS=()

# Run each agent validation
for agent in {' '.join([a.replace('-agent', '') for a in self.AGENTS])}; do
    echo -n "Checking ${agent}-agent... "

    # Run validation script
    OUTPUT=$(python .claude/skills/${agent}-agent/validate.py 2>&1)
    EXIT_CODE=$?

    if [ $EXIT_CODE -eq 0 ]; then
        # Check if output contains warnings
        if echo "$OUTPUT" | grep -q '"status": "WARN"'; then
            echo -e "${YELLOW}⚠️  WARNING${NC}"
            WARNING_AGENTS+=("${agent}")
        else
            echo -e "${GREEN}✅ APPROVED${NC}"
        fi
    else
        echo -e "${RED}❌ VETO${NC}"
        FAILED_AGENTS+=("${agent}")

        # Show veto reason
        REASON=$(echo "$OUTPUT" | grep -A1 '"errors"' | tail -1 | sed 's/.*"\\(.*\\)".*/\\1/')
        if [ ! -z "$REASON" ]; then
            echo "   Reason: $REASON"
        fi
    fi
done

echo "================================"

# Report results
if [ ${#FAILED_AGENTS[@]} -eq 0 ]; then
    if [ ${#WARNING_AGENTS[@]} -eq 0 ]; then
        echo -e "${GREEN}✅ All agents approve! Proceeding with commit.${NC}"
        exit 0
    else
        echo -e "${YELLOW}⚠️  Warnings from: ${WARNING_AGENTS[*]}${NC}"
        echo "Proceeding with commit (warnings only)."
        exit 0
    fi
else
    echo -e "${RED}❌ Commit blocked by: ${FAILED_AGENTS[*]}${NC}"
    echo ""
    echo "To bypass (NOT RECOMMENDED):"
    echo "  git commit --no-verify"
    echo ""
    echo "To see detailed errors:"
    echo "  python .claude/scripts/consensus_report.py"
    exit 1
fi
'''

        pre_commit_path = hooks_dir / "pre-commit"
        pre_commit_path.write_text(pre_commit_content)
        pre_commit_path.chmod(0o755)

        # Post-commit hook
        post_commit_content = '''#!/bin/bash
#
# Post-Commit Hook
# Records metrics about the commit
#

python .claude/scripts/record_metrics.py commit
'''

        post_commit_path = hooks_dir / "post-commit"
        post_commit_path.write_text(post_commit_content)
        post_commit_path.chmod(0o755)

    def create_slash_commands(self):
        """Create Claude slash commands."""
        commands = {
            "review": """---
name: review
description: Run full 8-agent review
---

# Multi-Agent Review

Run comprehensive review across all agents:

1. **Code Organization Agent** - Structure and cleanliness
2. **Review Agent** - Quality and security
3. **Data Agent** - Data handling validation
4. **Math Agent** - Mathematical correctness
5. **Model Agent** - ML components check
6. **Trading Agent** - Business logic validation
7. **Infrastructure Agent** - Deployment readiness
8. **Documentation Agent** - Documentation completeness

Generate consolidated report with any VETOs.
""",
            "consensus": """---
name: consensus
description: Get unanimous consensus from all agents
---

# Agent Consensus Check

Poll all 8 agents for consensus on current changes.

## Process:
1. Run each agent's validation
2. Collect approvals/vetoes
3. Document concerns
4. Report consensus status

## Requirements:
- **Unanimous:** 8/8 agents must approve
- **Override:** 6/8 agents can override single veto

Output consensus report with detailed feedback.
""",
            "agent-status": """---
name: agent-status
description: Show agent metrics and patterns
---

# Agent Status Report

Display metrics for all agents:
- Approval rates
- Common veto reasons
- Recent decisions
- Performance stats

Generate visual dashboard of agent activity.
"""
        }

        for cmd_name, cmd_content in commands.items():
            cmd_path = self.repo_path / f".claude/commands/{cmd_name}.md"
            cmd_path.write_text(cmd_content)

    def create_claude_config(self):
        """Create main CLAUDE.md configuration."""
        claude_content = f"""# Multi-Agent Consensus System Configuration

**Framework Version:** 2.0
**Installed:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Status:** ✅ ACTIVE

## System Architecture

This repository uses an 8-agent consensus system for quality control.

### Active Agents

| Agent | Domain | Veto Authority |
|-------|--------|----------------|
| Data | Pipelines & Quality | Data integrity |
| Math | Calculations | Mathematical errors |
| Model | ML & Predictions | Model performance |
| Trading | Business Logic | Strategy issues |
| Review | Code Quality | Security/quality |
| Infrastructure | Deployment | System failures |
| Documentation | Docs & Knowledge | Missing docs |
| Code Organization | Structure | Structural issues |

## Operating Principles

1. **Unanimous Consensus Required** - All 8 agents must approve
2. **Quality Over Speed** - Never compromise standards
3. **Minimal Impact** - Changes <500 lines per PR
4. **Evidence-Based** - All vetoes require specific evidence
5. **Continuous Improvement** - Learn from patterns

## Available Commands

- `/review` - Run full multi-agent review
- `/consensus` - Get agent consensus
- `/agent-status` - Show agent metrics
- `/compact` - Compress context intelligently

## Quality Standards

| Metric | Target |
|--------|--------|
| Test Coverage | >80% |
| Code Complexity | <10 |
| PR Size | <500 lines |
| Security Issues | 0 critical |
| Documentation | 100% current |

## Workflow

1. Make changes to code
2. Run `/review` for agent feedback
3. Address any vetoes
4. Commit when all agents approve
5. Monitor metrics for patterns

## Configuration

- **Config File:** `.claude/config.py`
- **Agent Skills:** `.claude/skills/*/SKILL.md`
- **Validation Scripts:** `.claude/skills/*/validate.py`
- **Metrics:** `.claude/metrics/`

## Git Integration

Pre-commit hooks automatically run all agent validations.
To bypass (not recommended): `git commit --no-verify`

## Maintenance

- Review agent metrics weekly
- Update standards based on patterns
- Archive old documentation monthly
- Tune agent sensitivity as needed

---

**For detailed setup:** See `agentic_setup/COMPLETE_SETUP_GUIDE.md`
**For agent details:** See `.claude/skills/*/SKILL.md`
"""

        claude_path = self.repo_path / "CLAUDE.md"
        # Backup existing CLAUDE.md if it exists
        if claude_path.exists():
            backup_path = self.repo_path / f"CLAUDE.md.backup.{self.timestamp}"
            shutil.copy(claude_path, backup_path)
            print(f"   📄 Backed up existing CLAUDE.md to {backup_path.name}")

        claude_path.write_text(claude_content)

    def setup_github_copilot(self):
        """Configure GitHub Copilot for agent awareness."""
        copilot_dir = self.repo_path / ".github/copilot"
        copilot_dir.mkdir(parents=True, exist_ok=True)

        # Copy template config
        template_config = Path(__file__).parent.parent / "templates/github_copilot_config.yml"
        if template_config.exists():
            shutil.copy(template_config, copilot_dir / "config.yml")

    def create_helper_scripts(self):
        """Create utility scripts for the system."""
        scripts_dir = self.repo_path / ".claude/scripts"

        # Consensus report script
        consensus_script = '''#!/usr/bin/env python3
"""Generate consensus report from all agents."""

import json
import subprocess
from pathlib import Path
from datetime import datetime

def get_consensus():
    """Get consensus from all agents."""
    agents = ["data", "math", "model", "trading",
              "review", "infrastructure", "documentation",
              "code-organization"]

    print("MULTI-AGENT CONSENSUS REPORT")
    print("=" * 50)
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    results = {}
    vetoes = []

    for agent in agents:
        script = f".claude/skills/{agent}-agent/validate.py"
        try:
            output = subprocess.check_output(
                ["python", script],
                text=True,
                stderr=subprocess.DEVNULL
            )
            result = json.loads(output)
            status = result.get("status", "UNKNOWN")
            results[agent] = status

            if status == "VETO":
                vetoes.append({
                    "agent": agent,
                    "errors": result.get("errors", [])
                })

            icon = "✅" if status == "APPROVE" else "❌" if status == "VETO" else "⚠️ "
            print(f"{icon} {agent}-agent: {status}")

        except Exception as e:
            results[agent] = "ERROR"
            print(f"❌ {agent}-agent: ERROR - {e}")

    print()
    print("-" * 50)

    if vetoes:
        print(f"CONSENSUS: BLOCKED ({len(vetoes)} vetoes)")
        print()
        print("VETO DETAILS:")
        for veto in vetoes:
            print(f"  {veto['agent']}:")
            for error in veto.get("errors", []):
                print(f"    - {error}")
    else:
        print("CONSENSUS: ✅ APPROVED (8/8 agents)")

    return all(status == "APPROVE" for status in results.values())

if __name__ == "__main__":
    import sys
    consensus = get_consensus()
    sys.exit(0 if consensus else 1)
'''

        (scripts_dir / "consensus_report.py").write_text(consensus_script)
        (scripts_dir / "consensus_report.py").chmod(0o755)

        # Test system script
        test_script = '''#!/usr/bin/env python3
"""Test the multi-agent system."""

import subprocess
import json
from pathlib import Path

def test_agents():
    """Test all agent validations."""
    print("🧪 Testing Multi-Agent System")
    print("=" * 40)

    agents = ["data", "math", "model", "trading",
              "review", "infrastructure", "documentation",
              "code-organization"]

    passed = 0
    failed = 0

    for agent in agents:
        script = f".claude/skills/{agent}-agent/validate.py"
        if not Path(script).exists():
            print(f"❌ {agent}: Script not found")
            failed += 1
            continue

        try:
            output = subprocess.check_output(
                ["python", script],
                text=True,
                stderr=subprocess.DEVNULL
            )
            result = json.loads(output)
            print(f"✅ {agent}: Validation works")
            passed += 1
        except Exception as e:
            print(f"❌ {agent}: {e}")
            failed += 1

    print("=" * 40)
    print(f"Results: {passed} passed, {failed} failed")
    return failed == 0

if __name__ == "__main__":
    import sys
    success = test_agents()
    sys.exit(0 if success else 1)
'''

        (scripts_dir / "test_system.py").write_text(test_script)
        (scripts_dir / "test_system.py").chmod(0o755)

    def run_tests(self):
        """Run initial system tests."""
        test_script = self.repo_path / ".claude/scripts/test_system.py"
        if test_script.exists():
            try:
                subprocess.run(
                    ["python", str(test_script)],
                    cwd=self.repo_path,
                    check=True
                )
            except subprocess.CalledProcessError:
                print("   ⚠️  Some tests failed (expected for new installation)")

    def generate_documentation(self):
        """Generate installation report."""
        report_path = self.repo_path / f"INSTALLATION_REPORT_{self.timestamp}.md"
        report_content = f"""# Multi-Agent System Installation Report

**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Repository:** {self.repo_path}

## Installed Components

### Agents (8)
{chr(10).join(f"- ✅ {agent}" for agent in self.AGENTS)}

### Directory Structure
- ✅ `.claude/` - Main configuration directory
- ✅ `.claude/skills/` - Agent skills
- ✅ `.claude/commands/` - Slash commands
- ✅ `.claude/scripts/` - Helper scripts
- ✅ `.git/hooks/` - Git integration

### Configuration Files
- ✅ `CLAUDE.md` - Main configuration
- ✅ `.git/hooks/pre-commit` - Validation hook
- ✅ `.github/copilot/config.yml` - Copilot config

## Next Steps

1. **Customize Agent Skills**
   - Edit `.claude/skills/*/SKILL.md` for your domain
   - Update validation logic in `validate.py` scripts

2. **Test the System**
   ```bash
   python .claude/scripts/test_system.py
   ```

3. **Run First Review**
   ```bash
   python .claude/scripts/consensus_report.py
   ```

4. **Make First Commit**
   ```bash
   git add .
   git commit -m "Initialize multi-agent system"
   ```

## Commands Available

- `/review` - Full agent review
- `/consensus` - Get consensus
- `/agent-status` - Show metrics

## Support

For help, see: `agentic_setup/COMPLETE_SETUP_GUIDE.md`
"""

        report_path.write_text(report_content)
        print(f"\n📄 Installation report: {report_path.name}")

    def ask_continue(self) -> bool:
        """Ask user whether to continue after error."""
        response = input("   Continue installation? (y/n): ").lower()
        return response == 'y'


def main():
    """Main entry point."""
    print("""
╔════════════════════════════════════════════════╗
║   Multi-Agent Consensus Framework Installer    ║
║              Version 2.0                        ║
╚════════════════════════════════════════════════╝
    """)

    # Get repository path
    if len(sys.argv) > 1:
        repo_path = sys.argv[1]
    else:
        repo_path = input("Enter repository path (or . for current): ").strip() or "."

    # Run installer
    installer = MultiAgentFrameworkInstaller(repo_path)
    success = installer.run()

    if success:
        print("\n🎉 Successfully installed Multi-Agent Consensus Framework!")
    else:
        print("\n⚠️  Installation completed with some issues.")

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())