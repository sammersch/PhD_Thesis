from MicroTopoLoadAllData import microTopoAll
from corpus_load import corpus
from collections import Counter

sections = []



def namesAndCounts(lookupName):
    with open('CSVExport/' + lookupName + '.csv', 'w', encoding='utf-8') as csv_file:
        csv_file.write('SECTION; NAMECOUNT\n')
        for i in microTopoAll:
            if i['section'] not in sections:
                sections.append(i['section'])
        for section in sections:
            sectionNames = []
            for item in microTopoAll:
                if section == item['section']:
                    sectionNames.append(item['name'])
            csv_file.write(section + '; ' + str(len(sectionNames)) + '\n')
            # print(section + ' ' + str(len(sectionNames)))
    csv_file.close()

def countsPerName(lookupName):
    with open('CSVExport/names/' + lookupName + '.csv', 'w', encoding='utf-8') as csv_file:
        csv_file.write('SECTION; NAMECOUNT\n')
        for i in microTopoAll:
            if i['section'] not in sections:
                sections.append(i['section'])
        for section in sections:
            sectionNames = []
            for item in microTopoAll:
                if section == item['section']:
                    if lookupName == item['name']:
                        sectionNames.append(item['name'])
            csv_file.write(section + '; ' + str(len(sectionNames)) + '\n')
            # print(section + ' ' + str(len(sectionNames)))
    csv_file.close()

def prepCOID(lookupName, cLass, query1='', query2='', query3='', query4='', query5='', query6=''):
    with open('CSVExport/classes/' + lookupName + '.csv', 'w', encoding='utf-8') as csv_file:
        csv_file.write('"object_ID","CLASS","LABEL"\n')
        for i in microTopoAll:
            for j in i['name'].split():
                if query1.lower() == j.lower():
                    csv_file.write('"')
                    csv_file.write(str(int(i['object_ID'])))
                    csv_file.write('",')
                    csv_file.write('"')
                    csv_file.write(cLass)
                    csv_file.write('",')
                    csv_file.write('"')
                    csv_file.write(i['name'])
                    csv_file.write('"\n')
                if query2 == '':
                    pass
                elif query2.lower() == j.lower():
                    csv_file.write('"')
                    csv_file.write(str(int(i['object_ID'])))
                    csv_file.write('",')
                    csv_file.write('"')
                    csv_file.write(cLass)
                    csv_file.write('",')
                    csv_file.write('"')
                    csv_file.write(i['name'])
                    csv_file.write('"\n')
                if query3 == '':
                    pass
                elif query3.lower() == j.lower():
                    csv_file.write('"')
                    csv_file.write(str(int(i['object_ID'])))
                    csv_file.write('",')
                    csv_file.write('"')
                    csv_file.write(cLass)
                    csv_file.write('",')
                    csv_file.write('"')
                    csv_file.write(i['name'])
                    csv_file.write('"\n')
                if query4 == '':
                    pass
                elif query4.lower() == j.lower():
                    csv_file.write('"')
                    csv_file.write(str(int(i['object_ID'])))
                    csv_file.write('",')
                    csv_file.write('"')
                    csv_file.write(cLass)
                    csv_file.write('",')
                    csv_file.write('"')
                    csv_file.write(i['name'])
                    csv_file.write('"\n')
                if query5 == '':
                    pass
                elif query5.lower() == j.lower():
                    csv_file.write('"')
                    csv_file.write(str(int(i['object_ID'])))
                    csv_file.write('",')
                    csv_file.write('"')
                    csv_file.write(cLass)
                    csv_file.write('",')
                    csv_file.write('"')
                    csv_file.write(i['name'])
                    csv_file.write('"\n')
                if query6 == '':
                    pass
                elif query4.lower() == j.lower():
                    csv_file.write('"')
                    csv_file.write(str(int(i['object_ID'])))
                    csv_file.write('",')
                    csv_file.write('"')
                    csv_file.write(cLass)
                    csv_file.write('",')
                    csv_file.write('"')
                    csv_file.write(i['name'])
                    csv_file.write('"\n')

    csv_file.close()




