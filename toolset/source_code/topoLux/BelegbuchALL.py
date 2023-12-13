# from MicroTopoLoadAllData import microTopoAll
# from CartoLoad import cartoLoad
# from BusStopLoad import busStopLoad
# from AllLoader import all_loader
from corpus_load import corpus
print('corpus loaded')

abc = 'aäbcdeéëèfghijklmnoöpqrstuüvwxyz'


# cartoList = []
# microList = []
# busList = []


# simple_list2 = []

counterList = []

uniqueList = [] # 102075
simple_list = [] # 62516
# #
# for item in corpus:
#     # if item['name'].upper() not in uniqueList:
#     #     if item['name'] == '':
#     #         print(item['name'], item['section'], item['adm_comm'], item['corpus'])
#     #     uniqueList.append(item['name'].upper())
#     if item['name'].split()[-1].upper() not in simple_list:
#         simple_list.append(item['name'].split()[-1].upper())
# print('lists loaded')
# print(len(uniqueList))
# print(len(simple_list))
# print(sorted(uniqueList)[:9])
# print(sorted(simple_list)[-20:])
# #
# for item in cartoLoad:
#     if item['name'].split()[-1].lower() not in simple_list:
#         if item['nature'] == 'Village':
#             pass
#         elif item['nature'] == 'Commune':
#             pass
#         elif item['name'] == '(B)':
#             pass
#         elif item['name'] == '(Dunkrodt)':
#             pass
#         elif item['name'].split()[-1].startswith('d\''):
#             temp = item['name'].split()[-1]
#             base_lemma = temp[2:]
#         elif item['name'].split()[-1].startswith('l\''):
#             temp = item['name'].split()[-1]
#             base_lemma = temp[2:]
#         elif item['name'].split()[-1].startswith('z\''):
#             temp = item['name'].split()[-1]
#             base_lemma = temp[2:]
#         else:
#             base_lemma = item['name'].split()[-1]
#         simple_list.append(base_lemma.lower())


#
# for item in microTopoAll:
#
#     if 'Pré' in item['name']:
#         if 'Préi' in item['name']:
#             base_lemma = item['name'].split()[-1]
#             if base_lemma not in simple_list:
#                 simple_list.append(base_lemma.lower())
#         else:
#             pass
#     elif item['name'].split()[-1] not in simple_list:
#         if item['name'].split()[-1] == 'im':
#             pass
#         elif item['name'].split()[-1] == 'grusse':
#             pass
#         elif item['name'].split()[-1] == 'dem':
#             pass
#         elif item['name'].split()[-1].startswith('d\''):
#             temp = item['name'].split()[-1]
#             base_lemma = temp[2:]
#         elif item['name'].split()[-1].startswith('l\''):
#             temp = item['name'].split()[-1]
#             base_lemma = temp[2:]
#         elif item['name'].split()[-1].startswith('z\''):
#             temp = item['name'].split()[-1]
#             base_lemma = temp[2:]
#         elif item['name'].split()[-1] == 'champ':
#             base_lemma = item['name'].split()[-3:-1]
#         elif item['name'].split()[-1] == 'Aus':
#             base_lemma = item['name'].split()[-2]
#         elif item['name'].split()[-1] in '123':
#             base_lemma = item['name'].split()[-2]
#         elif item['name'].split()[-1] in abc.upper():
#             base_lemma = item['name'].split()[-2]
#         else:
#             base_lemma = item['name'].split()[-1]
#
#         simple_list.append(base_lemma.lower())



#
# for item in busStopLoad:
#     if item['name'].split()[-1] not in simple_list:
#         if item['name'].split()[-1].startswith('d\''):
#             temp = item['name'].split()[-1]
#             base_lemma = temp[2:]
#         elif item['name'].split()[-1].startswith('l\''):
#             temp = item['name'].split()[-1]
#             base_lemma = temp[2:]
#         elif item['name'].split()[-1].startswith('z\''):
#             temp = item['name'].split()[-1]
#             base_lemma = temp[2:]
#         else:
#             base_lemma = item['name'].split()[-1]
#         simple_list.append(base_lemma.lower())



