from BaseClasses import Region, Location, ItemClassification
from .Types import LocData, CupLevel, CheckCategory, BestTrainerLocation, BestTrainerItem
from typing import Dict, List, TYPE_CHECKING
from .Options import BestTrainerOptions


if TYPE_CHECKING:
    from . import BestTrainerWorld



def get_total_locations(world: "BestTrainerWorld") -> int:
    total = 0
    
    for name in location_table.keys():
        if is_location_valid(world, name):
            total += 1

    return total


def gen_location_list(world: "BestTrainerWorld") -> List[Dict[str, LocData]]:
    loc_list: List[Dict[str, LocData]] = []
    
    #table = {**location_table, **event_locs}
    table = location_table
    for name in table.keys():
        if is_location_valid(world, name):
            loc_list.append([name, table[name]])

    return loc_list


def is_location_valid(world: "BestTrainerWorld", location: str) -> bool:

    data = location_table.get(location) or event_locs.get(location)
    if world.options.RegionsAvailables.value == 1 and data.category & CheckCategory.KANTO:
        return False
    if world.options.RegionsAvailables.value == 2 and data.category & CheckCategory.JOHTO:
        return False

    if world.options.TrainerRoundSanity.value == 0 and data.category & CheckCategory.TRAINERSANITY:
        return False

    if world.options.AddAchievements.value == 0 and data.category & CheckCategory.ACHIEVEMENT:
        return False


    return True


def get_location_names() -> Dict[str, int]:
    names = {name: data.id for name, data in location_table.items()}

    return names


def create_events(world: "BestTrainerWorld") -> int:
    count = 0

    for (name, data) in event_locs.items():
        if not is_location_valid(world, name):
            continue

        item_name: str = name

        event: Location = create_event(name, item_name, world.multiworld.get_region("Board", world.player), world)
        event.show_in_spoiler = False
        count += 1

    return count


def create_event(name: str, item_name: str, region: Region, world: "BestTrainerWorld") -> Location:
    event = BestTrainerLocation(world.player, name, None, region)
    region.locations.append(event)
    event.place_locked_item(BestTrainerItem(item_name, ItemClassification.progression, None, world.player))
    return event


