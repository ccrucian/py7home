from ex0 import FlameFactory, AquaFactory


def main() -> None:
    flamefactory = FlameFactory()
    aquafactory = AquaFactory()
    flameling = flamefactory.create_base()
    print("Testing factory")
    print(f"{flameling.describe()}")
    print(f"{flameling.attack()}")
    pyrodon = flamefactory.create_evolved()
    print(f"{pyrodon.describe()}")
    print(f"{pyrodon.attack()}")
    aquabub = aquafactory.create_base()
    print("Testing factory")
    print(f"{aquabub.describe()}")
    print(f"{aquabub.attack()}")
    bub = aquafactory.create_evolved()
    print(f"{bub.describe()}")
    print(f"{bub.attack()}")

    print("Testing battle")
    print(f"{flameling.describe()}")
    print("vs.")
    print(f"{aquabub.describe()}")
    print("fight!")
    print(f"{flameling.attack()}")
    print(f"{aquabub.attack()}")


if __name__ == "__main__":
    main()
