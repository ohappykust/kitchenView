export interface IRecipeComponentMeasureUnit {
    name: string;
    name_five: string;
    name_two: string;
}

export interface IRecipeComponent {
    amount: number;
    name: string;
    measure_unit: IRecipeComponentMeasureUnit;
}

export interface IRecipeStep {
    description: string;
    image_url: string | null;
}

export interface IRecipeNutritionInfo {
    carbohydrates: number;
    fats: number;
    kilocalories: number;
    proteins: number;
}

export interface IRecipe {
    id: number;
    name: string;
    image_url: string | null;
    components: IRecipeComponent[];
    category: string;
    kitchen: string | null;
    portions_count: number;
    preparation_time_minutes: number;
    cooking_time_minutes: number;
    likes: number;
    dislikes: number;
    steps: IRecipeStep[];
    nutrition_info: IRecipeNutritionInfo;
}

export interface IRecipeSearchResult {
    recipes: IRecipe[];

}