best_trainer_locations = {
    # "Pokedex": LocData(2000300000, CheckCategory.BASE, "Home", ""),
    # "Pokegear": LocData(2000300001, CheckCategory.BASE, "Home", ""),
    # "Badge Case": LocData(2000300002, CheckCategory.BASE, "Home", ""),
    "Gift from Mom": LocData(2000300003, CheckCategory.BASE, "Home", ""),
    # "Running Shoes": LocData(2000300004, CheckCategory.BASE, "Home", ""),


    # Johto Local Cups
    "Local Cup New Bark Town : Reach Finals": LocData(2000301000, CheckCategory.JOHTO, "Local Cup New Bark Town", "Local Cup Unlock : New Bark Town"),
    "Local Cup New Bark Town : Win Finals": LocData(2000301001, CheckCategory.JOHTO, "Local Cup New Bark Town", "Local Cup Unlock : New Bark Town"),
    "Local Cup New Bark Town completion": LocData(2000301002, CheckCategory.JOHTO, "Local Cup New Bark Town", "Local Cup Unlock : New Bark Town"),

    "Local Cup Cherrygrove City : Reach Finals": LocData(2000301003, CheckCategory.JOHTO, "Local Cup Cherrygrove City", "Local Cup Unlock : Cherrygrove City"),
    "Local Cup Cherrygrove City : Win Finals": LocData(2000301004, CheckCategory.JOHTO, "Local Cup Cherrygrove City", "Local Cup Unlock : Cherrygrove City"),
    "Local Cup Cherrygrove City completion": LocData(2000301005, CheckCategory.JOHTO, "Local Cup Cherrygrove City", "Local Cup Unlock : Cherrygrove City"),

    "Local Cup Violet City : Reach Finals": LocData(2000301006, CheckCategory.JOHTO, "Local Cup Violet City", "Local Cup Unlock : Violet City"),
    "Local Cup Violet City : Win Finals": LocData(2000301007, CheckCategory.JOHTO, "Local Cup Violet City", "Local Cup Unlock : Violet City"),
    "Local Cup Violet City completion": LocData(2000301008, CheckCategory.JOHTO, "Local Cup Violet City", "Local Cup Unlock : Violet City"),

    "Local Cup Azalea Town : Reach Finals": LocData(2000301009, CheckCategory.JOHTO, "Local Cup Azalea Town", "Local Cup Unlock : Azalea Town"),
    "Local Cup Azalea Town : Win Finals": LocData(2000301010, CheckCategory.JOHTO, "Local Cup Azalea Town", "Local Cup Unlock : Azalea Town"),
    "Local Cup Azalea Town completion": LocData(2000301011, CheckCategory.JOHTO, "Local Cup Azalea Town", "Local Cup Unlock : Azalea Town"),

    "Local Cup Cianwood City : Reach Finals": LocData(2000301012, CheckCategory.JOHTO, "Local Cup Cianwood City", "Local Cup Unlock : Cianwood City"),
    "Local Cup Cianwood City : Win Finals": LocData(2000301013, CheckCategory.JOHTO, "Local Cup Cianwood City", "Local Cup Unlock : Cianwood City"),
    "Local Cup Cianwood City completion": LocData(2000301014, CheckCategory.JOHTO, "Local Cup Cianwood City", "Local Cup Unlock : Cianwood City"),

    "Local Cup Mahogany Town : Reach Finals": LocData(2000301015, CheckCategory.JOHTO, "Local Cup Mahogany Town", "Local Cup Unlock : Mahogany Town"),
    "Local Cup Mahogany Town: Win Finals": LocData(2000301016, CheckCategory.JOHTO, "Local Cup Mahogany Town", "Local Cup Unlock : Mahogany Town"),
    "Local Cup Mahogany Town completion": LocData(2000301017, CheckCategory.JOHTO, "Local Cup Mahogany Town", "Local Cup Unlock : Mahogany Town"),


    # Johto City Cups
    "City Cup Goldenrod City : Reach Top 4": LocData(2000301018, CheckCategory.JOHTO, "City Cup Goldenrod City", "City Cup Unlock : Goldenrod City"),
    "City Cup Goldenrod City : Reach Finals": LocData(2000301019, CheckCategory.JOHTO, "City Cup Goldenrod City", "City Cup Unlock : Goldenrod City"),
    "City Cup Goldenrod City : Win Finals": LocData(2000301020, CheckCategory.JOHTO, "City Cup Goldenrod City", "City Cup Unlock : Goldenrod City"),
    "City Cup Goldenrod City completion ": LocData(2000301021, CheckCategory.JOHTO, "City Cup Goldenrod City", "City Cup Unlock : Goldenrod City"),

    "City Cup Ecruteak City : Reach Top 4": LocData(2000301022, CheckCategory.JOHTO, "City Cup Ecruteak City", "City Cup Unlock : Ecruteak City"),
    "City Cup Ecruteak City : Reach Finals": LocData(2000301023, CheckCategory.JOHTO, "City Cup Ecruteak City", "City Cup Unlock : Ecruteak City"),
    "City Cup Ecruteak City : Win Finals": LocData(2000301024, CheckCategory.JOHTO, "City Cup Ecruteak City", "City Cup Unlock : Ecruteak City"),
    "City Cup Ecruteak City completion": LocData(2000301025, CheckCategory.JOHTO, "City Cup Ecruteak City", "City Cup Unlock : Ecruteak City"),

    "City Cup Olivine City : Reach Top 4": LocData(2000301026, CheckCategory.JOHTO, "City Cup Olivine City", "City Cup Unlock : Olivine City"),
    "City Cup Olivine City : Reach Finals": LocData(2000301027, CheckCategory.JOHTO, "City Cup Olivine City", "City Cup Unlock : Olivine City"),
    "City Cup Olivine City : Win Finals": LocData(2000301028, CheckCategory.JOHTO, "City Cup Olivine City", "City Cup Unlock : Olivine City"),
    "City Cup Olivine City completion": LocData(2000301029, CheckCategory.JOHTO, "City Cup Olivine City", "City Cup Unlock : Olivine City"),

    "City Cup Blackthorn City : Reach Top 4": LocData(2000301030, CheckCategory.JOHTO, "City Cup Blackthorn City", "City Cup Unlock : Blackthorn City"),
    "City Cup Blackthorn City : Reach Finals": LocData(2000301031, CheckCategory.JOHTO, "City Cup Blackthorn City", "City Cup Unlock : Blackthorn City"),
    "City Cup Blackthorn City : Win Finals": LocData(2000301032, CheckCategory.JOHTO, "City Cup Blackthorn City", "City Cup Unlock : Blackthorn City"),
    "City Cup Blackthorn City completion": LocData(2000301033, CheckCategory.JOHTO, "City Cup Blackthorn City", "City Cup Unlock : Blackthorn City"),


    # Johto Subregions Cups
    "Subregion Cup West Johto : Reach Top 8": LocData(2000301034, CheckCategory.JOHTO, "Subregion Cup West Johto", "Subregion Cup Unlock : West Johto"),
    "Subregion Cup West Johto : Reach Top 4": LocData(2000301035, CheckCategory.JOHTO, "Subregion Cup West Johto", "Subregion Cup Unlock : West Johto"),
    "Subregion Cup West Johto : Reach Finals": LocData(2000301036, CheckCategory.JOHTO, "Subregion Cup West Johto", "Subregion Cup Unlock : West Johto"),
    "Subregion Cup West Johto : Win Finals": LocData(2000301037, CheckCategory.JOHTO, "Subregion Cup West Johto", "Subregion Cup Unlock : West Johto"),
    "Subregion Cup West Johto completion": LocData(2000301038, CheckCategory.JOHTO, "Subregion Cup West Johto", "Subregion Cup Unlock : West Johto"),

    
    "Subregion Cup South Johto : Reach Top 8": LocData(2000301039, CheckCategory.JOHTO, "Subregion Cup South Johto", "Subregion Cup Unlock : South Johto"),
    "Subregion Cup South Johto : Reach Top 4": LocData(2000301040, CheckCategory.JOHTO, "Subregion Cup South Johto", "Subregion Cup Unlock : South Johto"),
    "Subregion Cup South Johto : Reach Finals": LocData(2000301041, CheckCategory.JOHTO, "Subregion Cup South Johto", "Subregion Cup Unlock : South Johto"),
    "Subregion Cup South Johto : Win Finals": LocData(2000301042, CheckCategory.JOHTO, "Subregion Cup South Johto", "Subregion Cup Unlock : South Johto"),
    "Subregion Cup South Johto completion": LocData(2000301043, CheckCategory.JOHTO, "Subregion Cup South Johto", "Subregion Cup Unlock : South Johto"),
    
    "Subregion Cup North Johto : Reach Top 8": LocData(2000301044, CheckCategory.JOHTO, "Subregion Cup North Johto", "Subregion Cup Unlock : North Johto"),
    "Subregion Cup North Johto : Reach Top 4": LocData(2000301045, CheckCategory.JOHTO, "Subregion Cup North Johto", "Subregion Cup Unlock : North Johto"),
    "Subregion Cup North Johto : Reach Finals": LocData(2000301046, CheckCategory.JOHTO, "Subregion Cup North Johto", "Subregion Cup Unlock : North Johto"),
    "Subregion Cup North Johto : Win Finals": LocData(2000301047, CheckCategory.JOHTO, "Subregion Cup North Johto", "Subregion Cup Unlock : North Johto"),
    "Subregion Cup North Johto completion": LocData(2000301048, CheckCategory.JOHTO, "Subregion Cup North Johto", "Subregion Cup Unlock : North Johto"),

    
    # Johto Region Cup
    "Region Cup Johto : Reach Top 16": LocData(2000301049, CheckCategory.JOHTO, "Region Cup Johto", "Region Cup Unlock : Johto"),
    "Region Cup Johto : Reach Top 8": LocData(2000301050, CheckCategory.JOHTO, "Region Cup Johto", "Region Cup Unlock : Johto"),
    "Region Cup Johto : Reach Top 4": LocData(2000301051, CheckCategory.JOHTO, "Region Cup Johto", "Region Cup Unlock : Johto"),
    "Region Cup Johto : Reach Finals": LocData(2000301052, CheckCategory.JOHTO, "Region Cup Johto", "Region Cup Unlock : Johto"),
    "Region Cup Johto : Win Finals": LocData(2000301053, CheckCategory.JOHTO, "Region Cup Johto", "Region Cup Unlock : Johto"),
    "Region Cup Johto completion": LocData(2000301054, CheckCategory.JOHTO, "Region Cup Johto", "Region Cup Unlock : Johto"),

    
    # Indigo League World Cup
    "Indigo League : Reach Top 64": LocData(2000301055, CheckCategory.KANTO + CheckCategory.JOHTO, "Indigo League", "World Cup Unlock : Indigo League"),
    "Indigo League : Reach Top 32": LocData(2000301056, CheckCategory.KANTO + CheckCategory.JOHTO, "Indigo League", "World Cup Unlock : Indigo League"),
    "Indigo League : Reach Top 16": LocData(2000301057, CheckCategory.KANTO + CheckCategory.JOHTO, "Indigo League", "World Cup Unlock : Indigo League"),
    "Indigo League : Reach Top 8": LocData(2000301058, CheckCategory.KANTO + CheckCategory.JOHTO, "Indigo League", "World Cup Unlock : Indigo League"),
    "Indigo League : Reach Top 4": LocData(2000301059, CheckCategory.KANTO + CheckCategory.JOHTO, "Indigo League", "World Cup Unlock : Indigo League"),
    "Indigo League : Reach Finals": LocData(2000301060, CheckCategory.KANTO + CheckCategory.JOHTO, "Indigo League", "World Cup Unlock : Indigo League"),
    "Indigo League : Win Finals": LocData(2000301061, CheckCategory.KANTO + CheckCategory.JOHTO, "Indigo League", "World Cup Unlock : Indigo League"),
    "Indigo League completion": LocData(2000301062, CheckCategory.KANTO + CheckCategory.JOHTO, "Indigo League", "World Cup Unlock : Indigo League"),

    

    
    # Kanto Local Cups
    "Local Cup Pallet Town : Reach Finals": LocData(2000301063, CheckCategory.KANTO, "Local Cup Pallet Town", "Local Cup Unlock : Pallet Town"),
    "Local Cup Pallet Town : Win Finals": LocData(2000301064, CheckCategory.KANTO, "Local Cup Pallet Town", "Local Cup Unlock : Pallet Town"),
    "Local Cup Pallet Town completion": LocData(2000301065, CheckCategory.KANTO, "Local Cup Pallet Town", "Local Cup Unlock : Pallet Town"),

    "Local Cup Viridian City : Reach Finals": LocData(2000301066, CheckCategory.KANTO, "Local Cup Viridian City", "Local Cup Unlock : Viridian City"),
    "Local Cup Viridian City : Win Finals": LocData(2000301067, CheckCategory.KANTO, "Local Cup Viridian City", "Local Cup Unlock : Viridian City"),
    "Local Cup Viridian City completion": LocData(2000301068, CheckCategory.KANTO, "Local Cup Viridian City", "Local Cup Unlock : Viridian City"),

    "Local Cup Cerulean City : Reach Finals": LocData(2000301069, CheckCategory.KANTO, "Local Cup Cerulean City", "Local Cup Unlock : Cerulean City"),
    "Local Cup Cerulean City : Win Finals": LocData(2000301070, CheckCategory.KANTO, "Local Cup Cerulean City", "Local Cup Unlock : Cerulean City"),
    "Local Cup Cerulean City completion": LocData(2000301071, CheckCategory.KANTO, "Local Cup Cerulean City", "Local Cup Unlock : Cerulean City"),

    "Local Cup Vermilion City : Reach Finals": LocData(2000301072, CheckCategory.KANTO, "Local Cup Vermilion City", "Local Cup Unlock : Vermilion City"),
    "Local Cup Vermilion City : Win Finals": LocData(2000301073, CheckCategory.KANTO, "Local Cup Vermilion City", "Local Cup Unlock : Vermilion City"),
    "Local Cup Vermilion City completion": LocData(2000301074, CheckCategory.KANTO, "Local Cup Vermilion City", "Local Cup Unlock : Vermilion City"),

    "Local Cup Lavender Town : Reach Finals": LocData(2000301075, CheckCategory.KANTO, "Local Cup Lavender Town", "Local Cup Unlock : Lavender Town"),
    "Local Cup Lavender Town : Win Finals": LocData(2000301076, CheckCategory.KANTO, "Local Cup Lavender Town", "Local Cup Unlock : Lavender Town"),
    "Local Cup Lavender Town completion": LocData(2000301077, CheckCategory.KANTO, "Local Cup Lavender Town", "Local Cup Unlock : Lavender Town"),

    "Local Cup Cinnabar Island : Reach Finals": LocData(2000301078, CheckCategory.KANTO, "Local Cup Cinnabar Island", "Local Cup Unlock : Cinnabar Island"),
    "Local Cup Cinnabar Island : Win Finals": LocData(2000301079, CheckCategory.KANTO, "Local Cup Cinnabar Island", "Local Cup Unlock : Cinnabar Island"),
    "Local Cup Cinnabar Island completion": LocData(2000301080, CheckCategory.KANTO, "Local Cup Cinnabar Island", "Local Cup Unlock : Cinnabar Island"),
    

    # Kanto City Cups
    "City Cup Pewter City : Reach Top 4": LocData(2000301081, CheckCategory.KANTO, "City Cup Pewter City", "City Cup Unlock : Pewter City"),
    "City Cup Pewter City : Reach Finals": LocData(2000301082, CheckCategory.KANTO, "City Cup Pewter City", "City Cup Unlock : Pewter City"),
    "City Cup Pewter City : Win Finals": LocData(2000301083, CheckCategory.KANTO, "City Cup Pewter City", "City Cup Unlock : Pewter City"),
    "City Cup Pewter City completion": LocData(2000301084, CheckCategory.KANTO, "City Cup Pewter City", "City Cup Unlock : Pewter City"),

    "City Cup Celadon City : Reach Top 4": LocData(2000301085, CheckCategory.KANTO, "City Cup Celadon City", "City Cup Unlock : Celadon City"),
    "City Cup Celadon City : Reach Finals": LocData(2000301086, CheckCategory.KANTO, "City Cup Celadon City", "City Cup Unlock : Celadon City"),
    "City Cup Celadon City : Win Finals": LocData(2000301087, CheckCategory.KANTO, "City Cup Celadon City", "City Cup Unlock : Celadon City"),
    "City Cup Celadon City completion": LocData(2000301088, CheckCategory.KANTO, "City Cup Celadon City", "City Cup Unlock : Celadon City"),

    "City Cup Fuchsia City : Reach Top 4": LocData(2000301089, CheckCategory.KANTO, "City Cup Fuchsia City", "City Cup Unlock : Fuchsia City"),
    "City Cup Fuchsia City : Reach Finals": LocData(2000301090, CheckCategory.KANTO, "City Cup Fuchsia City", "City Cup Unlock : Fuchsia City"),
    "City Cup Fuchsia City : Win Finals": LocData(2000301091, CheckCategory.KANTO, "City Cup Fuchsia City", "City Cup Unlock : Fuchsia City"),
    "City Cup Fuchsia City completion ": LocData(2000301092, CheckCategory.KANTO, "City Cup Fuchsia City", "City Cup Unlock : Fuchsia City"),

    "City Cup Saffron City : Reach Top 4": LocData(2000301093, CheckCategory.KANTO, "City Cup Saffron City", "City Cup Unlock : Saffron City"),
    "City Cup Saffron City : Reach Finals": LocData(2000301094, CheckCategory.KANTO, "City Cup Saffron City", "City Cup Unlock : Saffron City"),
    "City Cup Saffron City : Win Finals": LocData(2000301095, CheckCategory.KANTO, "City Cup Saffron City", "City Cup Unlock : Saffron City"),
    "City Cup Saffron City completion": LocData(2000301096, CheckCategory.KANTO, "City Cup Saffron City", "City Cup Unlock : Saffron City"),

    # Kanto Subregions Cups
    "Subregion Cup West Kanto : Reach Top 8": LocData(2000301097, CheckCategory.KANTO, "Subregion Cup West Kanto", "Subregion Cup Unlock : West Kanto"),
    "Subregion Cup West Kanto : Reach Top 4": LocData(2000301098, CheckCategory.KANTO, "Subregion Cup West Kanto", "Subregion Cup Unlock : West Kanto"),
    "Subregion Cup West Kanto : Reach Finals": LocData(2000301099, CheckCategory.KANTO, "Subregion Cup West Kanto", "Subregion Cup Unlock : West Kanto"),
    "Subregion Cup West Kanto : Win Finals": LocData(2000301100, CheckCategory.KANTO, "Subregion Cup West Kanto", "Subregion Cup Unlock : West Kanto"),
    "Subregion Cup West Kanto completion": LocData(2000301101, CheckCategory.KANTO, "Subregion Cup West Kanto", "Subregion Cup Unlock : West Kanto"),
    
    "Subregion Cup East Kanto : Reach Top 8": LocData(2000301102, CheckCategory.KANTO, "Subregion Cup East Kanto", "Subregion Cup Unlock : East Kanto"),
    "Subregion Cup East Kanto : Reach Top 4": LocData(2000301103, CheckCategory.KANTO, "Subregion Cup East Kanto", "Subregion Cup Unlock : East Kanto"),
    "Subregion Cup East Kanto : Reach Finals": LocData(2000301104, CheckCategory.KANTO, "Subregion Cup East Kanto", "Subregion Cup Unlock : East Kanto"),
    "Subregion Cup East Kanto : Win Finals": LocData(2000301105, CheckCategory.KANTO, "Subregion Cup East Kanto", "Subregion Cup Unlock : East Kanto"),
    "Subregion Cup East Kanto completion": LocData(2000301106, CheckCategory.KANTO, "Subregion Cup East Kanto", "Subregion Cup Unlock : East Kanto"),
    
    # Kanto Region Cup
    "Region Cup Kanto : Reach Top 16": LocData(2000301107, CheckCategory.KANTO, "Region Cup Kanto", "Region Cup Unlock : Kanto"),
    "Region Cup Kanto : Reach Top 8": LocData(2000301108, CheckCategory.KANTO, "Region Cup Kanto", "Region Cup Unlock : Kanto"),
    "Region Cup Kanto : Reach Top 4": LocData(2000301109, CheckCategory.KANTO, "Region Cup Kanto", "Region Cup Unlock : Kanto"),
    "Region Cup Kanto : Reach Finals": LocData(2000301110, CheckCategory.KANTO, "Region Cup Kanto", "Region Cup Unlock : Kanto"),
    "Region Cup Kanto : Win Finals": LocData(2000301111, CheckCategory.KANTO, "Region Cup Kanto", "Region Cup Unlock : Kanto"),
    "Region Cup Kanto completion": LocData(2000301112, CheckCategory.KANTO, "Region Cup Kanto", "Region Cup Unlock : Kanto"),
    
}


