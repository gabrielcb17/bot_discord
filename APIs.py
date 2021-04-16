import requests

def get_cat_facts():
    return get_response("https://cat-fact.herokuapp.com/facts")

def get_random_drink():
    drink = get_response("https://www.thecocktaildb.com/api/json/v1/1/random.php")["drinks"][0]

    recipe = {
        "ingredients": [
            {drink[f"strIngredient{i}"]: drink[f"strMeasure{i}"]} for i in range(1, 15) if drink[f"strIngredient{i}"]
        ]}

    str_recipe = ""
    for item in recipe["ingredients"]:
        for key, value in item.items():
            str_recipe += f"{key}: {value}\n"

    info = {"info": [
        drink.get("strCategory"),
        drink.get("strIBA"),
        drink.get("strAlcoholic"),
        drink.get("strGlass")
    ]}

    footer = [info["info"][i] for i in range(len(info)) if not None]

    return drink, str_recipe, footer

def get_response(url):
    response = requests.get(url)
    return response.json()

print(get_random_drink()[1])