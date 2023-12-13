from MicroTopoLoadAllData import microTopoAll
import os

newItemList = []
newList = []
exceptionsList = []
# newListCut = []
for item in microTopoAll:
    if item['name'].split()[-1].islower():
        # newItem = item['name'].split()[-2]
        exceptionsList.append((item['name'], item['object_ID'], item['section'], item['adm_comm'], item['coordinateOne']))
        continue
    if item['name'].lower().startswith('zone indus'):
        newItem = item['name'].split()[-2]
    # elif item['name'].split()[-1].islower():
    #     newItem = item['name'].split()[-2]
    else:
        newItem = item['name'].split()[-1]
    newItemList.append(newItem)
    newList.append((newItem, item['name'], item['object_ID'], item['section'], item['adm_comm'], item['coordinateOne']))



def print_by_letter(directory='perLetter'):
    if not os.path.exists('topoSearch/' + directory):
        os.makedirs('topoSearch/' + directory)
    firstCharas = []
    for jtem in newItemList:
        if jtem[0].lower() not in firstCharas:
            firstCharas.append(jtem[0].lower())

    for htem in firstCharas: # this generates several files according to the first letter of the semantic main element

        with open('topoSearch/' + directory + '/' + htem.upper() + '.csv', 'w', encoding='utf-8') as dump:
            dump.write('Lemma,Name,ObjectID,Section,Commune,Long,Lat\n')
            for item in sorted(newList):
                if item[0].lower().startswith(htem.lower()):
                    dump.write(str(item[0]) + ',' + str(item[1]) + ',' + str(item[2])+ ',' + str(item[3])+ ',' + str(item[4])+ ',' + str(item[5]).lstrip('[').rstrip(']') + '\n')
        dump.close()



def print_whole(file_name='All_Items'):
    with open('topoSearch/' + file_name + '.csv', 'w', encoding='utf-8') as dump:
        dump.write('Lemma,Name,ObjectID,Section,Commune,Long,Lat\n')
        for item in sorted(newList):
            dump.write(str(item[0]) + ',' + str(item[1]) + ',' + str(item[2])+ ',' + str(item[3])+ ',' + str(item[4])+ ',' + str(item[5]).lstrip('[').rstrip(']') + '\n')
    dump.close()


nubi = []

for item in newItemList:
    if item not in nubi:
        nubi.append(item)


# cantons = []
# for item in microTopoAll:
#     if item['canton'] not in cantons:
#         cantons.append(item['canton'])

# SuffixEnd = []
# SuffixMiddle = []
# for item in microTopoAll:
#     # if item['canton'] == 'Remich':
#     if item['name'].startswith('per'):
#         continue
#     elif item['name'].endswith('pper'):
#         continue
#     elif item['name'].endswith('éiper'):
#         continue
#     elif item['name'].endswith('sper'):
#         continue
#     elif item['name'].endswith('eeper'):
#         continue
#     elif item['name'].endswith('perr'):
#         continue
#     elif 'pper' in item['name']:
#         continue
#     elif 'sper' in item['name']:
#         continue
#     elif 'mper' in item['name']:
#         continue
#     else:
#         if item['name'].endswith('per'):
#             SuffixEnd.append(item['name'])
#             # print(item['name'])
#         if 'per' in item['name']:
#             SuffixMiddle.append(item['name'])
#             print(item['name'])
#
# print(len(SuffixEnd))
# print(len(SuffixMiddle))



# with open('topoSearch/NewItemList.txt', 'w', encoding='utf-8') as dump:
#     for item in sorted(nubi):
#
#         dump.write(item + '\n')
# dump.close()

# for item in microTopoAll:
#     if 'schnuddelmier' in item['name'].lower():
#         print(item['name'] + " " + item['section'])



def getGraphSingle(name):
    results = []
    Vowels = 'aeiouéäëè'
    first = name.split('*')[0]
    second = name.split('*')[1]
    for item in microTopoAll:
        # # if item['sequence_length'] == 1:
        # if item['name'].startswith(first):
        #     if item['name'].endswith(second):
        #         results.append(item['name'])
        for Vowel in Vowels:
            for V in Vowels:
                if ''.join([first.lower(), Vowel, V, second]) in item['name']:
                    results.append([item['name'], ''.join([first.lower(), Vowel, V, second])])
    return results


def getGraphDouble(name):
    results = []
    Vowels = 'aeiouéäëè'

    first = name.split('*')[0]
    second = name.split('*')[1]
    for item in microTopoAll:
        for Vowel in Vowels:

            if ''.join([first.lower(), Vowel, second]) in item['name']:
                results.append([item['name'], ''.join([first.lower(), Vowel, second])])
    return results



def getBoth(name):
    results = []
    for item in getGraphSingle(name):
        results.append(item)
    for item in getGraphDouble(name):
        results.append(item)
    return results

# print(*getGraphDouble('gr*cht'), sep='\n')

# print(*getBoth('Gr*cht'), sep='\n')
# print(len(getBoth('Gr*cht')))


def getDifferentSpellings(name):
    results = []
    for item in getBoth(name):
        if item[1] not in results:
            results.append(item[1])
    return results


def getUniGraph(name):
    results = []
    first = name.split('*')[0]
    second = name.split('*')[1]
    for item in getDifferentSpellings(name):
        results.append(item.lstrip(first).rstrip(second))
    return results

# print(getUniGraph('gr*cht'))


def UniGraphPPrint(name):
    first = name.split('*')[0]
    second = name.split('*')[1]
    print(str(first) + '\t\t' + str(second))
    for item in getUniGraph(name):
        print('\t' + str(item))



# UniGraphPPrint('h*cht')
print(getDifferentSpellings('w*n'))

# for item in microTopoAll:
#     if item['name'].split()[-1].startswith('Koc'):
#         print(item)
