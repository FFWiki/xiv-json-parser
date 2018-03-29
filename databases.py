ENEMY_MAP_DATA_MAPS = {"placename_name": {}, "zone_name": {}}
ITEM_ATTRIBUTES_PARAMS = {"name": {}, "value": {}, "value_hq": {}}
LEVE_ITEMS = {"name": {}, "id": {}}
PLACENAME_ENEMIES = {"name": {}, positions: recursive(PLACENAME_ENEMIES_POSITIONS)}
PLACENAME_ENEMIES_POSITIONS = {"hp": {}, "level": {}, "x": {}, "y": {}}
PLACENAME_INSTANCES = {"name": {}, "level": {}, "content_type": {}, "help": {}}
PLACENAME_NPCS = {"name": {}, "position": {"x": {}, "y": {}}}
QUEST_TEXT = {"text": {}}
TITLE_ACHIEVEMENTS = {"name": {}}
EXPTABLE = {"exp": {}}

QUESTS = {"name": {}, "genre_name": {}, "npc_name": {}, "patch": {"name": {}, "number": {}}}
ITEM_CLASSES = {} # TODO: Add all item classes.

def recursive(args):
    d = {}
    for i in range(256): # this constant could be wrong?
        d[i] = args
    return d

def items(args):
    d = {}
    for cls in ITEM_CLASSES:
        sd = {}
        for subcls in cls:
            sd[subcls] = recursive(args)
        d[cls] = sd
    return d

