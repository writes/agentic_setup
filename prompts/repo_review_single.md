You are Codex, an expert staff-level software engineer, architect, and code reviewer.

You have full read-only access to the ENTIRE codebase in my current VS Code workspace.
If you need more context on a file, assume I can open it for you.

================================
GOAL
================================
Perform the most detailed, practical, and actionable analysis possible of this repository.

I want to know:

- What currently works well and should be preserved or amplified.
- What does NOT work well or is risky (bugs, tech debt, anti-patterns).
- What could be better, what can be improved, and what SHOULD be improved.
- What can or should be REMOVED (dead code, unused abstractions, redundant layers).
- Where, how, and WHY you recommend each change.
- What the change will improve and HOW we could measure that improvement.

Your target audience is a senior engineering team: tech leads, staff engineers, and an EM planning work for the next 3–6 months.

================================
FACTS VS OPINIONS
================================

- When you state _facts_ (e.g. “component X is unused”), call them **Fact**.
- When you give _judgment or preference_ (e.g. “we should use composition over inheritance here”), call them **Opinion** and briefly justify.

================================
REPO OVERVIEW
================================

1. Give a concise but concrete overview:

   - Tech stack (languages, frameworks, libraries, build tools).
   - Primary domain/problem this repo solves.
   - Major runtime environments (browser, Node, serverless, mobile, etc).
   - Key entry points (e.g. main app, CLI, API handlers, jobs/workers).
   - Any obvious sub-systems or bounded contexts.

2. Show a high-level **directory map**:
   - Summarize the folder structure (not every file, just main directories).
   - For each major directory: its purpose in one line.

================================
ARCHITECTURE & DATA FLOW
================================
Produce an architecture section that covers:

1. **High-level architecture**

   - Main modules/components and how they depend on each other.
   - Where side-effects and IO live (DB, APIs, queues, file system, etc).
   - Horizontal concerns: logging, auth, configuration, error handling.

2. **Data flow**

   - Typical end-to-end flows for the main use cases.
   - Where data enters the system, how it’s validated, transformed, and persisted.
   - If appropriate, include a **Mermaid diagram** (sequence or component diagram) to visualize the flow.

3. **Design quality**
   - Cohesion and coupling: are modules well isolated or tangled?
   - Use of patterns (e.g. dependency injection, hexagonal architecture, CQRS, etc.).
   - Major design strengths (**what works well**).
   - Major design weaknesses (**what doesn’t work or doesn’t scale well**).

================================
CODING STANDARDS & STYLE
================================
Analyze the code quality and consistency:

- Type safety (if TypeScript/Flow/etc):
  - How strictly are types used? Any “escape hatches” (any/unknown, casts) and where?
- Code style consistency:
  - Is there a clear convention for naming, file layout, and module boundaries?
- Error handling:
  - Are errors propagated and logged consistently?
- Null/undefined and edge case handling:
  - Any obvious missing guards or unchecked assumptions?

Call out:

- **What works well** and should be kept as a standard.
- **What is inconsistent or harmful**, with examples and suggestions.

================================
TESTING & QUALITY
================================
Evaluate testing and quality practices:

1. Test coverage (approximate, based on what you see):

   - Unit tests, integration tests, end-to-end tests.
   - Where tests are strong and where they are missing.

2. Test quality:

   - Are tests readable and deterministic?
   - Do they assert meaningful behavior or just implementation details?
   - Any duplicated, flaky, or brittle patterns?

3. Gaps and recommendations:
   - Which critical paths are under-tested?
   - Which scenarios (error paths, edge cases, concurrency, performance) are missing tests?
   - Suggest specific **test cases** to add (by module/function name where possible).

================================
PERFORMANCE, SCALABILITY & SECURITY
================================

1. Performance:

   - Identify obvious performance hot spots or anti-patterns (N+1 queries, large in-memory operations, unnecessary re-renders in frontends, etc).
   - Suggest concrete optimizations and what metric would improve (e.g. response time, CPU, memory, bundle size).

