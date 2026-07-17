from functools import reduce, partial, lru_cache, singledispatch
from operator import mul, add
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    result: int
    op = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min
    }

    if len(spells) == 0:
        return 0
    all_num = all(isinstance(spell, int) for spell in spells)
    is_op = operation in op
    if not all_num:
        raise ValueError("Please send only int values")
    if not is_op:
        raise ValueError(f"Unknown operation: {operation}")
    result = reduce(op[operation], spells)
    return result


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"element: {element} - Power: {power} - Target: {target}"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire = partial(base_enchantment, power=50, element="fire")
    ice = partial(base_enchantment, power=50, element="ice")
    lightning = partial(base_enchantment, power=50, element="lightning")

    enchantment: dict[str, Callable] = {
        "fire": fire,
        "ice": ice,
        "lightning": lightning
    }
    return enchantment


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatcher(var: Any):
        return "Unknown spell type"

    @dispatcher.register(int)
    def damage_spell(n: int) -> str:
        return f"{n} damage"

    @dispatcher.register(str)
    def enchantment(s: str):
        return f"{s}"

    @dispatcher.register(list)
    def multi_cast(lst: list):
        return f"{len(lst)} spells"

    return dispatcher


def main() -> None:
    spell_powers = [20, 37, 18, 14, 45, 50]
    operations = ['add', 'multiply', 'max', 'min']

    print("Testing spell reducer...")

    try:
        print(f"Sum: {spell_reducer(spell_powers, operations[0])}")
        print(f"Product: {spell_reducer(spell_powers, operations[1])}")
        print(f"Max: {spell_reducer(spell_powers, operations[2])}")
        print(f"Min: {spell_reducer(spell_powers, operations[3])}")
    except Exception as e:
        print(e)
    print()

    print("Testing partial enchantement...")
    ench = partial_enchanter(base_enchantment)
    print(ench["fire"](target="Dragon"))
    print(ench["ice"](target="Goblin"))
    print(ench["lightning"](target="Orc"))
    print()

    print("Testing memoized fibonacci...")
    print(f"fib(0): {memoized_fibonacci(0)}")
    print(f"fib(1): {memoized_fibonacci(1)}")
    print(f"fib(10): {memoized_fibonacci(10)}")
    print(f"fib(15): {memoized_fibonacci(15)}")
    print()

    print("Testing spell dispatcher...")
    dispatch = spell_dispatcher()
    print(f"Damage spell: {dispatch(42)}")
    print(f"Enchantment: {dispatch("fireball")}")
    print(f"Multi-cast: {dispatch(spell_powers)}")
    print(dispatch({1: "n", 2: "b", 3: "m"}))
    print()


if __name__ == "__main__":
    main()