# for item in simple_list:
#     if item not in counterList:
#         counterList.append(item)


# new_list = []
# for letter in 'a':
#     print(letter.upper())
#     for item in sorted(counterList):
#         if item.startswith(letter):
#             print('\t' + item.upper())
#
#             for x in microTopoAll:
#                 # print('\t\tM')
#                 if item == x['name'].split()[-1].lower():
#                     print('\t\t|M|\t' + x['name'] + '(' + x['section'] + ' / ' + x['adm_comm'] + ')')
#                     if x['name'] not in new_list:
#                         new_list.append(['M', x['name']])
#             for y in cartoLoad:
#                 if item == y['name'].split()[-1].lower():
#                     print('\t\tC\t' + y['name'] + '(' + y['section'] + ' / ' + y['adm_comm'] + ')')
#                     if y['name'] not in new_list:
#                         new_list.append(['C', y['name']])
#             for z in busStopLoad:
#                 if item == z['name'].split()[-1].lower():
#                     print('\t\tB\t' + z['name'] + '(' + z['section'] + ')')
#                     if z['name'] not in new_list:
#                         new_list.append(['B', z['name']])
# # print(new_list)
# print(len(uniqueList))
# def evidence_printer_tex(file_name):
#     with open(file_name + '_all.tex', 'w', encoding='utf-8') as printer:
#         for letter in abc:
#
#             # try:
#             #     test_list = []
#             #     for item in simple_list_sorted:
#             #         if item.lower().startswith(letter.lower()):
#             #             test_list.append(item)
#             #     test_list = sorted(test_list)
#             print(letter*40)
#             printer.write('\section{')
#             printer.write(letter.upper())
#             printer.write(letter.lower())
#             printer.write('}\n\n')
#
#             for item in sorted(uniqueList):
#                 print('\t', item)
#                 if item.startswith(letter.upper()):
#                     printer.write('\\textbf{')
#                     printer.write(item.upper())
#                     printer.write('}')
#                     printer.write('\n\n')
#
#                     for x in all_loader:
#                         if item in x['name'].upper().split(' '):
#                             printer.write(x['name'] + ' (' + x['section'] + ') (' + x['corpus'] + '), ')
#                             print(x['name'])
#                     printer.write('\n\n')
#             #     printer.write('\n\n')
#             # printer.write('\n\n')
#     printer.close()
#
# def evidence_printer_texLETTER(file_name, letter):
#     with open(file_name + '_all.tex', 'w', encoding='utf-8') as printer:
#
#         # printer.write('\section{')
#         printer.write(letter.upper())
#         printer.write(letter.lower())
#         # printer.write('}\n\n')
#
#         for item in sorted(uniqueList):
#             print('\t', item)
#             if item.startswith(letter.upper()):
#                 # printer.write('\\textbf{')
#                 printer.write(item.upper())
#                 # printer.write('}')
#                 printer.write('\n\n')
#
#                 for x in all_loader:
#                     if item in x['name'].upper().split(' '):
#                         printer.write(x['name'] + ' (' + x['section'] + ') (' + x['corpus'] + '), ')
#                         print(x['name'])
#                 printer.write('\n\n')
#             #     printer.write('\n\n')
#             # printer.write('\n\n')
#     printer.close()



# for item in sorted(uniqueList):
#     print(item)
# uniqueList = []
# for item in all_loader:
#     if item['name'].split(' ')[-1].upper() not in uniqueList:
#         uniqueList.append(item['name'].split(' ')[-1].upper())
# print(len(uniqueList))
# print(len(all_loader))
# for item in sorted(uniqueList):
#     print(item)
#     for jtem in all_loader:
#         if item in jtem['name'].split(' ')[-1].upper():
#             print('\t', jtem['name'], jtem['corpus'])

