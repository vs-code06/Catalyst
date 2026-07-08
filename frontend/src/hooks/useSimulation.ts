import { useMutation } from "@tanstack/react-query";
import { simulationService } from "@/services/simulation.service";

export function useSimulation(repoId: string) {
  const runSimulationMutation = useMutation({
    mutationFn: ({ scenario, parameters }: { scenario: string; parameters: any }) =>
      simulationService.runSimulation(repoId, scenario, parameters),
  });

  return {
    runSimulation: runSimulationMutation.mutateAsync,
    isSubmitting: runSimulationMutation.isPending,
  };
}
