import re
from MicroTopoLoad import streetNames




chemin = []
rue = []
route = []
cite = []
wee = []
strooss = []
anAmIm = []
place = []
others = []
boulevard = []

for item in streetNames:
    name = item['name'].lower()
    name = re.sub('"', '', name)
    if 'chemin' in name:
        chemin.append(item)
    if 'boulevard' in name:
        boulevard.append(item)
    elif 'rue' in name:
        rue.append(item)
    elif 'route' in name:
        route.append(item)
    elif 'cité' in name:
        cite.append(item)
    elif 'wee' in name:
        wee.append(item)
    elif 'strooss' in name:
        strooss.append(item)
    elif 'an' in name:
        anAmIm.append(item)
    elif 'am' in name:
        anAmIm.append(item)
    elif 'in' in name:
        anAmIm.append(item)
    elif 'place' in name:
        place.append(item)
    else:
        others.append(item)

# CheminNamesOnly = []
# CheminNamesCount = []
# CheminOnce = []
# for jtem in chemin:
#     CheminNamesOnly.append(jtem['name'])
#     if jtem['name'] not in CheminOnce:
#         CheminOnce.append(jtem['name'])

# print(len(CheminNamesOnly))
# print(len(CheminOnce))

# for item in others:
#     print(item['name'])
# print(len(others))

# for item in streetNames:
#     if 'erpelding' in item['name'].lower():
#         print(item)
# print(len(chemin))
# for item in chemin:
#     if len(item['name'].split()) > 2:
#         if len(item['name'].split()[-1]) > 3:
#             print(item['name'])

# print(len(streetNames))
# for item in streetNames:
#     print(item['name'])