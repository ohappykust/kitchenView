import {toast} from "~/components/ui/toast";
import useAuthedFetch from "~/extensions/useAuthedFetch";

import type {IRecipeStore} from "~/stores/interfaces/recipeStore.interface";
import type {IRecipeSearchResult} from "~/interfaces/recipe.interface";

export const useRecipeStore = defineStore('recipe', {
  state: (): IRecipeStore => ({
    search: {
      recipes: [],
      selectedRecipe: null,
      recipesLoadingError: null,
      recipesIsLoading: false,
      lastQuery: null,
    },
  }),
  actions: {
    async searchRecipe(query: string) {
      if (query.trim().length < 2) {
        toast({
          variant: "destructive",
          title: 'Шеф-повар в ступоре...',
          description: 'Название рецепта должно быть от 2 символов',
        });
        return
      }
      this.search.recipesIsLoading = true;
      try {
         this.search.recipes = (await useAuthedFetch<IRecipeSearchResult>("/recipes/search", {
           params: {
             query: query,
             external: true
           }
         })).recipes;
         this.search.lastQuery = query;
      } catch (error) {
        this.search.recipesLoadingError = error;
      }
      this.search.recipesIsLoading = false;
    }
  }
})