import aiohttp

from functools import lru_cache

from schemas import RecipesList

SEARCH_URL = "https://api.eda.ru/v2/graphql"


@lru_cache(typed=True)
async def search(query: str) -> RecipesList | None:
    """
    Search items by text query
    :param query:
    :return:
    """
    async with aiohttp.ClientSession() as session:
        async with session.post(url=SEARCH_URL, json=[{"variables": {}, "query": "{\n recipes(\n request: {first: 10, name: \""+query+"\", sortField: RELEVANCE, sortDirection: DESC, isEditorChoice: false}\n  ) {\n    edges {\n      node {\n          name\n recipeCover {\n     imageUrl\n      }\n        composition {\n          amount\n          ingredient {\n            name\n     }\n          measureUnit {\n            name\n            nameFive\n            nameTwo\n      }\n              }\n               relativeUrl\n       recipeCategory {\n          name\n                           }\n        cuisine {\n          name\n            }\n        portionsCount\n        preparationTime\n        cookingTime\n    likes\n           dislikes\n               recipeSteps {\n          description\n          imageUrl\n                  }\n        nutritionInfo {\n          carbohydrates\n          fats\n          kilocalories\n          proteins\n                  }\n              }\n          }\n    totalCount\n   }\n}"}]) as response:
            try:
                return RecipesList.parse_obj(await response.json())
            except Exception as e:
                print(e)
                return None
