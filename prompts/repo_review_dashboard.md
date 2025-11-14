If you ever want to pipe the AI’s output into code (e.g. via JSON), you can standardize what you ask it to emit using a shape like this:

export type Severity = 'Critical' | 'High' | 'Medium' | 'Low';
export type BenefitLevel = 'Very High' | 'High' | 'Medium' | 'Low';

export type FindingCategory =
  | 'Bug'
  | 'Design'
  | 'Performance'
  | 'Security'
  | 'Test Coverage'
  | 'DX'
  | 'Maintainability'
  | 'Documentation'
  | 'Process'
  | 'Other';

export interface RepoFinding {
  id: string;                 // e.g. "A-001"
  title: string;
  project?: 'A' | 'B';        // if comparing two repos
  category: FindingCategory;
  severity: Severity;
  expectedBenefit: BenefitLevel;
  locations: string[];        // file paths or modules
  facts: string[];            // objective observations
  opinions: string[];         // subjective recommendations
  whyItMatters: string;
  recommendedChange: string;
  implementationOutline: string;
  improvementMetrics: string[]; // e.g. ["increase test coverage of module X from ~40% to ~80%"]
}

You could even ask the AI: “Now output all findings strictly as JSON matching the RepoFinding interface.” and wire it into scripts, dashboards, or tracking tools.