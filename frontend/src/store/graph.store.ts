import { create } from "zustand";

interface GraphState {
  selectedNodeId: string | null;
  filters: Record<string, any>;
  setSelectedNodeId: (id: string | null) => void;
  setFilters: (filters: Record<string, any>) => void;
  resetGraph: () => void;
}

export const useGraphStore = create<GraphState>((set) => ({
  selectedNodeId: null,
  filters: {},
  setSelectedNodeId: (id) => set({ selectedNodeId: id }),
  setFilters: (filters) => set({ filters }),
  resetGraph: () => set({ selectedNodeId: null, filters: {} }),
}));
