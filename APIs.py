import requests

def get_cat_facts():
    return get_response("https://cat-fact.herokuapp.com/facts")

def get_cat_pics():
    return get_response("https://aws.random.cat/meow?ref=apilist.fun")["file"]

# API is buggy
# def get_dog_pics():
#     response = get_response("https://random.dog/woof.json?ref=apilist.fun")["url"]
#     file_format = response.split(".")[-1]
#     attemps = 0
#     while file_format != "jpeg" and file_format != "jpg" and attemps < 10:
#         print(f"file format not supported: {file_format}")
#         attemps += 1
#         response = get_response("https://random.dog/woof.json?ref=apilist.fun")["url"]
#         file_format = response.split(".")[-1]
#
#     print(f"file format sent: {file_format}")
#     return response

def get_fox_pics():
    return get_response("https://randomfox.ca/floof/?ref=apilist.fun")["image"]

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

# print(get_random_drink()[1])