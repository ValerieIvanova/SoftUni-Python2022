from exam_prep.oop_exam_15_aug_21.project.table.table import Table


class InsideTable(Table):
    START_NUMBER = 1
    END_NUMBER = 50

    def __init__(self, table_number, capacity):
        super().__init__(table_number, capacity)

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if not InsideTable.START_NUMBER <= value <= InsideTable.END_NUMBER:
            raise ValueError("Inside table's number must be between 1 and 50 inclusive!")
        self.__table_number = value
