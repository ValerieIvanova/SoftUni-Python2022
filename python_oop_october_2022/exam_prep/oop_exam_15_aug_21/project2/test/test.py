from exam_prep.oop_exam_15_aug_21.project2.pet_shop import PetShop
from unittest import TestCase, main


class TestPetShop(TestCase):
    def setUp(self) -> None:
        self.shop = PetShop('Test')

    def test_correct_init(self):
        self.assertEqual('Test', self.shop.name)
        self.assertEqual({}, self.shop.food)
        self.assertEqual([], self.shop.pets)

    def test_add_food_with_zero_or_less_quantity_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shop.add_food('Food', 0)
            self.shop.add_food('Food', -1)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ve.exception))

    def test_add_food_successfully(self):
        result1 = self.shop.add_food('Food', 10)
        result2 = self.shop.add_food('Food', 5)
        self.assertEqual("Successfully added 10.00 grams of Food.", result1)
        self.assertEqual("Successfully added 5.00 grams of Food.", result2)
        self.assertEqual({"Food": 15}, self.shop.food)

    def test_add_existing_pet_raise_exception(self):
        self.shop.pets = ['Tera']
        with self.assertRaises(Exception) as ex:
            self.shop.add_pet("Tera")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_add_pet_successfully(self):
        self.shop.pets = ['Tera']
        result = self.shop.add_pet('Jessey')
        self.assertEqual(["Tera", 'Jessey'], self.shop.pets)
        self.assertEqual("Successfully added Jessey.", result)

    def test_feed_non_existing_pet_raise_exception(self):
        self.shop.pets = ["Tera", 'Jessey']
        self.shop.food = {"Food": 30}
        with self.assertRaises(Exception) as ex:
            self.shop.feed_pet('Food', 'Hera')
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_with_unavailable_food(self):
        self.shop.pets = ["Tera", 'Jessey']
        self.shop.food = {"Food": 30}
        result = self.shop.feed_pet('Wiskas', 'Tera')
        self.assertEqual('You do not have Wiskas', result)

    def test_if_the_food_is_less_than_hundred_grams(self):
        self.shop.pets = ["Tera", 'Jessey']
        self.shop.food = {"Food": 30}
        result = self.shop.feed_pet('Food', 'Tera')
        self.assertEqual({"Food": 1030}, self.shop.food)
        self.assertEqual("Adding food...", result)

    def test_feed_pet_successfully(self):
        self.shop.pets = ["Tera", 'Jessey']
        self.shop.food = {"Food": 1000}
        result = self.shop.feed_pet('Food', 'Tera')
        self.assertEqual({"Food": 900}, self.shop.food)
        self.assertEqual("Tera was successfully fed", result)

    def test_repr_method(self):
        self.shop.pets = ['Tera', 'Jessey']
        result = repr(self.shop)
        self.assertEqual("Shop Test:\nPets: Tera, Jessey", result)


if __name__ == '__main__':
    main()