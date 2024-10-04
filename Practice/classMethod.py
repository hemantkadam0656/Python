class MyClass:
    @classmethod
    def class_method(cls):
        print(f"Class method called from {cls.__name__}")


obj = MyClass()
print(obj)
