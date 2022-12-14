from exam_prep.oop_exam_16_aug_20.project.software.software import Software


class Hardware:

    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software: Software):
        if not (software.capacity_consumption <= self.available_capacity
                and software.memory_consumption <= self.free_memory):
            raise Exception("Software cannot be installed")
        self.software_components.append(software)

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)

    @property
    def free_memory(self):
        return self.memory - sum(s.memory_consumption for s in self.software_components)

    @property
    def available_capacity(self):
        return self.capacity - sum(s.capacity_consumption for s in self.software_components)