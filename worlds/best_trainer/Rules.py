from worlds.AutoWorld import CollectionState
from worlds.generic.Rules import add_rule, set_rule
from .Locations import location_table, event_locs, is_location_valid
from .Types import RegionData, CupLevel, CheckCategory
from BaseClasses import Location, Entrance, Region
from typing import TYPE_CHECKING, List, Callable, Union, Dict
from .Options import Goal, DraftTypes, LockDraftPower

if TYPE_CHECKING:
    from . import BestTrainerWorld
    
    
cup_regions = {
    "Home" : RegionData(CupLevel.MISC, 0, "", {}),
    "Local Cup New Bark Town": RegionData(CupLevel.LOCAL, 3, "Local Cup Unlock : New Bark Town", {}),
    "Local Cup Cherrygrove City": RegionData(CupLevel.LOCAL, 3, "Local Cup Unlock : Cherrygrove City", {}),
    "Local Cup Violet City": RegionData(CupLevel.LOCAL, 3, "Local Cup Unlock : Violet City", {}),
    "Local Cup Azalea Town": RegionData(CupLevel.LOCAL, 3, "Local Cup Unlock : Azalea Town", {}),
    "City Cup Goldenrod City": RegionData(CupLevel.CITY, 5, "City Cup Unlock : Goldenrod City", {"Local Cup Azalea Town Trophy", "Local Cup Violet City Trophy", "Local Cup New Bark Town Trophy", "Local Cup Cherrygrove City Trophy", "Local Cup Cianwood City Trophy", "Local Cup Mahogany Town Trophy"}),
    "City Cup Ecruteak City": RegionData(CupLevel.CITY, 5, "City Cup Unlock : Ecruteak City", {"Local Cup Azalea Town Trophy", "Local Cup Violet City Trophy", "Local Cup New Bark Town Trophy", "Local Cup Cherrygrove City Trophy", "Local Cup Cianwood City Trophy", "Local Cup Mahogany Town Trophy"}),
    "City Cup Olivine City": RegionData(CupLevel.CITY, 5, "City Cup Unlock : Olivine City", {"Local Cup Azalea Town Trophy", "Local Cup Violet City Trophy", "Local Cup New Bark Town Trophy", "Local Cup Cherrygrove City Trophy", "Local Cup Cianwood City Trophy", "Local Cup Mahogany Town Trophy"}),
    "Local Cup Cianwood City": RegionData(CupLevel.LOCAL, 3, "Local Cup Unlock : Cianwood City", {}),
    "Local Cup Mahogany Town": RegionData(CupLevel.LOCAL, 3, "Local Cup Unlock : Mahogany Town", {}),
    "City Cup Blackthorn City": RegionData(CupLevel.CITY, 5, "City Cup Unlock : Blackthorn City", {"Local Cup Azalea Town Trophy", "Local Cup Violet City Trophy", "Local Cup New Bark Town Trophy", "Local Cup Cherrygrove City Trophy", "Local Cup Cianwood City Trophy", "Local Cup Mahogany Town Trophy"}),
    "Local Cup Pallet Town": RegionData(CupLevel.LOCAL, 3, "Local Cup Unlock : Pallet Town", {}),
    "Local Cup Viridian City": RegionData(CupLevel.LOCAL, 3, "Local Cup Unlock : Viridian City", {}),
    "City Cup Pewter City": RegionData(CupLevel.CITY, 5, "City Cup Unlock : Pewter City", {"Local Cup Cerulean City Trophy", "Local Cup Vermilion City Trophy", "Local Cup Lavender Town Trophy", "Local Cup Cinnabar Island Trophy", "Local Cup Pallet Town Trophy", "Local Cup Viridian City Trophy"}),
    "Local Cup Cerulean City": RegionData(CupLevel.LOCAL, 3, "Local Cup Unlock : Cerulean City", {}),
    "Local Cup Vermilion City": RegionData(CupLevel.LOCAL, 3, "Local Cup Unlock : Vermilion City", {}),
    "Local Cup Lavender Town": RegionData(CupLevel.LOCAL, 3, "Local Cup Unlock : Lavender Town", {}),
    "City Cup Celadon City": RegionData(CupLevel.CITY, 5, "City Cup Unlock : Celadon City", {"Local Cup Cerulean City Trophy", "Local Cup Vermilion City Trophy", "Local Cup Lavender Town Trophy", "Local Cup Cinnabar Island Trophy", "Local Cup Pallet Town Trophy", "Local Cup Viridian City Trophy"}),
    "City Cup Fuchsia City": RegionData(CupLevel.CITY, 5, "City Cup Unlock : Fuchsia City", {"Local Cup Cerulean City Trophy", "Local Cup Vermilion City Trophy", "Local Cup Lavender Town Trophy", "Local Cup Cinnabar Island Trophy", "Local Cup Pallet Town Trophy", "Local Cup Viridian City Trophy"}),
    "City Cup Saffron City": RegionData(CupLevel.CITY, 5, "City Cup Unlock : Saffron City", {"Local Cup Cerulean City Trophy", "Local Cup Vermilion City Trophy", "Local Cup Lavender Town Trophy", "Local Cup Cinnabar Island Trophy", "Local Cup Pallet Town Trophy", "Local Cup Viridian City Trophy"}),
    "Local Cup Cinnabar Island": RegionData(CupLevel.LOCAL, 3, "Local Cup Unlock : Cinnabar Island", {}),
    
    "Subregion Cup West Johto": RegionData(CupLevel.SUBREGION, 7, "Subregion Cup Unlock : West Johto", {"City Cup Goldenrod City Trophy", "City Cup Ecruteak City Trophy", "City Cup Olivine City Trophy", "City Cup Blackthorn City Trophy"}),
    "Subregion Cup South Johto": RegionData(CupLevel.SUBREGION, 7, "Subregion Cup Unlock : South Johto", {"City Cup Goldenrod City Trophy", "City Cup Ecruteak City Trophy", "City Cup Olivine City Trophy", "City Cup Blackthorn City Trophy"}),
    "Subregion Cup North Johto": RegionData(CupLevel.SUBREGION, 7, "Subregion Cup Unlock : North Johto", {"City Cup Goldenrod City Trophy", "City Cup Ecruteak City Trophy", "City Cup Olivine City Trophy", "City Cup Blackthorn City Trophy"}),
    "Subregion Cup West Kanto": RegionData(CupLevel.SUBREGION, 7, "Subregion Cup Unlock : West Kanto", {"City Cup Pewter City Trophy", "City Cup Celadon City Trophy", "City Cup Fuchsia City Trophy", "City Cup Saffron City Trophy"}),
    "Subregion Cup East Kanto": RegionData(CupLevel.SUBREGION, 7, "Subregion Cup Unlock : East Kanto", {"City Cup Pewter City Trophy", "City Cup Celadon City Trophy", "City Cup Fuchsia City Trophy", "City Cup Saffron City Trophy"}),

    "Region Cup Johto": RegionData(CupLevel.REGION, 9, "Region Cup Unlock : Johto", {"Subregion Cup East Johto Trophy", "Subregion Cup South Johto Trophy", "Subregion Cup North Johto Trophy"}),
    "Region Cup Kanto": RegionData(CupLevel.REGION, 9, "Region Cup Unlock : Kanto", {"Subregion Cup West Kanto Trophy", "Subregion Cup East Kanto Trophy"}),
    "Indigo League": RegionData(CupLevel.WORLD, 15, "World Cup Unlock : Indigo League", {"Region Cup Johto Trophy", "Region Cup Kanto Trophy"}),
    }

