import apiClient from "./api";

export const simulationService = {
  runSimulation: async (repoId: string, scenario: string, parameters = {}) => {
    const { data } = await apiClient.post("/simulation/run", { repo_id: repoId, scenario, parameters });
    return data;
  },
  getSimulationResult: async (simulationId: string) => {
    const { data } = await apiClient.get(`/simulation/${simulationId}`);
    return data;
  },
};
