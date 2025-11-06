# 🤖 Universal Multi-Agent Framework

## Automated Agent Detection & Consensus System

**Version:** 3.0
**Framework:** Compound Engineering + Superpowers
**Compatible:** Any codebase, any tech stack

---

## 📋 Quick Start

### One-Time Installation

Install the framework once on your machine:

```bash
# Clone to your home directory (or anywhere you prefer)
git clone https://github.com/yourorg/agentic-setup ~/agentic-setup

# Or download:
curl -L https://github.com/yourorg/agentic-setup/archive/main.zip -o agentic-setup.zip
unzip agentic-setup.zip -d ~/
```

### Use in Any Project

Run the installer in any project:

```bash
# Navigate to your project
cd /path/to/your/project

# Run the installer (auto-detects your stack)
python ~/agentic-setup/scripts/implement_framework.py .

# Test the system
python .claude/scripts/test_system.py

# Make your first validated commit
git add .
git commit -m "Add new feature"  # Agents run automatically!
```

### 🔒 Completely User-Specific

**Important:** This framework is a **personal development tool** - nothing gets committed.

- ✅ Framework stays in `~/agentic-setup` (or wherever you cloned it)
- ✅ Generated files (`.claude/`, `CLAUDE.md`) are automatically added to `.gitignore`
- ✅ Each team member installs separately with their own preferences
- ✅ Zero git noise - project repos contain only project code
- ✅ Optional tool - use it or don't, no coordination needed

**For teams:** Nothing is shared in git. Developers can coordinate via wiki/docs if desired, but the framework is completely optional and personal.

---

## 🎯 What This Is

A universal framework that automatically detects your project's tech stack and instantiates the right agents to ensure:

- **Code Quality:** Every change validated by domain experts
- **Zero Defects:** Security, logic, data integrity all verified
- **Minimal Impact:** Changes kept small and focused
- **Documentation:** Always current, never stale
- **Standards:** Enforced consistently across codebase

### Auto-Detection

The framework scans your codebase and automatically enables relevant agents based on:
- Programming languages detected
- Frameworks and libraries used
- Project type (web, API, ML, data pipeline, etc.)
- Existing tooling and patterns

---

## 🤖 Default Agents (Always Enabled)

These agents apply to ANY codebase:

| Agent | Core Role | Triggers | Veto Condition |
|-------|-----------|----------|----------------|
| **Data Agent** | Validates inputs, file formats, API schemas | `.csv`, `.json`, `.env`, migrations | Corrupt or missing input data |
| **Logic Agent** | Ensures core logic correctness and flow | `.ts`, `.py`, `.js`, `.go` | Failing tests or invalid logic |
| **Test Agent** | Enforces test coverage and regression control | `/tests/`, `.spec.*`, `.test.*` | Coverage < 80%, or missing cases |
| **Security Agent** | Scans for secrets, injections, vulnerable deps | All code changes | Found secret or high CVE |
| **Infra Agent** | Checks build, containers, and CI/CD safety | `.yaml`, `.tf`, `Dockerfile` | Unsafe permissions or violations |
| **Doc Agent** | Verifies docs and README sync with code | `README`, `/docs`, `.md` | Missing or outdated docs |

---

## 🔧 Optional Agents

These agents are enabled automatically when relevant patterns are detected:

### Core Optional Agents

| Agent | Purpose | Auto-Enabled When | Veto Triggers |
|-------|---------|-------------------|---------------|
| **Performance Agent** | Runtime efficiency, profiling, algorithmic complexity | APIs, backend services, data pipelines detected | CPU >80%, memory >75%, latency >300ms |
| **Refactor Agent** | Code structure and maintainability | Mature repos with tech debt | Maintainability index <85 |
| **Observability Agent** | Logging, tracing, metrics validation | Backend or distributed systems | Missing logs, coverage <90% critical paths |
| **Research Agent** | Monitors new patterns or libraries | Fast-moving stacks (AI/ML) | Updates <1 month old |
| **DevEx Agent** | DX productivity and tooling | Any team-scale repo | PR cycle >24h |

