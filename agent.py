from enum import Enum
from dataclasses import dataclass

class Action(Enum):
    FOLD = 0
    CALL = 1
    RAISE = 2

@dataclass
class Move:
    action: Action
    amount: int

class Agent:
    def __init__(self) -> None:
        self.hand:list[int] = []
        self.chips = 0

    def initiate(self, chips: int) -> None:
        self.chips = chips
    
    def set_hand(self, hand: list[int]) -> None:
        assert(len(hand) == 2)
        self.hand = hand

    def move(self, args) -> Move:
        pass