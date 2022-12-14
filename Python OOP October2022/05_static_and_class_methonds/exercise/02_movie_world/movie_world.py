from customer import Customer
from dvd import DVD


class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer_obj = [c for c in self.customers if c.id == customer_id][0]
        dvd_obj = [d for d in self.dvds if d.id == dvd_id][0]

        if dvd_obj in customer_obj.rented_dvds:
            return f"{customer_obj.name} has already rented {dvd_obj.name}"

        if dvd_obj.is_rented:
            return "DVD is already rented"

        if customer_obj.age < dvd_obj.age_restriction:
            return f"{customer_obj.name} should be at least {dvd_obj.age_restriction} to rent this movie"

        customer_obj.rented_dvds.append(dvd_obj)
        dvd_obj.is_rented = True
        return f"{customer_obj.name} has successfully rented {dvd_obj.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer_obj = [c for c in self.customers if c.id == customer_id][0]
        dvd_obj = [d for d in self.dvds if d.id == dvd_id][0]

        if dvd_obj in customer_obj.rented_dvds:
            dvd_obj.is_rented = False
            customer_obj.rented_dvds.remove(dvd_obj)
            return f"{customer_obj.name} has successfully returned {dvd_obj.name}"
        return f"{customer_obj.name} does not have that DVD"

    def __repr__(self):
        result = []
        [result.append(str(x)) for x in self.customers]
        [result.append(str(x)) for x in self.dvds]

        return '\n'.join(result)
