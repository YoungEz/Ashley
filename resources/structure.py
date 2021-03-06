user_data_structure = {
            "user_id": None,
            "guild_id": None,
            "user": {
                "experience": 0,
                "level": 1,
                "xp_time": None,
                "ranking": "Bronze",
                "titling": "Vagabond",
                "patent": 0,
                "raid": 0,
                "married": False,
                "married_at": None,
                "marrieding": False,
                "about": "Mude seu about, usando o comando \"ash about <text>\"",
                "stars": 0,
                "rec": 0,
                "commands": 0,
                "ia_response": False,
                "achievements": list()
            },
            "treasure": {
                "money": 0,
                "gold": 0,
                "silver": 0,
                "bronze": 0
            },
            "config": {
                "playing": False,
                "battle": False,
                "buying": False,
                "provinces": None,
                "mine": False,
                "vip": False,
                "roles": [],
                "points": 0
            },
            "moderation": {
                "credibility": {"ashley": 100, "guilds": [{"id": 0, "points": 100}]},
                "warns": [{"status": False, "author": None, "reason": None, "date": None, "point": 0}],
                "behavior": {"guild_id": 0, "historic": {"input": [], "output": []}},
                "notes": [{"guild_id": 0, "author": None, "date": None, "note": None}]
            },
            "rpg": {
                "vip": False,
                "lower_net": False,
                "class": 'default',
                "next_class": None,
                "level": 1,
                "xp": 0,
                "status": {"con": 5, "prec": 5, "agi": 5, "atk": 5, "luk": 0, "pdh": 1},
                "artifacts": dict(),
                "relics": dict(),
                'items': dict(),
                'skills': [0, 0, 0, 0, 0],
                'equipped_items': {
                    "shoulder": None,
                    "breastplate": None,
                    "gloves": None,
                    "leggings": None,
                    "boots": None,
                    "consumable": None,
                    "sword": None,
                    "shield": None,
                    "necklace": None,
                    "earring": None,
                    "ring": None
                },
                "active": False,
                "activated_at": None
            },
            "pet": {
                "status": False,
                "pet_equipped": None,
                "pet_bag": list(),
                "pet_skin_status": None,
                "pet_skin": None
            },
            "inventory": {
                "medal": 0,
                "rank_point": 0,
                "coins": 100
            },
            "artifacts": dict(),
            "box": {"status": {"active": False, "secret": 0, "ur": 0, "sr": 0, "r": 0, "i": 0, "c": 0}},
            "security": {
                "commands": 0,
                "commands_today": 0,
                "last_command": None,
                "last_channel": None,
                "last_verify": None,
                "last_blocked": None,
                "warns": {
                    "80": False,
                    "85": False,
                    "90": False,
                    "95": False,
                    "100": False
                },
                "strikes": 0,
                "strikes_to_ban": 0,
                "status": True,
                "blocked": False
            },
            "cooldown": dict(),
            "event": {"sam": False}
}

guild_data_structure = {
            "guild_id": None,
            "vip": False,
            "data": {
                "commands": 0,
                "ranking": "Bronze",
                "accounts": 0,
                "total_money": 0,
                "total_gold": 0,
                "total_silver": 0,
                "total_bronze": 0,
            },
            "treasure": {
                "total_money": 0,
                "total_gold": 0,
                "total_silver": 0,
                "total_bronze": 0
            },
            "log_config": {
                "log": False,
                "log_channel_id": None,
                "msg_delete": True,
                "msg_edit": True,
                "channel_edit_topic": True,
                "channel_edit_name": True,
                "channel_created": True,
                "channel_deleted": True,
                "channel_edit": True,
                "role_created": True,
                "role_deleted": True,
                "role_edit": True,
                "guild_update": True,
                "member_edit_avatar": True,
                "member_edit_nickname": True,
                "member_voice_entered": True,
                "member_voice_exit": True,
                "member_ban": True,
                "member_unBan": True,
                "emoji_update": True
            },
            "ia_config": {
                "auto_msg": False,
            },
            "bot_config": {
                "ash_news": False,
                "ash_news_id": None,
                "ash_git": False,
                "ash_git_id": None,
                "ash_draw": False,
                "ash_draw_id": None,
            },
            "func_config": {
                "cont_users": False,
                "cont_users_id": None,
                "member_join": False,
                "member_join_id": None,
                "member_remove": False,
                "member_remove_id": None,
            },
            "moderation": {
                "status": False,
                "moderation_log": False,
                "moderation_channel_id": None,
                "bad_word": False,
                "bad_word_list": list(),
                "flood": False,
                "flood_channels": list(),
                "ping": False,
                "ping_channels": list(),
                "join_system": {
                    "join_system": False,
                    "join_system_channel_door": None,
                    "join_system_channel_log": None,
                    "join_system_role": None,
                },
                "prison": {
                    "status": False,
                    "prison_channel": None,
                    "prison_role": None,
                    "prisoners": {"id": {"time": 0, "reason": None, "roles": list()}}
                }
            },
            "command_locked": {
                "status": False,
                "while_list": list(),
                "black_list": list()
            }
}
