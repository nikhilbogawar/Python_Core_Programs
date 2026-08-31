# 7. Create:
# • Class Sorter with change(strategy) method. Separate strategy classes: BS, MS, QS,
# each implementing a different logic method.
# Demonstrate how polymorphism can be achieved without inheritance by using
# interchangeable strategy objects.
class Sorter:
    def strategy(self,obj):
        obj.logic()

class MS:
    def logic(self):
        print("merge sort")
class QS:
    def logic(self):
        print("quick")
class BS:
    def logic(self):
        print('Bubble')

l=[MS(),QS(),BS()]

for i in l:
    Sorter().strategy(i)