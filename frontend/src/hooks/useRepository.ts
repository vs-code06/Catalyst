import { useQuery } from "@tanstack/react-query";
import { parserService } from "@/services/parser.service";

export function useRepository(repoId: string) {
  const symbolsQuery = useQuery({
    queryKey: ["symbols", repoId],
    queryFn: () => parserService.getSymbols(repoId),
    enabled: !!repoId,
  });

  return {
    symbols: symbolsQuery.data,
    isLoading: symbolsQuery.isLoading,
  };
}
