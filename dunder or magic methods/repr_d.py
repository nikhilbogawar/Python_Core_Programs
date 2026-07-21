class D:
    def __repr__(self):
        return "Nothing"
d1=D()
d2=D()
print(d1,d2)    # by using __str__ we can print easily and it uses only direct callings
l=[d1,d2]
print(l)    # but for this we use __repr__ to call indirectly and directly