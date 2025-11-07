# 🤖 Universal Agentic Setup Framework

**Multi-agent quality control for any codebase - works with Claude Code and GitHub Copilot**

[![Version](https://img.shields.io/badge/version-3.0-blue.svg)](https://github.com/yourorg/agentic-setup)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-yellow.svg)](https://python.org)

## 🚀 Quick Start - One Command!

```bash
# Clone once
git clone https://github.com/yourorg/agentic-setup ~/agentic-setup

# Run in any project
cd your-project
python ~/agentic-setup/quick_start.py

# Follow the interactive prompts!
```

That's it! The script will:
- 🔍 Detect your environment
- 📦 Let you choose Claude Code, GitHub Copilot, or both
- 🤖 Install and configure everything automatically
- ✅ Set up multi-agent quality control

---

## 🎯 What Is This?

A universal framework that turns AI coding assistants into intelligent, multi-agent systems:

- **Auto-detects** your project's tech stack
- **Installs relevant agents** for quality control
- **Enforces consensus** before code ships
- **Works with multiple platforms:**
  - 🟣 **Claude Code** - CLI-based AI assistant
  - 🟢 **GitHub Copilot** - VS Code integrated AI

### 🔐 Privacy First: Nothing Shared

**This is a personal development tool:**
- ❌ Not committed to your project repos
- ❌ Not shared with teammates via git
- ✅ Installed locally on each developer's machine
- ✅ Configured personally - your agents, your settings
- ✅ Completely optional - use it or don't, zero impact on team

Think of it like your personal linter, formatter, or IDE settings - it's yours alone.

---

## 📦 Choose Your Platform

This framework supports two AI coding platforms:

### 🟣 Claude Code Setup
**Best for:** CLI workflows, terminal-based development, deep code analysis

```bash
# Install once
git clone https://github.com/yourorg/agentic-setup ~/agentic-setup

# Use in any project
cd your-project
python ~/agentic-setup/agentic_setup/claude-code/scripts/implement_framework.py .
```

**Features:**
- 6 default agents (Data, Logic, Test, Security, Infra, Doc)
- 15+ optional agents (Performance, Refactor, Observability, etc.)
- Auto-detection of tech stack
- Git hooks integration
- Compound Engineering agents support
- Superpowers features (context management, navigation)

**[→ Full Claude Code Documentation](agentic_setup/claude-code/README.md)**

---

### 🟢 GitHub Copilot Setup
**Best for:** VS Code workflows, inline suggestions, real-time guidance

#### Quick Start (Recommended)
```bash
# One-command APM setup - installs everything!
python ~/agentic-setup/agentic_setup/github-copilot/scripts/install_apm.py .
```

#### Manual Setup (Alternative)
```bash
# Step 1: Analyze your project
python ~/agentic-setup/agentic_setup/github-copilot/scripts/analyze_project.py .

# Step 2: Install configuration
python ~/agentic-setup/agentic_setup/github-copilot/scripts/setup_copilot_agents.py .
```

**Features:**
- **APM (Agentic Project Management)** - Full TDD workflow automation
- Multi-agent guidance in Copilot suggestions
- Project-aware autocomplete
- Architecture and documentation integration
- Copilot Chat enhancements with custom modes
- VS Code Agent Mode integration
- Copilot Coding Agent support
- Always-on quality checks

**[→ Full GitHub Copilot Documentation](agentic_setup/github-copilot/README.md)**

---

## 🚀 Quick Comparison

| Feature | Claude Code | GitHub Copilot |
|---------|-------------|----------------|
| **Platform** | CLI / Terminal | VS Code |
| **Agents** | 6 default + 15 optional | 6 core + 15 optional (21 total!) |
| **Auto-Detection** | ✅ Full stack analysis | ✅ Full stack analysis |
| **Git Integration** | ✅ Pre-commit hooks | ⚠️ Manual review |
| **Real-time Suggestions** | ❌ On-demand | ✅ Inline autocomplete |
| **Deep Analysis** | ✅ Comprehensive | ✅ Comprehensive |
| **Documentation** | ✅ Auto-generated | ✅ Context-aware |
| **Learning Curve** | Moderate | Low |
| **Cost** | Free + API costs | Subscription required |
| **Best For** | CLI developers, deep reviews | VS Code users, fast coding |
| **Agent Timing** | Reactive (commit-time) | Proactive (as-you-type) |

---

## 📚 Directory Structure

```
agentic-setup/
├── README.md                    # This file
├── LICENSE
├── .gitignore
└── agentic_setup/
    ├── claude-code/             # Claude Code setup
    │   ├── README.md
    │   ├── COMPLETE_SETUP_GUIDE.md
    │   ├── prompts/
    │   │   └── MASTER_CLAUDE_PROMPT.md
    │   ├── scripts/
    │   │   ├── agent_detector.py
    │   │   └── implement_framework.py
    │   ├── templates/
    │   │   └── gitignore_template.txt
    │   └── documentation/
    │
    └── github-copilot/          # GitHub Copilot setup
        ├── README.md
        ├── prompts/
        ├── scripts/
        │   ├── analyze_project.py
        │   └── setup_copilot_agents.py
        ├── templates/
        └── examples/
```

---

## 🎯 Installation Paths

### Option 1: Clone Once, Use Everywhere (Recommended)

```bash
# Install framework to home directory
git clone https://github.com/yourorg/agentic-setup ~/agentic-setup

# Use in Project A (Claude Code)
cd ~/projects/project-a
python ~/agentic-setup/agentic_setup/claude-code/scripts/implement_framework.py .

# Use in Project B (GitHub Copilot)
cd ~/projects/project-b
python ~/agentic-setup/agentic_setup/github-copilot/scripts/analyze_project.py .
python ~/agentic-setup/agentic_setup/github-copilot/scripts/setup_copilot_agents.py .

# Use Both in Project C
cd ~/projects/project-c
python ~/agentic-setup/agentic_setup/claude-code/scripts/implement_framework.py .
python ~/agentic-setup/agentic_setup/github-copilot/scripts/setup_copilot_agents.py .
```

### Option 2: Download and Extract

```bash
# Download latest release
curl -L https://github.com/yourorg/agentic-setup/archive/main.zip -o agentic-setup.zip

# Extract
unzip agentic-setup.zip -d ~/

# Use as above
```

---

## ✨ Key Features

### 🔍 Auto-Detection
- Scans codebase for languages, frameworks, patterns
- Automatically enables appropriate agents
- Detects APIs, frontends, databases, CI/CD
- No manual configuration for basic setup

### 🤖 Multi-Agent System
**Default Agents (Always Active):**
1. Data Agent - Input validation, schemas
2. Logic Agent - Correctness, edge cases
3. Test Agent - Coverage >80%
4. Security Agent - Secrets, vulnerabilities
5. Infra Agent - Build, containers, CI/CD
6. Doc Agent - Documentation sync

**Optional Agents (Auto-Enabled):**
- Performance Agent (APIs, backends)
- Refactor Agent (mature codebases)
- Observability Agent (distributed systems)
- UX/Accessibility Agent (frontends)
- DevEx Agent (team repos)
- [10+ more...](agentic_setup/claude-code/README.md#optional-agents)

### 🔐 Privacy & Security
- **All local** - no data sent externally
- **User-specific** - not in version control
- **Optional** - team members can use or ignore
- **Clean repos** - project code stays clean

---

## 🎮 Usage Examples

### Claude Code Workflow

```bash
# Make changes
vim src/api/users.py

# Commit (agents run automatically)
git add .
git commit -m "Add user endpoint"

# 🤖 Multi-Agent Consensus Check
# ✅ Data Agent: APPROVE
# ✅ Logic Agent: APPROVE
# ✅ Test Agent: APPROVE
# ✅ Security Agent: APPROVE
# ✅ Infra Agent: APPROVE
# ✅ Doc Agent: APPROVE
# → Commit proceeds

# Or use slash commands
/review          # Full agent review
/consensus       # Get consensus report
/agent-status    # Show agent metrics
```

### GitHub Copilot Workflow

```python
# Start typing in VS Code
def get_user

# Copilot suggests (with agent guidance):
async def get_user(user_id: int) -> Optional[User]:
    """
    Retrieve user by ID.

    Args:
        user_id: User's unique identifier

    Returns:
        User object if found, None otherwise

    Raises:
        DatabaseError: If database connection fails

    Examples:
        >>> user = await get_user(123)
        >>> user.name
        'John Doe'
    """
    try:
        return await db.query(User).filter(User.id == user_id).first()
    except Exception as e:
        logger.error(f"Error fetching user {user_id}: {e}")
        raise DatabaseError(f"Failed to retrieve user: {e}")

# ✅ Security Agent: No hardcoded secrets
# ✅ Logic Agent: Error handling present
# ✅ Test Agent: Docstring with examples
# ✅ Performance Agent: Using async
# ✅ Doc Agent: Complete documentation
# → Suggestion approved by all agents
```

---

## 📖 Documentation

### Claude Code
- [Quick Start Guide](agentic_setup/claude-code/README.md)
- [Complete Setup Guide](agentic_setup/claude-code/COMPLETE_SETUP_GUIDE.md)
- [Master Prompt](agentic_setup/claude-code/prompts/MASTER_CLAUDE_PROMPT.md)
- [Agent Detector](agentic_setup/claude-code/scripts/agent_detector.py)

### GitHub Copilot
- [Quick Start Guide](agentic_setup/github-copilot/README.md)
- [Project Analyzer](agentic_setup/github-copilot/scripts/analyze_project.py)
- [Setup Script](agentic_setup/github-copilot/scripts/setup_copilot_agents.py)

---

## 🤝 Using Both Together

You can use **both** Claude Code and GitHub Copilot in the same project:

```bash
cd your-project

# Install Claude Code setup
python ~/agentic-setup/agentic_setup/claude-code/scripts/implement_framework.py .

# Install GitHub Copilot setup
python ~/agentic-setup/agentic_setup/github-copilot/scripts/analyze_project.py .
python ~/agentic-setup/agentic_setup/github-copilot/scripts/setup_copilot_agents.py .

# Result:
# - Claude Code agents run on commits (git hooks)
# - Copilot agents guide inline suggestions (VS Code)
# - Both use the same quality standards
# - Double-layer quality control!
```

**Benefits:**
- ✅ Real-time guidance (Copilot) + Deep review (Claude Code)
- ✅ Inline suggestions + Git hook validation
- ✅ VS Code integration + CLI power
- ✅ Consistent standards across both platforms

---

## ❓ FAQ

### Q: Which should I use - Claude Code or GitHub Copilot?

**A:** Depends on your workflow:
- **Claude Code** if you prefer CLI, want deep analysis, or need git hook integration
- **GitHub Copilot** if you live in VS Code and want real-time inline suggestions
- **Both** if you want maximum code quality with dual-layer checking

### Q: Can I switch between them?

**A:** Yes! Both systems are independent. Install one, both, or switch freely.

### Q: Do they conflict with each other?

**A:** No. They complement each other:
- Copilot guides you while typing
- Claude Code validates before commit
- Same quality standards, different enforcement points

### Q: What's in my project repo vs. local?

**In Git (Project Repo):**
- ✅ Your project code
- ✅ Updated `.gitignore` (excludes agentic files)
- ❌ No agentic framework
- ❌ No agent configs

**Local Only (Your Machine):**
- ✅ `~/agentic-setup/` - The framework
- ✅ `.claude/` - Claude Code configs (per project)
- ✅ `.copilot/` - Copilot configs (per project)
- ✅ `CLAUDE.md` - Claude settings (per project)

### Q: How do I uninstall?

```bash
# Remove Claude Code
rm -rf .claude/ CLAUDE.md .git/hooks/pre-commit .git/hooks/post-commit

# Remove GitHub Copilot
rm -rf .copilot/ .github/copilot/ .vscode/copilot-settings.json

# Remove both
rm -rf .claude/ .copilot/ CLAUDE.md .github/copilot/ .vscode/copilot-settings.json

# Your project repo was never affected!
```

---

## 🎯 Best Practices

1. **Start with one platform** - Claude Code OR Copilot, learn it first
2. **Trust auto-detection** - Let the framework suggest agents
3. **Iterate on standards** - Adjust agent settings to your team
4. **Use both for critical projects** - Double-layer quality control
5. **Keep framework updated** - `git pull` in ~/agentic-setup occasionally

---

## 🆘 Support

- **Issues:** [GitHub Issues](https://github.com/yourorg/agentic-setup/issues)
- **Claude Code Docs:** [Complete Guide](agentic_setup/claude-code/COMPLETE_SETUP_GUIDE.md)
- **Copilot Docs:** [Setup Guide](agentic_setup/github-copilot/README.md)

---

## 📝 License

MIT License - See [LICENSE](LICENSE) file

---

## 🙏 Credits

Built with:
- **Claude Code** by Anthropic
- **GitHub Copilot** by GitHub
- **Compound Engineering** agents
- Open source tools (PyTest, Jest, Trivy, etc.)

---

**Made with ❤️ for developers who care about code quality**

*Personal AI assistants that make you a better developer - locally, intelligently, effectively.*
