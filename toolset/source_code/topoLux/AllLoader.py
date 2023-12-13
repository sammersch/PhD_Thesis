import re
from MicroTopoLoadAllData import microTopoAll
from CartoLoad import cartoLoad
from BusStopLoad import busStopLoad
from IVV_load import IVV_load
from FERRARIS_load import FERRARIS_data
from IGDload import IGD_data, IGD_singles, IGD1930, IGDCAD
from ADL_load import ADL_load
from SchonkertLoad import schonkert_load
from cnra_load import cnra_load



all_loader = []

for item in microTopoAll:
    all_loader.append(dict({'name': item['name'],
                            # 'name2': '',
                            'section': item['section'],
                            'adm_comm': item['adm_comm'],
                            'corpus': 'ACT-PCN'}))

for item in cartoLoad:
    all_loader.append(dict({'name': item['name'],
                            # 'name2': '',
                            'section': item['section'],
                            'adm_comm': item['adm_comm'],
                            'corpus': 'ACT-CARTO'}))

for item in busStopLoad:
    all_loader.append(dict({'name': item['name'],
                            # 'name2': '',
                            'section': item['section'],
                            'adm_comm': '',
                            'corpus': 'BUS'}))

# for item in IGD_data:
#     all_loader.append(dict({'name': item['name1930'],
#                             'name2': item['nameCAD'],
#                             'section': item['section'],
#                             'adm_comm': item['adm_comm'],
#                             'corpus': 'IGD'}))

# for item in IGD_data:
#     all_loader.append(dict({'name': item['name1930'],
#                             # 'name2': item['nameCAD'],
#                             'section': item['section'],
#                             'adm_comm': item['adm_comm'],
#                             'corpus': 'IGD'}))
#
# for item in IGD_data:
#     all_loader.append(dict({'name': item['nameCAD'],
#                             # 'name2': item['nameCAD'],
#                             'section': item['section'],
#                             'adm_comm': item['adm_comm'],
#                             'corpus': 'IGD'}))

# for item in IGD_singles:
#     all_loader.append(dict({'name': item['name1930'],
#                             # 'name2': item['nameCAD'],
#                             'section': item['section'],
#                             'adm_comm': item['adm_comm'],
#                             'corpus': 'IGD'}))
#
# for item in IGD_singles:
#     all_loader.append(dict({'name': item['nameCAD'],
#                             # 'name2': item['nameCAD'],
#                             'section': item['section'],
#                             'adm_comm': item['adm_comm'],
#                             'corpus': 'IGD'}))

for item in IGD1930:
    all_loader.append(dict({'name': item['name'],
                            'section': item['section'],
                            'adm_comm': item['adm_comm'],
                            'corpus': 'IGD_1930'}))

for item in IGDCAD:
    all_loader.append(dict({'name': item['name'],
                            'section': item['section'],
                            'adm_comm': item['adm_comm'],
                            'corpus': 'IGD_CAD'}))

for item in FERRARIS_data:
    all_loader.append(dict({'name': item['name'],
                            # 'name2': '',
                            'section': item['section'],
                            'adm_comm': '',
                            'corpus': 'FERRARIS'}))

for item in IVV_load:
    all_loader.append(dict({'name': item['name'],
                            # 'name2': '',
                            'section': item['section'],
                            'adm_comm': item['adm_comm'],
                            'corpus': 'IVV'}))

for item in ADL_load:
    if item['name'] != '':
        all_loader.append(dict({'name': item['name'],
                                # 'name2': '',
                                'section': item['section'],
                                'adm_comm': item['adm_comm'],
                                'corpus': 'ADL'}))

for item in schonkert_load:
    if item['aal'] != '':
        all_loader.append(dict({'name': item['aal'],
                                # 'name2': '',
                                'section': item['section'],
                                'adm_comm': item['adm_comm'],
                                'corpus': 'S_A'}))

for item in schonkert_load:
    if item['nei'] != '':
        all_loader.append(dict({'name': item['nei'],
                                # 'name2': '',
                                'section': item['section'],
                                'adm_comm': item['adm_comm'],
                                'corpus': 'S_N'}))

for item in schonkert_load:
    if item['up1'] != '':
        all_loader.append(dict({'name': item['up1'],
                                # 'name2': '',
                                'section': item['section'],
                                'adm_comm': item['adm_comm'],
                                'corpus': 'S_UP'}))
