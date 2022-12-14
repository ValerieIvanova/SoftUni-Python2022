from exam_prep.oop_exam_16_aug_20.project.hardware.heavy_hardware import HeavyHardware
from exam_prep.oop_exam_16_aug_20.project.hardware.power_hardware import PowerHardware
from exam_prep.oop_exam_16_aug_20.project.software.express_software import ExpressSoftware
from exam_prep.oop_exam_16_aug_20.project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        new_power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(new_power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        new_heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(new_heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        if not hardware:
            return "Hardware does not exist"
        new_express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware[0].install(new_express_software)
        System._software.append(new_express_software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        if not hardware:
            return "Hardware does not exist"
        new_light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware[0].install(new_light_software)
        System._software.append(new_light_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        software = [s for s in System._software if s.name == software_name]
        if hardware and software:
            hardware[0].uninstall(software[0])
            System._software.remove(software[0])
        else:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        result = ["System Analysis",
                  f"Hardware Components: {len(System._hardware)}",
                  f"Software Components: {len(System._software)}",
                  f"Total Operational Memory: {sum(s.memory_consumption for s in System._software)} / "
                  f"{sum(h.memory for h in System._hardware)}",
                  f"Total Capacity Taken: {sum(s.capacity_consumption for s in System._software)} / "
                  f"{sum(h.capacity for h in System._hardware)}"
                  ]
        return '\n'.join(result)

    @staticmethod
    def system_split():
        result = []
        for h in System._hardware:
            result.append(f"Hardware Component - {h.name}")
            result.append(f"Express Software Components: {len([s for s in h.software_components if s.software_type == 'Express'])}")
            result.append(f"Light Software Components: {len([s for s in h.software_components if s.software_type == 'Light'])}")
            result.append(f"Memory Usage: {sum(s.memory_consumption for s in h.software_components)} / {h.memory}")
            result.append(f"Capacity Usage: {sum(s.capacity_consumption for s in h.software_components)} / {h.capacity}")
            result.append(f"Type: {h.hardware_type}")
            result.append(f"Software Components: {', '.join(s.name for s in h.software_components)}"
                          if h.software_components else 'Software Components: None')

        return '\n'.join(result)