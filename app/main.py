from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cash = {}
    def wrapper(*args, **kwargs) -> Any:
        nonlocal cash
        key = (args, tuple(sorted(kwargs.items())))
        if key in cash:
            print("Getting from cache")
            return cash[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cash[key] = result
        return result
    return wrapper
