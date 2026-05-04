import data as d

from praktikum.bun import Bun


class TestBun:
    def test_get_bun_name(self):
        bun = Bun(d.BUN_NAME, d.BUN_PRICE)

        assert bun.get_name() == d.BUN_NAME

    def test_get_bun_price(self):
        bun = Bun(d.BUN_NAME, d.BUN_PRICE)

        assert bun.get_price() == d.BUN_PRICE
