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


def get_names(spicy_foods):
    names = [food["name"] for food in spicy_foods]
    print(names)
    return names


get_names(spicy_foods)


def get_spiciest_foods(spicy_foods):
    names = [food for food in spicy_foods if food["heat_level"] > 5]
    print(names)
    return names


get_spiciest_foods(spicy_foods)


def print_spicy_foods(spicy_foods):
    emoji = "🌶"
    for food in spicy_foods:
        count_emoji = food["heat_level"] * emoji
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {count_emoji}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            print(food)
            return food


get_spicy_food_by_cuisine(spicy_foods, "American")


def print_spiciest_foods(spicy_foods):
    spicy_f = [foods for foods in spicy_foods if foods["heat_level"] > 5]

    for food in spicy_f:
        name = food["name"]
        heat = food["heat_level"]
        cuisine = food["cuisine"]
        print(f"{name} ({cuisine}) | Heat Level: {'🌶' * int(heat)}")


print_spiciest_foods(spicy_foods)


def get_average_heat_level(spicy_foods):
    heat = []
    for food in spicy_foods:
        heat_level = food["heat_level"]
        heat.append(heat_level)

    total_sum = sum(heat)
    average = total_sum / len(heat)
    print(int(average))
    return int(average)


get_average_heat_level(spicy_foods)


def create_spicy_food(spicy_foods, spicy_food):
    name = spicy_food["name"]
    cuisine = spicy_food["cuisine"]
    heat = spicy_food["heat_level"]

    new_food = {"name": name, "cuisine": cuisine, "heat_level": heat}

    spicy_foods.append(new_food)

    print(spicy_foods)
    return spicy_foods


create_spicy_food(
    spicy_foods,
    {
        "name": "Griot",
        "cuisine": "Haitian",
        "heat_level": 10,
    },
)
