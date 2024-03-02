def cookbook(*args):
    cookbook_dict = {}
    result = []
    for recipe_name, cuisine, ingredients in args:
        if cuisine not in cookbook_dict:
            cookbook_dict[cuisine] = {recipe_name: ingredients}

        elif cuisine in cookbook_dict:
            cookbook_dict[cuisine].update({recipe_name: ingredients})

    for cusisine, elements in sorted(cookbook_dict.items(), key=lambda x: (-len(x[1]), x[0])):
        result.append(f"{cusisine} cuisine contains {len(elements)} recipes:")
        for meal, ingredients in sorted(elements.items(), key=lambda x: x[0]):
            result.append(f"  * {meal} -> Ingredients: {', '.join(ingredients)}")

    return "\n".join(result)


print(cookbook(
                    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
                      ("Chicken Curry", "Indian", ["chicken", "curry paste", "coconut milk", "rice"]),
                      ("Caesar Salad", "American", ["romaine lettuce", "croutons", "parmesan", "caesar dressing"]),
                      ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
                      ("Mushroom Risotto", "Italian", ["arborio rice", "mushrooms", "onion", "parmesan", "broth"]),
                      ("Tacos", "Mexican", ["tortillas", "ground beef", "lettuce", "tomato", "cheese"]),
                      ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"]),
                      ("Chicken Alfredo", "Italian", ["fettuccine", "chicken", "alfredo sauce", "broccoli"]))
)