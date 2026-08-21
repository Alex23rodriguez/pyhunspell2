from hunspell2 import HunSpell

hs = HunSpell("../dicts/fr/fr.dic")

# %%
hs.spell("asdf")
# False

# %%
hs.spell("salut")
# True

# %%
hs.suggest("garcon")
# ['garçon', 'gardon', 'gascon']

# %%
hs.raw("garcon")

# %%
hs.stem("suis")
# ['suivre', 'être']

# %%
hs.analyze("est")
"""
[
    ['st:est', 'po:nom', 'is:mas', 'is:sg'],
    ['st:être', 'po:v0ei_____a', 'po:ipre', 'po:3sg']
]
"""

# %%
hs.close()
