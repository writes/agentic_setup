# 🤖 Multi-Agent Consensus Framework Setup

## Complete Implementation Guide for Compound Engineering & Superpowers

**Version:** 2.0
**Date:** November 6, 2025
**Framework:** 8-Agent Unanimous Consensus System

---

## 📋 Table of Contents

- [Quick Start](#quick-start)
- [What This Is](#what-this-is)
- [System Architecture](#system-architecture)
- [Installation](#installation)
- [Agent Descriptions](#agent-descriptions)
- [Usage](#usage)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)

---

## 🚀 Quick Start

Install the complete multi-agent system in any repository:

```bash
# Clone or copy this directory to your project
cp -r agentic_setup /path/to/your/project/

# Run the installer
cd /path/to/your/project
python agentic_setup/scripts/implement_framework.py .

# Test the system
python .claude/scripts/test_system.py

# Make your first validated commit
git add .
git commit -m "Initialize multi-agent system"
```

---

## 🎯 What This Is

A complete framework for implementing an 8-agent consensus system that ensures:

- **Code Quality:** Every change validated by domain experts
- **Zero Defects:** Security, math, data integrity all verified
- **Minimal Impact:** Changes kept small and focused
- **Documentation:** Always current, never stale
- **Standards:** Enforced consistently across codebase

### The 8 Agents

1. **Data Agent** - Data pipelines and quality
2. **Math Agent** - Calculations and formulas
3. **Model Agent** - ML models and predictions
4. **Trading Agent** - Business logic and strategies
5. **Review Agent** - Code quality and security
6. **Infrastructure Agent** - Deployment and AWS
7. **Documentation Agent** - Docs and knowledge
8. **Code Organization Agent** - Structure and cleanliness

---

## 🏗️ System Architecture

```
┌─────────────────────────────────┐
│     ORCHESTRATOR (Claude)        │
│         Opus 4.1 Model          │
└────────────┬────────────────────┘
             │
    ┌────────▼────────┐
    │  8 AGENT LAYER  │
    │  Sonnet 4.5     │
    └────────┬────────┘
             │
    ┌────────▼────────────────────────┐
    │         Unanimous Consensus      │
    │     All 8 Must Approve           │
    └────────┬────────────────────────┘
             │
    ┌────────▼────────┐
    │  CODE EXECUTION │
    └─────────────────┘
```

### Three-Tier Implementation

1. **Skills Layer** - Reusable patterns and tools
2. **Agent Layer** - Quality validation and standards
3. **Execution Layer** - Actual implementation

---

## 📦 Installation

### Prerequisites

- Python 3.8+
- Git repository
- 1GB free disk space
- Claude Code CLI or API access

### Step-by-Step Installation

#### 1. Copy Framework Files

```bash
# Copy the agentic_setup directory to your project root
cp -r agentic_setup /your/project/
cd /your/project
```

#### 2. Run Automated Installer

```bash
python agentic_setup/scripts/implement_framework.py .
```

This will:
- Create `.claude/` directory structure
- Install all 8 agent configurations
- Setup Git hooks for validation
- Configure slash commands
- Create helper scripts

#### 3. Verify Installation

```bash
# Test all agents are working
python .claude/scripts/test_system.py

# Check consensus system
python .claude/scripts/consensus_report.py
```

#### 4. Configure Claude

Copy the master prompt to Claude:

```bash
cat agentic_setup/prompts/MASTER_CLAUDE_PROMPT.md
```

Paste this into Claude's system prompt or initial message.

#### 5. Setup GitHub Copilot (Optional)

```bash
# Copy Copilot config
cp agentic_setup/templates/github_copilot_config.yml .github/copilot/config.yml
```

---

## 👥 Agent Descriptions

### Data Agent
- **Focus:** Data quality, pipelines, validation
- **Standards:** >95% coverage, <1% violations
- **Veto Triggers:** Data integrity issues, missing validation

### Math Agent
- **Focus:** Calculations, formulas, statistics
- **Standards:** 100% accuracy, safe operations
- **Veto Triggers:** Math errors, divide-by-zero

### Model Agent
- **Focus:** ML training, validation, predictions
- **Standards:** F1>0.60, Sharpe>2.0
- **Veto Triggers:** Overfitting, poor performance

### Trading Agent
- **Focus:** Business logic, strategies, signals
- **Standards:** Win rate>65%, profit factor>2.0
- **Veto Triggers:** Logic errors, incomplete features

### Review Agent
- **Focus:** Code quality, security, testing
- **Standards:** Coverage>80%, zero vulnerabilities
- **Veto Triggers:** Security issues, low coverage

### Infrastructure Agent
- **Focus:** Deployment, AWS, monitoring
- **Standards:** <$100/mo, >99.9% uptime
- **Veto Triggers:** System failures, cost overruns

### Documentation Agent
- **Focus:** Docs, knowledge, tracking
- **Standards:** 100% current, no placeholders
- **Veto Triggers:** Missing docs, outdated info

### Code Organization Agent
- **Focus:** Structure, cleanliness, modularity
- **Standards:** PR<500 lines, <5% duplication
- **Veto Triggers:** Circular dependencies, bloat

---

## 🎮 Usage

### Claude Commands

After installation, use these slash commands in Claude:

```
/review          - Run full 8-agent review
/consensus       - Get unanimous consensus
/agent-status    - Show agent metrics
```

### Git Integration

The system automatically validates on commit:

```bash
# Normal commit (runs validation)
git add .
git commit -m "Your message"

# If validation fails, you'll see:
❌ Commit blocked by: review-agent, code-organization-agent

# Fix issues and retry
# Or bypass (NOT RECOMMENDED):
git commit --no-verify
```

### Manual Validation

```bash
# Run specific agent
python .claude/skills/data-agent/validate.py

# Run all agents
python .claude/scripts/consensus_report.py

# Check metrics
python .claude/scripts/agent_metrics.py
```

---

## 🛠️ Customization

### Modify Agent Standards

Edit agent skill files:

```bash
# Edit standards for an agent
vim .claude/skills/review-agent/SKILL.md
```

### Add Custom Validation

Update validation scripts:

```python
# .claude/skills/data-agent/validate.py

def check_standards(self, repo_path: Path):
    """Add your custom checks here."""
    # Check for data quality
    if not self.validate_data_coverage():
        self.errors.append("Data coverage below 95%")

    # Check for validation
    if not self.has_data_validation():
        self.errors.append("Missing data validation")
```

### Adjust Sensitivity

Configure in `.claude/config.py`:

```python
AGENT_CONFIG = {
    "quality_standards": {
        "test_coverage_minimum": 80,  # Adjust this
        "max_complexity": 10,          # Adjust this
        "max_pr_lines": 500           # Adjust this
    }
}
```

### Add New Agents

```bash
# Create new agent structure
mkdir -p .claude/skills/new-agent/{PATTERNS,CHECKLISTS,VALIDATION,SCRIPTS}

# Create SKILL.md
cat > .claude/skills/new-agent/SKILL.md << EOF
---
name: New Agent
description: Your new agent description
---
# Agent content here
EOF

# Update config
echo 'AGENTS.append("new-agent")' >> .claude/config.py
```

---

## 🔧 Troubleshooting

### Common Issues

#### Agents Always Veto

```bash
# Check what's triggering vetoes
python .claude/scripts/consensus_report.py

# Review agent metrics
python .claude/scripts/agent_metrics.py

# Adjust standards if too strict
vim .claude/skills/[agent-name]/SKILL.md
```

#### Git Hook Not Running

```bash
# Ensure hook is executable
chmod +x .git/hooks/pre-commit

# Test manually
./.git/hooks/pre-commit
```

#### Claude Not Recognizing Commands

```bash
# Verify command files exist
ls -la .claude/commands/

# Re-initialize Claude with prompt
cat agentic_setup/prompts/MASTER_CLAUDE_PROMPT.md
```

### Debug Mode

```bash
# Enable verbose output
export AGENT_DEBUG=1

# Run with debug
python .claude/scripts/consensus_report.py
```

---

## 📁 Directory Structure

```
agentic_setup/
├── README.md                     # This file
├── COMPLETE_SETUP_GUIDE.md       # Detailed documentation
├── prompts/
│   └── MASTER_CLAUDE_PROMPT.md   # Claude initialization
├── templates/
│   └── github_copilot_config.yml # Copilot configuration
├── scripts/
│   └── implement_framework.py    # Automated installer
└── documentation/
    └── EVOLUTION_GUIDE.md        # How to evolve the system
```

After installation:
```
your-project/
├── .claude/
│   ├── agents/            # Agent configurations
│   ├── skills/            # Agent skills (8 subdirs)
│   ├── commands/          # Slash commands
│   ├── scripts/           # Helper scripts
│   └── metrics/           # Performance tracking
├── .git/hooks/
│   ├── pre-commit         # Validation hook
│   └── post-commit        # Metrics hook
└── CLAUDE.md              # Main configuration
```

---

## 📊 Metrics & Monitoring

The system tracks:
- Agent approval/veto rates
- Common veto reasons
- Resolution times
- Code quality trends

View metrics:
```bash
python .claude/scripts/agent_metrics.py
```

---

## 🚦 Best Practices

1. **Start Small** - Begin with 2-3 agents, add more gradually
2. **Tune Standards** - Adjust based on your team's needs
3. **Document Vetoes** - Learn from patterns
4. **Regular Reviews** - Check metrics weekly
5. **Iterate** - Continuously improve agent logic

---

## 🆘 Support

- **Documentation:** See `COMPLETE_SETUP_GUIDE.md`
- **Agent Details:** Check `.claude/skills/*/SKILL.md`
- **Examples:** Look in `templates/` directory

---

## 📝 License

This framework is open source and available for use in any project.

---

**Created by:** Multi-Agent Consensus System
**Maintained by:** Code Organization Agent
**Version:** 2.0
**Last Updated:** November 6, 2025