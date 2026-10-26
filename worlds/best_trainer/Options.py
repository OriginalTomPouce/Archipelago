from re import A
from typing import List, TYPE_CHECKING, Dict, Any
from schema import Schema, Optional
from dataclasses import dataclass
from worlds.AutoWorld import PerGameCommonOptions
from Options import Range, Toggle, Choice, OptionDict, DefaultOnToggle, OptionGroup, StartInventoryPool

if TYPE_CHECKING:
    from . import BestTrainerWorld


def create_option_groups() -> List[OptionGroup]:
    option_group_list: List[OptionGroup] = []
    for name, options in best_trainer_option_groups.items():
        option_group_list.append(OptionGroup(name=name, options=options))

    return option_group_list


def adjust_options(world: "BestTrainerWorld"):

    if world.options.DraftChangeAvailable.value > 20:
        world.options.DraftChangeAvailable.value = 20
        
    if world.options.RegionsAvailables.value != 0:
        world.options.Goal.value = 2

class Goal(Choice):
    """Goal required to beat the game.
    World Cup: Win a world cup tournament

    Region Cup: Win a region Cup
    """
    display_name = "Goal"
    option_indigo_league = 1
    option_region = 2
    default = 2



class RegionsAvailables(Choice):
    """Selected regions to be included in the game.
    Both: All regions are included in the game
    Johto: Only Johto regions are included in the game
    Kanto: Only Kanto regions are included in the game
    """
    display_name = "Regions available"
    option_both = 0
    option_johto = 1
    option_kanto = 2
    default = 0



class TrainerRoundSanity(Toggle):
    """If enabled, every swiss round won of a tournament will send a check."""
    display_name = "Trainer Round Sanity"
    

class DraftChangeAvailable(Range):
    """How much draft change points will be available."""
    display_name = "Draft change available"
    range_start = 0
    range_end = 20
    default = 10
    
class DraftTypes(Choice):
    """How Pokemon Types in draft will be handled: 
    All Available : All Pokemon Types will be available in the draft
    Random Locked : Random Pokemon Types will be locked in the draft
    Start with common : Start with common Pokemon Types in the draft
    """
    display_name = "Draft Types"
    option_all_available = 0
    option_random_locked = 1
    option_start_with_common = 2
    default = 0
    

class NumberOfStartingTypes(Range):
    """If you start with a random number of types, tell you how many types you'll get when you start the game.
    Minimum number is 1
    Maximum is 18"""
    display_name = "Number of Starting Types"
    range_start = 1
    range_end = 18
    default = 5

class AddExtraDraftTypesItems(Toggle):
    """If enabled, add extra common draft types items, depending of the locked type.
    The following types will have 2 more copies of the unlock item : Normal, Fire, Water, Electric, Bug, Flying
    The following types will have 1 more copies of the unlock item : Electric, Fighting, Ground, Rock, Poison, Psychic
    """
    display_name = "Add Extra Draft Types Items"

class LockDraftPower(Toggle):
    """If enabled, lock the power of the Pokemon you can draft."""
    display_name = "Lock Draft Power"

class AddAchievements(Toggle):
    """If enabled, achievements will send a check."""
    display_name = "Add Achievements"

@dataclass
class BestTrainerOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool

    Goal:                       Goal
    RegionsAvailables:          RegionsAvailables
    TrainerRoundSanity:         TrainerRoundSanity
    AddAchievements:            AddAchievements
    DraftChangeAvailable:       DraftChangeAvailable
    DraftTypes:                 DraftTypes
    NumberOfStartingTypes:      NumberOfStartingTypes
    AddExtraDraftTypesItems:    AddExtraDraftTypesItems
    LockDraftPower:             LockDraftPower


best_trainer_option_groups: Dict[str, List[Any]] = {
    "General Options": [Goal, RegionsAvailables, DraftTypes, LockDraftPower, NumberOfStartingTypes],

    "Checks Options": [TrainerRoundSanity, AddAchievements],

    "Item Options": [DraftChangeAvailable, AddExtraDraftTypesItems],
}


slot_data_options: List[str] = [
    "Goal",
    "RegionsAvailables",
    "TrainerRoundSanity",
    "AddAchievements",
    "DraftTypes",
    "NumberOfStartingTypes",
    "LockDraftPower",
    "DraftChangeAvailable",
    "AddExtraDraftTypesItems",
]
