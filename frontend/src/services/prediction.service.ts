import apiClient from "./api";

export const predictionService = {
  runPrediction: async (repoId: string, target: string, horizon = 1) => {
    const { data } = await apiClient.post("/prediction/predict", { repo_id: repoId, target, horizon });
    return data;
  },
  getPredictionResult: async (predictionId: string) => {
    const { data } = await apiClient.get(`/prediction/${predictionId}`);
    return data;
  },
};
