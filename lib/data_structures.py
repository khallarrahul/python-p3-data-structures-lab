spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


# def get_names(spicy_foods):
#     names = [food["name"] for food in spicy_foods]
#     print(names)
#     return names


# get_names(spicy_foods)


# def get_spiciest_foods(spicy_foods):
#     names = [food for food in spicy_foods if food["heat_level"] > 5]
#     print(names)
#     return names


# get_spiciest_foods(spicy_foods)


# def print_spicy_foods(spicy_foods):
#     for food in spicy_foods:
#         name = food["name"]
#         heat_lvl = food["heat_level"]
#         print(name, "|", "Heat Level:", "🌶" * int(heat_lvl))


# print_spicy_foods(spicy_foods)


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            print(food)


get_spicy_food_by_cuisine(spicy_foods, "American")


def print_spiciest_foods(spicy_foods):
    pass


def get_average_heat_level(spicy_foods):
    pass


def create_spicy_food(spicy_foods, spicy_food):
    pass
