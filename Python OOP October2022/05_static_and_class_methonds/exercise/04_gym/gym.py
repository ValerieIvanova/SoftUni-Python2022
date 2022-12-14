from customer import Customer
from equipment import Equipment
from exercise_plan import ExercisePlan
from subscription import Subscription
from trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscription_obj = [s for s in self.subscriptions if s.id == subscription_id][0]
        customer_obj = [c for c in self.customers if c.id == subscription_obj.customer_id][0]
        trainer_obj = [t for t in self.trainers if t.id == subscription_obj.trainer_id][0]
        plan_obj = [p for p in self.plans if p.trainer_id == trainer_obj.id][0]
        equipment_obj = [e for e in self.equipment if e.id == plan_obj.equipment_id][0]

        return f"{subscription_obj}\n{customer_obj}\n{trainer_obj}\n{equipment_obj}\n{plan_obj}"


