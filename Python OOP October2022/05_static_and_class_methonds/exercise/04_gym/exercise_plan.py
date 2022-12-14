class ExercisePlan:
    id = 1

    def __init__(self, trainer_id, equipment_id, duration):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan.get_next_id()

        __class__.id += 1

    @staticmethod
    def get_next_id():
        return __class__.id

    @classmethod
    def from_hours(cls, trainer_id, equipment_id, hours):
        minutes = hours * 60
        return cls(trainer_id, equipment_id, minutes)

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"