#!/usr/bin/env python3
"""
APM (Agentic Project Management) Installer for GitHub Copilot
Integrates APM workflow with repository-aware guidance, chat modes, and prompt files.
"""

import os
import json
import shutil
import subprocess
from pathlib import Path
from datetime import datetime


class APMInstaller:
    """Install APM-enhanced GitHub Copilot configuration."""

    def __init__(self, repo_path: str):
        self.repo_path = Path(repo_path).resolve()
        self.github_dir = self.repo_path / ".github"
        self.vscode_dir = self.repo_path / ".vscode"
        self.analysis = self._load_or_create_analysis()

    def _load_or_create_analysis(self) -> dict:
        """Load existing analysis or create a basic one."""
        analysis_path = self.repo_path / ".copilot/analysis.json"

        if analysis_path.exists():
            with open(analysis_path) as f:
                return json.load(f)

        # Basic defaults if no analysis
        return {
            "languages": {"TypeScript": 0, "JavaScript": 0, "Python": 0},
            "frameworks": [],
            "patterns": []
        }

    def run(self):
        """Execute full APM installation."""
        print("🚀 APM-Enhanced GitHub Copilot Setup")
        print("="*50)

        steps = [
            ("Installing APM CLI globally", self.install_apm_cli),
            ("Initializing APM in repository", self.init_apm),
            ("Creating VS Code settings", self.create_vscode_settings),
            ("Installing repository instructions", self.create_repo_instructions),
            ("Creating AGENTS.md", self.create_agents_md),
            ("Setting up chat modes", self.create_chat_modes),
            ("Installing prompt files", self.create_prompt_files),
            ("Creating issue templates", self.create_issue_templates),
            ("Setting up helper scripts", self.create_helper_scripts),
            ("Updating .gitignore", self.update_gitignore)
        ]

        for step_name, step_func in steps:
            print(f"\n📍 {step_name}...")
            try:
                step_func()
                print(f"   ✅ {step_name} complete")
            except Exception as e:
                print(f"   ⚠️  {step_name} warning: {e}")

        print("\n" + "="*50)
        print("✨ APM Setup Complete!")
        print("\n🎯 Quick Start:")
        print("1. Open VS Code in this repository")
        print("2. Open Copilot Chat (Cmd/Ctrl + I)")
        print("3. Type '/' to see available commands:")
        print("   - /repo-assess - Analyze your codebase")
        print("   - /apm-plan - Create implementation plan")
        print("   - /apm-implement - Execute the plan")
        print("   - /apm-verify - Review and validate")
        print("\n4. Or switch chat modes for specialized personas:")
        print("   - Plan Mode - Strategic planning")
        print("   - Implement Mode - Tactical execution")
        print("   - Review Mode - Quality verification")

        return True

    def install_apm_cli(self):
        """Install the APM CLI globally."""
        try:
            # Check if npm/pnpm/yarn exists
            pkg_managers = ["npm", "pnpm", "yarn"]
            pkg_manager = None

            for pm in pkg_managers:
                result = subprocess.run(
                    [pm, "--version"],
                    capture_output=True,
                    text=True
                )
                if result.returncode == 0:
                    pkg_manager = pm
                    break

            if not pkg_manager:
                print("   ℹ️  No Node.js package manager found, skipping APM CLI")
                return

            # Install APM globally
            if pkg_manager == "npm":
                cmd = ["npm", "install", "-g", "agentic-pm"]
            elif pkg_manager == "pnpm":
                cmd = ["pnpm", "add", "-g", "agentic-pm"]
            else:  # yarn
                cmd = ["yarn", "global", "add", "agentic-pm"]

            print(f"   Installing with {pkg_manager}...")
            subprocess.run(cmd, check=False, capture_output=True)

        except Exception as e:
            print(f"   ℹ️  APM CLI installation optional: {e}")

    def init_apm(self):
        """Initialize APM in the repository."""
        try:
            # Check if apm is available
            result = subprocess.run(
                ["apm", "--version"],
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                # Run apm init
                subprocess.run(
                    ["apm", "init"],
                    cwd=self.repo_path,
                    input="1\n",  # Select GitHub Copilot option
                    text=True,
                    capture_output=True
                )
                print("   APM initialized with GitHub Copilot support")
            else:
                print("   ℹ️  APM CLI not found, using built-in prompts")

        except Exception:
            print("   ℹ️  Skipping APM init, will use our prompt templates")

    def create_vscode_settings(self):
        """Create comprehensive VS Code settings."""
        self.vscode_dir.mkdir(exist_ok=True)

        settings = {
            # Enable prompt files
            "chat.promptFiles": True,

            # Show agent sessions in dedicated view
            "chat.agentSessionsViewLocation": "view",

            # Enable Copilot Coding Agent UI
            "githubPullRequests.codingAgent.uiIntegration": True,

            # Copilot settings
            "github.copilot.enable": {
                "*": True,
                "yaml": True,
                "markdown": True,
                "json": True,
                "dockerfile": True
            },

            # Advanced settings
            "github.copilot.advanced": {
                "debug.overrideEngine": "gpt-4",
                "contextWindow": 8000
            },

            # Editor settings
            "editor.inlineSuggest.enabled": True,
            "github.copilot.editor.enableAutoCompletions": True,

            # Optional prompt locations
            "chat.promptFilesLocations": [
                ".github/prompts",
                "docs/prompts",
                ".copilot/prompts"
            ]
        }

        settings_path = self.vscode_dir / "settings.json"

        # Merge with existing if present
        if settings_path.exists():
            with open(settings_path) as f:
                existing = json.load(f)
            settings = {**existing, **settings}

        with open(settings_path, 'w') as f:
            json.dump(settings, f, indent=2)

    def create_repo_instructions(self):
        """Create repository custom instructions."""
        self.github_dir.mkdir(exist_ok=True)

        # Main instructions
        copilot_instructions = f"""---
applyTo: "**"
---
# Repository Custom Instructions

You are an agentic assistant working in this repository.
Follow these global rules:

## Core Principles

- **Agentic by default**: For non-trivial tasks, propose a plan → get approval → execute iteratively
- **Test-Driven Development**: Write failing tests first when appropriate (red → green → refactor)
- **Codebase awareness**: Read existing docs (`README.md`, `docs/**`, `ARCHITECTURE.md`, ADRs) and scan #codebase before changes
- **Minimal diffs**: Prefer small, reviewable PRs; avoid large rewrites unless requested
- **Security first**: No secrets in code, use environment variables, consider security implications
- **Performance aware**: Consider performance baselines, measure where applicable
- **Documentation**: Update affected docs and READMEs with rationale and usage examples

## Technical Standards

### Language/Stack
- Primary languages: {', '.join(self.analysis.get('languages', {}).keys()) or 'TypeScript, Python'}
- Respect existing toolchain (linters, formatters, build tools)
- Follow established patterns in the codebase

### Testing
- Add/modify tests for each change
- Surface coverage deltas and critical paths
- Aim for >80% coverage on new code
- Keep tests fast and isolated

### Code Quality
- Follow existing code style and conventions
- Use meaningful variable and function names
- Add comments for complex logic
- Prefer composition over inheritance
- Keep functions small and focused

## Workflow

1. **Discovery**: Use #codebase, #githubRepo, and #fetch to understand context
2. **Planning**: Create step-by-step plans with file references
3. **Implementation**: Apply minimal diffs with tests
4. **Verification**: Ensure tests pass, update docs

When uncertain, ask for constraints or propose alternatives with tradeoffs.
"""

        with open(self.github_dir / "copilot-instructions.md", 'w') as f:
            f.write(copilot_instructions)

        # Path-specific instructions
        instructions_dir = self.github_dir / "instructions"
        instructions_dir.mkdir(exist_ok=True)

        # Backend instructions
        if any(p in self.analysis.get("patterns", []) for p in ["api", "backend", "server"]):
            backend_instructions = """---
applyTo: "services/**,src/**/server/**,api/**,backend/**"
---
# Backend Instructions

- Follow existing domain/service boundaries
- API changes must update OpenAPI schemas and integration tests
- Enforce logging/metrics conventions
- Keep request handlers thin - business logic in services
- Use dependency injection where established
- Validate all inputs at boundaries
- Handle errors gracefully with proper status codes
"""
            with open(instructions_dir / "backend.instructions.md", 'w') as f:
                f.write(backend_instructions)

        # Frontend instructions
        if any(p in self.analysis.get("patterns", []) for p in ["frontend", "ui", "web"]):
            frontend_instructions = """---
applyTo: "apps/**,src/**/web/**,client/**,frontend/**,components/**"
---
# Frontend Instructions

- Use existing UI library and design system
- State management must align with current approach
- Add accessibility attributes (ARIA labels, semantic HTML)
- Optimize for Core Web Vitals
- Add loading and error states
- Create reusable components
- Add Storybook stories for new components (if applicable)
"""
            with open(instructions_dir / "frontend.instructions.md", 'w') as f:
                f.write(frontend_instructions)

        # Test instructions
        test_instructions = """---
applyTo: "**/*.{spec,test}.{ts,tsx,js,jsx,py}"
---
# Test Instructions

- Write failing tests first for bugfixes (red → green)
- Aim for fast, isolated unit tests - mock external dependencies
- Keep tests deterministic - avoid time/network flakiness
- Use descriptive test names that explain the behavior
- Group related tests in describe/context blocks
- Include edge cases and error scenarios
- Add integration tests for critical paths
"""
        with open(instructions_dir / "tests.instructions.md", 'w') as f:
            f.write(test_instructions)

        # Database/migration instructions
        if any(p in self.analysis.get("patterns", []) for p in ["database", "models"]):
            db_instructions = """---
applyTo: "**/migrations/**,**/models/**,**/schemas/**,**/db/**"
---
# Database Instructions

- All schema changes require migrations
- Migrations must be reversible
- Add indexes for foreign keys and frequently queried columns
- Use transactions for data integrity
- Validate data at application layer
- Consider query performance implications
- Document schema changes in migrations
"""
            with open(instructions_dir / "database.instructions.md", 'w') as f:
                f.write(db_instructions)

    def create_agents_md(self):
        """Create AGENTS.md for agent guidance."""
        agents_content = """# AGENTS.md — Roles & Guardrails

## Agent Roles

### 🎯 Planner
- Produces step-by-step plans referencing repo files (#codebase) and docs
- Identifies dependencies and risks
- Proposes alternatives with tradeoffs
- Estimates effort and complexity
- Creates acceptance criteria

### 🛠️ Implementer
- Applies small, reviewable edits consistent with the plan
- Writes tests first (TDD approach)
- Keeps commits atomic and well-described
- Refactors only when tests are green
- Updates documentation inline

### 🔍 Reviewer
- Audits for security vulnerabilities and performance issues
- Verifies test coverage and quality
- Ensures documentation is updated
- Checks for breaking changes
- Validates against acceptance criteria

### 📚 Researcher
- Gathers upstream references using #fetch / #githubRepo
- Summarizes best practices and patterns
- Identifies similar implementations
- Researches library updates and alternatives
- Documents findings for future reference

### 🧪 Tester
- Creates comprehensive test suites
- Identifies edge cases and error scenarios
- Ensures test isolation and determinism
- Validates performance requirements
- Documents test scenarios

## Guardrails

### Security
- Never expose secrets, API keys, or passwords
- Use environment variables for sensitive configuration
- Validate and sanitize all user inputs
- Follow OWASP best practices
- Review dependencies for known vulnerabilities

### Quality
- Prefer incremental PRs with clear rationale
- Include tests for all changes
- Update documentation and examples
- Follow established patterns and conventions
- Consider performance implications

### Process
- Get explicit approval before risky operations
- Create backups before destructive changes
- Test in development before production
- Document rollback procedures
- Maintain audit trails in commits

### Communication
- Explain reasoning and tradeoffs
- Ask for clarification when uncertain
- Provide progress updates on long tasks
- Document assumptions and decisions
- Include screenshots/recordings for UI changes

## Tool Usage

### Available Tools
- `#codebase` - Search and read repository files
- `#githubRepo` - Access GitHub repository information
- `#fetch` - Retrieve external documentation
- `#problems` - Check for errors and warnings
- `#terminal` - Execute commands (with approval)
- `#file` - Read/write files

### Tool Constraints by Mode
- **Plan Mode**: Read-only tools (#codebase, #fetch, #githubRepo)
- **Implement Mode**: All tools available
- **Review Mode**: Read-only + #problems
- **Research Mode**: #fetch, #githubRepo primarily

## Success Metrics
- Tests pass (100% green)
- Coverage maintained or improved
- No security vulnerabilities introduced
- Documentation updated
- PR size < 500 lines
- Build time stable
- Performance benchmarks met
"""

        with open(self.github_dir / "AGENTS.md", 'w') as f:
            f.write(agents_content)

    def create_chat_modes(self):
        """Create custom chat modes for specialized personas."""
        chatmodes_dir = self.github_dir / "chatmodes"
        chatmodes_dir.mkdir(exist_ok=True)

        # Plan mode
        plan_mode = """---
description: "Strategic planning mode - generates implementation plans from repo context"
tools: ["fetch", "githubRepo", "codebase"]
handoffs:
  - label: "Implement Plan"
    agent: "implement"
    prompt: "Execute this plan with minimal, reviewable edits and tests"
    send: false
  - label: "Research Further"
    agent: "research"
    prompt: "Research best practices and alternatives for this approach"
    send: false
---
# Planning Mode

You are in strategic planning mode. Your role is to:

## 1. Context Gathering
- Read `README.md`, `ARCHITECTURE.md`, and relevant documentation
- Scan the codebase structure using #codebase
- Review recent issues and PRs if linked
- Understand existing patterns and conventions

## 2. Plan Creation
Generate a comprehensive Markdown plan including:

### Scope & Objectives
- Clear problem statement
- Success criteria and metrics
- Assumptions and constraints
- Out of scope items

### Technical Approach
- Architecture decisions
- Technology choices with rationale
- Integration points
- Data flow and state management

### Implementation Phases
Break down into small, testable increments:
1. Phase 1: Foundation (schemas, interfaces)
2. Phase 2: Core functionality
3. Phase 3: Edge cases and error handling
4. Phase 4: Performance optimization
5. Phase 5: Documentation and examples

### For Each Phase
- Affected files/modules (with #codebase references)
- Test strategy (unit/integration/e2e)
- Rollback plan
- Estimated effort

### Risk Analysis
- Technical risks and mitigations
- Dependencies and blockers
- Performance implications
- Security considerations

### Alternatives Considered
- Other approaches with pros/cons
- Why this approach was chosen
- Future optimization opportunities

## 3. Output Format
Present the plan in a clear, actionable format with:
- Numbered steps
- File references
- Code examples where helpful
- Decision points marked clearly
"""
        with open(chatmodes_dir / "plan.chatmode.md", 'w') as f:
            f.write(plan_mode)

        # Implement mode
        implement_mode = """---
description: "Tactical implementation mode - executes plans with TDD approach"
handoffs:
  - label: "Review Implementation"
    agent: "review"
    prompt: "Review this implementation for quality, security, and completeness"
    send: false
  - label: "Plan Next Phase"
    agent: "plan"
    prompt: "Plan the next phase of implementation"
    send: false
---
# Implementation Mode

You are in tactical implementation mode. Your approach:

## Principles
1. **Test-Driven Development (TDD)**
   - Write failing tests first (red)
   - Implement minimal code to pass (green)
   - Refactor while keeping tests green

2. **Incremental Progress**
   - Small, atomic commits
   - Each commit should leave the codebase functional
   - Push frequently to enable collaboration

3. **Continuous Validation**
   - Run tests after each change
   - Check linters and formatters
   - Verify no regressions

## Workflow

### Step 1: Setup
- Review the approved plan
- Set up development environment
- Create feature branch

### Step 2: Test First
For each requirement:
1. Write a failing test that describes the behavior
2. Run test to confirm it fails (red)
3. Implement minimal code to pass
4. Run test to confirm it passes (green)
5. Refactor if needed (keeping green)

### Step 3: Implementation Patterns
- Keep functions small and focused
- Use meaningful names
- Add error handling at boundaries
- Log important operations
- Update types/interfaces

### Step 4: Documentation
- Add/update JSDoc or docstrings
- Update README if needed
- Add inline comments for complex logic
- Create examples if applicable

### Step 5: Quality Checks
Before marking complete:
- All tests passing
- Coverage maintained/improved
- No linting errors
- Documentation updated
- Manual testing done

## Error Handling
When tests fail:
1. Read error carefully
2. Fix the implementation (not the test, unless test is wrong)
3. Re-run to confirm fix
4. Add edge case tests

## Progress Tracking
- ✅ Completed items
- 🚧 In progress
- 📝 TODO items
- ❌ Blocked items (with reason)
"""
        with open(chatmodes_dir / "implement.chatmode.md", 'w') as f:
            f.write(implement_mode)

        # Review mode
        review_mode = """---
description: "Quality review mode - validates implementation against standards"
tools: ["codebase", "fetch", "githubRepo", "problems"]
handoffs:
  - label: "Fix Issues"
    agent: "implement"
    prompt: "Fix the issues identified in this review"
    send: false
  - label: "Document Changes"
    agent: "document"
    prompt: "Update documentation based on these changes"
    send: false
---
# Review Mode

You are in quality review mode. Perform comprehensive validation:

## Review Checklist

### 1. Correctness
- [ ] Implementation matches requirements
- [ ] All acceptance criteria met
- [ ] Edge cases handled
- [ ] Error scenarios covered
- [ ] No regressions introduced

### 2. Testing
- [ ] Test coverage ≥80% for new code
- [ ] Tests are meaningful (not just coverage)
- [ ] Tests are isolated and fast
- [ ] Integration tests for critical paths
- [ ] Tests follow naming conventions

### 3. Security
- [ ] No hardcoded secrets
- [ ] Input validation present
- [ ] SQL injection prevention
- [ ] XSS prevention
- [ ] CSRF protection (if applicable)
- [ ] Rate limiting considered
- [ ] Dependencies scanned for vulnerabilities

### 4. Performance
- [ ] No N+1 queries
- [ ] Appropriate indexes
- [ ] Caching utilized where beneficial
- [ ] Bundle size impact assessed
- [ ] Memory leaks prevented
- [ ] Async operations optimized

### 5. Code Quality
- [ ] Follows established patterns
- [ ] No code duplication
- [ ] Functions are focused
- [ ] Naming is clear and consistent
- [ ] Comments explain why, not what
- [ ] TODO items tracked

### 6. Documentation
- [ ] README updated if needed
- [ ] API documentation current
- [ ] Changelog entry added
- [ ] Migration guide (if breaking changes)
- [ ] Examples updated

### 7. Accessibility (Frontend)
- [ ] Semantic HTML used
- [ ] ARIA labels present
- [ ] Keyboard navigation works
- [ ] Screen reader friendly
- [ ] Contrast ratios met

## Review Output

### Summary
- Overall assessment (Approve/Request Changes)
- Strengths of the implementation
- Areas for improvement

### Critical Issues (Must Fix)
List with severity and suggested fixes

### Suggestions (Nice to Have)
Improvements for consideration

### Follow-up Items
Future enhancements or tech debt to track

## PR Description Template
Generate a PR description with:
```markdown
## Summary
[What changed and why]

## Implementation Notes
- Key design decisions
- Tradeoffs made
- Interesting challenges

## Testing
- Test coverage: X%
- Manual testing performed
- Edge cases covered

## Screenshots/Demo
[If applicable]

## Breaking Changes
[If any]

## Follow-up Items
- [ ] Future optimizations
- [ ] Tech debt to address
```
"""
        with open(chatmodes_dir / "review.chatmode.md", 'w') as f:
            f.write(review_mode)

        # Research mode
        research_mode = """---
description: "Research mode - investigates best practices and alternatives"
tools: ["fetch", "githubRepo", "codebase"]
handoffs:
  - label: "Create Plan"
    agent: "plan"
    prompt: "Create an implementation plan based on this research"
    send: false
---
# Research Mode

You are in research mode. Investigate thoroughly:

## Research Areas

### 1. Best Practices
- Industry standards
- Framework/library recommendations
- Security guidelines
- Performance patterns
- Testing strategies

### 2. Similar Implementations
- How others solved this
- Open source examples
- Case studies
- Lessons learned

### 3. Technology Evaluation
- Available libraries/tools
- Pros and cons
- Community support
- Maintenance status
- License compatibility

### 4. Documentation Review
- Official documentation
- Tutorials and guides
- Stack Overflow insights
- GitHub discussions
- Blog posts/articles

## Output Format

### Executive Summary
- Key findings
- Recommended approach
- Critical considerations

### Detailed Findings
For each option researched:
- Description
- Pros and cons
- Example code
- Performance implications
- Maintenance burden

### Recommendations
- Primary recommendation with rationale
- Alternative approaches
- Risk mitigation strategies
- Implementation complexity

### Resources
- Links to documentation
- Example repositories
- Relevant articles
- Community discussions
"""
        with open(chatmodes_dir / "research.chatmode.md", 'w') as f:
            f.write(research_mode)

    def create_prompt_files(self):
        """Create reusable prompt files for APM workflow."""
        prompts_dir = self.github_dir / "prompts"
        prompts_dir.mkdir(exist_ok=True)

        # Repository assessment
        repo_assess = """---
description: "Comprehensive repository assessment - analyze structure, stack, and patterns"
mode: "plan"
tools: ["codebase", "githubRepo", "fetch"]
---
# Repository Assessment

Perform a comprehensive analysis of this repository.

## Tasks

1. **Documentation Review**
   - Read `README.md`, `CONTRIBUTING.md`, `ARCHITECTURE.md`
   - Check for ADRs (Architecture Decision Records)
   - Review API documentation
   - Scan changelog/release notes

2. **Technology Stack Analysis**
   - Identify programming languages and versions
   - List frameworks and major libraries
   - Detect build tools and package managers
   - Note testing frameworks
   - Check CI/CD configuration

3. **Architecture Discovery**
   - Map folder structure and module boundaries
   - Identify architectural patterns (MVC, microservices, etc.)
   - Detect service boundaries and APIs
   - Note data flow and state management
   - Find configuration and environment setup

4. **Code Quality Assessment**
   - Check test coverage if available
   - Review linting/formatting configuration
   - Identify code complexity hotspots
   - Note technical debt markers (TODOs, FIXMEs)
   - Assess documentation coverage

5. **Development Workflow**
   - Review branch protection rules
   - Check PR templates and processes
   - Note deployment strategies
   - Identify environments (dev/staging/prod)

## Output

### Stack Summary
```yaml
languages:
  - name: version
frameworks:
  - name: version
build_tools:
  - tool: version
testing:
  - framework: config_file
ci_cd:
  - platform: config_file
```

### Architecture Map
```
project-root/
├── apps/          # [Description]
├── packages/      # [Description]
├── services/      # [Description]
└── infrastructure/# [Description]
```

### Quality Metrics
- Test Coverage: X%
- Linting: Configured/Missing
- Type Safety: Full/Partial/None
- Documentation: Comprehensive/Adequate/Sparse

### Recommended Instructions
Propose `.github/instructions/*.instructions.md` files with appropriate `applyTo` globs.

### Risk Register
| Risk | Severity | Mitigation |
|------|----------|------------|
| Security | High/Med/Low | Proposed action |
| Performance | High/Med/Low | Proposed action |
| Debt | High/Med/Low | Proposed action |

### Immediate Actions
1. [ ] Quick wins (< 1 hour)
2. [ ] Important fixes (< 1 day)
3. [ ] Strategic improvements (> 1 day)
"""
        with open(prompts_dir / "repo-assess.prompt.md", 'w') as f:
            f.write(repo_assess)

        # APM Plan
        apm_plan = """---
description: "Create detailed implementation plan using APM methodology"
mode: "plan"
tools: ["codebase", "fetch", "githubRepo"]
---
# APM Planning

Create a comprehensive implementation plan using Agentic Project Management methodology.

## Input Required
- Goal/requirement description
- Constraints and non-negotiables
- Success criteria

## Planning Process

### 1. Validate Requirements
- Clarify ambiguous requirements
- Identify implicit requirements
- Confirm success criteria
- Note assumptions

### 2. Discovery Phase
- Review existing code that will be modified
- Identify integration points
- Check for similar implementations
- Review relevant documentation

### 3. Design Phase
- Propose high-level architecture
- Define interfaces and contracts
- Plan data models/schemas
- Design state management
- Create sequence diagrams if complex

### 4. Implementation Plan
Break down into phases:

#### Phase Structure
```markdown
### Phase N: [Name] (Estimated: X hours)
**Goal**: Specific outcome

**Prerequisites**: What must be complete first

**Changes**:
- File: path/to/file.ts
  - Add function X
  - Modify interface Y
  - Update tests

**Tests**:
- Unit: Test descriptions
- Integration: Test scenarios
- E2E: User flows

**Validation**:
- How to verify this phase works
- Metrics to check

**Rollback**:
- How to undo if needed
```

### 5. Test Strategy
- Unit test approach
- Integration test scenarios
- E2E test flows
- Performance tests if applicable
- Load tests if applicable

### 6. Rollout Strategy
- Feature flags needed?
- Gradual rollout plan
- Monitoring requirements
- Rollback triggers

## Output Format

### Executive Summary
- Objective in one sentence
- Approach in 2-3 sentences
- Timeline estimate
- Risk level (Low/Medium/High)

### Detailed Plan
[Structured phases as above]

### Dependencies
- External services
- Other teams/components
- Third-party libraries

### Definition of Done
- [ ] Acceptance criteria checklist
- [ ] Quality gates passed
- [ ] Documentation updated
- [ ] Stakeholders notified

### Metrics for Success
- Performance targets
- User metrics
- Business metrics
- Technical metrics
"""
        with open(prompts_dir / "apm-plan.prompt.md", 'w') as f:
            f.write(apm_plan)

        # APM Implement
        apm_implement = """---
description: "Execute implementation plan with TDD approach"
mode: "implement"
---
# APM Implementation

Execute the approved implementation plan using Test-Driven Development.

## Implementation Protocol

### 1. Pre-Implementation Checklist
- [ ] Plan reviewed and approved
- [ ] Development environment ready
- [ ] Feature branch created
- [ ] Dependencies installed

### 2. TDD Cycle for Each Feature
```
1. RED: Write failing test
   - Describe expected behavior
   - Run test - confirm failure

2. GREEN: Minimal implementation
   - Write just enough code to pass
   - Run test - confirm success

3. REFACTOR: Improve code
   - Clean up implementation
   - Ensure tests still pass
```

### 3. Implementation Guidelines

#### Code Structure
- Keep functions under 20 lines
- Single responsibility principle
- Clear naming conventions
- Consistent error handling

#### Testing Requirements
- Unit tests for all public methods
- Integration tests for workflows
- Edge cases covered
- Error scenarios tested

#### Documentation
- JSDoc/docstrings for public APIs
- README updates for new features
- Inline comments for complex logic
- Examples for non-obvious usage

### 4. Incremental Commits
```bash
# Commit message format
type(scope): description

# Examples
feat(auth): add JWT token validation
fix(api): handle null user response
test(auth): add edge cases for expiry
docs(api): update endpoint documentation
```

### 5. Progress Tracking
After each implementation session, update:

```markdown
## Progress Report
**Date**: [Today]
**Phase**: [Current Phase]

### Completed ✅
- [x] Item 1
- [x] Item 2

### In Progress 🚧
- [ ] Current item (50% done)

### Blocked ❌
- [ ] Item (Reason: waiting for X)

### Next Steps
1. Complete current item
2. Start next phase
```

### 6. Quality Gates
Before moving to next phase:
- All tests green
- No linting errors
- Coverage maintained
- Documentation updated
- Manual testing complete

## Error Recovery
If implementation gets stuck:
1. Review the plan - is it still valid?
2. Check assumptions - what changed?
3. Simplify scope - can we do less?
4. Ask for help - what's unclear?
"""
        with open(prompts_dir / "apm-implement.prompt.md", 'w') as f:
            f.write(apm_implement)

        # APM Verify
        apm_verify = """---
description: "Verify implementation meets requirements and quality standards"
mode: "review"
tools: ["codebase", "problems"]
---
# APM Verification

Validate the implementation against requirements and quality standards.

## Verification Process

### 1. Functional Verification
Compare implementation against requirements:

| Requirement | Implemented | Tested | Notes |
|------------|-------------|---------|--------|
| Feature A  | ✅/❌       | ✅/❌    | Details |

### 2. Test Verification
```
Test Summary:
- Total Tests: X
- Passing: Y
- Coverage: Z%
- Performance: All tests < 100ms

Critical Paths Covered:
- [ ] Happy path
- [ ] Error scenarios
- [ ] Edge cases
- [ ] Concurrent operations
```

### 3. Code Quality Audit

#### Maintainability
- Complexity score: X/10
- Duplication: X%
- Dependencies: Appropriate/Excessive
- Patterns: Consistent/Mixed

#### Security Review
- [ ] No hardcoded secrets
- [ ] Input validation present
- [ ] SQL injection safe
- [ ] XSS protected
- [ ] CSRF handled
- [ ] Rate limiting considered

#### Performance Check
- [ ] Database queries optimized
- [ ] Caching implemented where needed
- [ ] Bundle size acceptable
- [ ] Memory usage stable
- [ ] Response times meet SLA

### 4. Documentation Verification
- [ ] README updated
- [ ] API docs current
- [ ] Changelog entry added
- [ ] Migration guide (if needed)
- [ ] Examples work

### 5. Integration Verification
- [ ] Works with existing systems
- [ ] Backward compatible (or breaking changes documented)
- [ ] Feature flags configured
- [ ] Monitoring in place

## Verification Output

### Status: PASS ✅ / FAIL ❌

### Summary
[2-3 sentences on overall quality]

### Strengths
- Well-tested implementation
- Clear documentation
- Performance optimized

### Issues Found

#### Critical (Must Fix)
1. Issue description → Suggested fix

#### Important (Should Fix)
1. Issue description → Suggested fix

#### Minor (Could Fix)
1. Issue description → Suggested fix

### PR Description
```markdown
## What
[Brief description of changes]

## Why
[Business/technical reason]

## How
[Technical approach taken]

## Testing
- [x] Unit tests added/updated
- [x] Integration tests pass
- [x] Manual testing complete
- Coverage: X%

## Screenshots
[If UI changes]

## Breaking Changes
[If any, with migration guide]

## Checklist
- [x] Tests pass
- [x] Documentation updated
- [x] No security issues
- [x] Performance acceptable
```

### Next Steps
1. Address critical issues
2. Create follow-up tickets for improvements
3. Schedule team review
4. Plan deployment
"""
        with open(prompts_dir / "apm-verify.prompt.md", 'w') as f:
            f.write(apm_verify)

        # Quick fix prompt
        quick_fix = """---
description: "Quick fix for simple bugs or improvements"
mode: "implement"
---
# Quick Fix

For small, well-defined changes (< 1 hour).

## Process
1. Understand the issue
2. Write test that reproduces bug (if bugfix)
3. Implement minimal fix
4. Verify all tests pass
5. Update docs if needed

## Checklist
- [ ] Issue understood
- [ ] Test written
- [ ] Fix implemented
- [ ] Tests pass
- [ ] No regressions
- [ ] Docs updated

Provide concise summary of what was fixed and how.
"""
        with open(prompts_dir / "quick-fix.prompt.md", 'w') as f:
            f.write(quick_fix)

    def create_issue_templates(self):
        """Create issue templates optimized for Copilot Coding Agent."""
        templates_dir = self.github_dir / "ISSUE_TEMPLATE"
        templates_dir.mkdir(exist_ok=True)

        # Copilot task template
        copilot_task = """name: "Copilot Task"
description: "Well-scoped task for GitHub Copilot Coding Agent"
labels: ["copilot", "agentic"]
assignees: []
body:
  - type: markdown
    attributes:
      value: |
        ## Instructions for Copilot Coding Agent
        This issue is designed to be assigned to @copilot for autonomous implementation.

  - type: textarea
    id: objective
    attributes:
      label: "Objective"
      description: "Clear, single-sentence description of what needs to be done"
      placeholder: "Add user authentication with JWT tokens to the API"
    validations:
      required: true

  - type: textarea
    id: context
    attributes:
      label: "Context & Background"
      description: "Link relevant files, PRs, documentation, or related issues"
      placeholder: |
        - Related to #123
        - See docs/api.md for current structure
        - Uses existing User model in models/user.ts

  - type: textarea
    id: requirements
    attributes:
      label: "Requirements"
      description: "Specific technical requirements"
      placeholder: |
        - Use existing JWT library (already in package.json)
        - Add middleware to protect routes
        - Include refresh token logic
        - Store tokens securely

  - type: textarea
    id: acceptance
    attributes:
      label: "Definition of Done"
      description: "Checklist of verifiable outcomes"
      placeholder: |
        - [ ] JWT authentication implemented
        - [ ] Protected routes return 401 without token
        - [ ] Tokens expire after 1 hour
        - [ ] Refresh endpoint works
        - [ ] Tests cover all auth flows
        - [ ] Documentation updated
      value: |
        - [ ] Implementation complete
        - [ ] Tests written and passing
        - [ ] Documentation updated
        - [ ] No breaking changes (or documented if necessary)

  - type: textarea
    id: constraints
    attributes:
      label: "Constraints & Considerations"
      description: "Technical constraints, performance requirements, or security considerations"
      placeholder: |
        - Must be backward compatible
        - Response time < 100ms
        - Follow existing code patterns
        - No new dependencies without approval

  - type: dropdown
    id: priority
    attributes:
      label: "Priority"
      options:
        - "Low"
        - "Medium"
        - "High"
        - "Critical"
    validations:
      required: true

  - type: dropdown
    id: estimated_complexity
    attributes:
      label: "Estimated Complexity"
      description: "How complex is this task?"
      options:
        - "Simple (< 2 hours)"
        - "Medium (2-8 hours)"
        - "Complex (> 8 hours)"
    validations:
      required: true

  - type: textarea
    id: test_approach
    attributes:
      label: "Testing Approach"
      description: "How should this be tested?"
      placeholder: |
        - Unit tests for auth functions
        - Integration tests for protected endpoints
        - E2E test for login flow
"""
        with open(templates_dir / "copilot-task.yml", 'w') as f:
            f.write(copilot_task)

        # Bug report template
        bug_report = """name: "Bug Report"
description: "Report a bug for fixing (can be assigned to @copilot)"
labels: ["bug"]
body:
  - type: textarea
    id: description
    attributes:
      label: "Bug Description"
      description: "Clear description of the bug"
    validations:
      required: true

  - type: textarea
    id: reproduction
    attributes:
      label: "Steps to Reproduce"
      description: "How to reproduce the issue"
      placeholder: |
        1. Go to /api/users
        2. Send POST with invalid data
        3. See 500 error instead of 400
    validations:
      required: true

  - type: textarea
    id: expected
    attributes:
      label: "Expected Behavior"
      description: "What should happen instead"
    validations:
      required: true

  - type: textarea
    id: actual
    attributes:
      label: "Actual Behavior"
      description: "What actually happens"
    validations:
      required: true

  - type: textarea
    id: environment
    attributes:
      label: "Environment"
      description: "Version, OS, browser, etc."
      placeholder: |
        - Version: 1.2.3
        - OS: macOS 14
        - Node: 20.x

  - type: textarea
    id: fix_hints
    attributes:
      label: "Possible Fix"
      description: "Any hints about where/how to fix"
      placeholder: "The issue might be in controllers/user.ts line 45"
"""
        with open(templates_dir / "bug-report.yml", 'w') as f:
            f.write(bug_report)

    def create_helper_scripts(self):
        """Create helper scripts for APM workflow."""
        scripts_dir = self.github_dir / "scripts"
        scripts_dir.mkdir(exist_ok=True)

        # Path glob generator
        derive_globs = """#!/usr/bin/env node
/**
 * Derive applyTo globs for path-specific instructions
 * Run: node .github/scripts/derive-globs.js
 */

const fs = require('fs').promises;
const path = require('path');

async function main() {
  const root = process.cwd();
  const candidates = [
    'apps', 'packages', 'services', 'src',
    'server', 'client', 'web', 'api',
    'backend', 'frontend', 'components',
    'lib', 'utils', 'models', 'controllers'
  ];

  const found = [];

  for (const dir of candidates) {
    const dirPath = path.join(root, dir);
    try {
      const stat = await fs.stat(dirPath);
      if (stat.isDirectory()) {
        found.push(dir);
      }
    } catch {}
  }

  console.log('📁 Detected directories:', found.join(', '));
  console.log('\\nSuggested applyTo globs:\\n');

  const suggestions = {
    backend: generateBackendGlob(found),
    frontend: generateFrontendGlob(found),
    tests: '**/*.{test,spec}.{ts,tsx,js,jsx}',
    models: generateModelsGlob(found),
    api: generateApiGlob(found)
  };

  for (const [category, glob] of Object.entries(suggestions)) {
    if (glob) {
      console.log(`${category}.instructions.md:`);
      console.log(`  applyTo: "${glob}"`);
      console.log();
    }
  }
}

function generateBackendGlob(dirs) {
  const backendDirs = dirs.filter(d =>
    ['server', 'backend', 'api', 'services'].includes(d)
  );

  if (backendDirs.length === 0) {
    if (dirs.includes('src')) {
      return 'src/**/server/**,src/**/api/**';
    }
    return null;
  }

  return backendDirs.map(d => `${d}/**`).join(',');
}

function generateFrontendGlob(dirs) {
  const frontendDirs = dirs.filter(d =>
    ['client', 'frontend', 'web', 'apps', 'components'].includes(d)
  );

  if (frontendDirs.length === 0) {
    if (dirs.includes('src')) {
      return 'src/**/client/**,src/**/components/**';
    }
    return null;
  }

  return frontendDirs.map(d => `${d}/**`).join(',');
}

function generateModelsGlob(dirs) {
  if (dirs.includes('models')) {
    return 'models/**';
  }
  if (dirs.includes('src')) {
    return 'src/**/models/**,src/**/entities/**';
  }
  return '**/models/**,**/entities/**,**/schemas/**';
}

function generateApiGlob(dirs) {
  if (dirs.includes('api')) {
    return 'api/**';
  }
  if (dirs.includes('src')) {
    return 'src/**/api/**,src/**/routes/**';
  }
  return '**/api/**,**/routes/**,**/endpoints/**';
}

main().catch(err => {
  console.error('Error:', err);
  process.exit(1);
});
"""
        with open(scripts_dir / "derive-globs.js", 'w') as f:
            f.write(derive_globs)

        # Test runner helper
        test_runner = """#!/bin/bash
# Test runner with coverage reporting

echo "🧪 Running tests with coverage..."

# Detect test runner
if [ -f "package.json" ]; then
    if grep -q '"test"' package.json; then
        npm test -- --coverage || yarn test --coverage || pnpm test --coverage
    fi
elif [ -f "pytest.ini" ] || [ -f "setup.cfg" ]; then
    pytest --cov=. --cov-report=term-missing
elif [ -f "go.mod" ]; then
    go test -cover ./...
else
    echo "⚠️  No test runner detected"
    exit 1
fi

echo "✅ Tests complete"
"""
        with open(scripts_dir / "test-coverage.sh", 'w') as f:
            f.write(test_runner)

        # Make scripts executable
        for script in scripts_dir.glob("*.sh"):
            script.chmod(0o755)

    def create_tasks_json(self):
        """Create VS Code tasks for common operations."""
        tasks = {
            "version": "2.0.0",
            "tasks": [
                {
                    "label": "APM: Run Tests",
                    "type": "shell",
                    "command": ".github/scripts/test-coverage.sh",
                    "group": "test",
                    "presentation": {
                        "echo": True,
                        "reveal": "always",
                        "panel": "shared"
                    },
                    "problemMatcher": []
                },
                {
                    "label": "APM: Derive Globs",
                    "type": "shell",
                    "command": "node .github/scripts/derive-globs.js",
                    "group": "build",
                    "presentation": {
                        "echo": True,
                        "reveal": "always"
                    }
                },
                {
                    "label": "APM: Lint",
                    "type": "shell",
                    "command": "npm run lint --silent || yarn lint --silent || pnpm lint --silent",
                    "group": "build"
                },
                {
                    "label": "APM: Format",
                    "type": "shell",
                    "command": "npm run format --silent || yarn format --silent || pnpm format --silent",
                    "group": "build"
                }
            ]
        }

        tasks_path = self.vscode_dir / "tasks.json"
        with open(tasks_path, 'w') as f:
            json.dump(tasks, f, indent=2)

    def update_gitignore(self):
        """Update .gitignore with APM entries."""
        gitignore_entries = """
# APM / GitHub Copilot Configuration (User-Specific)
.copilot/
.vscode/copilot-settings.json

# APM generated files
.apm/
apm-cache/
"""

        gitignore_path = self.repo_path / ".gitignore"

        if gitignore_path.exists():
            with open(gitignore_path) as f:
                content = f.read()

            if ".copilot/" not in content:
                with open(gitignore_path, 'a') as f:
                    f.write(gitignore_entries)
        else:
            with open(gitignore_path, 'w') as f:
                f.write(gitignore_entries)


def main():
    """CLI entry point."""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python install_apm.py <repo_path>")
        sys.exit(1)

    repo_path = sys.argv[1]
    installer = APMInstaller(repo_path)
    success = installer.run()

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()