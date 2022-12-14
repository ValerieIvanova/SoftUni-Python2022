from exam_prep.oop_exam_15_aug_21.project.table.table import Table


class OutsideTable(Table):
    START_NUMBER = 51
    END_NUMBER = 100

    def __init__(self, table_number, capacity):
        super().__init__(table_number, capacity)

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if not OutsideTable.START_NUMBER <= value <= OutsideTable.END_NUMBER:
            raise ValueError("Outside table's number must be between 51 and 100 inclusive!")
        self.__table_number = value
