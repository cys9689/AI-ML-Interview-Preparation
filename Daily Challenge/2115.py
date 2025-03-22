from typing import List
from collections import deque

# BFS
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        available = set(supplies)
        recipe_queue = deque(range(len(recipes)))
        result = []
        last_size = -1
        while len(available)  > last_size:
            last_size = len(available)
            queue_size = len(recipe_queue)
            while queue_size > 0:
                queue_size -=1
                recipe_idx = recipe_queue.popleft()
                if all(
                    ingredient in available
                    for ingredient in ingredients[recipe_idx]):
                        available.add(recipes[recipe_idx])
                        result.append(recipes[recipe_idx])
                else:
                    recipe_queue.append(recipe_idx)
        return result

# DFS
class Solution1:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        can_make = dict.fromkeys(supplies, True)
        recipe_to_idx = {recipe: idx for idx, recipe in enumerate(recipes)}

        def _check_recipe(recipe: str, visited: set) -> bool:
            if can_make.get(recipe, False):
                return True

            if recipe not in recipe_to_idx or recipe in visited:
                return False

            visited.add(recipe)
            can_make[recipe] = all(
                _check_recipe(ingredient, visited)
                for ingredient in ingredients[recipe_to_idx[recipe]]
            )

            return can_make[recipe]

        return [recipe for recipe in recipes if _check_recipe(recipe, set())]
    

bfs_solution = Solution()
dfs_solution = Solution1()
recipes = ["bread"]
ingredients = [["yeast","flour"]]
supplies = ["yeast","flour","corn"]
print("Solutoin 1 : " , bfs_solution.findAllRecipes(recipes,ingredients,supplies))
print("Solution 2 : ", dfs_solution.findAllRecipes(recipes,ingredients,supplies))