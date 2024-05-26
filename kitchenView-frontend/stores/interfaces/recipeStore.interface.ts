import type { IRecipe } from "~/interfaces/recipe.interface";

interface IRecipeSearch {
  recipes: IRecipe[];
  selectedRecipe: IRecipe | null;
  recipesLoadingError: any | null;
  recipesIsLoading: boolean;
  lastQuery: string | null;
}

export interface IRecipeStore {
  search: IRecipeSearch;
}