def nameCOID(lookupName, cLass, query1='', query2='', query3='', query4='', query5='', query6=''):
    with open('CSVExport/classes/' + lookupName + '.csv', 'w', encoding='utf-8') as csv_file:
        csv_file.write('"object_ID","CLASS","LABEL"\n')
        for i in microTopoAll:
            if query1.lower() in i['name'].lower():
                csv_file.write('"')
                csv_file.write(str(int(i['object_ID'])))
                csv_file.write('",')
                csv_file.write('"')
                csv_file.write(cLass)
                csv_file.write('",')
                csv_file.write('"')
                csv_file.write(i['name'])
                csv_file.write('"\n')
            if query2 == '':
                pass
            elif query2.lower() in i['name'].lower():
                csv_file.write('"')
                csv_file.write(str(int(i['object_ID'])))
                csv_file.write('",')
                csv_file.write('"')
                csv_file.write(cLass)
                csv_file.write('",')
                csv_file.write('"')
                csv_file.write(i['name'])
                csv_file.write('"\n')
            if query3 == '':
                pass
            elif query3.lower() in i['name'].lower():
                csv_file.write('"')
                csv_file.write(str(int(i['object_ID'])))
                csv_file.write('",')
                csv_file.write('"')
                csv_file.write(cLass)
                csv_file.write('",')
                csv_file.write('"')
                csv_file.write(i['name'])
                csv_file.write('"\n')
            if query4 == '':
                pass
            elif query4.lower() in i['name'].lower():
                csv_file.write('"')
                csv_file.write(str(int(i['object_ID'])))
                csv_file.write('",')
                csv_file.write('"')
                csv_file.write(cLass)
                csv_file.write('",')
                csv_file.write('"')
                csv_file.write(i['name'])
                csv_file.write('"\n')
            if query5 == '':
                pass
            elif query5.lower() in i['name'].lower():
                csv_file.write('"')
                csv_file.write(str(int(i['object_ID'])))
                csv_file.write('",')
                csv_file.write('"')
                csv_file.write(cLass)
                csv_file.write('",')
                csv_file.write('"')
                csv_file.write(i['name'])
                csv_file.write('"\n')
            if query6 == '':
                pass
            elif query6.lower() in i['name'].lower():
                csv_file.write('"')
                csv_file.write(str(int(i['object_ID'])))
                csv_file.write('",')
                csv_file.write('"')
                csv_file.write(cLass)
                csv_file.write('",')
                csv_file.write('"')
                csv_file.write(i['name'])
                csv_file.write('"\n')


    csv_file.close()

# nameCOID('hemp', 'HEMP', 'hanf', 'flachs', 'flues', 'huer', 'haarg', 'rost')
# nameCOID('metalProcessing', 'METAL', 'schmelz', 'schmëtt', 'schmit', 'schmid', 'schmied')

# prepCOID('along', 'ORIENTATION_BESIDES', 'längs', 'laanscht')

# emptyList = []
# for item in microTopoAll:
#     if 'dar'.lower() in item['name'].lower():
#         emptyList.append(item['name'])
#         print('"', int(item['object_ID']), '"', item['name'], item['section'])
# print(len(emptyList))

# countsPerName('Stross')

# namesAndCounts('CountPerSection')

# with open('CSVExport/names/gaass.csv', 'w', encoding='utf-8') as csv_file:
#     csv_file.write('SECTION; NAMECOUNT\n')
#     for i in microTopoAll:
#         if i['section'] not in sections:
#             sections.append(i['section'])
#     for section in sections:
#         sectionNames = []
#         for item in microTopoAll:
#             if section == item['section']:
#                 if 'gäss' in item['name']:
#                     sectionNames.append(item['name'])
#                 if 'gass' in item['name']:
#                     sectionNames.append(item['name'])
#                 if 'gaas' in item['name']:
#                     sectionNames.append(item['name'])
#
#
#         csv_file.write(section + '; ' + str(len(sectionNames)) + '\n')
#         # print(section + ' ' + str(len(sectionNames)))
# csv_file.close()


