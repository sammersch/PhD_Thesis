from MicroTopoLoadAllData import microTopoAll
import re

abc = 'aäbcdeéëèfghijklmnopqrstuvwxyz'

common_list = []
lemmata = []

with open('MostCommonTXT.txt', 'r', encoding='utf-8') as reader:
    reader = reader.readlines()
    for i in reader:
        j = re.sub('\n', '', i)
        # print(j.split('\t')[])
        common_list.append(dict({'lemma': j.split('\t')[0], 'var': j.split('\t')[1]}))
        lemmata.append(j.split('\t')[0])

cp_list = []
with open('commonPrinter.csv', 'w', encoding='utf-8') as cp:
    for lemma in sorted(lemmata):
        # print(lemma)
        for word in common_list:
            if word['lemma'] == lemma:
                for toponym in microTopoAll:
                    if word['var'].upper() in toponym['name'].split()[-1].upper():
                        # print('\t' + word['var'])
                        # print('\t\t' + toponym['name'])
                        # print(lemma + ';' + word['var'] + ';' + toponym['name'])
                        # with open('commonPrinter.csv', 'w', encoding='utf-8') as cp:
                        cp.write(lemma)
                        cp.write(';')
                        cp.write(word['var'])
                        cp.write(';')
                        cp.write(toponym['name'])
                        cp.write('\n')
cp.close()