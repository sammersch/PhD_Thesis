import cologne_phonetics, ngram
from corpus_load import corpus
from collections import Counter
import re
from unidecode import unidecode

vowel_patterns = re.compile('[oeüiuaöéàëäyíèôêìåûïâú]+')

# re.sub(vowel_patterns, '', 'BruechtebAach'.lower())
def simplifier(input_string):
    return re.sub(vowel_patterns, '0', input_string.lower())

lexes = []
for item in corpus:
    lex = item['name'].split(' ')[-1].lower()
    if lex not in lexes:
        lexes.append(lex)

lexes = sorted(lexes)

print(*lexes, sep='\n')
# print()
# print(len(lexes))
# print(lexes)
# print(lexes.index('sports'))
# print(lexes[lexes.index('sports'):])
# print(len(lexes))
# print(len(lexes[lexes.index('sports'):]))

# with open('allnamesEvidenceDict20210514.csv', 'w', encoding='utf-8') as duplo:
#     everything = []
#
#     # for item in corpus:
#         # lex = item['name'].split(' ')[-1].lower()
#         # print(item['name'])
#         # print('\t', lex)
#     counter = len(lexes)
#     for lex in lexes[lexes.index('sports'):]:
#         simple_lex = simplifier(lex)
#
#         all_sim = []
#         comparisons = []
#         all_comp = []
#
#         all_stuff = []
#         print('we are working on corpus item :    ' + lex)
#         print(counter)
#         counter = counter - 1
#         # all_stuff.append([lex])
#         for jtem in corpus:
#             lex2 = jtem['name'].split(' ')[-1].lower()
#             if lex == lex2:
#                 add_up = jtem['name'] + ' (' + jtem['section'] + ') ' + '(' + jtem['corpus'] + ')'
#                 if add_up not in all_stuff:
#                     all_stuff.append(add_up)
#             else:
#                 simple_comp = simplifier(jtem['name'].split(' ')[-1])
#                 if simple_lex == simple_comp:
#                     if lex2 not in all_comp:
#                         all_comp.append(lex2)
#
#                     # add_up = jtem['name'] + ' (' + jtem['section'] + ') ' + '(' + jtem['corpus'] + ')'
#                     # if add_up not in all_stuff:
#                     #     all_stuff.append(add_up)
#         # print(lex)
#         # print(', '.join(all_stuff))
#         # print(', '.join(all_comp))
#
#         duplo.write(lex)
#         duplo.write(';')
#         duplo.write(', '.join(all_stuff))
#         duplo.write(';')
#         duplo.write(', '.join(all_comp))
#         duplo.write('\n')
#     # print(run)
#     # run = run + 1
# duplo.close()

    # everything.append(all_stuff)

    # for jtem in corpus:
    #     lex2 = jtem['name'].split(' ')[-1]
    #     if lex.lower() == lex2.lower():
    #         all_sim.append(lex2)
    #     simple_comp = simplifier(jtem['name'].split(' ')[-1])
    #     if simple_lex in simple_comp:
    #         comparisons.append(simple_comp)
    #         # print('\t\t',jtem['name'])
    # for ktem in comparisons:
    #     for ltem in corpus:
    #         l_comp = simplifier(ltem['name'].split(' ')[-1])
    #         if ktem == l_comp:
    #             all_comp.append([ltem['name']])
    # print(all_comp)

# print(sorted(everything))



han_dict = []
lemma_dict = []


###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################

# print('bein instnce')
# with open('allnamesEvidenceDict20210513BIS.csv', 'r', encoding='utf-8') as hanuta:
#     # hanuta.read()
#     with open('Belegwoerterbuch20210513.tex', 'w', encoding='utf-8') as writer:
#         for lin in hanuta.readlines():
#             han_dict.append(lin)
#             # print(lin)
#             lemma, instances, counter_lemma = lin.split(';')
#
#             writer.write('\entry{')
#             writer.write(lemma)
#             writer.write('}{')
#             writer.write(instances)
#             writer.write('}{')
#             writer.write(counter_lemma.rstrip('\n'))
#             writer.write('}')
#             writer.write('\n\n')
#     writer.close()
# hanuta.close()
        # if lemma.lower().startswith('a'):
        #     print(r'\entry{' + lemma + '}{' + instances + '}{' + counter_lemma + '}')


###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################



ref_list = []
code_only = []
pure_list = []


# for item in corpus:
#     coded = simplifier(item['name'])
#     # print(coded.split())
#     for sequence in coded.split():
#         pure_list.append(sequence[-1])
#         if sequence not in code_only:
#             code_only.append(sequence[-1])
#
#
# # for item in corpus:
# #     coded = cologne_phonetics.encode(item['name'])
# #     for sequence in coded:
# #         pure_list.append(sequence[-1])
# #         if sequence[-1] not in code_only:
# #             code_only.append(sequence[-1])
# #
# #
# #
#
# print(len(code_only))
# print(len(pure_list))
#
#
#
# #
# comp_list = []
#
#
# for item in sorted(code_only):
#     if item == '':
#         continue
#     if len(item) < 2:
#         continue
#     if len(item) > 10:
#         continue
#     for comp in sorted(pure_list):
#         if item in comp:
#             print(item, comp)
#             comp_list.append(str(item) + ',' + str(comp))
#
# # print(Counter(comp_list))
#
# print()
# print(len(comp_list))
#
# MyList = comp_list
# MyFile=open('outputCounterALT.txt','w')
# MyFile.write(str(Counter(MyList)))
# # for element in MyList:
# #      MyFile.write(element)
# #      MyFile.write('\n')
# MyFile.close()

####################################
####################################
### just run the code ##############
####################################
### will take forever ##############
####################################

#
# re.compile('[\']*[oeüiuaöéàëäyíèôêìåûïâú]+[\']*[j]*[oeüiuaöéàëäyíèôêìåûïâú]*[h]*', re.I)
#
# vowel_patterns = re.compile('[oeüiuaöéàëäyíèôêìåûïâú]+')
#
# print(re.findall(vowel_patterns, 'BruechtebAach'.lower()))
#
# print(re.sub(vowel_patterns, '', 'BruechtebAach'.lower()))