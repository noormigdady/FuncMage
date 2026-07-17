from collections.abc import Callable
from functools import wraps
from time import perf_counter, sleep


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        time = end - start
        print(f"Spell comleted in {time:.3f} seconds")
        return result
    return wrapper


@spell_timer
def cast(name: str) -> str:
    sleep(0.5)
    return f"{name} cast!"


def main() -> None:
    print("Testing spell timer...")
    print(f"{cast.__name__}...")
    print(f"Result: {cast("fireball")}")
    print()


if __name__ == "__main__":
    main()
