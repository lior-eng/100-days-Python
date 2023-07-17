######################## First option ########################
from time import time

def speed_calc_decorator(function) -> None:
    def wrapper() -> None:
        return function()
    
    return wrapper    
        
@speed_calc_decorator   
def fast_function() -> float:
    start_time = time()
    for _ in range(100000):
        pass
    return start_time

@speed_calc_decorator   
def slow_function() -> float:
    for _ in range(100000):
        pass
    end_time = time()
    return end_time

start_time = fast_function()
end_time = slow_function()
print(f"Whole program run time: {end_time - start_time}")

######################## second option ########################
current_time = time()
print(f"Current_time {current_time}")

def speed_calc_decorator(function) -> None:
    def wrapper() -> None:
        start_time = time()
        function()
        end_time = time()
        print(f"{function.__name__} run speed: {end_time - start_time}s")
    return wrapper    
        
@speed_calc_decorator   
def fast_function() -> float:
    start_time = time()
    for _ in range(100000):
        pass
    return start_time

@speed_calc_decorator   
def slow_function() -> float:
    for _ in range(1000000):
        pass
    end_time = time()
    return end_time

fast_function()
slow_function()

