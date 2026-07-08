import { useMutation } from "@tanstack/react-query";
import { predictionService } from "@/services/prediction.service";

export function usePrediction(repoId: string) {
  const predictMutation = useMutation({
    mutationFn: ({ target, horizon }: { target: string; horizon?: number }) =>
      predictionService.runPrediction(repoId, target, horizon),
  });

  return {
    predict: predictMutation.mutateAsync,
    isPredicting: predictMutation.isPending,
  };
}
