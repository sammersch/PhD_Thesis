
IGD_data = [] # this is the dictionary that is fed by nameSectionShape, which was generated from the shape files
                  # LIM_SECTION and act_pcn_toponymes_1:
IGD_singles = []
IGD_singles_all = []

IGD1930 = []
IGD1930_2 = []
IGDCAD = []
IGDCAD_2 = []

empty_query = []

with open('IGD_load/IGDdata.csv', encoding='utf-8') as cabernet:#, encoding='utf-8'
    pinot = cabernet.readlines()
for item in pinot:
    elbling = item.rstrip('\n')
    # print(elbling)
    if elbling not in empty_query:
        empty_query.append(elbling)
    section, adm_comm, name1930, nameCAD = elbling.split(',')
    IGD_data.append(dict({'name1930': name1930,
                          'nameCAD': nameCAD,
                          'section': section,
                          'adm_comm': adm_comm}))
cabernet.close()

outList = ['auf', 'bei', 'beim', 'der',
           'vor', 'de', 'den', 'in',
           'im', 'am', 'an', 'op',
           'von', 'obent', 'a', 'vrun',
           'vir']


for item in empty_query:
    section, adm_comm, name1930, nameCAD = item.split(',')

    if name1930 != '':
        IGD1930.append(dict({'name': name1930,
                          'section': section,
                          'adm_comm': adm_comm}))
        IGD_singles_all.append(dict({'name': name1930,
                             'section': section,
                             'adm_comm': adm_comm}))

        if len(name1930.split(' ')) > 1:
            for btem in outList:
                if btem in name1930.lower().split(' ')[1:]:
                    IGD1930_2.append(dict({'name': ' '.join(name1930.split(' ')[1:]) + ' ' + name1930.split(' ')[0],
                                         'section': section,
                                         'adm_comm': adm_comm}))
        else:
            IGD1930_2.append(dict({'name': ' '.join(name1930.split(' ')[1:]) + ' ' + name1930.split(' ')[0],
                                   'section': section,
                                   'adm_comm': adm_comm}))
                    # print(item['name'], '>>>', ' '.join(item['name'].split(' ')[1:]) + ' ' + item['name'].split(' ')[0])


    if nameCAD != '':
        IGDCAD.append(dict({'name': nameCAD,
                          'section': section,
                          'adm_comm': adm_comm}))
        IGD_singles_all.append(dict({'name': name1930,
                                     'section': section,
                                     'adm_comm': adm_comm}))

    # IGD_singles.append(dict({'name1930': name1930,
    #                       'nameCAD': nameCAD,
    #                       'section': section,
    #                       'adm_comm': adm_comm}))
# print('IGD1930', len(IGD1930))
# print('IGD1930_2', len(IGD1930_2))
# print(len(IGD1930))
# print(len(IGDCAD))
# outList = ['auf', 'bei', 'beim', 'der', 'vor', 'de', 'den', 'in', 'im', 'am', 'an', 'op', 'von', 'obent', 'a', 'vrun', 'vir']
# for item in IGD1930:
#     if len(item['name'].split(' ')) > 1:
#         print(item['name'])
# print('#' * 60)
# print('#' * 60)
# print('#' * 60)
# for item in IGD1930:
#     if len(item['name'].split(' ')) > 1:
#         for btem in outList:
#             if btem in item['name'].lower().split(' ')[1:]:
#                 print(item['name'], '>>>', ' '.join(item['name'].split(' ')[1:]) +' '+ item['name'].split(' ')[0])

# print(len(IGD_data))
