import json, os, re
from MicroTopoLoad import microToponyms
from MicroTopoLoadAllData import microTopoAll
from corpus_load import corpus_syntax
from phoneticDistribution import vowel_clusters
from Syntax import syl_core_counter



def simplex(name):
    results = []
    for x in microTopoAll:
        if name == x['name'].split()[-1]:
            results.append(x['name'])
    return results


def lenSimplex(name):
    # results = []
    results = 0
    for item in simplex(name):
    #     results.append(item)
        results += 1
    # return len(results)
    return results


def KVG(KVG): # Kompositionsvorderglied; needs a specified dictionary outside of the
    # function. Is looking for the front element of a composition, indexing the official name of the macrotoponym.
    results = []
    for x in microTopoAll:
        # if x['microtoponym'] == KVG:
        #     continue
        if x['name'].split()[-1] == KVG:
            continue
        elif x['name'].split()[-1] == KVG + 'en':
            continue
        elif x['name'].split()[-1].startswith(KVG) == True:
            results.append(x['name'])

    return results

def lenKVG(name):
    results = 0
    for item in KVG(name):
        results += 1
    return results



def KHG(KHG): # Kompositionshinterglied; needs a specified dictionary outside of the
    # function. Is looking for the front element of a composition, indexing the official name of the macrotoponym.
    # Up to now, there is a minor bug in this function. If the query is capitalized, the results will be different
    # syntactic units where the query is the last. So this bug actually returns the queried word in a simplex, but in a
    # syntactic unit higher than 1.
    # If the query is in minuscules, the function returns morphological KHG.
    results = []
    for x in microTopoAll:
        if x['name'].endswith(KHG.lower()) == True:
            results.append(x['name'])

    return results

def lenKHG(name):
    results = 0
    for item in KHG(name):
        results += 1
    return results


def nameLookUp_syntax(name, syntactic_length=None): # needs a specified dictionary outside of the function.
    # Is looking for any microtoponym with name in it.
    # syntactic_length restricts the search to any such microtoponyms that have n syntactic units.
    # min=1, max=7. If not specified (or None), syntactic_length is set to all possible lengths.
    results = []
    for x in micro_dict:
        if syntactic_length is None:
            if name.lower() in x['microtoponym'].lower():
                results.append(x['microtoponym'])
        else:
            if syntactic_length == x['sequence_length']:
                if name.lower() in x['microtoponym'].lower():
                    results.append(x['microtoponym'])
    return results


def HowManyAre_syntax(name, syntactic_length):
    return len(nameLookUp_syntax(name, syntactic_length))



# ----Under construction!----
def nameLookUp_morphology(name, syntactic_length, morphology=None): # looks for correlation of syntactic length and
    # morphological build.
    # syntactic_length: min=1, max=7.
    # morphology: args: simplex, KVG, KHG.
    # results = []
    # if morphology is None:
    #     results.append(nameLookUp_syntax(name, syntactic_length))
    # else:
    # for item in micro_dict:
    #     if syntactic_length == item['sequence_length']:
    # if morphology == simplex:
    # new_input = nameLookUp_syntax(name, syntactic_length).split()
    # return simplex(new_input)
    # if simplex(nameLookUp_syntax(name, syntactic_length)) is True:
    # for item in micro_dict:
    #     if syntactic_length == item['sequence_length']:
    #         if name.lower() in item['microtoponym'].lower():
    #             if name == item['microtoponym']:
    #                 results.append(item['microtoponym'])

    # else:
    #     return 'Simplex Error, Will Robinson'
    # elif morphology == KVG:
    #     # new_input = nameLookUp_syntax(name, syntactic_length).split()
    #     # return KVG(new_input)
    #     # return KVG(name)
    #     for item in micro_dict:
    #         if syntactic_length == item['sequence_length']:
    #             return KVG(name)
    # elif morphology == KHG:
    #     # new_input = nameLookUp_syntax(name, syntactic_length).split()
    #     # return KHG(new_input)
    #     # return KHG(name)
    #     for item in micro_dict:
    #         if syntactic_length == item['sequence_length']:
    #             return KHG(name)
    # else:
    #     return 'Error, Error, Will Robinson'

    # if nameLookUp_syntax(name, syntactic_length) is True:
    # if morphology == 'simplex':
    #     return simplex(nameLookUp_syntax(name, syntactic_length))
    # if morphology == 'KVG':
    #     return KVG(nameLookUp_syntax(name, syntactic_length))
    # if morphology == 'KHG':
    #     return KHG(nameLookUp_syntax(name, syntactic_length))
    # if morphology is None:
    #     return nameLookUp_syntax(name, syntactic_length)


    if morphology == 'simplex':
        # put in intersection of simplex(name) and nameLookUp_Syntax(name, n)
        for i in  nameLookUp_syntax(name, syntactic_length): # and simplex(name):
            return simplex(i)
    if morphology == 'KVG':
        for i in nameLookUp_syntax(name, syntactic_length): # and KVG(name):
            return KVG(i)
    if morphology == 'KHG':
        for i in nameLookUp_syntax(name, syntactic_length): # and KHG(name):
            return KHG(i)
    if morphology is None:
        return nameLookUp_syntax(name, syntactic_length)

    # return results
