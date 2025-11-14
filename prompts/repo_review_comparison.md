You are Codex, an expert staff-level software engineer and software architect.

You have read-only access to TWO related repositories in this workspace:

- Project A: <describe or name the first repo here, or indicate its folder>
- Project B: <describe or name the second repo here, or indicate its folder>

================================
GOAL
================================
Perform a **deep comparative analysis** of Project A and Project B.

I want to know:

- How they differ in architecture, quality, tests, and engineering process.
- What each project does BETTER than the other.
- What is MISSING from one that exists in the other.
- Where to align or consolidate patterns between them.
- A prioritized list of changes for each project with clear severity and expected benefit.

Follow the same Fact vs Opinion split:

- Label objective observations as **Fact**.
- Label judgements as **Opinion** and justify.

================================
STEP 1: INDIVIDUAL SUMMARIES
================================
For each project (A and B):

1. Provide a short but concrete overview:

   - Tech stack, frameworks, build tools.
   - Primary domain and main responsibilities.
   - Key entry points and major sub-systems.

2. Give a brief directory map:

   - Main directories and their responsibilities.

3. Summarize:
   - Major strengths.
   - Major weaknesses.

================================
STEP 2: ARCHITECTURE & DESIGN COMPARISON
================================
Compare A and B:

- Architecture:

  - How each is structured (layers, modules, boundaries).
  - Where they follow similar or completely different patterns.
  - Which architecture is more scalable / maintainable, and why (Opinion).

- Data & control flow:

  - Compare how each handles a typical request or workflow.
  - Provide simple Mermaid diagrams if helpful.

- Cross-project learnings:
  - Design patterns or approaches from A that B should adopt.
  - Design patterns or approaches from B that A should adopt.

================================
STEP 3: TESTING, QUALITY & DX COMPARISON
================================
Compare the two projects in terms of:

- Testing:

  - Relative test coverage (approximate).
  - Types of tests present (unit/integration/e2e) in each.
  - Which project has the stronger testing strategy and why.

- Code quality & standards:

  - Consistency of style, patterns, and abstractions.
  - Use of types, error handling, and defensive coding.
  - Which codebase is easier to understand and safely refactor.

- Developer experience:
  - Ease of setup, running, and testing.
  - Quality of documentation.
  - Tooling (linters/formatters, scripts, CI hints).

================================
STEP 4: WHAT’S MISSING IN EACH
================================
Create two sections:

1. “Things Project A is missing that Project B has”
2. “Things Project B is missing that Project A has”

For each item, specify:

- Category: [Architecture | Feature | Test | Tooling | Documentation | Process | Other]
- Fact: What exists in one project and not the other.
- Opinion: Whether A and/or B should adopt it, with brief justification.
- Expected Benefit if adopted: [Very High | High | Medium | Low].

================================
STEP 5: DETAILED FINDINGS FOR EACH PROJECT
================================
For each project separately, list detailed findings using this structure:

- ID: [SHORT-ID prefixed with A- or B-]
- Title:
- Category: [Bug | Design | Performance | Security | Test Coverage | DX | Maintainability | Documentation | Process | Other]
- Severity: [Critical | High | Medium | Low]
- Expected Benefit: [Very High | High | Medium | Low]
- Locations:
- Fact(s):
- Opinion(s):
- Why it matters:
- Recommended change:
- How to implement:
- How to measure improvement:

Group by project (A then B), and within each project:

- Group by Severity, then Category.
- Focus detailed descriptions on the top 20–40 highest-impact findings in each.

================================
STEP 6: ALIGNMENT & CONSOLIDATION PLAN
================================
Propose an alignment roadmap covering BOTH projects:

- Identify a **target set of standards** (architecture, code style, testing approach) that both projects should converge on.
- List specific actions for:
  - Project A (what to adopt from B, what to drop).
  - Project B (what to adopt from A, what to drop).
- Call out:
  - Quick wins (small effort, high benefit).
  - Larger migrations/refactors (higher effort, with justification).

Where helpful, reference the finding IDs (A-_, B-_).

================================
STYLE
================================

- Use clear sections and tables where appropriate (e.g. side-by-side comparison tables).
- Always distinguish Facts vs Opinions.
- Prefer actionable, concrete advice over vague statements.

NOTE:
Run the big overview prompt first, then

Follow up with focused prompts like:

“Apply the same framework but only for src/domain and go deeper.”

“Now do a dedicated test gap analysis for src/services.”

“Generate a Mermaid diagram for the data flow from API layer to persistence.”

That way you get depth where it matters instead of a single, shallow sweep.