### Extended Optional Agents

<details>
<summary>Click to see all optional agents</summary>

- **UX/Accessibility Agent** - UI/UX flow, WCAG 2.1 AA compliance (frontend repos)
- **Error Handling Agent** - Robustness and failure tolerance (production codebases)
- **Dependency Agent** - Package hygiene and version stability (JS, Python, package managers)
- **Build Agent** - CI/CD speed and determinism (CI/CD-intensive projects)
- **Cost Agent** - Cloud cost optimization (cloud, serverless, ML projects)
- **Knowledge Agent** - Context capture and internal wiki updates (fast iteration teams)
- **Ethics/Compliance Agent** - Regulatory or ethical constraints (fintech, healthcare, research)
- **Benchmark Agent** - Performance baselining & regression detection (high-performance systems)
- **Security Red-Team Agent** - Ethical penetration and attack simulation (customer-facing apps)
- **Human Oversight Agent** - Acts as a final arbiter (enterprise pipelines)

</details>

---

## 🏗️ System Architecture

```
┌─────────────────────────────────┐
│   ORCHESTRATOR (Claude Opus)    │
│    Coordinates all agents        │
└────────────┬────────────────────┘
             │
    ┌────────▼────────┐
    │  AGENT LAYER    │
    │  (Sonnet 4.5)   │
    └────────┬────────┘
             │
    ┌────────▼────────────────────────┐
    │    Unanimous Consensus           │
    │  (All active agents approve)     │
    └────────┬────────────────────────┘
             │
    ┌────────▼────────┐
    │  CODE EXECUTION │
    └─────────────────┘
```

### Three-Tier Implementation
1. **Skills Layer** - Reusable patterns and tools (HOW)
2. **Agent Layer** - Quality validation and standards (WHEN)
3. **Execution Layer** - Core business logic (WHAT)

---

## 📦 Installation & Plugin Setup

### Prerequisites
- Python 3.8+
- Git repository
- Claude Code CLI or API access
- 1GB free disk space

### Step 1: Install Framework

```bash
python agentic_setup/scripts/implement_framework.py .
```

This automatically:
- Scans your codebase to detect tech stack
- Enables default agents (6 core agents)
- Enables relevant optional agents
- Creates `.claude/` directory structure
- Configures Git hooks for validation
- Sets up slash commands
- Creates helper scripts

### Step 2: Install Compound Engineering Agents

Compound Engineering provides specialized Claude Code agents that integrate with this framework:

```bash
# Available agents:
# - kieran-rails-reviewer (Rails projects)
# - kieran-typescript-reviewer (TypeScript/React projects)
# - kieran-python-reviewer (Python projects)
# - dhh-rails-reviewer (Rails with DHH's conventions)
# - architecture-strategist
# - performance-oracle
# - security-sentinel
# - data-integrity-guardian

# These are already available in Claude Code's Task tool
# Configuration is in your CLAUDE.md
```

**To use Compound Engineering agents:**
1. They're invoked via Claude Code's `Task` tool with `subagent_type` parameter
2. They integrate automatically with your local agents
3. Configure which ones to use in `.claude/config.py`

**Example configuration:**

```python
# .claude/config.py
COMPOUND_ENGINEERING_AGENTS = {
    "enabled": True,
    "agents": [
        "kieran-python-reviewer",  # If Python project
        "architecture-strategist",
        "performance-oracle",
        "security-sentinel"
    ],
    "auto_invoke": {
        "kieran-python-reviewer": ["after_implementation"],
        "security-sentinel": ["before_commit"]
    }
}
```

### Step 3: Install Superpowers (Optional)

Superpowers are productivity-enhancing Claude Code extensions:

