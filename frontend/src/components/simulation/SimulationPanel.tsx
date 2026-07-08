import Button from "../ui/Button";

export function SimulationPanel() {
  return (
    <div className="p-6 border border-surface-border rounded-xl bg-surface-secondary space-y-4">
      <h3 className="text-lg font-medium text-white">Simulation Engine</h3>
      <p className="text-sm text-gray-400">
        Run scenarios to model potential architectural adjustments and project downstream risks.
      </p>
      <Button className="w-full">
        Run Current Scenario
      </Button>
    </div>
  );
}
export default SimulationPanel;
