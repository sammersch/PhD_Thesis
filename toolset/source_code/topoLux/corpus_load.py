from collections import Counter
import csv
import gc

gc.collect()


corpus = []
corpus_syntax = []
with open('corpus/corpus.csv', encoding='utf-8') as cabernet:
    pinot = cabernet.readlines()
    for item in pinot:
        elbling = item.rstrip('\n')
        rivaner = elbling.split(';')

        corpus.append(dict({'name': rivaner[0],
                                'section': rivaner[1],
                                'adm_comm': rivaner[2],
                               'corpus':rivaner[3]}))
        corpus_syntax.append(dict({'name': rivaner[0],
                            'section': rivaner[1],
                            'adm_comm': rivaner[2],
                            'corpus': rivaner[3],
                            'sequence_length': len(rivaner[0].split())}))
cabernet.close()


# UniQ = []
# for item in corpus:
#     if item['name'] not in UniQ:
#         UniQ.append(item['name'])
# with open('corpus/unique.csv', 'w', encoding='utf-8') as printer:
#     printer.write(str(UniQ))
# printer.close()






# print('corpus:\t', len(corpus)) # 208643
# unique_count = [] # 121541
# for item in corpus:
#     if item['name'] not in unique_count:
#         unique_count.append(item['name'])
# print('unique:\t', len(unique_count))
# unique_lower = [] # 102194
# for item in corpus:
#     if item['name'].lower() not in unique_lower:
#         unique_lower.append(item['name'].lower())
# print('unique lower:\t', len(unique_lower))
# single_count = [] # 77735
# for item in corpus:
#     if item['name'].split()[-1] not in single_count:
#         single_count.append(item['name'].split()[-1])
# print('single:\t', len(single_count))
# single_lower = [] # 62605
# for item in corpus:
#     if item['name'].lower().split()[-1] not in single_lower:
#         single_lower.append(item['name'].lower().split()[-1])
# print('single lower:\t', len(single_lower))
# nilbil = []
# for item in corpus:
#     if item['corpus'] not in nilbil:
#         nilbil.append(item['corpus'])
#
# print(nilbil)

get_uniks = []
get_sekts = []
# for item in corpus:
#     if "wéngert" in item['name'].lower():
# #         # if item['section'].startswith('Echt'):
#         getjd = [item['name'], item['section']]
#         geths = item['section']
#         if getjd not in get_uniks:
#             get_uniks.append(getjd)
#         if geths not in get_sekts:
#             get_sekts.append(geths)
        # print(item['name'], item['section'], item['corpus'])
#
# print(len(get_sekts))
print(*sorted(get_sekts), sep='\n')
# hfkd = []
# for item in sorted(get_sekts):
#     # print("SECTION = '" + item + "' OR ")
#     hfkd.append('"SECTION" = ' + "'" + item + "' OR ")
#
# print(''.join(hfkd))
c = 0
section_count = []
comm_count = []
# input_list = ['rod', 'rot', 'rat', 'rad', 'rued', 'ruet', 'röd', 'roed', 'röt', 'roet', 'ried', 'riéd', 'riet', 'riét']
# input_list = ['mersch', 'miersch']
# input_list = ['wéngert', 'wengert', 'wingert']
# input_list = ['mees', 'maes', 'mais']
input_list = ['bambësch', 'bambesch', 'baambësch', 'baambesch', 'baumbüsch', 'baumbuesch', 'baumbusch']
# s_zero = []
# c_zero = []
for item in corpus:
#     if item['section'].lower() not in s_zero:
#         s_zero.append(item['section'].lower())
#     if item['adm_comm'].lower() not in c_zero:
#         c_zero.append(item['adm_comm'].lower())
    for jtem in input_list:
        if jtem in item['name'].lower():
#             c += 1
#             print(item)
            if item['section'] not in section_count:
                section_count.append(item['section'])
#             if item['adm_comm'].lower() not in comm_count:
#                 comm_count.append(item['adm_comm'].lower())
# print(c)
# print(len(section_count), 'from', len(s_zero)) # 16 + 75
# print(len(comm_count), 'from', len(c_zero))
# print(*sorted(s_zero), sep='\n')

#
# for item in section_count:
#     print(""""Section" = '""" + item + "' OR ")

# Kronenberg :Assel, Mersch, Rollingen
# Krounebierg : Rolling et Assel, Erpeldange, Mersch, Assel, Erpeldange, Rollingen
# all K_Berg: Assel, Mersch, Rollingen, Erpeldange
# others: Junglinster, Pissange, Gonderange, Mamer-Sud

