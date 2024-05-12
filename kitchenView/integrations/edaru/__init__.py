from kitchenView.integrations import RecipeIntegration

from kitchenView.integrations.edaru.api import search


class EdaRuRecipeIntegration(RecipeIntegration):
    async def search(self, query: str):
        return await search(query)
