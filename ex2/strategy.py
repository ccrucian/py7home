from abc import ABC, abstractmethod
from ex0 import Creature
from ex1 import ( TransformCapability,
                 HealCapability
                 )


class InvalidStrategy(Exception):
    pass


class BattleStrategy(ABC):

    @abstractmethod
    def act(self) -> str:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> str:
        return creature.attack()


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategy("Invalid Strategy for aggressive")
        act1 = creature.transform()
        act2 = creature.attack()
        act3 = creature.revert()

        return f"{act1}\n{act2}\n{act3}"


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategy("Invalid strategy for difensive")
        act1 = creature.attack()
        act2 = creature.heal()
        return f"{act1}\n{act2}"