# ----Under construction!----



def plurals(name):
    results = []
    for item in simplex(name + 'en'):
        results.append(item)
    for item in KVG(name + 'en'):
        results.append(item)
    for item in KHG(name + 'en'):
        results.append(item)
    return results




def morpho_quantifyer(corpus, sequence_length, syl_core_count):
    ''''returns a list of the counts of all the items in the corpus list with the queried sequence_length,
    the sublist of all those with the queried for sequence_length and syllable cores, and the percentage of these.'''
    query_list = []
    control_list = []
    for item in corpus:
        if item['sequence_length'] == sequence_length:
            control_list.append(item['name'])
            if syl_core_counter(item['name'].split()[-1])[0] == syl_core_count:
                query_list.append(item['name'])
    return [len(control_list), len(query_list), (len(query_list)/len(control_list))*100]

# print(morpho_quantifyer(corpus_syntax, 3, 0))

def morpho_quantifyer_position(corpus, sequence_length, syl_core_count, position):
    ''''returns a list of the counts of all the items in the corpus list with the queried sequence_length,
    the sublist of all those with the queried for sequence_length and syllable cores, and the percentage of these.
    Needs a position that defines its sequence order in the sytagma.'''
    query_list = []
    control_list = []
    for item in corpus:
        if item['sequence_length'] == sequence_length:
            control_list.append(item['name'])
            if syl_core_counter(item['name'].split()[position])[0] == syl_core_count:
                query_list.append(item['name'])
    return [len(control_list), len(query_list), (len(query_list)/len(control_list))*100]

# print(morpho_quantifyer(corpus_syntax, 2, 1))
# print(morpho_quantifyer_position(corpus_syntax, 3, 0, 0))


def morpho_check_position(corpus, sequence_length, syl_core_count, position):
    ''''returns a list of the items in the corpus list with the queried sequence_length and syllable cores.
    Needs a position that defines its sequence order in the sytagma.'''
    query_list = []
    # control_list = []
    for item in corpus:
        if item['sequence_length'] == sequence_length:
            # control_list.append(item['name'])
            if syl_core_counter(item['name'].split()[position])[0] == syl_core_count:
                if item['name'].lower() not in query_list:
                    query_list.append(item['name'].lower())
    return query_list

# print(*morpho_check_position(corpus_syntax, 1, 1, 0), sep='\n')
# print(len(morpho_check_position(corpus_syntax, 1, 1, 0)))

# dall = []
# delt = []
# for item in corpus_syntax:
#     if item['sequence_length'] == 1:
#         # print(item)
#         if syl_core_counter(item['name'].lower())[0] == 1:
#             # if 'dall' in item['name'].lower():
#             #     dall.append(item['name'])
#             # if 'delt' in item['name'].lower():
#             #     delt.append(item['name'])
#             print(item)
# print(len(dall))
# print(len(delt))


