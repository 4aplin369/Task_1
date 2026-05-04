import data as d
import pytest

from unittest.mock import Mock

from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.bun import Bun


class TestBurger:
    def test_burger_empty_buns(self):
        burger = Burger()

        assert burger.bun is None

    def test_burger_empty_ingredients(self):
        burger = Burger()

        assert burger.ingredients == []

    def test_burger_set_bun(self):
        burger = Burger()
        bun_mock = Mock()

        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    def test_burger_add_ingredient(self):
        burger = Burger()
        ingredient_mock = Mock()

        burger.add_ingredient(ingredient_mock)
        assert burger.ingredients[0] == ingredient_mock

    def test_burger_remove_ingredient(self):
        burger = Burger()
        ingredient_mock = Mock()

        burger.add_ingredient(ingredient_mock)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_burger_move_ingredient(self):
        burger = Burger()
        ingredient_mock_1 = Mock()
        ingredient_mock_2 = Mock()

        burger.add_ingredient(ingredient_mock_1)
        burger.add_ingredient(ingredient_mock_2)

        burger.move_ingredient(0, 1)
        assert (
            burger.ingredients[0] == ingredient_mock_2
            and burger.ingredients[-1] == ingredient_mock_1
        )

    @pytest.mark.parametrize(
        "ingredient_list, price",
        [(d.ONE_INGREDIENT, 120), (d.TWO_INGREDIENTS, 170), ("", 20)],
        ids=["one_ing", "two_ing", "empty_ing"],
    )
    def test_burger_get_price(self, ingredient_list, price):
        burger = Burger()
        bun = Bun("lavash", 10)

        burger.set_buns(bun)

        for i in ingredient_list:
            ingredient = Ingredient(*i)
            burger.add_ingredient(ingredient)

        assert burger.get_price() == price

    @pytest.mark.parametrize(
        "ingredient_list, price",
        [(d.ONE_INGREDIENT, 120), (d.TWO_INGREDIENTS, 170), ("", 20)],
        ids=["one_ing", "two_ing", "empty_ing"],
    )
    def test_burger_get_receipt(self, ingredient_list, price):
        burger = Burger()
        bun = Bun("lavash", 10)

        burger.set_buns(bun)

        for i in ingredient_list:
            ingredient = Ingredient(*i)
            burger.add_ingredient(ingredient)

        receipt = burger.get_receipt()

        assert bun.get_name(), burger.get_price() in receipt
