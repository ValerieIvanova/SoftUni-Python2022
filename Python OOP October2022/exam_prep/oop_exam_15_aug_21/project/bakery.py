from exam_prep.oop_exam_15_aug_21.project.baked_food.bread import Bread
from exam_prep.oop_exam_15_aug_21.project.baked_food.cake import Cake
from exam_prep.oop_exam_15_aug_21.project.drink.tea import Tea
from exam_prep.oop_exam_15_aug_21.project.drink.water import Water
from exam_prep.oop_exam_15_aug_21.project.table.inside_table import InsideTable
from exam_prep.oop_exam_15_aug_21.project.table.outside_table import OutsideTable


class Bakery:
    FOOD_TYPES_REF = {
        'Bread': Bread,
        'Cake': Cake,
    }

    DRINK_TYPES_REF = {
        'Tea': Tea,
        'Water': Water
    }

    TABLE_TYPES_REF = {
        'InsideTable': InsideTable,
        'OutsideTable': OutsideTable
    }

    def __init__(self, name):
        self.name = name
        self.food_menu = []  # every type of food in the bakery's menu.
        self.drinks_menu = []  # every type of drink in the bakery's menu.
        self.tables_repository = []  # every table at the bakery.
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def __get_table(self, table_number):
        for t in self.tables_repository:
            if t.table_number == table_number:
                return t

    @staticmethod
    def get_item(name, menu):
        for item in menu:
            if name == item.name:
                return item

    def add_food(self, food_type, name, price):
        if name in [f.name for f in self.food_menu]:
            raise Exception(f"{food_type} {name} is already in the menu!")

        if food_type in Bakery.FOOD_TYPES_REF:
            self.food_menu.append(Bakery.FOOD_TYPES_REF[food_type](name, price))
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name, portion, brand):
        if name in [d.name for d in self.drinks_menu]:
            raise Exception(f"{drink_type} {name} is already in the menu!")

        if drink_type in Bakery.DRINK_TYPES_REF:
            self.drinks_menu.append(Bakery.DRINK_TYPES_REF[drink_type](name, portion, brand))
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type, table_number, capacity):
        if table_number in [t.table_number for t in self.tables_repository]:
            raise Exception(f"Table {table_number} is already in the bakery!")

        if table_type in Bakery.TABLE_TYPES_REF:
            self.tables_repository.append(Bakery.TABLE_TYPES_REF[table_type](table_number, capacity))
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people):
        for table in self.tables_repository:
            if not table.is_reserved and number_of_people <= table.capacity:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        table = self.__get_table(table_number)

        if not table:
            return f"Could not find table {table_number}"

        ordered = []
        not_ordered = []

        for f in food_names:
            food_to_order = self.get_item(f, self.food_menu)

            if food_to_order:
                table.order_food(food_to_order)
                ordered.append(repr(food_to_order))
            else:
                not_ordered.append(f)

        result = []
        if ordered:
            result.append(f"Table {table_number} ordered:")
            result.extend(ordered)
        if not_ordered:
            result.append(f"{self.name} does not have in the menu:")
            result.extend(not_ordered)

        return '\n'.join(result)

    def order_drink(self, table_number: int, *drinks_names):
        table = self.__get_table(table_number)

        if not table:
            return f"Could not find table {table_number}"

        ordered = []
        not_ordered = []

        for d in drinks_names:
            drink_to_order = self.get_item(d, self.drinks_menu)
            if drink_to_order:
                table.order_drink(drink_to_order)
                ordered.append(repr(drink_to_order))
            else:
                not_ordered.append(d)

        result = []
        if ordered:
            result.append(f"Table {table_number} ordered:")
            result.extend(ordered)
        if not_ordered:
            result.append(f"{self.name} does not have in the menu:")
            result.extend(not_ordered)

        return '\n'.join(result)

    def leave_table(self, table_number):
        table = self.__get_table(table_number)
        total = table.get_bill()
        self.total_income += total
        table.clear()
        return f"Table: {table_number}\n" \
               f"Bill: {total:.2f}"

    def get_free_tables_info(self):
        result = [table.free_table_info() for table in self.tables_repository if not table.is_reserved]
        return '\n'.join(result)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"