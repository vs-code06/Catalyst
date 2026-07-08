interface ScenarioSelectorProps {
  selectedScenario: string;
  onChange: (scenario: string) => void;
}

export function ScenarioSelector({ selectedScenario, onChange }: ScenarioSelectorProps) {
  const scenarios = [
    { id: "extract_service", label: "Extract Microservice" },
    { id: "merge_modules", label: "Merge Bounded Contexts" },
    { id: "add_dep", label: "Introduce Shared Dependency" },
  ];

  return (
    <div className="space-y-2">
      <label className="text-sm font-medium text-gray-300">Select Scenario</label>
      <select
        value={selectedScenario}
        onChange={(e) => onChange(e.target.value)}
        className="w-full bg-surface border border-surface-border rounded-lg p-2.5 text-sm text-white focus:outline-none focus:ring-1 focus:ring-catalyst-500"
      >
        {scenarios.map((s) => (
          <option key={s.id} value={s.id}>
            {s.label}
          </option>
        ))}
      </select>
    </div>
  );
}
export default ScenarioSelector;
