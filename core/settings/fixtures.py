# Fixtures Settings
FIXTURES_DIR_NAME = '_fixtures'
FIXTURES_DEV_DIR_NAME = 'dev'

# These lists are used to force the order fixtures are return
# Named fixtures will be run in the order listed
# Fixtures not included in these settings will be run afterwards
FIXTURES_LIST_BASE = [
    'auth.User',
    'game_data.Adventurer',
    'game_data.Wyrmprint',
    'game_data.Dragon',
    'game_data.Weapon',
    'comps.CompDifficulty',
    'comps.compSection',
    'comps.CompQuest',
    'comps.CompType',
    'comps.CompCreator',
    'comps.AdventurerBuild',
    'comps.Comp',
]

FIXTURES_LIST_DEV = [
    'auth.User',
    'game_data.Adventurer',
    'game_data.Wyrmprint',
    'game_data.Dragon',
    'game_data.Weapon',
    'comps.CompDifficulty',
    'comps.compSection',
    'comps.CompQuest',
    'comps.CompType',
    'comps.CompCreator',
    'comps.AdventurerBuild',
    'comps.Comp',
]
