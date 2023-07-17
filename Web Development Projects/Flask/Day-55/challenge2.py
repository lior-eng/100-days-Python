from typing import Callable, Any

def logging_decorator(function: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args) -> int:
        func = function(args)
        print(f"{function.__name__}")
        return func
    return wrapper

def a_function(*args) -> int:
    total_sum = 0
    for num in args:
        total_sum += num
    return total_sum

@logging_decorator
def my_func(*args) -> int:
    result = a_function(1,1,6)
    return result

print(my_func())
