from abc import ABC, abstractmethod
from ex0 import Creature


class HealCapability(ABC):

    @abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability(ABC):

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self) -> str:
        return f"{self.name} heals and other for a large amount."


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self) -> str:
        return f"{self.name} heals and other for a large amount."


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")
        self.transformed: bool = False

    def attack(self) -> str:
        if self.transformed:
            return f"{self.name}"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} shifts into a sharper form."

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} return to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")
        self.transformed: bool = False

    def attack(self) -> str:
        if self.transformed:
            return f"{self.name} unleashes a devastating strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} morphs into a dragonic battle form"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} stabilizes its form."