# def csv_export(lexeme):
#     results = []
#     for item in corpus:
#         if lexeme.lower() in item['name'].lower():
#             results.append(item['section'])
#     return results
#
#
# def csv_export_counter(lexeme, filename):
#     full_list = csv_export(lexeme)
#     unique_list = set(csv_export(lexeme))
#     results= []
#     for item in unique_list:
#         item_count = []
#         for jtem in full_list:
#             if item == jtem:
#                 item_count.append(item)
#         results.append(item + ',' + str(len(item_count)))
#     with open(filename + '.csv', 'w', encoding='utf8') as csv_writer:
#         for entry in results:
#             csv_writer.write(entry + '\n')
#
#
#
# csv_export_counter('schnuddel', 'CSVTEST')

# query_list = ['weiler', 'wéiler', 'weiller', 'wailer', 'wiler']
# query_list = ['mees', 'maes', 'mäs', 'määs']
# query_list = ['hardt', 'hart', 'haard', 'haart']
# query_list = ['rad', 'rued', 'rod', 'rood', 'roed', 'ried']
# query_list = ['scheed', 'scheid']
# query_list = ['seitert', 'säitert']
# query_list = ['bësch', 'büsch', 'busch', 'buesch', 'boesch', 'bösch']
# query_list = ['sang', 'saang', 'sank', 'saank']
# query_list = ['dall', 'däll', 'dell', 'delt']
# query_list = ['wanger', 'wenger', 'winger', 'wénger', 'wënger']
# # query_list = ['horg', 'hoerg', 'huerg']
# query_list = ['rippe', 'reppe', 'rëppe', 'röppe', 'roeppe']
# query_list = ['wels', 'welc', 'wals', 'walc','vals', 'valc']
# # results = []
# for item in query_list:
#     for jtem in corpus:
#         if item.lower() in jtem['name'].lower():
#             if 'schwalsb' in jtem['name'].lower():
#                 continue
#             elif 'sewelch' in jtem['name'].lower():
#                 continue
#             elif 'saewelch' in jtem['name'].lower():
#                 continue
#             elif 'säiwelch' in jtem['name'].lower():
#                 continue
#             elif 'séwelch' in jtem['name'].lower():
#                 continue
#             elif 'kiewel' in jtem['name'].lower():
#                 continue
#             elif 'seiwel' in jtem['name'].lower():
#                 continue
#             elif 'giewel' in jtem['name'].lower():
#                 continue
#             elif 'stiwwel' in jtem['name'].lower():
#                 continue
#             elif 'stiwel' in jtem['name'].lower():
#                 continue
#             elif "griewel" in jtem['name'].lower():
#                 continue
#             elif 'grewel' in jtem['name'].lower():
#                 continue
#             elif 'däiwel' in jtem['name'].lower():
#                 continue
#             elif 'stouwel' in jtem['name'].lower():
#                 continue
#             elif 'stuwel' in jtem['name'].lower():
#                 continue
#             elif 'diewel' in jtem['name'].lower():
#                 continue
#             elif 'deiwel' in jtem['name'].lower():
#                 continue
#             elif 'gréiwels' in jtem['name'].lower():
#                 continue
#             elif 'niwwel' in jtem['name'].lower():
#                 continue
#             elif 'wiérwel' in jtem['name'].lower():
#                 continue
#             elif 'dauwel' in jtem['name'].lower():
#                 continue
#             elif 'stiewel' in jtem['name'].lower():
#                 continue
#             elif 'gierwel' in jtem['name'].lower():
#                 continue
#             elif 'kiwel' in jtem['name'].lower():
#                 continue
#             elif 'siewel' in jtem['name'].lower():
#                 continue
#             elif 'howel' in jtem['name'].lower():
#                 continue
#             elif 'hiwwel' in jtem['name'].lower():
#                 continue
#             elif 'suwel' in jtem['name'].lower():
#                 continue
#             elif 'schwiewel' in jtem['name'].lower():
#                 continue
#             elif 'iewel' in jtem['name'].lower():
#                 continue
#             elif 'iwel' in jtem['name'].lower():
#                 continue
#             elif "ie'wels" in jtem['name'].lower():
#                 continue
#             elif 'säiwel' in jtem['name'].lower():
#                 continue
#             elif 'hewel' in jtem['name'].lower():
#                 continue
#             elif 'hiewel' in jtem['name'].lower():
#                 continue
#             elif 'werwel' in jtem['name'].lower():
#                 continue
#             elif 'frowel' in jtem['name'].lower():
#                 continue
#             elif 'kewel' in jtem['name'].lower():
#                 continue
#             elif 'suewel' in jtem['name'].lower():
#                 continue
#             elif 'stauwel' in jtem['name'].lower():
#                 continue
#             elif 'mierwels' in jtem['name'].lower():
#                 continue
#             elif 'mirwels' in jtem['name'].lower():
#                 continue
#             elif 'dorwels' in jtem['name'].lower():
#                 continue
#             elif 'kerwel' in jtem['name'].lower():
#                 continue
#             elif 'gewels' in jtem['name'].lower():
#                 continue
#             elif 'biwwel' in jtem['name'].lower():
#                 continue
#             elif 'kruboewels' in jtem['name'].lower():
#                 continue
#             elif 'krupuewelsbierg' in jtem['name'].lower():
#                 continue
#             elif 'krupewel' in jtem['name'].lower():
#                 continue
#             elif 'kruppewel' in jtem['name'].lower():
#                 continue
#             elif 'krupoewel' in jtem['name'].lower():
#                 continue
#             elif 'géwel' in jtem['name'].lower():
#                 continue
#             elif 'goewel' in jtem['name'].lower():
#                 continue
#             elif 'doorwels' in jtem['name'].lower():
#                 continue
#             elif 'wierwel' in jtem['name'].lower():
#                 continue
#             elif 'diéwel' in jtem['name'].lower():
#                 continue
#             elif 'felleschwelchen' in jtem['name'].lower():
#                 continue
#             else:
#                 print(jtem['name']+','+jtem['section']+','+jtem['adm_comm']+','+jtem['corpus'])
#             # results.append(jtem['section'])
#         # if jtem['name'].lower().endswith(item.lower()):
#             if 'belair' in jtem['name'].lower():
#                 continue
#                 # print(jtem)
#                 # results.append(jtem['section'])
#             elif 'parad' in jtem['name'].lower():
#                 continue
#             elif 'sankt' in jtem['name'].lower():
#                 continue
            # elif 'laid' in jtem['name'].lower():
            #     continue
            # elif 'schlaid' in jtem['name'].lower():
            #     continue
            # elif 'madelain' in jtem['name'].lower():
            #     continue
            # elif 'klais' in jtem['name'].lower():
            #     continue
            # elif 'lain' in jtem['name'].lower():
            #     continue
            # elif 'palais' in jtem['name'].lower():
            #     continue
            # elif 'relais' in jtem['name'].lower():
            #     continue
            # elif 'funiculaire' in jtem['name'].lower():
            #     continue
            # elif 'laiterie' in jtem['name'].lower():
            #     continue
            # elif 'blaise' in jtem['name'].lower():
            #     continue
            # elif 'clair' in jtem['name'].lower():
            #     continue
            # elif 'lehn' in jtem['name'].lower():
            #     continue
            # elif 'lehm' in jtem['name'].lower():
            #     continue
            # elif 'lehr' in jtem['name'].lower():
            #     continue
            # elif 'fleh' in jtem['name'].lower():
            #     continue
            # elif 'leem' in jtem['name'].lower():
            #     continue
            # elif 'leen' in jtem['name'].lower():
            #     continue
            # elif 'schleed' in jtem['name'].lower():
            #     continue
            # elif 'schleeg' in jtem['name'].lower():
            #     continue
            # elif 'schleef' in jtem['name'].lower():
            #     continue
            # elif 'kle' in jtem['name'].lower():
            #     continue
            # elif 'galeh' in jtem['name'].lower():
            #     continue
            # elif 'bleh' in jtem['name'].lower():
            #     continue
            # elif 'blees' in jtem['name'].lower():
            #     continue
            # elif 'leetem' in jtem['name'].lower():
            #     continue
            # elif 'schleek' in jtem['name'].lower():
            #     continue
            # elif 'leeschen' in jtem['name'].lower():
            #     continue
            # elif 'fleesch' in jtem['name'].lower():
            #     continue
            # elif 'fleer' in jtem['name'].lower():
            #     continue
            # elif 'vallee' in jtem['name'].lower():
            #     continue
            # elif 'culee' in jtem['name'].lower():
            #     continue
            # elif 'fleet' in jtem['name'].lower():
            #     continue
            # elif 'gallee' in jtem['name'].lower():
            #     continue
            # elif 'allee' in jtem['name'].lower():
            #     continue
            # elif 'schlees' in jtem['name'].lower():
            #     continue
            # elif 'leek' in jtem['name'].lower():
            #     continue
            # elif 'leede' in jtem['name'].lower():
            #     continue
            # elif 'leesg' in jtem['name'].lower():
            #     continue
            # elif 'léiw' in jtem['name'].lower():
            #     continue
            # elif 'gléisch' in jtem['name'].lower():
            #     continue
            # elif 'léier' in jtem['name'].lower():
            #     continue
            # elif 'kléi' in jtem['name'].lower():
            #     continue
            # elif 'léis' in jtem['name'].lower():
            #     continue
            # elif 'léin' in jtem['name'].lower():
            #     continue
            # elif 'pléi' in jtem['name'].lower():
            #     continue
            # elif 'fléib' in jtem['name'].lower():
            #     continue
            # elif 'bléi' in jtem['name'].lower():
            #     continue
            # elif 'léim' in jtem['name'].lower():
            #     continue
