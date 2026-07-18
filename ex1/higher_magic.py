from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return f"Heals {target} with power = {power}"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} with power = {power}"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combiner(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combiner


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def new_spell(target: str, power: int) -> str:
        power2 = power * multiplier
        return (f"Original: {base_spell(target, power)},"
                f" {base_spell(target, power2)}")
    return new_spell


def condition(num: int) -> bool:
    return num > 20


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def inner(target: str, power: int) -> str:
        if condition(power):
            return spell(target, power)
        return "Spell fizzled"
    return inner


def spell_sequence(spells: list[Callable]) -> Callable:
    def inner(target: str, power: int) -> list[str]:
        result = []
        for spell in spells:
            result.append(spell(target, power))
        return result
    return inner


def main() -> None:
    dragon = ("Dragon", 10)
    knight = ("Knight", 50)
    spells = [fireball, heal]

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    combined_dragon = combined(dragon[0], dragon[1])
    print(f"Combined spell result: {combined_dragon[0]}, {combined_dragon[1]}")
    print()

    print("Testing power amplifier...")
    mage_fireball = power_amplifier(fireball, 3)
    amplified = mage_fireball(dragon[0], dragon[1])
    print(amplified)
    print()

    print("Testing conditional caster")
    caster = conditional_caster(condition, heal)
    knight_caster = caster(knight[0], knight[1])
    dragon_caster = caster(dragon[0], dragon[1])
    print(knight_caster)
    print()
    print(dragon_caster)
    print()

    print("Testing spell sequence...")
    speller = spell_sequence(spells)
    speller_result = speller(knight[0], knight[1])
    for result in speller_result:
        print(result)


if __name__ == "__main__":
    main()
