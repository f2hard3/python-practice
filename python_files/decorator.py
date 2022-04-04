def deco(number):
    def decorator(func):
        print(number)
        print(type(func))
        return func
    return decorator

@deco(number=100)
def test_func():
    print('hello')

test_func()