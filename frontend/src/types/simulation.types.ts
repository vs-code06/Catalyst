export interface SimulationResult {
  simulationId: string;
  status: "completed" | "failed";
  impactScore: number;
  modifiedNodes: string[];
}
