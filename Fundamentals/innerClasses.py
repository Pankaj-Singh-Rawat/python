from io import IncrementalNewlineDecoder


class Outer:
    def __init__(self):
        self.name = "Outer"

    class Inner:
        def __init__(self):
            self.name = "Inner"

        def display(self):
            print("Hello from inner class")

        class Deeper:
            def __init__(self):
                self.name = "Deeper class"

            def display(self):
                print("Hello from Deeper class")




obj1 = Outer()
obj2 = obj1.Inner()
obj3 = Outer().Inner()
obj2.display()
obj3.display()


obj4 = Outer().Inner().Deeper()
obj4.display()

class Outer:
    def __init__(self):
        self.name = "Outer"

    class Inner:
        def __init__(self, outer):
            self.outer = outer

        def display(self):
            print("Hey Outer Class name is :", self.outer.name)



obj1 = Outer()
obj2 = obj1.Inner(obj1)
obj2.display()