#             else:
#                 print(jtem)
#                 results.append(jtem['section'])
#
# print(Counter(results))
#
# for item in Counter(results):
#     print(item)
# testi = Counter(results)

# for key, count in testi.iteritems():
#     print(key)
#     print(count)




nimm = []
for item in corpus:
    if item['adm_comm'] == 'Habscht':
        # print(item['name'].split())
        if item['name'].split()[-1].lower() not in nimm:
            nimm.append([item['name'].split()[-1].upper(), item['name'], item['section'], item['corpus']])

print(*sorted(nimm), sep='\n')

# for item in corpus:
#     if 'wels' in item['name'].lower():
#         print(item)

# nimm = []
# for item in corpus:
#     nimm.append(item['section'])
#
# print(Counter(nimm))

# for item in corpus:
#     if 'frummes' in item['name'].lower():
#         print(item)

# for item in corpus:
#     if item['section'] == 'Mersch':
#         for jtem in nimm:
#             print(jtem)
#             if jtem in item['name'].lower():
#                 print('\t', item['name'], item['corpus'])

# # print(len(nimm))
# # print(*sorted(nimm), sep='\n')
# als = []
# for jtem in sorted(nimm):
#     middle = []
#     for item in corpus:
#         if item['section'] == 'Contern':
#             if jtem in item['name'].lower():
#                 # print(jtem, item['name'], item['corpus'])
#                 middle.append([item['name'] + ' (' + item['corpus'] + ')'])
#     # print(', '.join(str(jtem) + str(middle)))
#     # print(''.join(middle))
#     als.append([jtem,middle])
# # print(*als, sep='\n')
# for item in sorted(als):
#     print(item)