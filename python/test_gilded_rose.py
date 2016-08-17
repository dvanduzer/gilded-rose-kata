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

if __name__ == '__main__':
    unittest.main()
