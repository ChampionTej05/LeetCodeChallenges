class Base:
    def method(self):
        return "Base Method"

class DerivedA(Base):
    def method(self):
        return "DerivedA Method"

class DerivedB(Base):
    def method(self):
        return "DerivedB Method"

class Diamond(DerivedB, DerivedA):
    pass

diamond = Diamond()
print(diamond.method())