def get_all_morpho_quantifyers(corpus):
    results = []
    for i in range(1,9):
        for j in range(1,9):
            results.append([i, j, morpho_quantifyer(corpus, i, j)])
    return results


def get_all_position(corpus, sequence_length, position):
    results = []
    for i in range(1, 9):
        results.append([sequence_length, i, position, morpho_quantifyer_position(corpus, sequence_length, i, position)])
    return results

# print(*get_all_position(corpus_syntax, 2, 0), sep='\n')
# print(*get_all_position(corpus_syntax, 10, 2), sep='\n')

# for item in get_all_position(corpus_syntax, 7, -1):
#     print(item[0], item[1], item[2], item[3][0], item[3][1], item[3][2])

def get_syl_cores(corpus, syl_cores):
    results = []
    for item in corpus:
        for jtem in item['name'].split():
            if syl_core_counter(jtem)[0] == syl_cores:
                results.append([syl_cores, jtem, item['name'], item['section'], item['corpus']])
    return results

# print(*get_syl_cores(corpus_syntax, 6), sep='\n')

def query_for_names_starting_vowel(corpus):
    list_with_vowel = []
    control = []
    vowels = 'oeüiuaöéàëäyíèôêìåûïâú'
    for item in corpus:
        control.append(item['name'])
        for v in vowels:
            if item['name'].lower().split()[-1].startswith(v):
                list_with_vowel.append(item['name'])
    return [len(list_with_vowel), len(control), len(list_with_vowel) / len(control) * 100]


def catch_two_lexemes(corpus, lexeme1, lexeme2):
    ''''queries for two lexemes in any name. Is useful for query for correlation as in dvandva compounds'''
    results = []
    for item in corpus:
        if lexeme1.lower() in item['name'].lower():
            if lexeme2.lower() in item['name'].lower():
                results.append([[lexeme1, lexeme2], [item['name'], item['section'], item['corpus']]])
    return results

print(*catch_two_lexemes(corpus_syntax, 'himmel', 'blick'), sep='\n')

e_list = []
for item in corpus_syntax:
    if 'oi' in item['name'].lower():
        # if 'm' in item['name'].lower():
    #     # if 'bierg' not in item['name'].lower():
        print(item)
        # if not 'wangert' in item['name'].lower():
    # if item['section'].startswith('Lux'):
    # #     if 'm' in item['name']:
    #     print(item)
    # for word in item['name'].lower().split():
    #     if word.endswith('ert'):
    #         # if word != 'der':
    #         #     if word != 'unter':
    #         #         if word != 'ënner':
    #         #             if word != 'hinter':
    #         #                 if word != 'hanner':
    #         if word not in e_list:
    #             e_list.append(word)
# print(*sorted(e_list), sep='\n')
# print(query_for_names_starting_vowel(corpus_syntax))
# ahler, bafer, zongert

art_count = []
# for item in corpus_syntax:
#     for w in item['name'].lower().split()[:-1]:
#         if w not in art_count:
#             art_count.append(w)
#
# print(len(art_count))
#
# print(*sorted(art_count), sep='\n')

#
# for item in corpus_syntax:
#     for w in item['name'].lower().split():
#         if w == "inter":
#             print(item)
#



# print(len(art_count))
#
# die_initial = 103
# die_pl = 18

n1 = 105319
n2 = 55212
n3 = 43631
n4 = 4059
n5 = 620
n6 = 158
n7 = 20
n8 = 21
n10 = 3

total_n = n1+n2+n3+n4+n5+n6+n7+n8+n10

# print('TOTAL:\t', total_n)
#
# print('n1', round(n1/total_n*100, 6))
# print('n2', round(n2/total_n*100, 6))
# print('n3', round(n3/total_n*100, 6))
# print('n4', round(n4/total_n*100, 6))
# print('n5', round(n5/total_n*100, 6))
# print('n6', round(n6/total_n*100, 6))
# print('n7', round(n7/total_n*100, 6))
# print('n8', round(n8/total_n*100, 6))
# print('n10', round(n10/total_n*100, 6))
#
# print('printn1-4', round(n1/total_n*100, 6)+round(n2/total_n*100, 6)+round(n3/total_n*100, 6)+round(n4/total_n*100, 6))
# print('printn5-7', round(n5/total_n*100, 6)+round(n6/total_n*100, 6)+round(n7/total_n*100, 6))
# print('printn8n10', round(n8/total_n*100, 6)+round(n10/total_n*100, 6))


