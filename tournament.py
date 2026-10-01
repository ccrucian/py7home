from ex2 import (
            NormalStrategy,
            AggressiveStrategy,
            DefensiveStrategy,
            BattleStrategy, InvalidStrategy
                )

from ex1 import (
    TransformCreatureFactory,
    HealingCreatureFactory
)

from ex0 import (
    FlameFactory, AquaFactory,
    CreatureFactory, Creature)


def tournament(opponents: list[tuple[
        CreatureFactory, BattleStrategy
        ]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    creatures: list[
        tuple[Creature, BattleStrategy]
    ] = []

    for factory, strategy in opponents:
        creature = factory.create_base()
        creatures.append((creature, strategy))

    for i in range(len(creatures)):
        for j in range(i + 1, len(creatures)):
            creature1, strategy1 = creatures[i]
            creature2, strategy2 = creatures[j]
            print("* Battle *")
            print(f"{creature1.describe()}")
            print(" vs.")
            print(f"{creature2.describe()}")
            print("now fight!")

            try:
                print(strategy1.act(creature1))
                print(strategy2.act(creature2))
            except InvalidStrategy as e:
                print(
                    "Battle error,"
                    f" aborting tournament: {e}"
                )
                return


def main() -> None:
    flame = FlameFactory()
    aqua = AquaFactory()
    healer = HealingCreatureFactory()
    trans = TransformCreatureFactory()
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defense = DefensiveStrategy()
    opponents = [
        (flame, normal), (aqua, normal),
        (healer, defense), (trans, aggressive),
        (trans, normal)
    ]
    tournament(opponents)


if __name__ == "__main__":
    main()
