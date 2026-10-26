from BaseClasses import Item, ItemClassification, Region, Entrance, Tutorial, Location, MultiWorld
from .Items import item_table, create_item, create_itempool, junk_weights
from .Locations import location_table, event_locs, is_location_valid, gen_location_list, get_total_locations, create_events
from .Rules import set_rules
from .Options import BestTrainerOptions, slot_data_options, adjust_options, RegionsAvailables, Goal, create_option_groups
from .Types import CheckCategory, CupLevel, RegionData, BestTrainerLocation
from worlds.AutoWorld import World, WebWorld, CollectionState
from worlds.generic.Rules import add_rule
from typing import List, Dict, TextIO
from Utils import local_path

class BestTrainerWorld(World):
    """
    Best Trainer is a game heavily inspired from Pokemon Stadium.
    Pick your team, compete in tournaments, unlock better Pokemon, and become the best trainer ever !
    """
    game = "Best Trainer"
    apworld_version = "1.0.0"
    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.id for name, data in location_table.items()}
    options_dataclass = BestTrainerOptions
    options: BestTrainerOptions

    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)

    def get_filler_item_name(self) -> str:
        return self.random.choices(list(junk_weights.keys()), weights=junk_weights.values(), k=1)[0]

    def generate_early(self):
        adjust_options(self)

        # Starting cup
        if self.options.RegionsAvailables.value == 1 or self.options.RegionsAvailables.value == 0:
            self.multiworld.push_precollected(self.create_item("Local Cup Unlock : New Bark Town"))
        if self.options.RegionsAvailables.value == 2 or self.options.RegionsAvailables.value == 0:
            self.multiworld.push_precollected(self.create_item("Local Cup Unlock : Pallet Town"))
            
        self.multiworld.push_precollected(self.create_item("Draft : Normal Type"))
        self.multiworld.push_precollected(self.create_item("Draft : Fire Type"))
        self.multiworld.push_precollected(self.create_item("Draft : Grass Type"))
        self.multiworld.push_precollected(self.create_item("Draft : Water Type"))
        self.multiworld.push_precollected(self.create_item("Draft : Flying Type"))


    def create_regions(self):
        
        home = Region("Menu", self.player, self.multiworld)
        board = Region("Board", self.player, self.multiworld)
        board.locations += [BestTrainerLocation(self.player, loc_name, loc_data.id, board)
                            for loc_name, loc_data in gen_location_list(self)]

        connection = Entrance(self.player, "New Board", home)
        home.exits.append(connection)
        connection.connect(board)
        self.multiworld.regions += [home, board]
        
        create_events(self)

    def create_items(self):
        self.multiworld.itempool += create_itempool(self)

    def set_rules(self):
        set_rules(self)

    def create_item(self, name: str) -> Item:
        return create_item(self, name)

    def fill_slot_data(self) -> dict:
        return {
            "apworld_version": self.apworld_version,

            "regions_availables": self.options.RegionsAvailables.value,
            "draft_change_available": self.options.DraftChangeAvailable.value,
            "trainer_round_sanity": self.options.TrainerRoundSanity.value,
            "add_achievements": self.options.AddAchievements.value,
            "draft_types": self.options.DraftTypes.value,
            "number_of_starting_types": self.options.NumberOfStartingTypes.value,
            "add_extra_draft_types_items": self.options.AddExtraDraftTypesItems.value,
            "lock_draft_power": self.options.LockDraftPower.value,
        }
    
