from mimetypes import common_types
from BaseClasses import Item, ItemClassification
from .Types import ItemData, BestTrainerItem, ItemCategory
from .Locations import get_total_locations
from .Options import RegionsAvailables, AddExtraDraftTypesItems, DraftChangeAvailable
from typing import List, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from . import BestTrainerWorld


def create_itempool(world: "BestTrainerWorld") -> List[Item]:
    itempool: List[Item] = []

    if world.options.LockDraftPower:
        draft_upgrade_pool: List[Item] = create_multiple_items(world, "Draft Upgrade",
                                                        6,
                                                        ItemClassification.progression)

        #for i in range(5):
        #    draft_upgrade_pool[i].classification = ItemClassification.progression

        itempool += draft_upgrade_pool

    for name in item_table.keys():
        if name == "Draft Upgrade":
            continue
        if name == "Local Cup Unlock : New Bark Town":
            continue
        if name == "Local Cup Unlock : Pallet Town":
            continue
        
        
        if name == "Draft Point":
            continue

        item_type: ItemClassification = item_table.get(name).classification
        item_group: str = item_table.get(name).group
        item_cat: ItemCategory = item_table.get(name).category
        number_to_push: int = 1
        

        if item_type is ItemClassification.filler or item_type is ItemClassification.trap:
            continue

        if item_cat & ItemCategory.KANTO and world.options.RegionsAvailables.value == 1:
            continue
        if item_cat & ItemCategory.JOHTO and world.options.RegionsAvailables.value == 2:
            continue
        if item_group == "Draft Type" and world.options.DraftTypes.value == 0:
            continue

        if item_group == "Draft Type" and world.options.AddExtraDraftTypesItems:
            if name in draft_groups.get("Common"):
                continue
                #number_to_push = 3
            if name in draft_groups.get("Rare"):
                number_to_push = 2

        itempool += create_multiple_items(world, name, item_frequencies.get(name, number_to_push), item_type)

    itempool += create_draft_points(world, get_total_locations(world) - len(itempool))
    itempool += create_junk_items(world, get_total_locations(world) - len(itempool))
    return itempool





def create_item(world: "BestTrainerWorld", name: str) -> Item:
    data = item_table[name]
    return BestTrainerItem(name, data.classification, data.code, world.player)


def create_multiple_items(world: "BestTrainerWorld", name: str, count: int = 1,
                          item_type: ItemClassification = ItemClassification.progression) -> List[Item]:

    data = item_table[name]
    itemlist: List[Item] = []

    for i in range(count):
        itemlist += [BestTrainerItem(name, item_type, data.code, world.player)]

    return itemlist


def create_draft_points(world: "BestTrainerWorld", count: int) -> List[Item]:
    number: int = world.options.DraftChangeAvailable
    if (count < number):
        number = count

    draft_pool: List[Item] = create_multiple_items(world, "Draft Point",
                                                    number,
                                                    ItemClassification.useful)

    return draft_pool


def create_junk_items(world: "BestTrainerWorld", count: int) -> List[Item]:
    junk_pool: List[Item] = []
    junk_list: Dict[str, int] = {}
    ic: ItemClassification

    for name in item_table.keys():
        ic = item_table[name].classification
        if ic == ItemClassification.filler:

            junk_list[name] = junk_weights.get(name)

    for i in range(count):
        junk_pool.append(world.create_item(
            world.random.choices(list(junk_list.keys()), weights=list(junk_list.values()), k=1)[0]))

    return junk_pool



