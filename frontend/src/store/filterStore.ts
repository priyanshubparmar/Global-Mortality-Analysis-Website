import { create } from "zustand";

interface FilterState {
  country: string;
  setCountry: (country: string) => void;
}

export const useFilterStore = create<FilterState>((set) => ({
  country: "World",
  setCountry: (country) => set({ country }),
}));