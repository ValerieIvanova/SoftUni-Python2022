class Everland:
    def __init__(self):
        self.rooms = []  # all rooms (objects)

    def add_room(self, room: object):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total = 0
        for room in self.rooms:
            total += room.expenses + room.room_cost
        return f"Monthly consumption: {total:.2f}$."

    def pay(self):
        result = []
        for room in self.rooms:
            if room.budget >= room.expenses + room.room_cost:
                room.budget -= room.expenses + room.room_cost
                result.append(
                    f"{room.family_name} paid {room.expenses + room.room_cost:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)

        return '\n'.join(result)

    def status(self):
        total_population = sum(r.members_count for r in self.rooms)
        result = [f"Total population: {total_population}"]
        for room in self.rooms:
            result.append(
                f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$")

            if room.children:
                for i in range(1, len(room.children)+1):
                    result.append(f"--- Child {i} monthly cost: {room.children[i-1].cost * 30:.2f}$")
            if hasattr(room, 'appliances'):
                result.append(f"--- Appliances monthly cost: {sum(a.get_monthly_expense() for a in room.appliances):.2f}$")

        return '\n'.join(result)

#
# from people.child import Child
# from rooms.young_couple import YoungCouple
# from rooms.young_couple_with_children import YoungCoupleWithChildren
#
# everland = Everland()
#
#
# def test_one():
#     young_couple = YoungCouple("Johnsons", 150, 205)
#
#     child1 = Child(5, 1, 2, 1)
#     child2 = Child(3, 2)
#     young_couple_with_children = YoungCoupleWithChildren("Peterson", 480, 520, child1, child2)
#     everland.add_room(young_couple)
#     everland.add_room(young_couple_with_children)
#
#     print(everland.get_monthly_consumptions())
#     print(everland.pay())
#     print(everland.status())
#
#
# if __name__ == "__main__":
#     test_one()