best_trainer_items = {
    # Mc Guffins
    "Draft Upgrade": ItemData(2000300001, ItemClassification.progression, "Upgrade", ItemCategory.DRAFT),

    # Draft Types
    "Draft : Normal Type": ItemData(2000300011, ItemClassification.progression, "Draft Type", ItemCategory.DRAFT),
    "Draft : Fire Type": ItemData(2000300012, ItemClassification.progression, "Draft Type", ItemCategory.DRAFT),
    "Draft : Water Type": ItemData(2000300013, ItemClassification.progression, "Draft Type", ItemCategory.DRAFT),
    "Draft : Grass Type": ItemData(2000300014, ItemClassification.progression, "Draft Type", ItemCategory.DRAFT),
    "Draft : Electric Type": ItemData(2000300015, ItemClassification.progression, "Draft Type", ItemCategory.DRAFT),
    "Draft : Bug Type": ItemData(2000300016, ItemClassification.progression, "Draft Type", ItemCategory.DRAFT),
    "Draft : Flying Type": ItemData(2000300017, ItemClassification.progression, "Draft Type", ItemCategory.DRAFT),
    "Draft : Fighting Type": ItemData(2000300018, ItemClassification.progression, "Draft Type", ItemCategory.DRAFT),
    "Draft : Ground Type": ItemData(2000300019, ItemClassification.progression, "Draft Type", ItemCategory.DRAFT),
    "Draft : Rock Type": ItemData(2000300020, ItemClassification.progression, "Draft Type", ItemCategory.DRAFT),
    "Draft : Poison Type": ItemData(2000300021, ItemClassification.progression, "Draft Type", ItemCategory.DRAFT),
    "Draft : Psychic Type": ItemData(2000300022, ItemClassification.progression, "Draft Type", ItemCategory.DRAFT),
    "Draft : Ice Type": ItemData(2000300023, ItemClassification.progression, "Draft Type", ItemCategory.DRAFT),
    "Draft : Ghost Type": ItemData(2000300024, ItemClassification.progression, "Draft Type", ItemCategory.DRAFT),
    "Draft : Dragon Type": ItemData(2000300025, ItemClassification.progression, "Draft Type", ItemCategory.DRAFT),
    "Draft : Steel Type": ItemData(2000300026, ItemClassification.progression, "Draft Type", ItemCategory.DRAFT),
    "Draft : Dark Type": ItemData(2000300027, ItemClassification.progression, "Draft Type", ItemCategory.DRAFT),
    "Draft : Fairy Type": ItemData(2000300028, ItemClassification.progression, "Draft Type", ItemCategory.DRAFT),


    # Cup Unlocks
    "Local Cup Unlock : New Bark Town": ItemData(2000300101, ItemClassification.progression, "Cup", ItemCategory.JOHTO),
    "Local Cup Unlock : Cherrygrove City": ItemData(2000300102, ItemClassification.progression, "Cup", ItemCategory.JOHTO),
    "Local Cup Unlock : Violet City": ItemData(2000300103, ItemClassification.progression, "Cup", ItemCategory.JOHTO),
    "Local Cup Unlock : Azalea Town": ItemData(2000300104, ItemClassification.progression, "Cup", ItemCategory.JOHTO),
    "Local Cup Unlock : Cianwood City": ItemData(2000300105, ItemClassification.progression, "Cup", ItemCategory.JOHTO),
    "Local Cup Unlock : Mahogany Town": ItemData(2000300106, ItemClassification.progression, "Cup", ItemCategory.JOHTO),
    
    "City Cup Unlock : Goldenrod City": ItemData(2000300107, ItemClassification.progression, "Cup", ItemCategory.JOHTO),
    "City Cup Unlock : Ecruteak City": ItemData(2000300108, ItemClassification.progression, "Cup", ItemCategory.JOHTO),
    "City Cup Unlock : Olivine City": ItemData(2000300109, ItemClassification.progression, "Cup", ItemCategory.JOHTO),
    "City Cup Unlock : Blackthorn City": ItemData(2000300110, ItemClassification.progression, "Cup", ItemCategory.JOHTO),

    
    "Subregion Cup Unlock : West Johto": ItemData(2000300111, ItemClassification.progression, "Cup", ItemCategory.JOHTO),
    "Subregion Cup Unlock : South Johto": ItemData(2000300112, ItemClassification.progression, "Cup", ItemCategory.JOHTO),
    "Subregion Cup Unlock : North Johto": ItemData(2000300113, ItemClassification.progression, "Cup", ItemCategory.JOHTO),
    "Region Cup Unlock : Johto": ItemData(2000300114, ItemClassification.progression, "Cup", ItemCategory.JOHTO),
    
    "World Cup Unlock : Indigo League": ItemData(2000300115, ItemClassification.progression, "Cup", ItemCategory.JOHTO + ItemCategory.KANTO),

    
    "Local Cup Unlock : Pallet Town": ItemData(2000300201, ItemClassification.progression, "Cup", ItemCategory.KANTO),
    "Local Cup Unlock : Viridian City": ItemData(2000300202, ItemClassification.progression, "Cup", ItemCategory.KANTO),
    "Local Cup Unlock : Cerulean City": ItemData(2000300203, ItemClassification.progression, "Cup", ItemCategory.KANTO),
    "Local Cup Unlock : Vermilion City": ItemData(2000300204, ItemClassification.progression, "Cup", ItemCategory.KANTO),
    "Local Cup Unlock : Lavender Town": ItemData(2000300205, ItemClassification.progression, "Cup", ItemCategory.KANTO),
    "Local Cup Unlock : Cinnabar Island": ItemData(2000300206, ItemClassification.progression, "Cup", ItemCategory.KANTO),

    
    "City Cup Unlock : Pewter City": ItemData(2000300207, ItemClassification.progression, "Cup", ItemCategory.KANTO),
    "City Cup Unlock : Celadon City": ItemData(2000300208, ItemClassification.progression, "Cup", ItemCategory.KANTO),
    "City Cup Unlock : Fuchsia City": ItemData(2000300209, ItemClassification.progression, "Cup", ItemCategory.KANTO),
    "City Cup Unlock : Saffron City": ItemData(2000300210, ItemClassification.progression, "Cup", ItemCategory.KANTO),

    
    "Subregion Cup Unlock : West Kanto": ItemData(2000300211, ItemClassification.progression, "Cup", ItemCategory.KANTO),
    "Subregion Cup Unlock : East Kanto": ItemData(2000300212, ItemClassification.progression, "Cup", ItemCategory.KANTO),
    "Region Cup Unlock : Kanto": ItemData(2000300213, ItemClassification.progression, "Cup", ItemCategory.KANTO),


    # Progression
    "Draft Point": ItemData(2000300301, ItemClassification.useful, "Upgrade"),

    # Garbage items
    "a single Pokeball": ItemData(2000300311, ItemClassification.filler, "Junk"),
    "used Potion": ItemData(2000300312, ItemClassification.filler, "Junk"),
    "Nugget (chicken nugget)": ItemData(2000300313, ItemClassification.filler, "Junk"),
    "Plastic Badge": ItemData(2000300314, ItemClassification.filler, "Junk"),
    "Fan Letter": ItemData(2000300315, ItemClassification.filler, "Junk"),  
}

draft_groups = {
    "Common": {"Draft : Normal Type", "Draft : Fire Type", "Draft : Water Type", "Draft : Grass Type", "Draft : Bug Type", "Draft : Flying Type"},
    "Rare" : {"Draft : Electric Type", "Draft : Fighting Type", "Draft : Ground Type", "Draft : Rock Type", "Draft : Poison Type", "Draft : Psychic Type"},
    "Legendary" : {"Draft : Ice Type", "Draft : Ghost Type", "Draft : Dragon Type", "Draft : Steel Type", "Draft : Dark Type", "Draft : Fairy Type"},
}

item_frequencies = {
    "Draft Point": 2,
    "a single Pokeball": 2,
    "used Potion": 2,
    "Nugget (chicken nugget)": 2,
    "Plastic Badge": 2,
    "Fan Letter": 2,
}

junk_weights = {
    "a single Pokeball": 10,
    "used Potion": 10,
    "Nugget (chicken nugget)": 10,
    "Plastic Badge": 10,
    "Fan Letter": 10,
}

item_table = {
    **best_trainer_items
}
