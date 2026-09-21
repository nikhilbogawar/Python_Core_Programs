# 18. Design a system without abstraction first:
# • Write separate functions for EmailSender, SMSSender, PushSender
# Show how the main program becomes a mess with constant if/else.
# Then:
# • Redesign using an abstract base class Notifier.

# def send_notification(type,msg):
#     if type == "email":
#         print("Email:",msg)
#     elif type == "sms":
#         print("SMS:",msg)
#     elif type == "push":
#         print("Push:",msg)
# send_notification("email","Hello")
# send_notification("sms","Hi")

from abc import ABC, abstractmethod
class Notifier(ABC):
    @abstractmethod
    def send(self, msg):
        pass
class EmailNotifier(Notifier):
    def send(self,msg):
        print("Email:", msg)
class SMSNotifier(Notifier):
    def send(self,msg):
        print("SMS:", msg)
class PushNotifier(Notifier):
    def send(self,msg):
        print("Push:", msg)
notifiers = [EmailNotifier(),SMSNotifier(),PushNotifier()]
for n in notifiers:
    n.send("Hii Guys")