d = 52
die = 131
die_pl = 18

das = 2

d_pl = 2


der = 22661
derM = 41
dem = 7466
den = 4493
denM = 154

des = 4
ds = 3

total = d + die + der + dem + den + des + ds + das

# print('total', total)
#
# print("d'", round((d-d_pl)/total*100,6))
#
# print((d-d_pl))
#
# print("die", round((die-die_pl)/total*100,6))
#
# print((die-die_pl))
#
# print("den M", round(denM/total*100,6))
#
# print("der M", round(derM/total*100,6))
#
# print("das", round(das/total*100,6))
#
# print("d' pl", round(d_pl/total*100,6))
#
# print("die pl", round(die_pl/total*100,6))
#
# print("der", round((der-derM)/total*100,6))
#
# print(der-derM)
#
# print("dem", round(dem/total*100,6))
#
# print("den", round((den-denM)/total*100,6))
#
# print((den-denM))
#
# print("des", round(des/total*100,6))
#
# print("d's", round(ds/total*100,6))
#
# print("DS", round((des+ds)/total*100,6))
# #
# print()
# print('TOTAL')
# print(round(d/total*100,6)+round(die/total*100,6)+round(der/total*100,6)+round(dem/total*100,6)+round(den/total*100,6)+round(des/total*100,6)+round(ds/total*100,6))

# # print()
# print('TOTAL DATIVE')
# # #
# print(round((der-derM)/total*100,6)+round(dem/total*100,6)+round((den-denM)/total*100,6))

D_sg = (der-derM)+dem
D_pl = den-denM

NA_sg = (d-d_pl)+(die-die_pl)+denM+derM+das
NA_pl = d_pl+die_pl

G_sg = 7
total_cases = D_sg+D_pl+NA_pl+NA_sg+G_sg

# print('Dative sg:\t', D_sg, round(D_sg/total_cases*100, 6))
# print('Dative pl:\t', D_pl, round(D_pl/total_cases*100, 6))
# print('NA sg:\t', NA_sg, round(NA_sg/total_cases*100, 6))
# print('NA pl:\t', NA_pl, round(NA_pl/total_cases*100, 6))
# print('Genitive sg:\t', G_sg, round(G_sg/total_cases*100, 6))


singulars = D_sg+NA_sg+G_sg
plural_names = D_pl+NA_pl

# print(singulars, round(singulars/total_cases*100,6))
# print(plural_names, round(plural_names/total_cases*100, 6))




# print(round(8.8888,3))


des_without_rue = 134

# print(der+dem) # 30121
#
# print(der/(der+dem)*100) # 75.22326615982206
#
# print(dem/(der+dem)*100) # 24.77673384017795





# almost no genetive!

# 'HersbergerTeil des Marscherwaldes', 'section': 'Marscherwald', 'a\\textsubscript{p}',
# 'Zittiger Teil des Marscherwaldes', 'section': 'Marscherwald',  'a\\textsubscript{p}',
# 'Rippiger Teil des Marscherwaldes', 'section': 'Marscherwald',  'a\\textsubscript{p}',
# 'Hemstaler Teil des Marscherwaldes', 'section': 'Marscherwald','a\\textsubscript{p}',

# # tëscht der Schock', 'section': 'Eischen', 'adm_comm': 'Habscht', 'corpus': 's\\textsubscript{n}'
# tëscht der Haart', 'section': 'Mertzig', 'adm_comm': 'Mertzig', 'corpus': 's\\textsubscript{n}',
# Pesch zwischen der Syr und Groiff', 'section': 'Oetrange', 'adm_comm': 'Contern', 'corpus': 'a'