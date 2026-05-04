from praktikum.database import Database


class TestDatabase:
    def test_init_database(self):
        database = Database()

        buns = database.available_buns()
        ingredients = database.available_ingredients()
        assert len(buns) == 3 and len(ingredients) == 6
