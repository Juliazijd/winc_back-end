from unicodedata import name
import models
from typing import List
import peewee
from peewee import fn


__winc_id__ = "286787689e9849969c326ee41d8c53c4"
__human_name__ = "Peewee ORM"


def cheapest_dish() -> models.Dish:
    """You want ot get food on a budget

    Query the database to retrieve the cheapest dish available
    """
    cheapest_dish = models.Dish.select(fn.MIN(models.Dish.price_in_cents))
    return cheapest_dish


def vegetarian_dishes() -> List[models.Dish]:
    """You'd like to know what vegetarian dishes are available

    Query the database to return a list of dishes that contain only
    vegetarian ingredients.
    """
    if models.Dish.ingredients == models.Ingredient.is_vegetarian:
        return models.Dish.select(models.Dish.name)


def best_average_rating() -> models.Restaurant:
    """You want to know what restaurant is best

    Query the database to retrieve the restaurant that has the highest
    rating on average
    """
    best_rating = models.Restaurant.select(models.Restaurant.name).join(models.Rating).where(fn.MAX(models.Rating.rating))
    return best_rating


def add_rating_to_restaurant() -> None:
    """After visiting a restaurant, you want to leave a rating

    Select the first restaurant in the dataset and add a rating
    """
    restaurant = models.Restaurant.get_by_id(1)
    models.Rating.create(restaurant=restaurant, rating=4, comment="outstanding")


def dinner_date_possible() -> List[models.Restaurant]:
    """You have asked someone out on a dinner date, but where to go?

    You want to eat at around 19:00 and your date is vegan.
    Query a list of restaurants that account for these constraints.
    """
    ...


def add_dish_to_menu() -> models.Dish:
    """You have created a new dish for your restaurant and want to add it to the menu

    The dish you create must at the very least contain 'cheese'.
    You do not know which ingredients are in the database, but you must not
    create ingredients that already exist in the database. You may create
    new ingredients however.
    Return your newly created dish
    """
    ...


if __name__ == "__main__":
    cheapest_dish()
    best_average_rating()
    add_rating_to_restaurant()
