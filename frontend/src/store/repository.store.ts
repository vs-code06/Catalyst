import { create } from "zustand";

interface RepositoryState {
  activeRepositoryId: string | null;
  setActiveRepositoryId: (id: string | null) => void;
}

export const useRepositoryStore = create<RepositoryState>((set) => ({
  activeRepositoryId: null,
  setActiveRepositoryId: (id) => set({ activeRepositoryId: id }),
}));