trainersanity_locations = {


    # Johto Local Cups
    "Local Cup New Bark Town : Win 1 match": LocData(2000401001, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Local Cup New Bark Town", "Local Cup Unlock : New Bark Town"),
    "Local Cup New Bark Town : Win 2 matchs": LocData(2000401002, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Local Cup New Bark Town", "Local Cup Unlock : New Bark Town"),
    "Local Cup New Bark Town : Win 3 matchs": LocData(2000401003, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Local Cup New Bark Town", "Local Cup Unlock : New Bark Town"),

    "Local Cup Cherrygrove City : Win 1 match": LocData(2000401004, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Local Cup Cherrygrove City", "Local Cup Unlock : Cherrygrove City"),
    "Local Cup Cherrygrove City : Win 2 matchs": LocData(2000401005, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Local Cup Cherrygrove City", "Local Cup Unlock : Cherrygrove City"),
    "Local Cup Cherrygrove City : Win 3 matchs": LocData(2000401006, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Local Cup Cherrygrove City", "Local Cup Unlock : Cherrygrove City"),

    "Local Cup Violet City : Win 1 match": LocData(2000401007, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Local Cup Violet City", "Local Cup Unlock : Violet City"),
    "Local Cup Violet City : Win 2 matchs": LocData(2000401008, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Local Cup Violet City", "Local Cup Unlock : Violet City"),
    "Local Cup Violet City : Win 3 matchs": LocData(2000401009, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Local Cup Violet City", "Local Cup Unlock : Violet City"),

    "Local Cup Azalea Town : Win 1 match": LocData(2000401010, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Local Cup Azalea Town", "Local Cup Unlock : Azalea Town"),
    "Local Cup Azalea Town : Win 2 matchs": LocData(2000401011, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Local Cup Azalea Town", "Local Cup Unlock : Azalea Town"),
    "Local Cup Azalea Town : Win 3 matchs": LocData(2000401012, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Local Cup Azalea Town", "Local Cup Unlock : Azalea Town"),

    "Local Cup Cianwood City : Win 1 match": LocData(2000401013, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Local Cup Cianwood City", "Local Cup Unlock : Cianwood City"),
    "Local Cup Cianwood City : Win 2 matchs": LocData(2000401014, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Local Cup Cianwood City", "Local Cup Unlock : Cianwood City"),
    "Local Cup Cianwood City : Win 3 matchs": LocData(2000401015, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Local Cup Cianwood City", "Local Cup Unlock : Cianwood City"),

    "Local Cup Mahogany Town : Win 1 match": LocData(2000401016, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Local Cup Mahogany Town", "Local Cup Unlock : Mahogany Town"),
    "Local Cup Mahogany Town : Win 2 matchs": LocData(2000401017, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Local Cup Mahogany Town", "Local Cup Unlock : Mahogany Town"),
    "Local Cup Mahogany Town : Win 3 matchs": LocData(2000401018, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Local Cup Mahogany Town", "Local Cup Unlock : Mahogany Town"),


    # Johto City Cups
    "City Cup Goldenrod City : Win 1 match": LocData(2000401019, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "City Cup Goldenrod City", "City Cup Unlock : Goldenrod City"),
    "City Cup Goldenrod City : Win 2 matchs": LocData(2000401020, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "City Cup Goldenrod City", "City Cup Unlock : Goldenrod City"),
    "City Cup Goldenrod City : Win 3 matchs": LocData(2000401021, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "City Cup Goldenrod City", "City Cup Unlock : Goldenrod City"),
    "City Cup Goldenrod City : Win 4 matchs": LocData(2000401022, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "City Cup Goldenrod City", "City Cup Unlock : Goldenrod City"),
    "City Cup Goldenrod City : Win 5 matchs": LocData(2000401023, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "City Cup Goldenrod City", "City Cup Unlock : Goldenrod City"),

    "City Cup Ecruteak City : Win 1 match": LocData(2000401024, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "City Cup Ecruteak City", "City Cup Unlock : Ecruteak City"),
    "City Cup Ecruteak City : Win 2 matchs": LocData(2000401025, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "City Cup Ecruteak City", "City Cup Unlock : Ecruteak City"),
    "City Cup Ecruteak City : Win 3 matchs": LocData(2000401026, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "City Cup Ecruteak City", "City Cup Unlock : Ecruteak City"),
    "City Cup Ecruteak City : Win 4 matchs": LocData(2000401027, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "City Cup Ecruteak City", "City Cup Unlock : Ecruteak City"),
    "City Cup Ecruteak City : Win 5 matchs": LocData(2000401028, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "City Cup Ecruteak City", "City Cup Unlock : Ecruteak City"),

    "City Cup Olivine City : Win 1 match": LocData(2000401029, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "City Cup Olivine City", "City Cup Unlock : Olivine City"),
    "City Cup Olivine City : Win 2 matchs": LocData(2000401030, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "City Cup Olivine City", "City Cup Unlock : Olivine City"),
    "City Cup Olivine City : Win 3 matchs": LocData(2000401031, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "City Cup Olivine City", "City Cup Unlock : Olivine City"),
    "City Cup Olivine City : Win 4 matchs": LocData(2000401032, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "City Cup Olivine City", "City Cup Unlock : Olivine City"),
    "City Cup Olivine City : Win 5 matchs": LocData(2000401033, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "City Cup Olivine City", "City Cup Unlock : Olivine City"),

    "City Cup Blackthorn City : Win 1 match": LocData(2000401034, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "City Cup Blackthorn City", "City Cup Unlock : Blackthorn City"),
    "City Cup Blackthorn City : Win 2 matchs": LocData(2000401035, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "City Cup Blackthorn City", "City Cup Unlock : Blackthorn City"),
    "City Cup Blackthorn City : Win 3 matchs": LocData(2000401036, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "City Cup Blackthorn City", "City Cup Unlock : Blackthorn City"),
    "City Cup Blackthorn City : Win 4 matchs": LocData(2000401037, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "City Cup Blackthorn City", "City Cup Unlock : Blackthorn City"),
    "City Cup Blackthorn City : Win 5 matchs": LocData(2000401038, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "City Cup Blackthorn City", "City Cup Unlock : Blackthorn City"),


    # Johto Subregions Cups
    "Subregion Cup West Johto : Win 1 match": LocData(2000401039, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Subregion Cup West Johto", "Subregion Cup Unlock : West Johto"),
    "Subregion Cup West Johto : Win 2 matchs": LocData(2000401040, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Subregion Cup West Johto", "Subregion Cup Unlock : West Johto"),
    "Subregion Cup West Johto : Win 3 matchs": LocData(2000401041, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Subregion Cup West Johto", "Subregion Cup Unlock : West Johto"),
    "Subregion Cup West Johto : Win 4 matchs": LocData(2000401042, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Subregion Cup West Johto", "Subregion Cup Unlock : West Johto"),
    "Subregion Cup West Johto : Win 5 matchs": LocData(2000401043, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Subregion Cup West Johto", "Subregion Cup Unlock : West Johto"),
    "Subregion Cup West Johto : Win 6 matchs": LocData(2000401044, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Subregion Cup West Johto", "Subregion Cup Unlock : West Johto"),
    "Subregion Cup West Johto : Win 7 matchs": LocData(2000401045, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Subregion Cup West Johto", "Subregion Cup Unlock : West Johto"),

    "Subregion Cup South Johto : Win 1 match": LocData(2000401046, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Subregion Cup South Johto", "Subregion Cup Unlock : South Johto"),
    "Subregion Cup South Johto : Win 2 matchs": LocData(2000401047, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Subregion Cup South Johto", "Subregion Cup Unlock : South Johto"),
    "Subregion Cup South Johto : Win 3 matchs": LocData(2000401048, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Subregion Cup South Johto", "Subregion Cup Unlock : South Johto"),
    "Subregion Cup South Johto : Win 4 matchs": LocData(2000401049, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Subregion Cup South Johto", "Subregion Cup Unlock : South Johto"),
    "Subregion Cup South Johto : Win 5 matchs": LocData(2000401050, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Subregion Cup South Johto", "Subregion Cup Unlock : South Johto"),
    "Subregion Cup South Johto : Win 6 matchs": LocData(2000401051, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Subregion Cup South Johto", "Subregion Cup Unlock : South Johto"),
    "Subregion Cup South Johto : Win 7 matchs": LocData(2000401052, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Subregion Cup South Johto", "Subregion Cup Unlock : South Johto"),

    "Subregion Cup North Johto : Win 1 match": LocData(2000401053, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Subregion Cup North Johto", "Subregion Cup Unlock : North Johto"),
    "Subregion Cup North Johto : Win 2 matchs": LocData(2000401054, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Subregion Cup North Johto", "Subregion Cup Unlock : North Johto"),
    "Subregion Cup North Johto : Win 3 matchs": LocData(2000401055, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Subregion Cup North Johto", "Subregion Cup Unlock : North Johto"),
    "Subregion Cup North Johto : Win 4 matchs": LocData(2000401056, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Subregion Cup North Johto", "Subregion Cup Unlock : North Johto"),
    "Subregion Cup North Johto : Win 5 matchs": LocData(2000401057, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Subregion Cup North Johto", "Subregion Cup Unlock : North Johto"),
    "Subregion Cup North Johto : Win 6 matchs": LocData(2000401058, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Subregion Cup North Johto", "Subregion Cup Unlock : North Johto"),
    "Subregion Cup North Johto : Win 7 matchs": LocData(2000401059, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Subregion Cup North Johto", "Subregion Cup Unlock : North Johto"),


    
    # Johto Region Cup
    "Region Cup Johto : Win 1 match": LocData(2000401060, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Region Cup Johto", "Region Cup Unlock : Johto"),
    "Region Cup Johto : Win 2 matchs": LocData(2000401061, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Region Cup Johto", "Region Cup Unlock : Johto"),
    "Region Cup Johto : Win 3 matchs": LocData(2000401062, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Region Cup Johto", "Region Cup Unlock : Johto"),
    "Region Cup Johto : Win 4 matchs": LocData(2000401063, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Region Cup Johto", "Region Cup Unlock : Johto"),
    "Region Cup Johto : Win 5 matchs": LocData(2000401064, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Region Cup Johto", "Region Cup Unlock : Johto"),
    "Region Cup Johto : Win 6 matchs": LocData(2000401065, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Region Cup Johto", "Region Cup Unlock : Johto"),
    "Region Cup Johto : Win 7 matchs": LocData(2000401066, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Region Cup Johto", "Region Cup Unlock : Johto"),
    "Region Cup Johto : Win 8 matchs": LocData(2000401067, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Region Cup Johto", "Region Cup Unlock : Johto"),
    "Region Cup Johto : Win 9 matchs": LocData(2000401068, CheckCategory.JOHTO + CheckCategory.TRAINERSANITY, "Region Cup Johto", "Region Cup Unlock : Johto"),
    
    # Indigo League World Cup
    "Indigo League : Win 1 match": LocData(2000401069, CheckCategory.JOHTO + CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Indigo League", "World Cup Unlock : Indigo League"),
    "Indigo League : Win 2 matchs": LocData(2000401070, CheckCategory.JOHTO + CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Indigo League", "World Cup Unlock : Indigo League"),
    "Indigo League : Win 3 matchs": LocData(2000401071, CheckCategory.JOHTO + CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Indigo League", "World Cup Unlock : Indigo League"),
    "Indigo League : Win 4 matchs": LocData(2000401072, CheckCategory.JOHTO + CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Indigo League", "World Cup Unlock : Indigo League"),
    "Indigo League : Win 5 matchs": LocData(2000401073, CheckCategory.JOHTO + CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Indigo League", "World Cup Unlock : Indigo League"),
    "Indigo League : Win 6 matchs": LocData(2000401074, CheckCategory.JOHTO + CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Indigo League", "World Cup Unlock : Indigo League"),
    "Indigo League : Win 7 matchs": LocData(2000401075, CheckCategory.JOHTO + CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Indigo League", "World Cup Unlock : Indigo League"),
    "Indigo League : Win 8 matchs": LocData(2000401076, CheckCategory.JOHTO + CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Indigo League", "World Cup Unlock : Indigo League"),
    "Indigo League : Win 9 matchs": LocData(2000401077, CheckCategory.JOHTO + CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Indigo League", "World Cup Unlock : Indigo League"),
    "Indigo League : Win 10 matchs": LocData(2000401078, CheckCategory.JOHTO + CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Indigo League", "World Cup Unlock : Indigo League"),
    "Indigo League : Win 11 matchs": LocData(2000401079, CheckCategory.JOHTO + CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Indigo League", "World Cup Unlock : Indigo League"),
    "Indigo League : Win 12 matchs": LocData(2000401080, CheckCategory.JOHTO + CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Indigo League", "World Cup Unlock : Indigo League"),
    "Indigo League : Win 13 matchs": LocData(2000401081, CheckCategory.JOHTO + CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Indigo League", "World Cup Unlock : Indigo League"),
    "Indigo League : Win 14 matchs": LocData(2000401082, CheckCategory.JOHTO + CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Indigo League", "World Cup Unlock : Indigo League"),
    "Indigo League : Win 15 matchs": LocData(2000401083, CheckCategory.JOHTO + CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Indigo League", "World Cup Unlock : Indigo League"),

    

    
    # Kanto Local Cups
    "Local Cup Pallet Town : Win 1 match": LocData(2000401084, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Local Cup Pallet Town", "Local Cup Unlock : Pallet Town"),
    "Local Cup Pallet Town : Win 2 matchs": LocData(2000401085, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Local Cup Pallet Town", "Local Cup Unlock : Pallet Town"),
    "Local Cup Pallet Town : Win 3 matchs": LocData(2000401086, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Local Cup Pallet Town", "Local Cup Unlock : Pallet Town"),

    "Local Cup Viridian City : Win 1 match": LocData(2000401087, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Local Cup Viridian City", "Local Cup Unlock : Viridian City"),
    "Local Cup Viridian City : Win 2 matchs": LocData(2000401088, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Local Cup Viridian City", "Local Cup Unlock : Viridian City"),
    "Local Cup Viridian City : Win 3 matchs": LocData(2000401089, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Local Cup Viridian City", "Local Cup Unlock : Viridian City"),

    "Local Cup Cerulean City : Win 1 match": LocData(2000401090, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Local Cup Cerulean City", "Local Cup Unlock : Cerulean City"),
    "Local Cup Cerulean City : Win 2 matchs": LocData(2000401091, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Local Cup Cerulean City", "Local Cup Unlock : Cerulean City"),
    "Local Cup Cerulean City : Win 3 matchs": LocData(2000401092, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Local Cup Cerulean City", "Local Cup Unlock : Cerulean City"),

    "Local Cup Vermilion City : Win 1 match": LocData(2000401093, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Local Cup Vermilion City", "Local Cup Unlock : Vermilion City"),
    "Local Cup Vermilion City : Win 2 matchs": LocData(2000401094, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Local Cup Vermilion City", "Local Cup Unlock : Vermilion City"),
    "Local Cup Vermilion City : Win 3 matchs": LocData(2000401095, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Local Cup Vermilion City", "Local Cup Unlock : Vermilion City"),

    "Local Cup Lavender Town : Win 1 match": LocData(2000401096, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Local Cup Lavender Town", "Local Cup Unlock : Lavender Town"),
    "Local Cup Lavender Town : Win 2 matchs": LocData(2000401097, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Local Cup Lavender Town", "Local Cup Unlock : Lavender Town"),
    "Local Cup Lavender Town : Win 3 matchs": LocData(2000401098, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Local Cup Lavender Town", "Local Cup Unlock : Lavender Town"),

    "Local Cup Cinnabar Island : Win 1 match": LocData(2000401099, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Local Cup Cinnabar Island", "Local Cup Unlock : Cinnabar Island"),
    "Local Cup Cinnabar Island : Win 2 matchs": LocData(2000401100, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Local Cup Cinnabar Island", "Local Cup Unlock : Cinnabar Island"),
    "Local Cup Cinnabar Island : Win 3 matchs": LocData(2000401101, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Local Cup Cinnabar Island", "Local Cup Unlock : Cinnabar Island"),
    

    # Kanto City Cups
    "City Cup Pewter City : Win 1 match": LocData(2000401102, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "City Cup Pewter City", "City Cup Unlock : Pewter City"),
    "City Cup Pewter City : Win 2 matchs": LocData(2000401103, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "City Cup Pewter City", "City Cup Unlock : Pewter City"),
    "City Cup Pewter City : Win 3 matchs": LocData(2000401104, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "City Cup Pewter City", "City Cup Unlock : Pewter City"),
    "City Cup Pewter City : Win 4 matchs": LocData(2000401105, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "City Cup Pewter City", "City Cup Unlock : Pewter City"),
    "City Cup Pewter City : Win 5 matchs": LocData(2000401106, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "City Cup Pewter City", "City Cup Unlock : Pewter City"),

    "City Cup Celadon City : Win 1 match": LocData(2000401107, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "City Cup Celadon City", "City Cup Unlock : Celadon City"),
    "City Cup Celadon City : Win 2 matchs": LocData(2000401108, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "City Cup Celadon City", "City Cup Unlock : Celadon City"),
    "City Cup Celadon City : Win 3 matchs": LocData(2000401109, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "City Cup Celadon City", "City Cup Unlock : Celadon City"),
    "City Cup Celadon City : Win 4 matchs": LocData(2000401110, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "City Cup Celadon City", "City Cup Unlock : Celadon City"),
    "City Cup Celadon City : Win 5 matchs": LocData(2000401111, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "City Cup Celadon City", "City Cup Unlock : Celadon City"),

    "City Cup Fuchsia City : Win 1 match": LocData(2000401112, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "City Cup Fuchsia City", "City Cup Unlock : Fuchsia City"),
    "City Cup Fuchsia City : Win 2 matchs": LocData(2000401113, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "City Cup Fuchsia City", "City Cup Unlock : Fuchsia City"),
    "City Cup Fuchsia City : Win 3 matchs": LocData(2000401114, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "City Cup Fuchsia City", "City Cup Unlock : Fuchsia City"),
    "City Cup Fuchsia City : Win 4 matchs": LocData(2000401115, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "City Cup Fuchsia City", "City Cup Unlock : Fuchsia City"),
    "City Cup Fuchsia City : Win 5 matchs": LocData(2000401116, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "City Cup Fuchsia City", "City Cup Unlock : Fuchsia City"),

    "City Cup Saffron City : Win 1 match": LocData(2000401117, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "City Cup Saffron City", "City Cup Unlock : Saffron City"),
    "City Cup Saffron City : Win 2 matchs": LocData(2000401118, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "City Cup Saffron City", "City Cup Unlock : Saffron City"),
    "City Cup Saffron City : Win 3 matchs": LocData(2000401119, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "City Cup Saffron City", "City Cup Unlock : Saffron City"),
    "City Cup Saffron City : Win 4 matchs": LocData(2000401120, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "City Cup Saffron City", "City Cup Unlock : Saffron City"),
    "City Cup Saffron City : Win 5 matchs": LocData(2000401121, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "City Cup Saffron City", "City Cup Unlock : Saffron City"),

    # Kanto Subregions Cups
    "Subregion Cup West Kanto : Win 1 match": LocData(2000401122, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Subregion Cup West Kanto", "Subregion Cup Unlock : West Kanto"),
    "Subregion Cup West Kanto : Win 2 matchs": LocData(2000401123, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Subregion Cup West Kanto", "Subregion Cup Unlock : West Kanto"),
    "Subregion Cup West Kanto : Win 3 matchs": LocData(2000401124, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Subregion Cup West Kanto", "Subregion Cup Unlock : West Kanto"),
    "Subregion Cup West Kanto : Win 4 matchs": LocData(2000401125, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Subregion Cup West Kanto", "Subregion Cup Unlock : West Kanto"),
    "Subregion Cup West Kanto : Win 5 matchs": LocData(2000401126, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Subregion Cup West Kanto", "Subregion Cup Unlock : West Kanto"),
    "Subregion Cup West Kanto : Win 6 matchs": LocData(2000401127, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Subregion Cup West Kanto", "Subregion Cup Unlock : West Kanto"),
    "Subregion Cup West Kanto : Win 7 matchs": LocData(2000401128, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Subregion Cup West Kanto", "Subregion Cup Unlock : West Kanto"),
    
    "Subregion Cup East Kanto : Win 1 match": LocData(2000401129, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Subregion Cup East Kanto", "Subregion Cup Unlock : East Kanto"),
    "Subregion Cup East Kanto : Win 2 matchs": LocData(2000401130, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Subregion Cup East Kanto", "Subregion Cup Unlock : East Kanto"),
    "Subregion Cup East Kanto : Win 3 matchs": LocData(2000401131, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Subregion Cup East Kanto", "Subregion Cup Unlock : East Kanto"),
    "Subregion Cup East Kanto : Win 4 matchs": LocData(2000401132, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Subregion Cup East Kanto", "Subregion Cup Unlock : East Kanto"),
    "Subregion Cup East Kanto : Win 5 matchs": LocData(2000401133, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Subregion Cup East Kanto", "Subregion Cup Unlock : East Kanto"),
    "Subregion Cup East Kanto : Win 6 matchs": LocData(2000401134, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Subregion Cup East Kanto", "Subregion Cup Unlock : East Kanto"),
    "Subregion Cup East Kanto : Win 7 matchs": LocData(2000401135, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Subregion Cup East Kanto", "Subregion Cup Unlock : East Kanto"),
    
    # Kanto Region Cup
    "Region Cup Kanto : Win 1 match": LocData(2000401136, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Region Cup Kanto", "Region Cup Unlock : Kanto"),
    "Region Cup Kanto : Win 2 matchs": LocData(2000401137, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Region Cup Kanto", "Region Cup Unlock : Kanto"),
    "Region Cup Kanto : Win 3 matchs": LocData(2000401138, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Region Cup Kanto", "Region Cup Unlock : Kanto"),
    "Region Cup Kanto : Win 4 matchs": LocData(2000401139, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Region Cup Kanto", "Region Cup Unlock : Kanto"),
    "Region Cup Kanto : Win 5 matchs": LocData(2000401140, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Region Cup Kanto", "Region Cup Unlock : Kanto"),
    "Region Cup Kanto : Win 6 matchs": LocData(2000401141, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Region Cup Kanto", "Region Cup Unlock : Kanto"),
    "Region Cup Kanto : Win 7 matchs": LocData(2000401142, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Region Cup Kanto", "Region Cup Unlock : Kanto"),
    "Region Cup Kanto : Win 8 matchs": LocData(2000401143, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Region Cup Kanto", "Region Cup Unlock : Kanto"),
    "Region Cup Kanto : Win 9 matchs": LocData(2000401144, CheckCategory.KANTO + CheckCategory.TRAINERSANITY, "Region Cup Kanto", "Region Cup Unlock : Kanto"),
    
}


achievements_locations = {
    "Win a battle": LocData(2000501001, CheckCategory.ACHIEVEMENT, "Achievement", ""),
    "Win 5 battles": LocData(2000501002, CheckCategory.ACHIEVEMENT, "Achievement", ""),
    "Win 10 battles": LocData(2000501003, CheckCategory.ACHIEVEMENT, "Achievement", ""),
    "Win 20 battles": LocData(2000501004, CheckCategory.ACHIEVEMENT, "Achievement", ""),
    "Win 30 battles": LocData(2000501005, CheckCategory.ACHIEVEMENT, "Achievement", ""),
    "Win 40 battles": LocData(2000501006, CheckCategory.ACHIEVEMENT, "Achievement", ""),
    "Win 50 battles": LocData(2000501007, CheckCategory.ACHIEVEMENT, "Achievement", ""),

    "Win a Local Cup": LocData(2000501008, CheckCategory.ACHIEVEMENT, "Achievement", ""),
    "Win 2 Local Cups": LocData(2000501009, CheckCategory.ACHIEVEMENT, "Achievement", ""),
    "Win 3 Local Cups": LocData(2000501010, CheckCategory.ACHIEVEMENT, "Achievement", ""),
    "Win 5 Local Cups": LocData(2000501011, CheckCategory.ACHIEVEMENT, "Achievement", ""),
    
    "Win a City Cup": LocData(2000501012, CheckCategory.ACHIEVEMENT, "Achievement", ""),
    "Win 2 City Cups": LocData(2000501013, CheckCategory.ACHIEVEMENT, "Achievement", ""),
    "Win 3 City Cups": LocData(2000501014, CheckCategory.ACHIEVEMENT, "Achievement", ""),
    
    "Win a Subregion Cup": LocData(2000501015, CheckCategory.ACHIEVEMENT, "Achievement", ""),
    "Win 2 Subregion Cups": LocData(2000501016, CheckCategory.ACHIEVEMENT, "Achievement", ""),

    "Win a Region Cup": LocData(2000501017,  CheckCategory.KANTO + CheckCategory.JOHTO + CheckCategory.ACHIEVEMENT, "Achievement", ""),

    
    "Beat Brock": LocData(2000502001, CheckCategory.KANTO + CheckCategory.ACHIEVEMENT, "City Cup Pewter City", "City Cup Unlock : Pewter City"),
    "Beat Misty": LocData(2000502002, CheckCategory.KANTO + CheckCategory.ACHIEVEMENT, "Local Cup Cerulean City", "Local Cup Unlock : Cerulean City"),
    "Beat Bob": LocData(2000502003, CheckCategory.KANTO + CheckCategory.ACHIEVEMENT, "Local Cup Vermilion City", "Local Cup Unlock : Vermilion City"),
    "Beat Erika": LocData(2000502004, CheckCategory.KANTO + CheckCategory.ACHIEVEMENT, "City Cup Celadon City", "City Cup Unlock : Celadon City"),
    "Beat Jeanine": LocData(2000502005, CheckCategory.KANTO + CheckCategory.ACHIEVEMENT, "City Cup Fuchsia City", "City Cup Unlock : Fuchsia City"),
    "Beat Sabrina": LocData(2000502006, CheckCategory.KANTO + CheckCategory.ACHIEVEMENT, "City Cup Saffron City", "City Cup Unlock : Saffron City"),
    "Beat Blaine": LocData(2000502007, CheckCategory.KANTO + CheckCategory.ACHIEVEMENT, "Local Cup Cinnabar Island", "Local Cup Unlock : Cinnabar Island"),
    "Beat Blue": LocData(2000502008, CheckCategory.KANTO + CheckCategory.ACHIEVEMENT, "Local Cup Viridian City", "Local Cup Unlock : Viridian City"),

    "Beat Falkner": LocData(2000502009, CheckCategory.JOHTO + CheckCategory.ACHIEVEMENT, "Local Cup Violet City", "Local Cup Unlock : Violet City"),
    "Beat Bugsy": LocData(2000502010, CheckCategory.JOHTO + CheckCategory.ACHIEVEMENT, "Local Cup Azalea Town", "Local Cup Unlock : Azalea Town"),
    "Beat Whitney": LocData(2000502011, CheckCategory.JOHTO + CheckCategory.ACHIEVEMENT, "City Cup Goldenrod City", "City Cup Unlock : Goldenrod City"),
    "Beat Morty": LocData(2000502012, CheckCategory.JOHTO + CheckCategory.ACHIEVEMENT, "City Cup Ecruteak City", "City Cup Unlock : Ecruteak City"),
    "Beat Chuck": LocData(2000502013, CheckCategory.JOHTO + CheckCategory.ACHIEVEMENT, "Local Cup Cianwood City", "Local Cup Unlock : Cianwood City"),
    "Beat Jasmine": LocData(2000502014, CheckCategory.JOHTO + CheckCategory.ACHIEVEMENT, "City Cup Olivine City", "City Cup Unlock : Olivine City"),
    "Beat Pryce": LocData(2000502015, CheckCategory.JOHTO + CheckCategory.ACHIEVEMENT, "Local Cup Mahogany Town", "Local Cup Unlock : Mahogany Town"),
    "Beat Clair": LocData(2000502016, CheckCategory.JOHTO + CheckCategory.ACHIEVEMENT, "City Cup Blackthorn City", "City Cup Unlock : Blackthorn City"),

    
    "Beat Lorelei": LocData(2000502017, CheckCategory.KANTO + CheckCategory.ACHIEVEMENT, "Region Cup Kanto", "Region Cup Unlock : Kanto"),
    "Beat Agatha": LocData(2000502018, CheckCategory.KANTO + CheckCategory.ACHIEVEMENT, "Region Cup Kanto", "Region Cup Unlock : Kanto"),
    "Beat Aldo": LocData(2000502021, CheckCategory.KANTO + CheckCategory.ACHIEVEMENT, "Region Cup Kanto", "Region Cup Unlock : Kanto"),
    "Beat Will": LocData(2000502019, CheckCategory.JOHTO + CheckCategory.ACHIEVEMENT, "Region Cup Johto", "Region Cup Unlock : Johto"),
    "Beat Koga": LocData(2000502020, CheckCategory.KANTO + CheckCategory.ACHIEVEMENT, "Region Cup Kanto", "Region Cup Unlock : Kanto"),
    "Beat Karen": LocData(2000502022, CheckCategory.JOHTO + CheckCategory.ACHIEVEMENT, "Region Cup Johto", "Region Cup Unlock : Johto"),
    "Beat Lance": LocData(2000502023, CheckCategory.JOHTO + CheckCategory.ACHIEVEMENT, "Region Cup Johto", "Region Cup Unlock : Johto"),

    "Beat Giovanni": LocData(2000502024, CheckCategory.KANTO + CheckCategory.JOHTO + CheckCategory.ACHIEVEMENT, "Indigo League", "World Cup Unlock : Indigo League"),
    "Beat Red": LocData(2000502025, CheckCategory.KANTO + CheckCategory.JOHTO + CheckCategory.ACHIEVEMENT, "Indigo League", "World Cup Unlock : Indigo League"),
    "Beat Silver": LocData(2000502026, CheckCategory.KANTO + CheckCategory.JOHTO + CheckCategory.ACHIEVEMENT, "Indigo League", "World Cup Unlock : Indigo League"),
}





event_locs = {
    "Local Cup New Bark Town Trophy": LocData(2000601001, CheckCategory.JOHTO, "Local Cup New Bark Town", "Local Cup Unlock : New Bark Town"),
    "Local Cup Cherrygrove City Trophy": LocData(2000601002, CheckCategory.JOHTO, "Local Cup Cherrygrove City", "Local Cup Unlock : Cherrygrove City"),
    "Local Cup Violet City Trophy": LocData(2000601003, CheckCategory.JOHTO, "Local Cup Violet City", "Local Cup Unlock : Violet City"),
    "Local Cup Azalea Town Trophy": LocData(2000601004, CheckCategory.JOHTO, "Local Cup Azalea Town", "Local Cup Unlock : Azalea Town"),
    "Local Cup Cianwood City Trophy": LocData(2000601005, CheckCategory.JOHTO, "Local Cup Cianwood City", "Local Cup Unlock : Cianwood City"),
    "Local Cup Mahogany Town Trophy": LocData(2000601006, CheckCategory.JOHTO, "Local Cup Mahogany Town", "Local Cup Unlock : Mahogany Town"),


    # Johto City Cups
    "City Cup Goldenrod City Trophy ": LocData(2000601007, CheckCategory.JOHTO, "City Cup Goldenrod City", "City Cup Unlock : Goldenrod City"),
    "City Cup Ecruteak City Trophy": LocData(2000601008, CheckCategory.JOHTO, "City Cup Ecruteak City", "City Cup Unlock : Ecruteak City"),
    "City Cup Olivine City Trophy": LocData(2000601009, CheckCategory.JOHTO, "City Cup Olivine City", "City Cup Unlock : Olivine City"),
    "City Cup Blackthorn City Trophy": LocData(2000601010, CheckCategory.JOHTO, "City Cup Blackthorn City", "City Cup Unlock : Blackthorn City"),


    # Johto Subregions Cups
    "Subregion Cup West Johto Trophy": LocData(2000601011, CheckCategory.JOHTO, "Subregion Cup West Johto", "Subregion Cup Unlock : West Johto"),
    "Subregion Cup South Johto Trophy": LocData(2000601013, CheckCategory.JOHTO, "Subregion Cup South Johto", "Subregion Cup Unlock : South Johto"),
    "Subregion Cup North Johto Trophy": LocData(2000601014, CheckCategory.JOHTO, "Subregion Cup North Johto", "Subregion Cup Unlock : North Johto"),

    
    # Johto Region Cup
    "Region Cup Johto Trophy": LocData(2000601015, CheckCategory.JOHTO, "Region Cup Johto", "Region Cup Unlock : Johto"),

    
    # Indigo League World Cup
    "Indigo League Trophy": LocData(2000601016, CheckCategory.KANTO + CheckCategory.JOHTO, "Indigo League", "World Cup Unlock : Indigo League"),

    

    
    # Kanto Local Cups
    "Local Cup Pallet Town Trophy": LocData(2000601017, CheckCategory.KANTO, "Local Cup Pallet Town", "Local Cup Unlock : Pallet Town"),
    "Local Cup Viridian City Trophy": LocData(2000601018, CheckCategory.KANTO, "Local Cup Viridian City", "Local Cup Unlock : Viridian City"),
    "Local Cup Cerulean City Trophy": LocData(2000601019, CheckCategory.KANTO, "Local Cup Cerulean City", "Local Cup Unlock : Cerulean City"),
    "Local Cup Vermilion City Trophy": LocData(2000601020, CheckCategory.KANTO, "Local Cup Vermilion City", "Local Cup Unlock : Vermilion City"),
    "Local Cup Lavender Town Trophy": LocData(2000601021, CheckCategory.KANTO, "Local Cup Lavender Town", "Local Cup Unlock : Lavender Town"),
    "Local Cup Cinnabar Island Trophy": LocData(2000601022, CheckCategory.KANTO, "Local Cup Cinnabar Island", "Local Cup Unlock : Cinnabar Island"),
    

    # Kanto City Cups
    "City Cup Pewter City Trophy": LocData(2000601023, CheckCategory.KANTO, "City Cup Pewter City", "City Cup Unlock : Pewter City"),
    "City Cup Celadon City Trophy": LocData(2000601024, CheckCategory.KANTO, "City Cup Celadon City", "City Cup Unlock : Celadon City"),
    "City Cup Fuchsia City Trophy": LocData(2000601025, CheckCategory.KANTO, "City Cup Fuchsia City", "City Cup Unlock : Fuchsia City"),
    "City Cup Saffron City Trophy": LocData(2000601026, CheckCategory.KANTO, "City Cup Saffron City", "City Cup Unlock : Saffron City"),

    # Kanto Subregions Cups
    "Subregion Cup West Kanto Trophy": LocData(2000601027, CheckCategory.KANTO, "Subregion Cup West Kanto", "Subregion Cup Unlock : West Kanto"),
    "Subregion Cup East Kanto Trophy": LocData(2000601028, CheckCategory.KANTO, "Subregion Cup East Kanto", "Subregion Cup Unlock : East Kanto"),
    
    # Kanto Region Cup
    "Region Cup Kanto Trophy": LocData(2000601029, CheckCategory.KANTO, "Region Cup Kanto", "Region Cup Unlock : Kanto"),
    
}


location_table = {
    **best_trainer_locations,
    **trainersanity_locations,
    **achievements_locations,
}
