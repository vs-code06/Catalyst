import { create } from "zustand";

interface SimulationState {
  currentScenario: string;
  parameters: Record<string, any>;
  results: Record<string, any> | null;
  setCurrentScenario: (scenario: string) => void;
  setParameters: (params: Record<string, any>) => void;
  setResults: (results: Record<string, any> | null) => void;
}

export const useSimulationStore = create<SimulationState>((set) => ({
  currentScenario: "extract_service",
  parameters: {},
  results: null,
  setCurrentScenario: (scenario) => set({ currentScenario: scenario }),
  setParameters: (params) => set({ parameters: params }),
  setResults: (results) => set({ results }),
}));
