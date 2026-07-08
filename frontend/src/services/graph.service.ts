import apiClient from "./api";

export const graphService = {
  getDependencyGraph: async (repoId: string) => {
    const { data } = await apiClient.get(`/graph/${repoId}/dependency`);
    return data;
  },
  getCallGraph: async (repoId: string) => {
    const { data } = await apiClient.get(`/graph/${repoId}/callgraph`);
    return data;
  },
  getArchitectureGraph: async (repoId: string) => {
    const { data } = await apiClient.get(`/graph/${repoId}/architecture`);
    return data;
  },
};
