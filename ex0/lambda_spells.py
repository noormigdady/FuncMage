def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x.get("power", 0), reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x.get("power", 0) >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map((lambda x: f"*{x}*"), spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}
    stats = {}
    sum_power = round(sum(mage["power"] for mage in mages) / len(mages), 2)
    stats["max_power"] = max(mages, key=lambda x: x.get("power", 0))["power"]
    stats["min_power"] = min(mages, key=lambda x: x.get("power", 0))["power"]
    stats["avg_power"] = sum_power
    return stats


def main() -> None:
    artifacts = [
        {"name": "Crystal Orb", "power": 78, "type": "armor"},
        {"name": "Crystal Orb", "power": 103, "type": "relic"},
        {"name": "Light Prism", "power": 104, "type": "weapon"},
        {"name": "Shadow Blade", "power": 107, "type": "relic"}
    ]
    mages = [
        {"name": "Storm", "power": 53, "element": "earth"},
        {"name": "Casey", "power": 57, "element": "light"},
        {"name": "Riley", "power": 65, "element": "lightning"},
        {"name": "Alex", "power": 97, "element": "ice"},
        {"name": "Riley", "power": 77, "element": "earth"}
    ]

    spells = ["tornado", "lightning", "tsunami", "heal"]

    sorted_artifacs = artifact_sorter(artifacts)
    filtered_mages = power_filter(mages, 60)
    transformed_spells = spell_transformer(spells)
    mages_stats_result = mage_stats(mages)

    print("Testing artifact sorter...")
    for s in sorted_artifacs:
        print(s)

    print()
    print("Testing power filter with min_power = 60...")
    for mage in filtered_mages:
        print(f"{mage['name']} - Power: {mage['power']} - "
              f"Element: {mage['element']}")

    print()
    print("Testing spell transformer...")
    for spell in transformed_spells:
        print(spell, end=" ")
    print()

    print()
    print("Testing mage stats...")
    for key, value in mages_stats_result.items():
        print(f"{key} =  {value}")


if __name__ == "__main__":
    main()
