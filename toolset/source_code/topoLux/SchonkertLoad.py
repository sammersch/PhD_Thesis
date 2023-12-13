
numbers_sections = []
with open('Schonkert/limadm_sections.csv', encoding='utf-8') as merlot:
    pineau = merlot.readlines()
    # print(pineau)
    for item in pineau:
        sylvaner = item.rstrip('\n')
        syrah = sylvaner.split(',')
        # print(syrah[-3].lstrip('"').rstrip('"')+syrah[-1], syrah[3])
        numbers_sections.append(dict({'code': syrah[-3].lstrip('"').rstrip('"')+syrah[-1],
                                      'section': syrah[3],
                                      'adm_comm': syrah[-2]}))

merlot.close()
# print(numbers_sections)
# for jtem in numbers_sections:
#     if jtem['code'] == '130A':
#         print(jtem['code'], jtem['section'])
#
# print(''.join([x['code']+x['section'] for x in numbers_sections if x['code']=='130A']))


schonkert_load = [] # commune;localité;section;lieu-dit;page
# CommuneSection;Ur-Plang;aal lieudit;nei lieudit;Haaptwuert;nummer;Doubles toponymes;Remarques;Ur-Plang;;

with open('Schonkert/SchonkertShort.csv', encoding='utf-8') as cabernet:
    pinot = cabernet.readlines()
for item in pinot:
    elbling = item.rstrip('\n')
    # print(elbling.split(','))
    rivaner = elbling.split(',')


    # CommuneSection, urplang1, aal_lieudit, nei_lieudit = elbling.split(',')
    # print(rivaner[0])

    schonkert_load.append(dict({'section': ''.join([x['section'] for x in numbers_sections if x['code']==rivaner[0]]),
                                'adm_comm': ''.join([x['adm_comm'] for x in numbers_sections if x['code']==rivaner[0]]),
                                'up1': rivaner[1],
                                'aal': rivaner[2],
                                'nei': rivaner[3]}))
cabernet.close()

# print(schonkert_load)


# count = 0
# for item in schonkert_load:
#     if item['up1'] != '':
#         count += 1
#
# print(count)