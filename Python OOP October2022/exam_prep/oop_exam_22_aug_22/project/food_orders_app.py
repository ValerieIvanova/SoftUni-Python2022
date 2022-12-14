from exam_prep.oop_exam_22_aug_22.project.client import Client
from exam_prep.oop_exam_22_aug_22.project.meals.dessert import Dessert
from exam_prep.oop_exam_22_aug_22.project.meals.main_dish import MainDish
from exam_prep.oop_exam_22_aug_22.project.meals.meal import Meal
from exam_prep.oop_exam_22_aug_22.project.meals.starter import Starter


class FoodOrdersApp:
    MEAL_TYPES_REF = {
        'Starter': Starter,
        'MainDish': MainDish,
        'Dessert': Dessert,
    }

    RECEIPT_ID = 0

    def __init__(self):
        self.menu = []  # all the meals (objects)
        self.clients_list = []  # all the clients (objects)

    def __find_client(self, phone_number):
        for client in self.clients_list:
            if client.phone_number == phone_number:
                return client

    def __find_meal(self, meal_name):
        for meal in self.menu:
            if meal.name == meal_name:
                return meal

    def __check_if_menu_is_ready(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    def register_client(self, client_phone_number: str):
        client = self.__find_client(client_phone_number)
        if client:
            raise Exception("The client has already been registered!")

        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if type(meal).__name__ in FoodOrdersApp.MEAL_TYPES_REF:
                self.menu.append(meal)

    def show_menu(self):
        self.__check_if_menu_is_ready()
        result = []
        [result.append(meal.details()) for meal in self.menu]
        return '\n'.join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        self.__check_if_menu_is_ready()
        client = self.__find_client(client_phone_number)
        if not client:
            client = Client(client_phone_number)
            self.clients_list.append(client)

        meals_to_order = []

        for meal_name, quantity in meal_names_and_quantities.items():
            meal = self.__find_meal(meal_name)
            if not meal:
                raise Exception(f"{meal_name} is not on the menu!")
            if meal.quantity < quantity:
                raise Exception(f"Not enough quantity of {type(meal).__name__}: {meal_name}!")

        for meal_name, quantity in meal_names_and_quantities.items():
            meal = self.__find_meal(meal_name)
            meal_type = type(meal).__name__
            order = FoodOrdersApp.MEAL_TYPES_REF[meal_type](meal_name, meal.price, quantity)
            meals_to_order.append(order)
            meal.quantity -= quantity

        client.shopping_cart.extend(meals_to_order)
        client.bill += sum(m.quantity * m.price for m in meals_to_order)
        return f"Client {client_phone_number} successfully ordered {', '.join(m.name for m in client.shopping_cart)} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self.__find_client(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for returned_meal in client.shopping_cart:
            meal = self.__find_meal(returned_meal.name)
            meal.quantity += returned_meal.quantity

        client.shopping_cart = []
        client.bill = 0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.__find_client(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        client.shopping_cart = []
        payed = client.bill
        client.bill = 0
        FoodOrdersApp.RECEIPT_ID += 1
        return f"Receipt #{FoodOrdersApp.RECEIPT_ID} with total amount of " \
               f"{payed:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

#
# from project.meals.starter import Starter
# from project.meals.dessert import Dessert
# from project.meals.main_dish import MainDish
#
# food_orders_app = FoodOrdersApp()
# print(food_orders_app.register_client("0899999999"))
# french_toast = Starter("French toast", 6.50, 5)
# hummus_and_avocado_sandwich = Starter("Hummus and Avocado Sandwich", 7.90)
# tortilla_with_beef_and_pork = MainDish("Tortilla with Beef and Pork", 12.50, 12)
# risotto_with_wild_mushrooms = MainDish("Risotto with Wild Mushrooms", 15)
# chocolate_cake_with_mascarpone = Dessert("Chocolate Cake with Mascarpone", 4.60, 17)
# chocolate_and_violets = Dessert("Chocolate and Violets", 5.20)
# print(food_orders_app.add_meals_to_menu(
#     french_toast, hummus_and_avocado_sandwich,
#     tortilla_with_beef_and_pork,
#     risotto_with_wild_mushrooms,
#     chocolate_cake_with_mascarpone,
#     chocolate_and_violets))
# print(food_orders_app.show_menu())
# food = {"Hummus and Avocado Sandwich": 5,
#         "Risotto with Wild Mushrooms": 1,
#         "Chocolate and Violets": 4}
# print(food_orders_app.add_meals_to_shopping_cart('0899999999', **food))
# additional_food = {"Risotto with Wild Mushrooms": 2,
#                    "Tortilla with Beef and Pork": 2}
# print(food_orders_app.add_meals_to_shopping_cart('0899999999', **additional_food))
# print(food_orders_app.finish_order("0899999999"))
# print(food_orders_app)
