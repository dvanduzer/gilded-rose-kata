# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

    def test_degradation(self):
        items = [Item("My First Gilded Rose", 2, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(4, items[0].quality)
        self.assertEquals(1, items[0].sell_in)
        gilded_rose.update_quality()
        self.assertEquals(3, items[0].quality)
        self.assertEquals(0, items[0].sell_in)
        gilded_rose.update_quality()
        self.assertEquals(1, items[0].quality)
        self.assertEquals(-1, items[0].sell_in)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)
        self.assertEquals(-2, items[0].sell_in)

    def test_not_negative(self):
        items = [Item("Limited Liability", 3, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

    def test_brie(self):
        items = [Item("Aged Brie", 3, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    def test_max_brie(self):
        items = [Item("Aged Brie", 3, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    def test_legendary(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 3, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(80, items[0].quality)


if __name__ == '__main__':
    unittest.main()
