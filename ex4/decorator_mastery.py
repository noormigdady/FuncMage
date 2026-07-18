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


def power_validator(min_power: int) -> Callable:
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = args[2] if len(args) > 2 else kwargs.get("power", 0)
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return inner


@power_validator(50)
def fireball(target: str, power: int) -> str:
    return f"target: {target} - power: {power}"


def retry_spell(max_attempts: int) -> Callable:
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    func(*args, **kwargs)
                    break
                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying..."
                              f"(attempt {attempt}/ {max_attempts})")
                    if attempt == 3:
                        print(f"Spell casting failed after {max_attempts} "
                              f"attempts")
        return wrapper
    return inner


@retry_spell(3)
def spell(num: int):
    power = int(input("enter power: "))
    if power >= num:
        print("Waaaaaaagh spelled !")
        return
    else:
        raise f"{power} < {num}"


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        for i in name:
            if not i.isalpha() and not i.isspace():
                return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("Testing spell timer...")
    print(f"{cast.__name__}...")
    print(f"Result: {cast("fireball")}")
    print()

    print("Testing power validator...")
    print(fireball("Dragon", 70))
    print(fireball("Dragon", power=20))
    print()

    print("Testing retrying spell...")
    spell(20)
    print()

    print("Testing MageGuild...")
    ob = MageGuild()
    print(MageGuild.validate_mage_name("mage"))
    print(MageGuild.validate_mage_name("ma3"))
    print(ob.cast_spell("fireball", 50))
    print(ob.cast_spell("fireball", 5))


if __name__ == "__main__":
    main()
