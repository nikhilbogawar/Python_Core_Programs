# Design a class Vehicle that:
# •	Keeps a record of service charge rate common to all vehicles.
# •	Each vehicle has a model, kilometers_run, and service history.
# •	Has a function to calculate service charge based on km and rate.
# •	Provides a method to update the service rate for all vehicles.
# •	Provides a static tool to check if a vehicle model is eligible for service (not older than 15 years).
# Demonstrate:
# 1.	Creating vehicles with different km and models.
# 2.	Updating the service rate.
# 3.	Showing charges and eligibility checks.

class Vehicle:
    service_rate=5
    def __init__(self,model,km_run,year):
        self.model=model
        self.km_run=km_run
        self.year=year
        self.service_history=[]

    def service_charge(self):
        charge=self.km_run * Vehicle.service_rate
        self.service_history.append(charge)
        return charge

    @classmethod
    def update_rate(cls,new_rate):
        cls.service_rate=new_rate

    @staticmethod
    def is_eligible(year):
        return (2026-year)<=15

veh1=Vehicle("Volkswagen Polo",100,2015)
veh2=Vehicle("BMW M5", 85, 2020)
print(veh1.model, veh1.service_charge())
print(veh2.model, veh2.service_charge())

Vehicle.update_rate(10)
print(veh1.model, veh1.service_charge())
print(veh2.model, veh2.service_charge())
print(Vehicle.is_eligible(2000))  #False