draft_logic = {
    CupLevel.MISC: [0, 0],
    CupLevel.EXTRA: [0, 0],
    CupLevel.LOCAL: [0, 0],
    CupLevel.CITY: [1, 5],
    CupLevel.SUBREGION: [3, 11],
    CupLevel.REGION: [5, 17],
    CupLevel.WORLD: [6, 18],
    }



def cups_available_per_tier(state: CollectionState, world: "BestTrainerWorld", tier: CupLevel, count: int) -> bool:
    res: int = 0
    for region_name, data in cup_regions.items():
        if data.level == tier and region_is_reachable(state, world, data):
            res += 1

    return res >= count

def cups_available(state: CollectionState, world: "BestTrainerWorld", count: int) -> bool:
    res: int = 0
    for region_name, data in cup_regions.items():
        if data.level > 0 and region_is_reachable(state, world, data):
            res += 1

    return res >= count

def trainers_available(state: CollectionState, world: "BestTrainerWorld", count: int) -> bool:
    res: int = 0
    for region_name, data in cup_regions.items():
        if region_is_reachable(state, world, data):
            res += data.battle_number

    return res >= count

def draft_pool_power(state: CollectionState, world: "BestTrainerWorld", strength: CupLevel) -> bool:

    """
    Check if the draft pool has enough power and types available for the given strength.
    """
    power: bool = world.options.LockDraftPower.value == 0 or state.has("Draft Upgrade", world.player, draft_logic[strength][0])
    types: bool = world.options.DraftTypes.value == 0 or state.count_from_list_unique({"Draft : Normal Type", "Draft : Fire Type", "Draft : Water Type", "Draft : Grass Type", "Draft : Electric Type", "Draft : Bug Type", "Draft : Flying Type", "Draft : Rock Type", "Draft : Poison Type", "Draft : Psychic Type", "Draft : Ice Type", "Draft : Ghost Type", "Draft : Dragon Type", "Draft : Steel Type", "Draft : Dark Type", "Draft : Fairy Type"},
                                            world.player) >= draft_logic[strength][1]
    types = True
    return power and types