# for item in corpus: # zopp, sop, rotz, schnuddel, mersch, marsch, mar, mor, moor, muer, mier(chen), meer(chen)
#     if item['name'].lower().endswith('ingen'):
#         print(item)

# for item in corpus: # zopp, sop, rotz, schnuddel, mersch, marsch, mar, mor, moor, muer, mier(chen), meer(chen)
    # if 'dudel' in item['section'].lower():
    # if 'mohren' in item['name'].lower():

    # if 'waler' in item['name'].lower():
    # if item['name'].lower().endswith('en'):
        # if 'gewann' in item['name'].lower():
        #     continue
        # else:
        # print(item)


# section_list = []
# for item in corpus:
#     if 'molt' in item['name'].lower():
#         if item['section'] not in section_list:
#             section_list.append(item['section'])
#
# print(*sorted(section_list), sep='\n')
# count_k = []
# quers = ['iewecht', 'iëwecht', 'iwecht', 'iwwecht', 'oberst', 'unterst', 'ënnescht', 'ennescht'] # 2080
# quers2 = ['bierg', 'berg', 'kop', 'knap', 'knop', 'dal', 'del', 'däl', 'gruecht', 'gracht', 'griecht'] # 177331
# quers2 = ['bierg', 'berg'] # 110939
# quers2 = ['kop', 'knap', 'knop'] # 15254
# quers2 = ['dal', 'del', 'däl'] # 45385
# quers2 = ['gruecht', 'gracht', 'griecht'] # 5733
# for item in corpus:
#     for jtem in quers2:
#         if jtem in item['name'].lower():
#             for ktem in quers:
#                 if ktem not in item['name'].lower():
#
#                     count_k.append(item['name'])
# #
# print(len(count_k))
# query_item = ["dell", "delt", "däl", "dal", "tal", "thal"]
# query_item = ["bierg", "berg", "berreg", "biär"]
# query_item = ["knap", "knaap", "knep", "knab", "knäp", "knob", "knop", "knoep", "knoeb", "knöb", "knöp"]
s_list = [] # Ap': 1, 'Ac': 1, 'F': 1, 'DAL': 1, 'Sa': 1, 'Sn': 1, 'A': 1, 'Tp': 1, 'IVV': 1, 'IL30': 1, 'ILc': 1, 'Su': 1}
# for item in corpus_syntax:
#    if 'kelte' in item['name'].lower():
#        print(item)
#
#
#
# print(Counter(s_list))


test_list = []
# print(' '.join([w.capitalize() for w in item['adm_comm'].split()]))
# for item in corpus:
#     if item['adm_comm'] not in test_list:
#         test_list.append(item['adm_comm'])
#
# for item in corpus:
#     if 'weinberg' in item['name'].lower():
#         print(item)
index_counter = 0
wangert = 12 + 36 + 7
berg = 192
kopp = 7 + 4
loch = 12 + 3
graecht = 4
bour = 9 + 8
fels = 4 + 23
lee = 2 + 7

totalIVV = 887

wangTotal = 700 + 127 + 104 + 116

all_names = []
all_words = []


# for item in corpus:
#     # if 'dal' in item['corpus'].lower():
#     if 'déi' in item['name'].lower():
#     # if item['name'].lower().endswith('lach'):
#         print(r'\emph{' + item['name'] + '} (' + item['section'] + r') (\textsc{' + item['corpus'] + '})')
# #     # if item['corpus'] == 'Ap':
# #         # print(item)
#     all_names.append(item['name'].lower())
#     for word in item['name'].split(' '):
#         all_words.append(word.lower())
# #         index_counter = index_counter +1
# # print(index_counter)
# # ollek, olek, olk, olëk
# # print(wangTotal)
# # print(wangTotal/208643*100)
#

# print(*Counter(all_words).most_common(110), sep='\n') # gets the mos common words in all names

# correspo = []
# uniques = []
# for item in sorted(all_words):
#     # print(item)
#     if item not in uniques:
#         uniques.append(item)
#
# for item in uniques:
#     for jtem in sorted(all_names):
#         if item in jtem:
#             correspo.append(item)
#
# print(len(correspo))
# print(*Counter(correspo).most_common(500), sep='\n')


# rad = ['Binsfeld', 'Breidweiler', 'Colbette',  'Hollenfels', 'Hollenfels', 'Hollenfels', 'Hollenfels', 'Hollenfels', 'Hollenfels', 'Hollenfels', 'Lellig','Roeser', 'Roeser', 'Scheidgen', 'Scheidgen']
# print(Counter(rad))

