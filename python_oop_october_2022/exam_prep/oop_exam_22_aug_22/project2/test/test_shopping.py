from exam_prep.oop_exam_22_aug_22.project2.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCart(TestCase):

    def setUp(self) -> None:
        self.shopping_cart = ShoppingCart('Shop', 100)

    def test_correct_initializing(self):
        self.assertEqual(self.shopping_cart.shop_name, 'Shop')
        self.assertEqual(self.shopping_cart.budget, 100)
        self.assertEqual(self.shopping_cart.products, {})

    def test_name_setter_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.shop_name = 'shop123'
        self.assertEqual(str(ve.exception), "Shop must contain only letters and must start with capital letter!")

    def test_product_price_equal_or_over_100_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.add_to_cart('banana', 100)
        self.assertEqual(str(ve.exception), "Product banana cost too much!")

    def test_add_correct_product_to_cart(self):
        result = self.shopping_cart.add_to_cart('banana', 50)
        self.assertEqual(self.shopping_cart.products, {'banana': 50})
        self.assertEqual("banana product was successfully added to the cart!", result)

    def test_remove_non_existing_product_from_cart_raise_value_error(self):
        self.shopping_cart.products = {'banana': 50}
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.remove_from_cart('orange')
        self.assertEqual(str(ve.exception), "No product with name orange in the cart!")

    def test_remove_existing_product_from_cart(self):
        self.shopping_cart.products = {'banana': 50, 'orange': 50}
        result = self.shopping_cart.remove_from_cart('banana')
        self.assertEqual("Product banana was successfully removed from the cart!", result)
        self.assertEqual({'orange': 50}, self.shopping_cart.products)

    def test_creating_new_shop(self):
        self.other = ShoppingCart('ShopTwo', 200)
        self.shopping_cart.products = {'banana': 50}
        self.other.products = {'orange': 50}
        new_shop = self.shopping_cart.__add__(self.other)
        self.assertEqual(new_shop.shop_name, 'ShopShopTwo')
        self.assertEqual(new_shop.budget, 300)
        self.assertEqual(new_shop.products, {'banana': 50, 'orange': 50})

    def test_total_sum_more_than_budget_raise_value_error(self):
        self.shopping_cart.products = {'banana': 50, 'orange': 50, 'berries': 50}
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.buy_products()
        self.assertEqual(str(ve.exception), "Not enough money to buy the products! Over budget with 50.00lv!")

    def test_successful_order(self):
        self.shopping_cart.products = {'banana': 50, 'orange': 20}
        result = self.shopping_cart.buy_products()
        self.assertEqual(result, 'Products were successfully bought! Total cost: 70.00lv.')


if __name__ == '__main__':
    main()