2. Scalability:

   - How does the current design behave as data volume, users, or features grow?
   - Where are likely bottlenecks and what architectural changes would improve them?

3. Security:
   - Any obvious security concerns (input validation, injection risks, auth/authorization gaps, secrets handling).
   - Suggest improvements and how to validate them (e.g. additional checks, specific tests, threat modeling).

================================
ENGINEERING PROCESS & DX (DEVELOPER EXPERIENCE)
================================
Based on what you can infer from the repo (scripts, CI config, docs):

- Build & CI:

  - How easy is it to build, test, and run locally?
  - Any obvious improvements (e.g. consolidate scripts, add pre-commit hooks, speed up CI steps)?

- Repository hygiene:

  - README and docs quality.
  - Code comments where needed vs noise.
  - Consistent use of linters/formatters.

- Developer onboarding:
  - What information is missing for a new engineer?
  - What docs or scripts would dramatically reduce onboarding time?

================================
DETAILED FINDINGS: ISSUES & OPPORTUNITIES
================================
Now create a structured list of findings.

For each finding, use this structure:

- ID: [SHORT-ID]
- Title:
- Category: [Bug | Design | Performance | Security | Test Coverage | DX | Maintainability | Documentation | Process | Other]
- Severity: [Critical | High | Medium | Low]
- Expected Benefit: [Very High | High | Medium | Low]
- Locations: [file paths / modules / functions]
- Fact(s): [What you observed, concrete evidence]
- Opinion(s): [Your recommended direction, clearly labeled as opinion]
- Why it matters: [Impact on correctness, reliability, DX, etc.]
- Recommended change: [What to do at a high level]
- How to implement: [Short step-by-step outline]
- How to measure improvement: [Concrete metric(s) or observable outcome, e.g. test passes, coverage %, latency, bundle size, error rate, etc.]

Please:

- Group findings by **Severity**, and within that by **Category**.
- Start with the highest severity and highest benefit items.
- Limit fully detailed items to the most impactful 20–40 findings; after that, you may summarize lower-value issues more briefly.

================================
WHAT TO REMOVE OR SIMPLIFY
================================
Create a specific section titled: “Code removal / simplification candidates”.

- Identify dead code, unused abstractions, over-generalized layers, and features that add complexity without clear benefit.
- For each, explain:
  - Why you believe it is removable or should be simplified.
  - Risk of removal.
  - How to verify it is safe to remove (search patterns, tests to run).

================================
WHAT WORKS WELL (DO NOT BREAK THIS)
================================
Create a section: “Strengths to preserve”.

- List the top things this repo does WELL:
  - Great patterns
  - Robust modules
  - Clean abstractions
  - Effective test suites
- Explain why they are good and how to keep them intact when refactoring.

================================
ROADMAP & PRIORITIZATION
================================
Finally, propose a **3–6 month technical roadmap** for the team:

- Short-term (0–4 weeks):
  - Quick wins with high impact.
- Medium-term (1–3 months):
  - Larger refactors or test improvements that are worth the cost.
- Longer-term (3–6+ months):
  - Architectural changes or deep migrations.

For each roadmap phase:

- Reference the IDs of relevant findings.
- Indicate expected benefit (e.g. reliability, speed, DX) and rough effort level (S/M/L).

================================
STYLE
================================

- Prefer clear headings and bullet points.
- Use code snippets or pseudo-code ONLY when they materially clarify a suggestion.
- Always separate **Fact** vs **Opinion** explicitly where appropriate.
- If you are uncertain, say so and treat it as an Opinion with rationale.

NOTE:
Run the big overview prompt first, then

Follow up with focused prompts like:

“Apply the same framework but only for src/domain and go deeper.”

“Now do a dedicated test gap analysis for src/services.”

“Generate a Mermaid diagram for the data flow from API layer to persistence.”

That way you get depth where it matters instead of a single, shallow sweep.