def region_is_reachable(state: CollectionState, world: "BestTrainerWorld", region: RegionData) -> bool:

    if region is None:
        return True
    
    required_key = region.key_name
    if required_key != "" and not state.has(required_key, world.player):
        return False
    
    if not draft_pool_power(state, world, region.level):
        return False
    
    # Beat previous cups if needed
    
    prev_requirements = region.required_key
    if prev_requirements and not any(
                state.has(req, world.player) for req in prev_requirements
            ):
        return False
    
    return True


def set_rules(world: "BestTrainerWorld"):
    # First, chapter access
    
    table = {**location_table, **event_locs}
    for location_name, data in table.items():
        if not is_location_valid(world, location_name):
            continue

        loc = world.multiworld.get_location(location_name, world.player)


        region_data = cup_regions.get(data.region)
        if region_data:
            if region_data.key_name:
                set_rule(
                    loc,
                    lambda state, key_name=region_data.key_name: state.has(key_name, world.player)
                )

            if data.required_key:
                add_rule(
                    loc,
                    lambda state, required_key=data.required_key: (state.has(req, world.player) for req in required_key),
                    "and"
                )
        
        if data.category & CheckCategory.ACHIEVEMENT:
            if location_name == "Win 5 battles":
                set_rule(
                    loc,
                    lambda state: trainers_available(state, world, 5)
                )
            elif location_name == "Win 10 battles":
                set_rule(
                    loc,
                    lambda state: trainers_available(state, world, 10)
                )
            elif location_name == "Win 20 battles":
                set_rule(
                    loc,
                    lambda state: trainers_available(state, world, 20)
                )
            elif location_name == "Win 30 battles":
                set_rule(
                    loc,
                    lambda state: trainers_available(state, world, 30)
                )
            elif location_name == "Win 40 battles":
                set_rule(
                    loc,
                    lambda state: trainers_available(state, world, 40)
                )
            elif location_name == "Win 50 battles":
                set_rule(
                    loc,
                    lambda state: trainers_available(state, world, 50)
                )
            elif location_name == "Win 2 Local Cups":
                set_rule(
                    loc,
                    lambda state: cups_available_per_tier(state, world, CupLevel.LOCAL, 2)
                )
            elif location_name == "Win 3 Local Cups":
                set_rule(
                    loc,
                    lambda state: cups_available_per_tier(state, world, CupLevel.LOCAL, 3)
                )
            elif location_name == "Win 5 Local Cups":
                set_rule(
                    loc,
                    lambda state: cups_available_per_tier(state, world, CupLevel.LOCAL, 5)
                )
            elif location_name == "Win a City Cup":
                set_rule(
                    loc,
                    lambda state: cups_available_per_tier(state, world, CupLevel.CITY, 1)
                )
            elif location_name == "Win 2 City Cups":
                set_rule(
                    loc,
                    lambda state: cups_available_per_tier(state, world, CupLevel.CITY, 2)
                )
            elif location_name == "Win 3 City Cups":
                set_rule(
                    loc,
                    lambda state: cups_available_per_tier(state, world, CupLevel.CITY, 3)
                )
            elif location_name == "Win a Subregion Cup":
                set_rule(
                    loc,
                    lambda state, level=CupLevel.SUBREGION: cups_available_per_tier(state, world, CupLevel.SUBREGION, 1)
                )
            elif location_name == "Win 2 Subregion Cups":
                set_rule(
                    loc,
                    lambda state: cups_available_per_tier(state, world, CupLevel.SUBREGION, 2)
                )
            elif location_name == "Win a Region Cup":
                set_rule(
                    loc,
                    lambda state: cups_available_per_tier(state, world, CupLevel.REGION, 1)
                )
            if data.required_key:
                add_rule(
                    loc,
                    lambda state, key_name=data.required_key: state.has(key_name, world.player),
                    "and"
                )

        elif region_data:
            # Drafting power for the cup level
            add_rule(
                loc,
                lambda state, level=region_data.level: draft_pool_power(state, world, level),
                "and"
            )



    if world.options.Goal == Goal.option_indigo_league:
        world.multiworld.completion_condition[world.player] = lambda state: state.has("Indigo League Trophy", world.player)
    elif world.options.Goal == Goal.option_region:
        world.multiworld.completion_condition[world.player] = lambda state: state.has("Region Cup Johto Trophy", world.player) or state.has("Region Cup Kanto Trophy", world.player)