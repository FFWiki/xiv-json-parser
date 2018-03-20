ENEMY_MAP_DATA_MAPS = {"placename_name": {}, "zone_name": {}}

def recursive(args):
    pass # TODO: This

table = {
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
                    # 'maps': recursive(ENEMY_MAP_DATA_MAPS)
                    # TODO: This
                    'stats': {'hpAvg': {}, 'hpMax': {}, 'hpMin': {}, 'levelMax': {}, 'levelMin': {}, 'mpAvg': {}, 'mpMax': {}, 'mpMin': {}},
                },
                'patch': {'name': {}, 'number': {}},
            },
        },
}

def databases():
	return table
