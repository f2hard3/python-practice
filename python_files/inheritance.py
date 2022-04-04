class Parent:
    def test(self):
        print('hello')

class Child(Parent):
    pass

instance = Child()
instance.test()