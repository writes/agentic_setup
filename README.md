# 🤖 Universal Agentic Setup Framework

**A self-configuring multi-agent quality control system for any codebase**

[![Version](https://img.shields.io/badge/version-3.0-blue.svg)](https://github.com/yourorg/agentic-setup)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-yellow.svg)](https://python.org)

---

## 🎯 What Is This?

A universal framework that:
- **Automatically detects** your project's tech stack
- **Installs relevant agents** for quality control
- **Enforces consensus** before code ships
- **Integrates with Claude Code** for AI-powered reviews
- **Works with any codebase** - Python, TypeScript, Go, Ruby, etc.

## ✨ Key Features

### 🔍 Auto-Detection
- Scans your codebase to identify languages, frameworks, and patterns
- Automatically enables appropriate agents based on what it finds
- No manual configuration required for basic setup

### 🤖 6 Default Agents (Always Active)
1. **Data Agent** - Validates inputs, schemas, file formats
2. **Logic Agent** - Ensures correctness and control flow
3. **Test Agent** - Enforces >80% coverage
4. **Security Agent** - Scans for secrets, CVEs, injections
5. **Infra Agent** - Validates containers, CI/CD, deployments
6. **Doc Agent** - Keeps docs in sync with code

### 🔧 Optional Agents (Auto-Enabled When Detected)
- **Performance Agent** - For APIs and backend services
- **Refactor Agent** - For mature codebases
- **Observability Agent** - For distributed systems
- **DevEx Agent** - For team repositories
- **UX/Accessibility Agent** - For frontend projects
- And [10+ more optional agents](agentic_setup/README.md#optional-agents)

### 🚀 Compound Engineering Integration
Built-in support for specialized Claude Code agents:
- `kieran-rails-reviewer`, `kieran-python-reviewer`, `kieran-typescript-reviewer`
- `architecture-strategist`, `performance-oracle`, `security-sentinel`
- `data-integrity-guardian`, `pattern-recognition-specialist`

### ⚡ Superpowers Features
- **Smart Context Management** - Auto-compaction at 150K tokens
- **Intelligent Navigation** - Jump to relevant code instantly
- **Pattern Recognition** - Learn from agent feedback

---

## 🚀 Quick Start

### 1. Install Framework
```bash
# Copy to your project
cp -r agentic_setup /path/to/your/project/

# Run installer (auto-detects your stack)
cd /path/to/your/project
python agentic_setup/scripts/implement_framework.py .
```

### 2. Review Detection Results
The installer will:
- Scan your codebase
- Show detected languages, frameworks, patterns
- Suggest which agents to enable
- Ask for confirmation

Example output:
```
🔍 Codebase Analysis Report
==================================================

📝 Languages Detected:
  - Python: 127 files
  - JavaScript: 45 files

🛠️ Frameworks Detected:
  - flask
  - react

🤖 Enabled Agents:
  Default Agents (always enabled):
    ✅ data-agent
    ✅ logic-agent
    ✅ test-agent
    ✅ security-agent
    ✅ infra-agent
    ✅ doc-agent

  Optional Agents (detected):
    ✅ performance-agent
       → Detected API/backend services
    ✅ ux-accessibility-agent
       → Detected frontend/UI project
```

### 3. Start Using
```bash
# Make a change
git add .
git commit -m "Add new feature"

# Agents run automatically!
🤖 Multi-Agent Consensus Check
================================
Checking data-agent... ✅ APPROVED
Checking logic-agent... ✅ APPROVED
Checking test-agent... ✅ APPROVED
Checking security-agent... ✅ APPROVED
Checking infra-agent... ✅ APPROVED
Checking doc-agent... ✅ APPROVED
================================
✅ All agents approve! Proceeding with commit.
```

---

## 📦 What Gets Installed

```
your-project/
├── .claude/
│   ├── agents/              # Agent configurations
│   ├── skills/              # Agent skills (auto-generated based on detection)
│   │   ├── data-agent/
│   │   ├── logic-agent/
│   │   ├── test-agent/
│   │   ├── security-agent/
│   │   ├── infra-agent/
│   │   └── doc-agent/
│   ├── commands/            # Slash commands (/review, /consensus, etc.)
│   ├── scripts/             # Helper scripts
│   │   ├── consensus_report.py
│   │   ├── test_system.py
│   │   └── agent_metrics.py
│   ├── metrics/             # Performance tracking
│   └── config.py            # Main configuration
├── .git/hooks/
│   ├── pre-commit           # Runs agents before commit
│   └── post-commit          # Records metrics
├── .github/copilot/
│   └── config.yml           # GitHub Copilot integration
└── CLAUDE.md                # Claude Code configuration
```

---

## 🎮 Usage

### In Claude Code

Use slash commands:
```
/review          - Run full agent review
/consensus       - Get unanimous consensus
/agent-status    - Show agent metrics
/detect-agents   - Re-scan and update agents
```

### Git Integration

Agents run automatically:
```bash
git commit -m "Your message"

# If agents block:
❌ Commit blocked by: security-agent, test-agent
   Reason: Found hardcoded secret in config.py:42

# Fix and retry
# Or bypass (not recommended):
git commit --no-verify
```

### Manual Validation

```bash
# Run specific agent
python .claude/skills/security-agent/validate.py

# Run all agents
python .claude/scripts/consensus_report.py

# Check metrics
python .claude/scripts/agent_metrics.py
```

---

## 🔌 Compound Engineering Integration

### How It Works

1. **Local agents validate first** (Data, Logic, Test, etc.)
2. **If approved, CE agents review** (kieran-python-reviewer, etc.)
3. **Consensus required from both** local and CE agents

### Configuration

Edit `.claude/config.py`:
```python
COMPOUND_ENGINEERING_AGENTS = {
    "enabled": True,
    "agents": [
        "kieran-python-reviewer",  # Auto-detected for Python projects
        "security-sentinel",        # Always useful
        "performance-oracle"        # For backend/API projects
    ],
    "auto_invoke": {
        "kieran-python-reviewer": ["after_implementation"],
        "security-sentinel": ["before_commit"]
    }
}
```

### Available CE Agents

| Agent | Use For | When |
|-------|---------|------|
| kieran-python-reviewer | Python code | After implementation |
| kieran-rails-reviewer | Rails code | After implementation |
| kieran-typescript-reviewer | TypeScript/React | After components |
| dhh-rails-reviewer | Rails (DHH style) | After implementation |
| architecture-strategist | Architecture | Before major changes |
| performance-oracle | Performance | After optimization |
| security-sentinel | Security | Before commit |
| data-integrity-guardian | Migrations | Before schema changes |

---

## ⚡ Superpowers Features

### Smart Context Management

Automatically activates when context reaches 75% (150K tokens):
```python
# .claude/config.py
SUPERPOWERS_CONFIG = {
    "smart_compaction": {
        "enabled": True,
        "threshold": 150000,
        "preserve_priority": [
            "current_task",
            "agent_standards",
            "recent_vetoes",
            "active_code_changes"
        ]
    }
}
```

### Pattern Recognition

Learns from agent feedback:
```python
{
    "pattern_recognition": {
        "learn_from_vetoes": True,
        "identify_anti_patterns": True,
        "suggest_improvements": True
    }
}
```

### Intelligent Navigation

Find code faster:
```python
{
    "intelligent_navigation": {
        "enabled": True,
        "auto_jump_to_relevant": True,
        "context_aware_search": True
    }
}
```

---

## 🛠️ Customization

### Adjust Standards

```python
# .claude/config.py
AGENT_CONFIG = {
    "quality_standards": {
        "test_coverage_minimum": 80,  # Change to 90 for stricter
        "max_complexity": 10,
        "max_pr_lines": 500
    }
}
```

### Enable/Disable Agents

```python
# Add an agent
AGENTS.append("performance-agent")

# Remove an agent
AGENTS.remove("doc-agent")
```

### Create Custom Agents

```bash
mkdir -p .claude/skills/custom-agent/{PATTERNS,CHECKLISTS,VALIDATION}
vim .claude/skills/custom-agent/SKILL.md
echo 'AGENTS.append("custom-agent")' >> .claude/config.py
```

---

## 📊 Metrics & Monitoring

Track agent decisions:
```bash
python .claude/scripts/agent_metrics.py
```

Output:
```
Multi-Agent System Metrics Report
==================================================

Agent Statistics:
  data-agent:
    Reviews: 47
    Approval Rate: 89.4%
    Veto Rate: 10.6%
  security-agent:
    Reviews: 47
    Approval Rate: 91.5%
    Veto Rate: 8.5%

Top Veto Reasons:
  - Missing test coverage: 8 times
  - Hardcoded secrets: 5 times
  - Missing documentation: 3 times
```

---

## 📚 Documentation

- **[Complete Setup Guide](agentic_setup/COMPLETE_SETUP_GUIDE.md)** - Detailed installation and configuration
- **[Agent Details](agentic_setup/README.md)** - All agents explained
- **[Master Prompt](agentic_setup/prompts/MASTER_CLAUDE_PROMPT.md)** - Claude Code configuration

---

## 🤝 Integration Examples

### Python + Flask + PostgreSQL
**Auto-detected agents:**
- Data Agent, Logic Agent, Test Agent, Security Agent, Infra Agent, Doc Agent
- Performance Agent (API detected)
- Observability Agent (backend detected)

**CE agents:**
- kieran-python-reviewer
- security-sentinel
- data-integrity-guardian

### TypeScript + React + Node.js
**Auto-detected agents:**
- Data Agent, Logic Agent, Test Agent, Security Agent, Infra Agent, Doc Agent
- UX/Accessibility Agent (React detected)
- Performance Agent (backend detected)

**CE agents:**
- kieran-typescript-reviewer
- architecture-strategist

### Ruby on Rails
**Auto-detected agents:**
- Data Agent, Logic Agent, Test Agent, Security Agent, Infra Agent, Doc Agent
- Refactor Agent (Rails projects tend to be mature)

**CE agents:**
- kieran-rails-reviewer or dhh-rails-reviewer
- data-integrity-guardian
- security-sentinel

---

## 🔍 How Detection Works

The framework scans for:

1. **Programming Languages**
   - File extensions (.py, .js, .ts, .rb, .go, etc.)

2. **Frameworks & Libraries**
   - Package files (package.json, requirements.txt, Gemfile, etc.)
   - Import statements
   - Configuration files

3. **Project Patterns**
   - Directory structure (api/, tests/, models/, etc.)
   - File naming conventions
   - CI/CD configurations

4. **Team Metrics**
   - Git contributors
   - PR activity
   - Repository size

Based on these signals, it enables appropriate agents automatically.

---

## 🎯 Best Practices

1. **Start Small** - Use default 6 agents initially
2. **Trust Auto-Detection** - Let the system suggest agents
3. **Review Metrics** - Check agent decisions weekly
4. **Tune Standards** - Adjust thresholds to your team
5. **Iterate** - Add/remove agents as project evolves

---

## 🆘 Troubleshooting

### Agents Too Strict?
```python
# .claude/config.py
AGENT_CONFIG["quality_standards"]["test_coverage_minimum"] = 70  # Lower from 80
```

### Wrong Agents Detected?
```bash
# Re-run detection
python .claude/scripts/detect_agents.py

# Or manually edit
vim .claude/config.py
```

### Git Hook Not Running?
```bash
chmod +x .git/hooks/pre-commit
./.git/hooks/pre-commit  # Test manually
```

---

## 🚀 Advanced Usage

### Running Agents in Parallel

The framework automatically runs independent agents concurrently for speed.

### Veto Override

If 6 out of N agents approve, you can override a single veto:
```python
# In .claude/config.py
AGENT_CONFIG["consensus"]["veto_override_threshold"] = 6
```

### Custom Validation Logic

Edit any agent's `validate.py`:
```python
# .claude/skills/security-agent/validate.py
def check_standards(self, repo_path: Path):
    # Add your custom security checks
    if self.has_hardcoded_api_keys():
        self.errors.append("Found hardcoded API keys")
```

---

## 📈 Roadmap

- [ ] VS Code extension
- [ ] Web dashboard for metrics
- [ ] AI-powered agent tuning
- [ ] Multi-repo support
- [ ] Cloud-based agent execution

---

## 🤝 Contributing

Contributions welcome! Areas needing help:
- Additional language detection
- More framework patterns
- Agent templates
- Documentation improvements

---

## 📝 License

MIT License - See [LICENSE](LICENSE) file

---

## 🙏 Credits

Built with:
- **Claude Code** by Anthropic
- **Compound Engineering** agents
- Open source tools (PyTest, Jest, Trivy, etc.)

Inspired by:
- Rails testing culture
- UNIX philosophy
- Clean code principles

---

## 📞 Support

- **Issues:** [GitHub Issues](https://github.com/yourorg/agentic-setup/issues)
- **Docs:** [Complete Setup Guide](agentic_setup/COMPLETE_SETUP_GUIDE.md)
- **Examples:** See `examples/` directory

---

**Made with ❤️ for developers who care about code quality**

*Transform any codebase into a self-validating, high-quality system in minutes.*
