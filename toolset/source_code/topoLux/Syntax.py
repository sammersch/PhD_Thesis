import json, os, re
from MicroTopoLoad import microToponyms
# from MicroTopoLoadAllData import microTopoAll
from corpus_load import corpus_syntax
from phoneticDistribution import vowel_clusters

# for item in corpus_syntax:
#     if 'sich' in item['name'].lower():
#         print(item['name'], item['section'], item['corpus'])

def get_corpora(topo_dict): # retrives a list of all corpora
    corpus_list = []
    for item in topo_dict:
        if item['corpus'] not in corpus_list:
            corpus_list.append(item['corpus'])
    return corpus_list

def get_sections(topo_dict):
    section_list = []
    for item in topo_dict:
        if item['section'] not in section_list:
            section_list.append(item['section'])
    return section_list

def SyntacticLengths(topo_dict):
    results = []
    for item in topo_dict:
        if item["sequence_length"] not in results:
            results.append(item['sequence_length'])
    return sorted(results)


def SyntacticLengthsPPrint(topo_dict):
    print(*SyntacticLengths(topo_dict), sep='\n')



def SynLenBySection(topo_dict, section):
    results = []
    for item in topo_dict:
        if item['section'] == section:
            if item['sequence_length'] not in results:
                results.append(item['sequence_length'])
    return sorted(results)

# print(*get_corpora(corpus_syntax), sep='\n')



def get_n_count_by_corpus(topo_dict, corpus, n):
    results = []
    for item in topo_dict:
        if item['corpus'] == corpus:
            if item['sequence_length'] == n:
                results.append(item['name'])
    return len(results)


def all_counts_by_corpus(topo_dict):
    results = []
    for corpus in get_corpora(topo_dict):
        for n in SyntacticLengths(topo_dict):
            roffeloffel = ','.join([corpus, str(n), str(get_n_count_by_corpus(topo_dict, corpus, n))])
            toelleboele = [corpus, n, get_n_count_by_corpus(topo_dict, corpus, n)]
            results.append(roffeloffel)
    return results

# print(all_counts_by_corpus(corpus_syntax))

def all_counts_by_corpus_pprint(topo_dict):
    print(*all_counts_by_corpus(topo_dict), sep='\n')

# all_counts_by_corpus_pprint(corpus_syntax)





def SynLenByCorpus(topo_dict, corpus_query):
    results = []
    for item in topo_dict:
        if item['corpus'] == corpus_query:
            if item['sequence_length'] not in results:
                results.append(item['sequence_length'])
    return sorted(results)


def SynLenAllSections(topo_dict):
    sections = []
    results = []
    for item in topo_dict:
        if item['section'] not in sections:
            sections.append(item['section'])
    for item in sections:
        results.append([item, SynLenBySection(topo_dict, item)])
    return results

def SynLenAllCorpora(topo_dict):
    corpora = []
    results = []
    for item in topo_dict:
        if item['corpus'] not in corpora:
            corpora.append(item['corpus'])
    for item in corpora:
        results.append([item, SynLenByCorpus(topo_dict, item)])
    return results



# print(*SynLenAllCorpora(corpus_syntax), sep='\n')
# print(*SynLenAllSections(corpus_syntax), sep='\n')





# empty = []
# for item in corpus_syntax:
#     if ';'+item['section']+';'+item['adm_comm']+';' not in empty:
#         empty.append(';'+item['section']+';'+item['adm_comm']+';')
# print(*sorted(empty), sep='\n')




# with open('LenAllSectionsSemiColon.csv', 'w', encoding='utf-8') as dabo:
#     dabo.write('Section, Instances\n')
#     for item in SynLenAllSections(microTopoAll):
#         dabo.write(str(item[0]) + '; ' + str(sorted(item[1])).lstrip('[').rstrip(']') + '\n')
# dabo.close()

# for item in SynLenAllSections(microTopoAll):
#     print(sorted(item[-1])[-1])

def MaxLength(topo_dict):
    return sorted(SyntacticLengths(topo_dict))[-1]


def MinLength(topo_dict):
    return sorted(SyntacticLengths(topo_dict))[0]


def MaxLengthBySection(topo_dict, section):
    return sorted(SynLenBySection(topo_dict, section))[-1]


def MinLengthBySection(topo_dict, section):
    return sorted(SynLenBySection(topo_dict, section))[0]


def MaxLengthAllSections(topo_dict):
    results = []
    for item in SynLenAllSections(topo_dict):
        results.append([item[0], sorted(item[-1])[-1]])
    return results


def MinLengthAllSections():
    results = []
    for item in SynLenAllSections(microTopoAll):
        results.append([item[0], sorted(item[-1])[0]])
    return results


def SyntacticQuery(topo_dict, n): # displays all microtoponyms with a syntactic length n.
    # min = 1, max = 10
    results = []
    for item in topo_dict:
        if item["sequence_length"] == n:
            results.append([item['name'], item['section'], item['corpus']])
    return results






def BiggestToponym(topo_dict):
    pass

def BiggestBySection(topo_dict, section):
    lengths = []
    results_dict = []
    results = []
    for item in topo_dict:
        if item['section'] == section:
            if item['sequence_length'] == MaxLengthBySection(topo_dict, section):
                results_dict.append(dict({'name': item['name'], 'length': len(item['name'])}))
                lengths.append(len(item['name']))
    for item in results_dict:
        if item['length'] == sorted(lengths)[-1]:
                results.append(item['name'])
    return results


def SyntacticQueryPPrint(topo_dict, n):
    print(*SyntacticQuery(topo_dict, n), sep='\n')

