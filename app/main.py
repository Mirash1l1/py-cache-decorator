from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cash = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))

        if key in cash:
            print("Getting from cache")
            return cash[key]

        print("Calculating new result")
        result = func(*args, **kwargs)

        return result

    return wrapper