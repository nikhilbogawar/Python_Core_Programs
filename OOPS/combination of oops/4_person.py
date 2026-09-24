# 4. Create classes:
# • Person → base
# • MedicalStaff(Person)
# • Doctor(MedicalStaff)
# • Surgeon(Doctor)
# Requirements:
# • Hide sensitive data (e.g., salary, patient notes)
# • Abstract method perform_duty()
# • Each level overrides the method with more specific behavior
# • Use super() to chain constructor calls
from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
class MedicalStaff(Person):
    @abstractmethod
    def perform_duty(self):
        pass
class Doctor(MedicalStaff):
    def perform_duty(self):
        # super().perform_duty()
        task = "Diagnose patients"
        return task
class Surgeon(Doctor):
    def perform_duty(self):
        super().perform_duty()
        task = "Perform surgery"
        return task
surgeon1 = Surgeon("Dr. Rao", 100000)
print(surgeon1.perform_duty())