**What are Superpowers?**
- Enhanced context management (smart compaction)
- Intelligent code navigation
- Advanced refactoring capabilities
- Pattern recognition and suggestions

**Installation:**

Superpowers are installed via Claude Code settings:

1. **Enable Superpowers Mode:**
   ```bash
   # Add to .claude/config.py
   SUPERPOWERS_ENABLED = True
   SUPERPOWERS_MODE = "enhanced"  # or "standard", "minimal"
   ```

2. **Configure Features:**
   ```python
   SUPERPOWERS_CONFIG = {
       "smart_compaction": {
           "enabled": True,
           "threshold": 150000,  # Compact at 150K tokens
           "preserve_priority": ["current_task", "agent_standards", "recent_vetoes"]
       },
       "intelligent_navigation": {
           "enabled": True,
           "auto_jump_to_relevant": True
       },
       "pattern_recognition": {
           "enabled": True,
           "learn_from_vetoes": True
       }
   }
   ```

3. **Activate in Claude Prompt:**
   The master prompt (automatically created) includes superpowers directives.

---

## 🎮 Usage

### Claude Commands

After installation, use these slash commands:

```
/review          - Run full agent review
/consensus       - Get unanimous consensus
/agent-status    - Show agent metrics
/detect-agents   - Re-scan project and suggest agents
```

### Git Integration

The system automatically validates on commit:

```bash
# Normal commit (runs validation)
git add .
git commit -m "Your message"

# If validation fails:
❌ Commit blocked by: security-agent, test-agent

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

### Adjust Agent Sensitivity

```python
# .claude/config.py
AGENT_CONFIG = {
    "quality_standards": {
        "test_coverage_minimum": 80,  # Adjust this
        "max_complexity": 10,          # Adjust this
        "max_pr_lines": 500           # Adjust this
    }
}
```

### Enable/Disable Agents

```bash
# Edit agent list
vim .claude/config.py

# Add agent to AGENTS list
AGENTS.append("performance-agent")

# Or disable an agent
AGENTS.remove("doc-agent")
```

### Add Custom Agents

```bash
# Create new agent structure
mkdir -p .claude/skills/custom-agent/{PATTERNS,CHECKLISTS,VALIDATION,SCRIPTS}

# Create SKILL.md
vim .claude/skills/custom-agent/SKILL.md

# Update config
echo 'AGENTS.append("custom-agent")' >> .claude/config.py
```

---

## 📊 Metrics & Monitoring

The system tracks:
- Agent approval/veto rates
- Common veto reasons
- Resolution times
- Code quality trends

```bash
python .claude/scripts/agent_metrics.py
```

---

## 🚦 Best Practices

1. **Start Small** - Begin with 6 default agents
2. **Let Auto-Detection Work** - Trust the scanner
3. **Tune Standards** - Adjust based on your team
4. **Document Vetoes** - Learn from patterns
5. **Regular Reviews** - Check metrics weekly
6. **Iterate** - Continuously improve

---

## 📁 Directory Structure After Installation

```
your-project/
├── .claude/
│   ├── agents/              # Agent configurations
│   ├── skills/              # Agent skills (auto-generated)
│   ├── commands/            # Slash commands
│   ├── scripts/             # Helper scripts
│   ├── metrics/             # Performance tracking
│   └── config.py            # Main configuration
├── .git/hooks/
│   ├── pre-commit           # Validation hook
│   └── post-commit          # Metrics hook
└── CLAUDE.md                # Main configuration doc
```

---

## 🆘 Support

- **Documentation:** See `COMPLETE_SETUP_GUIDE.md`
- **Agent Details:** Check `.claude/skills/*/SKILL.md`
- **Templates:** Look in `templates/` directory
- **Troubleshooting:** See troubleshooting section in guide

---

## 📝 License

This framework is open source and available for use in any project.

---

**Created by:** Universal Agent Detection System
**Version:** 3.0
**Last Updated:** November 6, 2025
