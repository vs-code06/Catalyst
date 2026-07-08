import { useQuery } from "@tanstack/react-query";
import { graphService } from "@/services/graph.service";

export function useGraph(repoId: string) {
  const dependencyGraphQuery = useQuery({
    queryKey: ["dependencyGraph", repoId],
    queryFn: () => graphService.getDependencyGraph(repoId),
    enabled: !!repoId,
  });

  return {
    dependencyGraph: dependencyGraphQuery.data,
    isLoading: dependencyGraphQuery.isLoading,
    error: dependencyGraphQuery.error,
  };
}