# print(len(all_loader))
# alla = len(all_loader)
for item in cnra_load:
    all_loader.append(dict({'name': item['name'],
                            # 'name2': '',
                            'section': item['section'],
                            'adm_comm': item['adm_comm'],
                            'corpus': 'CNRA'}))

# print(len(all_loader))
# with open('corpus/corpus.csv', 'w', encoding='utf-8') as printer:
#     for item in all_loader:
#         printer.write(item['name'])
#         printer.write(';')
#         printer.write(item['section'])
#         printer.write(';')
#         printer.write(item['adm_comm'])
#         printer.write(';')
#         printer.write(item['corpus'])
#         printer.write('\n')
# printer.close()


singles = []

# for item in all_loader:
#     if item['name'] == '':
#         print(item['corpus'])
#     else:
#         if item['name'].lower().split()[-1] not in singles:
#             singles.append(item['name'].lower().split()[-1])
#
#
# for item in all_loader:
#     if 'foll' in item['name'].lower():
#         print(item['name'], item['section'], item['corpus'])
# print(len(all_loader))
# print(len(singles))
#     if item['name2'] == '':
#         continue
#     else:
#         if item['name2'] not in singles:
#             singles.append(item['name2'])
#     count += 1
#     print(count)
#
# print(singles)
#

# for item in sorted(singles):
#     if item.startswith('a'):
#         print(item)
#         for jtem in all_loader:
#             for htem in jtem['name'].split(' '):
#                 if item == htem.lower():
#                     print('\t', htem, '\t', jtem['name'])
# with open('all_loader/allDATA_list.txt', 'w', encoding='utf-8') as winePLOTTER2:
#     for item in sorted(singles):
#         if item.startswith('a'):
#             print(item)
#             winePLOTTER2.write('----------')
#             winePLOTTER2.write('\n')
#             winePLOTTER2.write(item.upper())
#             winePLOTTER2.write('\n')
#             for jtem in all_loader:
#                 for htem in jtem['name'].split(' '):
#                     if item == htem.lower():
#                         winePLOTTER2.write(jtem['name'])
#                         winePLOTTER2.write(', ')
#         winePLOTTER2.write('\n')
# winePLOTTER2.close()

# for item in all_loader:
#     if item['name'] not in singleNames:
#         singleNames.append(item['name'])
#         print('name1')
#     if item['name2'] not in singleNames:
#         singleNames.append(item['name2'])
#         print('name2')
#     print('nameALL')

# print(len(singleNames))

# with open('all_loader/allDATA_singles2.txt', encoding='utf-8') as singlesReader:
#     singlesReader.readlines()
#     for item in singlesReader:
#         print(item)
#     # instance = singlesReader.split(',')

sign = []

# for item in all_loader:
#     for jtem in item['name']:
#         if jtem not in sign:
#             sign.append(jtem)
#
#
# print(sign)
# print(len(sign))



signs = ['R', 'o', 'm', 'e', 'n', 'b', 'ü', 's', 'c', 'h', 'i', 'J', 'k', 'M', 'l', 'u', 'r', 'D', 'd', 'w', 'g', 'H', 'a', 'E', 't', 'W', 'K', 'f', 'B', 'ö', 'z', 'G', 'L', 'S', 'p', 'é', 'C', 'à', 'Z', 'ë', 'ä', 'v', "'", 'A', 'P', 'I', 'F', 'U', 'y', 'T', 'O', 'N', 'Q', 'Ä', '-', 'Í', 'V', 'j', 'Ë', '2', 'x', 'q', '1', 'è', '.', 'ô', 'ê', '3', 'Ì', 'å', 'û', 'É', '(', ')', 'ï', 'ç', 'â', 'Å', 'Y', 'X', 'Û', '/', '&', 'Ü', 'Ö', '’', '‘', '0', 'À', 'Ç', 'Ô', '`', 'ß', 'ú']

# print(len(all_loader))
#
# singleInstance = []
# for item in all_loader:
#     if item['name'] not in singleInstance:
#         singleInstance.append(item['name'])
#
# print(len(singleInstance))



    # testlist.append(dict({'name': item['name1930'],
    #                         # 'name2': item['nameCAD'],
    #                         'section': item['section'],
    #                         'adm_comm': item['adm_comm'],
    #                         'corpus': 'IGD'}))

# for item in IGD_data:
#     all_loader.append(dict({'name': item['nameCAD'],
#                             # 'name2': item['nameCAD'],
#                             'section': item['section'],
#                             'adm_comm': item['adm_comm'],
#                             'corpus': 'IGD'}))


