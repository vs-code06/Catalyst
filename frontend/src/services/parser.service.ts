import apiClient from "./api";

export const parserService = {
  submitRepository: async (repoUrl: string, branch = "main") => {
    const { data } = await apiClient.post("/parser/repositories", { repo_url: repoUrl, branch });
    return data;
  },
  getJobStatus: async (jobId: string) => {
    const { data } = await apiClient.get(`/parser/repositories/${jobId}/status`);
    return data;
  },
  getSymbols: async (repoId: string) => {
    const { data } = await apiClient.get(`/parser/repositories/${repoId}/symbols`);
    return data;
  },
};
