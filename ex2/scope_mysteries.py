from collections.abc import Callable


def mage_counter() -> Callable:
    counter = 0

    def counting_calls() -> int:
        nonlocal counter
        counter += 1
        return counter
    return counting_calls


def spell_accumulator(initial_power: int) -> Callable:
    def accumulator(amount: int) -> int:
        nonlocal initial_power
        initial_power += amount
        return initial_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchantement_description(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchantement_description


def memory_vault() -> dict[str, Callable]:
    vault = {}

    def store(key, value):
        vault[key] = value

    def recall(key):
        return vault.get(key, "Memory not found")
    return {"store": store, "recall": recall}


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call: {counter_a()}")
    print(f"counter_a call: {counter_a()}")
    print(f"counter_b call: {counter_b()}")
    print()

    print("Testing spell accumulator...")
    acc = spell_accumulator(100)
    print(f"Base 100, add 20: {acc(20)}")
    print(f"Base 100, add 30: {acc(30)}")
    print()

    print("Testing enchantement factory...")
    enchantement1 = enchantment_factory("Flaming")
    enchantement2 = enchantment_factory("Windy")
    print(enchantement1("Sword"))
    print(enchantement2("Wand"))
    print()

    print("Testing memory vault...")
    mem = memory_vault()
    print("Store 'secret' = 42")
    mem["store"]("secret", 42)
    print(f"Recall 'secret': {mem["recall"]("secret")}")
    print(f"Recall 'unknown': {mem["recall"]("unknown")}")


if __name__ == "__main__":
    main()
