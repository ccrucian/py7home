from ex1 import (
    TransformCreatureFactory,
    HealingCreatureFactory
)


def main() -> None:
    print("Test: Creature with healing capability")
    healfactory = HealingCreatureFactory()
    sprout = healfactory.create_base()
    print("base:")
    print(f"{sprout.describe()}")
    print(f"{sprout.attack()}")
    print("evolved:")
    bloom = healfactory. create_evolved()
    print(f"{bloom.describe()}")
    print(f"{bloom.attack()}")
    print(f"{bloom.heal()}")
    print("")
    print("Test: Creature with transforming capability")
    tfactory = TransformCreatureFactory()
    shift = tfactory.create_base()
    morf = tfactory.create_evolved()
    print("base:")
    print(f"{shift.describe()}")
    print(f"{shift.attack()}")
    print(f"{shift.transform()}")
    print(f"{shift.attack()}")
    print(f"{shift.revert()}")
    print("evolved:")
    print(f"{morf.describe()}")
    print(f"{morf.attack()}")
    print(f"{morf.transform()}")
    print(f"{morf.attack()}")
    print(f"{morf.revert()}")


if __name__ == "__main__":
    main()