table = {
        # TODO: Gathering, crafting
	"achievement": {
		"url": "https://api.xivdb.com/achievement",
		"keys": {
			'name': {},
                        'name_de': {},
                        'name_fr': {},
                        'name_ja': {},
			'patch': {'name': {}, 'number': {}},
			'kind_name': {},
                        'type_name': {},
                        'category_name': {},
                        'help': {},
                        'item': {},
                        'title': {}
		}
	},
        "action": {
            "url": "https://api.xivdb.com/action",
            "keys": {
                'name': {},
                'name_ja': {},
                'name_fr': {},
                'name_de': {},
                'help_en': {},
                'level': {},
                'cost_cp': {},
                'cost_hp': {},
                'cost_mp': {},
                'cost_tp': {},
                'cast_range': {},
                'cast_time': {},
                'recast_time': {},
                'is_trait': {},
                'type_name': {},
                'patch': {'name': {}, 'number': {}},
            },
        },
        "emote": {
            "url": "https://api.xivdb.com/emote",
            "keys": {
                'name': {},
                'name_ja': {},
                'name_fr': {},
                'name_de': {},
                'text_command': {'command_1': {}, 'command_2': {}, 'command_3': {}, 'command_4': {}},
                'patch': {'name': {}, 'number': {}},
            },
        },
        "enemy": {
            "url": "https://api.xivdb.com/enemy",
            "keys": {
                'name': {},
                'name_ja': {},
                'name_fr': {},
                'name_de': {},
                'map_data': {
                    'maps': recursive(ENEMY_MAP_DATA_MAPS),
                    'stats': {'hpAvg': {}, 'hpMax': {}, 'hpMin': {}, 'levelMax': {}, 'levelMin': {}, 'mpAvg': {}, 'mpMax': {}, 'mpMin': {}},
                },
                'patch': {'name': {}, 'number': {}},
            },
        },
        "fate": {
            "url": "https://api.xivdb.com/fate",
            "keys": {
                'name': {},
                'name_ja': {},
                'name_fr': {},
                'name_de': {},
                'help_en': {},
                'class_level': {},
                'class_level_max': {},
                'map': {'placename': {'name': {}}},
                'patch': {'name': {}, 'number': {}},
            },
        },
        "instance": {
            "url": "https://api.xivdb.com/instance",
            "keys": {
                'name': {},
                'name_ja': {},
                'name_fr': {},
                'name_de': {},
                'help_en': {},
                'level': {},
                'level_sync': {},
                'time_limit': {},
                'tanks_per_party': {},
                'healers_per_party': {},
                'dps_per_party': {},
                'item_level': {},
                'item_level_sync': {},
                'content_name': {},
                'patch': {'name': {}, 'number': {}},
            },
        },
        "item": {
            "url": "https://api.xivdb.com/item",
            "keys": {
                'name': {},
                'name_ja': {},
                'name_fr': {},
                'name_de': {},
                'help_en': {},
                'classjob_category': {},
                'level_equip': {},
                'level_item': {},
                'category_name': {},
                'attributes_base': {'auto_attack': {}, 'auto_attack_hq': {}, 'block_rate': {}, 'block_rate_hq': {}, 'block_strength': {}, 'block_strength_hq': {},
                    'damage': {}, 'damage_hq': {}, 'defense': {}, 'defense_hq': {}, 'delay': {}, 'delay_hq': {}, 'magic_damage': {}, 'magic_damage_hq': {},
                    'magic_defense': {}, 'magic_defense_hq': {}},
                'attributes_params': recursive(ITEM_ATTRIBUTES_PARAMS),
                'patch': {'name': {}, 'number': {}},
            },
        },
        "leve": {
            "url": "https://api.xivdb.com/leve",
            "keys": {
                'name': {},
                'name_ja': {},
                'name_fr': {},
                'name_de': {},
                'help_en': {},
                'gil_reward': {},
                'exp_reward': {},
                'leve_client': {},
                'class_level': {},
                'classjob_category': {},
                'time_limit': {},
                'placename': {'name': {}},
                'patch': {'name': {}, 'number': {}},
                #'items': items(LEVE_ITEMS),
                #TODO: This
            },
        },
        "minion": {
            "url": "https://api.xivdb.com/minion",
            "keys": {
                'name': {},
                'name_ja': {},
                'name_fr': {},
                'name_de': {},
                'info1': {},
                'info2': {},
                'summon': {},
                'behavior': {},
                'action': {},
                'attack': {},
                'cost': {},
                'hp': {},
                'defense': {},
                'skill_cost': {},
                'speed': {},
                'patch': {'name': {}, 'number': {}},
            },
        },
        "npc": {
            "norepeat": True, #TODO: This
            "url": "https://api.xivdb.com/npc",
            "keys": {
                'name': {},
                'name_de': {},
                'name_jp': {},
                'name_fr': {},
                'title': {},
                'title_de': {},
                'title_fr': {},
                'title_jp': {},
                'patch': {'name': {}, 'number': {}},
            },
        },
        "placename": {
            "url": "https://api.xivdb.com/placename",
            "keys": {
                'name': {},
                'name_de': {},
                'name_jp': {},
                'name_fr': {},
                'enemies': recursive(PLACENAME_ENEMIES),
                'instances': recursive(PLACENAME_INSTANCES),
                'npcs': recursive(PLACENAME_NPCS),
                'quests': recursive(QUESTS),
                'patch': {'name': {}, 'number': {}},
            },
        },
        "quest": {
            "url": "https://api.xivdb.com/quest",
            "keys": {
                'category_name': {},
                'exp_reward': {},
                'genre_name': {},
                'gil_reward': {},
                'name': {},
                'name_jp': {},
                'name_fr': {},
                'name_de': {},
                'npc_start': {'name': {}},
                'npc_end': {'name': {}},
                'patch': {'name': {}, 'number': {}},
                'pre_quests': recursive(QUESTS),
                'post_quests': recursive(QUESTS),
                'text': {'journal': recursive(QUEST_TEXT), 'todo': recursive(QUEST_TEXT)},
            },
        },
        "status": {
            "url": "https://api.xivdb.com/status",
            "keys": {
                'name': {},
                'name_de': {},
                'name_jp': {},
                'name_fr': {},
                'help': {},
                'patch': {'name': {}, 'number': {}},
            },
        },
        "title": {
            "url": "https://api.xivdb.com/title",
            "keys": {
                'name': {},
                'name_de': {},
                'name_jp': {},
                'name_fr': {},
                'name_female': {},
                'name_female_de': {},
                'name_female_jp': {},
                'name_female_fr': {},
                'achivements': recursive(TITLE_ACHIEVEMENTS),
                'patch': {'name': {}, 'number': {}},
            },
        },
        "weather": {
            "url": "https://api.xivdb.com/weather",
            "keys": {
                'name': {},
                'name_de': {},
                'name_jp': {},
                'name_fr': {},
            },
        },
        "exptable": {
            "url": "https://api.xivdb.com/data/exp_table",
            "keys": recursive(EXPTABLE),
        },

}

def databases():
	return table