# SyntacticQueryPPrint(corpus_syntax, 5)
# print(SyntacticQuery(corpus_syntax, 3)[0:20])
# for item in corpus_syntax:
#     if 'um' in item['name']:
#         print(item)
#     if item['sequence_length'] == 4:
#         if item['name'].split()[0][-1] != 'm':
#             # if item['name'].split()[1][0] != 'd':
#             if item['name'].split()[0][0] == 'u':
#                 print(item)

def SyntacticQuery_ctrl(topo_dict, n): # displays all microtoponyms with a syntactic length n.
    # min = 1, max = 7
    # control version which can specify which dictionary to access.
    results = []
    for item in topo_dict:
        if item["sequence_length"] == n:
            results.append(item['name'])
    return results


def SyntacticQuery_ctrl2(topo_dict, n): # displays all microtoponyms with a syntactic length n.
    # min = 1, max = 7
    # control version which can specify which dictionary to access.
    results = []
    for item in topo_dict:
        if item["sequence_length"] == n:
            results.append(item['name'])
    return results


def HowManyHave(topo_dict, n): # queries for how many items there are with a syntactic length n.
    # min = 1, max = 10
    return len(SyntacticQuery(topo_dict, n))



def SyntacticQuery_by_corpus(topo_dict, n): # displays all microtoponyms with a syntactic length n.
    # min = 1, max = 10
    results = []
    for item in topo_dict:
        if item["sequence_length"] == n:
            results.append(item['name'])
    return results










def get_all_lengthsDICT(topo_dict):
    lengths = []
    for item in topo_dict:
        if item["sequence_length"] not in lengths:
            lengths.append(item["sequence_length"])
    results = []
    for n in sorted(lengths):
        results.append(dict({'length': n,
                             'count': HowManyHave(topo_dict, n)}))
        # results.append([n, HowManyHave(topo_dict, n)])
    return results


def get_all_lengthsLIST(topo_dict):
    lengths = []
    for item in topo_dict:
        if item["sequence_length"] not in lengths:
            lengths.append(item["sequence_length"])
    results = []
    for n in sorted(lengths):
        # results.append(dict({'length': n, 'count': HowManyHave(topo_dict, n)}))
        results.append([n, HowManyHave(topo_dict, n)])
    return results


# print(get_all_lengthsLIST(corpus_syntax))


def HowManyHave_ctrl(topo_dict, n): # queries for how many items there are with a syntactic length n.
    # min = 1, max = 7
    # control version which can specify which dictionary to access.
    return len(SyntacticQuery_ctrl(topo_dict, n))



# should this not be in a module NameStructure? Or call this module that, as the syntax fits into it.

def CharacterLength(n): # querries for absolute character length in a microtoponym (i.e. any character!)
    # minimal length is 3, maximal length is 43. Spaces are not taken into account.
    results = []
    for item in micro_dict:
        if item["character_length"] == n:
            results.append(item["microtoponym"])
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


# print(*nameLookUp_syntax('Wangert', 3), sep='\n')
# print(*nameLookUp_syntax('Bësch', 1), sep='\n')




def HowManyAre_syntax(name, syntactic_length):
    return len(nameLookUp_syntax(name, syntactic_length))

# print(HowManyAre_syntax('Wangert', 3))
# count = 0
# for item in corpus_syntax:
# #     if "et" in item['name'].split(' '):
# #         # if "an" != item['name'].split(' ')[0]:
# #         count += 1
#     if item['sequence_length'] == 5:
#         print(item)
#         # print(count)

def syntax_morpho_query(topo_dict, length): # crossreferences syntactic lengths and syllable cores
    results = []
    for item in topo_dict:
        if item['sequence_length'] == length:
            r1 = [length, len(vowel_clusters(item['name'].split()[-1]))]
            if r1 not in results:
                results.append(r1)
    return results

def syntax_morpho_query_character(topo_dict, length): # crossreferences syntactic lengths and syllable cores
    results = []
    for item in topo_dict:
        if item['sequence_length'] == length:
            r1 = [length, len(item['name'].split()[-1])]
            if r1 not in results:
                results.append(r1)
    return results


# print(sorted(syntax_morpho_query(corpus_syntax, 2)))
# print()
#
# print(sorted(syntax_morpho_query_character(corpus_syntax, 2)))


def syl_core_counter(input_string):
    return [len(vowel_clusters(w)) for w in input_string.split()]

def char_counter(input_string):
    return [len(w) for w in input_string.split()]



def syl_count_all(topo_dict):
    results = []
    for item in topo_dict:
        query = syl_core_counter(item['name'])
        if query not in results:
            results.append(query)
    return results
#
# print(syl_count_all(corpus_syntax))
#
# q_list = [1, 0, 2]
#
# for item in corpus_syntax:
#     if item['sequence_length'] == 3:
#         if syl_core_counter(re.sub('-|St.|ST.|st.|St', '',item['name'])) == q_list:
#             print(item)

def char_count_all(topo_dict):
    results = []
    for item in topo_dict:
        query = char_counter(item['name'])
        if query not in results:
            results.append(query)
    return results

# for l in SyntacticLengths(corpus_syntax):
#     for c in sorted(syl_count_all(corpus_syntax)):
#         if l == len(c):
#             print(*c)
            # print(c)
#             # print(','.join(str(c)))

# for l in SyntacticLengths(corpus_syntax):
#     # print(l)
#     for w in sorted(char_count_all(corpus_syntax)):
#         if l == len(w):
#             print(*w)

# for item in corpus_syntax:
#     if item['sequence_length'] == 2:
#         if len(vowel_clusters(item['name'].split()[-2])) == 0 :
#             print(item)