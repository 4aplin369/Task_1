import data as d

from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.ingredient import Ingredient

class TestBun():

    def test_get_ingredient_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, d.INGREDIENT_NAME, d.INGREDIENT_PRICE)

        assert ingredient.get_name() == d.INGREDIENT_NAME


    def test_get_ingredient_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, d.INGREDIENT_NAME, d.INGREDIENT_PRICE)

        assert ingredient.get_price() == d.INGREDIENT_PRICE


    def test_get_ingredient_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, d.INGREDIENT_NAME, d.INGREDIENT_PRICE)

        assert ingredient.get_type() == INGREDIENT_TYPE_FILLING

