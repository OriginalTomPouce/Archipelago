from enum import IntEnum, IntFlag
from tokenize import group
from typing import NamedTuple, Optional, List
from BaseClasses import Location, Item, ItemClassification


class BestTrainerLocation(Location):
    game = "Best Trainer"

class BestTrainerItem(Item):
    game = "Best Trainer"


class CheckCategory(IntEnum):
    BASE = 0
    KANTO = 1
    JOHTO = 2
    TRAINERSANITY = 4
    ACHIEVEMENT = 8
    

class ItemCategory(IntEnum):
    BASE = 0
    KANTO = 1
    JOHTO = 2
    DRAFT = 4

class CupLevel(IntEnum):
    MISC = 0
    EXTRA = 1
    LOCAL = 2
    CITY = 3
    SUBREGION = 4
    REGION = 5
    WORLD = 6

    
class RegionData(NamedTuple):
    level: CupLevel = CupLevel.LOCAL
    battle_number: int = 3
    key_name: str = ""
    required_key: List[str] = []


class LocData(NamedTuple):
    id: int = 0
    category: int = CheckCategory.BASE
    region: str = ""    
    required_key: str = ""


class ItemData(NamedTuple):
    code: Optional[int]
    classification: ItemClassification
    group: str
    category: int = ItemCategory.BASE