# evidence_printer_tex('Belegbuch_20190920')
# evidence_printer_texLETTER('LetterA_20190923', 'a')
#
# print('start while loop')
# # abc = 'aäbcdeéëèfghijklmnoöpqrstuüvwxyz'
# signs_vowel_lower = ['o', 'ü', 'u', 'ö', 'y', 'í', 'ô', 'ê', 'ì', 'û', 'ï', 'â', 'ú']
#
# littera = 'z'
# with open('letter_' + littera + '.tex', 'w', encoding='utf-8') as printer:
#     for i in sorted(simple_list):
#         if i.startswith(littera.upper()):
#             # print(i + '      start')
#             printer.write('\\paragraph*{')
#             printer.write(i)
#             printer.write('} ')
#             for j in corpus:
#                 if i == j['name'].split()[-1].upper():
#                     printer.write('\\emph{')
#                     printer.write(j['name'])
#                     printer.write('} ')
#                     printer.write(j['section'].capitalize())
#                     printer.write(' (')
#                     printer.write(j['adm_comm'].upper()[:1])
#                     printer.write('): \\textsc{')
#                     printer.write(j['corpus'])
#                     printer.write('}, ')
#             printer.write('\n')
#         # printer.write('\n')
#
#
#     # empty_dict = {}
#     # # print('first for loop')
#     # for i in sorted(simple_list):
#     #     if i.startswith(littera.upper()):
#     #         blura = []
#     #         for j in corpus:
#     #             if i == j['name'].split()[-1].upper():
#     #                 if j['name'] not in blura:
#     #                     blura.append(j['name'])
#     #         empty_dict[i] = blura
#     # # print('second for loop')
#     # kucki = []
#     # for i in sorted(simple_list):
#     #     if i.startswith(littera.upper()):
#     #
#     #         for k in empty_dict[i]:
#     #             # print('this is k: ', k)
#     #             blumo = []
#     #             for j in corpus:
#     #                 # print('this is j: ', j)
#     #                 if k == j['name']:
#     #                     # print(k)
#     #                     blumo.append(''.join([j['section'], ' (', j['adm_comm'][0], '): ', j['corpus']]))
#     #             kucki.append([i, k, ', '.join(blumo)])
#     # # print('third for loop')
#     # # print(kucki)
#     # nuppu = []
#     # for gugli in kucki:
#     #     if gugli[0] not in nuppu:
#     #         nuppu.append(gugli[0])
#     # for gugli in kucki:
#     #     for kiki in sorted(nuppu):
#     #         print(kiki)
#     #         # printer.write('\\paragraph*{')
#     #         # printer.write(kiki)
#     #         # printer.write('} ')
#     #
#     #         if kiki == gugli[0]:
#     #             print(kiki, gugli[1], gugli[2])
#     #             printer.write(gugli[1])
#     #             printer.write(gugli[2])
#         # for i in sorted(simple_list):
#         #     print(i)
#         #     if i == gugli[0]:
#         #         print(gugli[1:])
#     # for i in sorted(simple_list):
#     #     if i.startswith(littera.upper()):
#     #         # print(i + '      start')
#     #         printer.write('\\paragraph*{')
#     #         printer.write(i)
#     #         printer.write('} ')
#     #         for j in corpus:
#     #             for k in kucki:
#     #                 if k[0] == i:
#     #                     print(i, k, k[1], k[2])
#     #                     printer.write('\\emph{')
#     #                     printer.write(k[1])
#     #                     printer.write('} ')
#     #                     printer.write(k[2])
#                 # if i == j['name'].split()[-1].upper():
#                 #
#                 #     intermittend = []
#                 #     if j['name'] not in intermittend:
#                 #         intermittend.append(j['name'])
#                 #
#                 #     for i_name in sorted(intermittend):
#                 #         print('\t\t'+i_name)
#                 #         printer.write('\\emph{')
#                 #         printer.write(i_name)
#                 #         printer.write('} ')
#                 #         if i_name == j['name']:
#                 #             print('\t\t\t'+i_name)
#                 #             printer.write('')
#                 #             printer.write(j['section'].capitalize())
#                 #             printer.write(' (')
#                 #             printer.write(j['adm_comm'].upper()[:1])
#                 #             printer.write('): \\textsc{')
#                 #             printer.write(j['corpus'])
#                 #             printer.write('}, ')
#
#
#                     # printer.write(j['name'])
#                     # printer.write(' (')
#                     # printer.write(j['section'].capitalize())
#                     # printer.write(', ')
#                     # printer.write(j['adm_comm'].capitalize())
#                     # printer.write(': ')
#                     # printer.write(j['corpus'])
#                     # printer.write('), ')
#             # print(i + '      end')
#             # printer.write('\n')
# printer.close()
#
# # # ae_test = 'unter  Aeschleidchen,Untereisenbach,Parc Hosingen,ap\nvor Maeschleidchen,Dorscheid,Parc Hosingen,ap\nober Aeschleidchen,Untereisenbach,Parc Hosingen,ap\nauf Aeschleidchen,Holtz,Rambrouch,ap\nan Aeschleidchen,Untereisenbach,Parc Hosingen,ap\nAESCHLEIDCHEN,HOLTZ,PERL,il30\nAESCHLEIDCHEN,HOLTZ,PERL,ilc\nAESCHLEIDCHEN,ULFLINGEN,NIEDERBESSLINGEN,ilc\nAN AESCHLEIDCHEN,Untereisenbach,Parc Hosingen,sa\nOBER AESCHLEIDCHEN,Untereisenbach,Parc Hosingen,sa\nUNTER AESCHLEIDCHEN,Untereisenbach,Parc Hosingen,sa\nAESCHLEIDCHEN,Holtz,Rambrouch,sa\nAUF AESCHLEIDCHEN,Holtz,Rambrouch,sa'
# ae_test = 'unter Aeschleidchen,Untereisenbach,Parc Hosingen,ap1\nunter Aeschleidchen,Dorscheid,Parc Hosingen,ap2\nober Aeschleidchen,Untereisenbach,Parc Hosingen,ap\nauf Aeschleidchen,Holtz,Rambrouch,ap\nan Aeschleidchen,Untereisenbach,Parc Hosingen,ap\nAESCHLEIDCHEN,HOLTZ,PERL,il30\nAESCHLEIDCHEN,HOLTZ,PERL,ilc\nAESCHLEIDCHEN,ULFLINGEN,NIEDERBESSLINGEN,ilc\nAN AESCHLEIDCHEN,Untereisenbach,Parc Hosingen,sa\nOBER AESCHLEIDCHEN,Untereisenbach,Parc Hosingen,sa\nUNTER AESCHLEIDCHEN,Untereisenbach,Parc Hosingen,sa\nAESCHLEIDCHEN,Holtz,Rambrouch,sa\nAUF AESCHLEIDCHEN,Holtz,Rambrouch,sa'
#
# test_dict = []
# new_list = ae_test.split('\n')
# for i in new_list:
#     j = i.split(',')
#     test_dict.append(dict({'name': j[0],
#                            'section': j[1],
#                            'adm_comm': j[2],
#                            'corpus': j[3]}))
#
# simple_test_list = ['AACK', 'AESCHLEIDCHEN', 'TOURELBAACH']
# empty_list = []
# boozinUSA = []
# #
# #
# empty_dict = {}
# for i in simple_test_list:
#     blura = []
#     for j in test_dict:
#         if i == j['name'].split()[-1].upper():
#             if j['name'] not in blura:
#                 blura.append(j['name'])
#     empty_dict[i] = blura
# kucki = []
# for i in simple_test_list:
#     for k in empty_dict[i]:
#         blumo = []
#         for j in test_dict:
#             if k == j['name']:
#                 blumo.append(''.join([j['section'], ' (', j['adm_comm'][0], '): ', j['corpus']]))
#         kucki.append([i,k,', '.join(blumo)])
# for item in kucki:
#     if item[0] == 'AESCHLEIDCHEN':
#         print(item[1])
#
# #
