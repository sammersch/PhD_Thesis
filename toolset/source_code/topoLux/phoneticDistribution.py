import re
# from MicroTopoLoadAllData import microTopoAll
from act_actuel_load import act_actu_dict, up_counter
# from AllLoader import all_loader
from corpus_load import corpus
from unique_list import UniQ


signs = ['R', 'o', 'm', 'e', 'n', 'b', 'ü', 's', 'c', 'h', 'i', ' ', 'J', 'k', 'M', 'l', 'u', 'r', 'D', 'd', 'w', 'g', 'H', 'a', 'E', 't', 'W', 'K', 'f', 'B', 'ö', 'z', 'G', 'L', 'S', 'p', 'é', 'C', 'à', 'Z', 'ë', 'ä', 'v', "'", 'A', 'P', 'I', 'F', 'U', 'y', 'T', 'O', 'N', 'Q', 'Ä', '-', 'Í', 'V', 'j', 'Ë', '2', 'x', 'q', '1', 'è', '.', 'ô', 'ê', '3', 'Ì', 'å', 'û', 'É', '(', ')', 'ï', 'ç', 'â', 'Å', 'Y', 'X', 'Û', '/', '&', 'Ö', 'Ü', 'Ç', 'Ô', 'À', 'ß', 'ú']
# there 91 signs

signs_vowel = ['o', 'e', 'ü', 'i', 'u', 'a', 'E', 'ö', 'é', 'à', 'ë', 'ä', 'A', 'I', 'U', 'y', 'O', 'Ä', 'Ë', 'è', 'ô', 'ê', 'Ì', 'å', 'û', 'É', 'ï', 'â', 'Å', 'Y', 'Û', 'Ü', 'Ö', 'À', 'Ô', 'ú']
signs_extra = []
signs_weird = []
signs_consonants = ['R', 'o', 'm', 'e', 'n', 'b', 'ü', 's', 'c', 'h', 'i', 'J', 'k', 'M', 'l', 'u', 'r', 'D', 'd', 'w', 'g', 'H', 'a', 'E', 't', 'W', 'K', 'f', 'B', 'ö', 'z', 'G', 'L', 'S', 'p', 'é', 'C', 'à', 'Z', 'ë', 'ä', 'v', "'", 'A', 'P', 'I', 'F', 'U', 'y', 'T', 'O', 'N', 'Q', 'Ä', '-', 'Í', 'V', 'j', 'Ë', '2', 'x', 'q', '1', 'è', '.', 'ô', 'ê', '3', 'Ì', 'å', 'û', 'É', '(', ')', 'ï', 'ç', 'â', 'Å', 'Y', 'X', 'Û', '/', '&', 'Ü', 'Ö', '’', '‘', '0', 'À', 'Ç', 'Ô', '`', 'ß', 'ú']

signs_lower = ['r', 'o', 'm', 'e', 'n', 'b', 'ü', 's', 'c', 'h', 'i', ' ', 'j', 'k', 'l', 'u', 'd', 'w', 'g', 'a', 't', 'f', 'ö', 'z', 'p', 'é', 'à', 'ë', 'ä', 'v', "'", 'y', 'q', '-', 'í', '2', 'x', '1', 'è', '.', 'ô', 'ê', '3', 'ì', 'å', 'û', '(', ')', 'ï', 'ç', 'â', '/', '&', 'ß', 'ú']
# there 51 signs
signs_vowel_lower = ['o', 'e', 'ü', 'i', 'u', 'a', 'ö', 'é', 'à', 'ë', 'ä', "'", 'y', '-', 'í', 'è', '.', 'ô', 'ê', 'ì', 'å', 'û', 'ï', 'â', 'ú']



# print(''.join(signs_vowel_lower))
# oeüiuaöéàëä'y-íè.ôêìåûïâú






def vowel_clusters(input_string): # code from phonsearch project
    #  returnsstring with any vowel replaced by '0'. aeiouéëèäüöíìïàáòóùú
    # v = re.compile('[\']*[oeüiuaöéàëäyíèôêìåûïâú]+[\']*[j]*[oeüiuaöéàëäyíèôêìåûïâú]*[\']*[j]*[h]*[oeüiuaöéàëäyíèôêìåûïâú]*', re.I)
    v = re.compile('[\']*[oeüiuaöéàëäyíèôêìåûïâú]+[\']*[j]*[oeüiuaöéàëäyíèôêìåûïâú]*[h]*', re.I)
    return v.findall(input_string)

# print(vowel_clusters('fr\'enerooderuechterhaffenbeerg'))

def consonant_clusters(input_string): # code from phonsearch project
    c = re.compile('[bcdfghjklmnpqrstvwxz]+', re.I)
    return c.findall(input_string)

# print(consonant_clusters('fräechenhaamentraditionnsky'))

def vowel_remove(input_string): # removes vowel clusters
    pass

def vowel_length_query(input_string):
    return len(vowel_clusters(input_string))

def grapheme_query_vowel(grapheme):
    results = []
    # for item in all_loader:
    for item in corpus:
        queryList = item['name'].lower().split(' ')
        for jtem in queryList:
            for htem in vowel_clusters(jtem):
                if grapheme.lower() == htem.lower():
                    results.append([htem, jtem, item['name'], item['section'], item['adm_comm'], item['corpus']])
    return results

# print(*grapheme_query_vowel('a'), sep='\n')


def grapheme_query_vowelUNIQ(grapheme):
    results = []
    # for item in all_loader:
    for item in UniQ:
        queryList = item.lower().split(' ')
        for jtem in queryList:
            for htem in vowel_clusters(jtem):
                if grapheme.lower() == htem.lower():
                    results.append([htem, jtem, item])
    return results



def grapheme_query_v_all(grapheme, syllable_count, place): # apparently works now, put not idiot proof. 'u' works anyway, 'p' of course only with a a word of two syllables, ..., scratch that, made it idiot proof now, as long as you enter one of the correct values.
    # grapheme needs string input
    # syllable_count needs numerical input, starting from 1 (no 0), from 1 to 8.
    # place is querying for ultima ('u'), penultima ('p') and  antepenultima ('a').

    results = []

    # for item in all_loader:
    for item in corpus:
        queryList = item['name'].lower().split(' ')
        for jtem in queryList:
            if vowel_length_query(jtem) == syllable_count:
                if syllable_count == 0:
                    syllable_count = 1
                if syllable_count > 8:
                    syllable_count = 8
                if syllable_count == 1:
                    place = 'u'
                if syllable_count == 2:
                    if place == 'a':
                        place = 'p'
                if place not in ['u', 'p', 'a']:
                    place = 'u'
                # print(jtem, item['name'])
                for htem in vowel_clusters(jtem):
                    if grapheme.lower() == htem.lower():
                        # print(grapheme, jtem, item['name'])
                        if place == 'u':
                            if grapheme == vowel_clusters(jtem)[-1]:
                                # print(grapheme, 'u', jtem, item['name'])
                                extraString = '\emph{' + item['name'] + '} (' + item['section'].capitalize() + ')'
                                results.append([place, grapheme, jtem, item['name'], item['section'].capitalize(), item['adm_comm'].capitalize(), item['corpus'], extraString])
                        elif place == 'p':
                            if grapheme == vowel_clusters(jtem)[-2]:
                                # print(grapheme, 'p', jtem, item['name'])
                                extraString = '\emph{' + item['name'] + '} (' + item['section'].capitalize() + ')'
                                results.append([place, grapheme, jtem, item['name'], item['section'].capitalize(), item['adm_comm'].capitalize(), item['corpus'], extraString])
                        else:
                            if grapheme == vowel_clusters(jtem)[-3]:
                                # print(grapheme, 'a', jtem, item['name'])
                                extraString = '\emph{'+item['name']+'} ('+item['section'].capitalize()+')'
                                results.append([place, grapheme, jtem, item['name'], item['section'].capitalize(), item['adm_comm'].capitalize(), item['corpus'], extraString])
            else:
                pass
    return results


def grapheme_query_v_allUNIQ(grapheme, syllable_count, place): # apparently works now, put not idiot proof. 'u' works anyway, 'p' of course only with a a word of two syllables, ..., scratch that, made it idiot proof now, as long as you enter one of the correct values.
    # grapheme needs string input
    # syllable_count needs numerical input, starting from 1 (no 0), from 1 to 8.
    # place is querying for ultima ('u'), penultima ('p') and  antepenultima ('a').

    results = []

    # for item in all_loader:
    for item in UniQ:
        queryList = item.lower().split(' ')
        for jtem in queryList:
            if vowel_length_query(jtem) == syllable_count:
                if syllable_count == 0:
                    syllable_count = 1
                if syllable_count > 8:
                    syllable_count = 8
                if syllable_count == 1:
                    place = 'u'
                if syllable_count == 2:
                    if place == 'a':
                        place = 'p'
                if place not in ['u', 'p', 'a']:
                    place = 'u'
                # print(jtem, item['name'])
                for htem in vowel_clusters(jtem):
                    if grapheme.lower() == htem.lower():
                        # print(grapheme, jtem, item['name'])
                        if place == 'u':
                            if grapheme == vowel_clusters(jtem)[-1]:
                                # print(grapheme, 'u', jtem, item['name'])
                                extraString = '\emph{' + item + '} (' + item + ')'
                                results.append([place, grapheme, jtem, item, item.capitalize(), item.capitalize(), item, extraString])
                        elif place == 'p':
                            if grapheme == vowel_clusters(jtem)[-2]:
                                # print(grapheme, 'p', jtem, item['name'])
                                extraString = '\emph{' + item + '} (' + item + ')'
                                results.append([place, grapheme, jtem, item, item, item, item, extraString])
                        else:
                            if grapheme == vowel_clusters(jtem)[-3]:
                                # print(grapheme, 'a', jtem, item['name'])
                                extraString = '\emph{'+item+'} ('+item+')'
                                results.append([place, grapheme, jtem, item, item, item, item, extraString])
            else:
                pass
    return results


def graph_vowel_pretty_print(grapheme, syllable_count, place):
    print(*sorted(grapheme_query_v_all(grapheme, syllable_count, place)), sep='\n')

def graph_vowel_pretty_printUNIQ(grapheme, syllable_count, place):
    print(*sorted(grapheme_query_v_allUNIQ(grapheme, syllable_count, place)), sep='\n')

def grapheme_query_v_UPA(grapheme, place):
    # grapheme needs string input
    # place is querying for ultima ('u'), penultima ('p') and  antepenultima ('a').
    results = []
    # for item in all_loader:
    for item in corpus:
        queryList = item['name'].lower().split(' ')
        for jtem in queryList:
            if place not in ['u', 'p', 'a']:
                place = 'u'
            for htem in vowel_clusters(jtem):
                if grapheme.lower() == htem.lower():
                    # print(grapheme, jtem, item['name'])
                    if place == 'u':
                        if grapheme == vowel_clusters(jtem)[-1]:
                            # print(grapheme, 'u', jtem, item['name'])
                            extraString = '\emph{' + item['name'] + '} (' + item['section'].capitalize() + ')'
                            results.append([place, grapheme, jtem, item['name'], item['section'].capitalize(), item['adm_comm'].capitalize(), item['corpus'], extraString])
                    elif place == 'p':
                        if len(vowel_clusters(jtem)) > 1:
                            if grapheme == vowel_clusters(jtem)[-2]:
                                # print(grapheme, 'p', jtem, item['name'])
                                extraString = '\emph{' + item['name'] + '} (' + item['section'].capitalize() + ')'
                                results.append([place, grapheme, jtem, item['name'], item['section'].capitalize(), item['adm_comm'].capitalize(), item['corpus'], extraString])
                    else:
                        if len(vowel_clusters(jtem)) > 2:
                            if grapheme in vowel_clusters(jtem)[:-2]:
                                # print(grapheme, 'a', jtem, item['name'])
                                extraString = '\emph{'+item['name']+'} ('+item['section'].capitalize()+')'
                                results.append([place, grapheme, jtem, item['name'], item['section'].capitalize(), item['adm_comm'].capitalize(), item['corpus'], extraString])
            else:
                pass
    return results

def grapheme_query_v_UPA_UNIQ(grapheme, place):
    # grapheme needs string input
    # place is querying for ultima ('u'), penultima ('p') and  antepenultima ('a').
    results = []
    # for item in all_loader:
    for item in UniQ:
        queryList = item.lower().split(' ')
        for jtem in queryList:
            if place not in ['u', 'p', 'a']:
                place = 'u'
            for htem in vowel_clusters(jtem):
                if grapheme.lower() == htem.lower():
                    # print(grapheme, jtem, item['name'])
                    if place == 'u':
                        if grapheme == vowel_clusters(jtem)[-1]:
                            # print(grapheme, 'u', jtem, item['name'])
                            extraString = '\emph{' + item + '} (' + item.capitalize() + ')'
                            results.append([place, grapheme, jtem, item, item, item, item, extraString])
                    elif place == 'p':
                        if len(vowel_clusters(jtem)) > 1:
                            if grapheme == vowel_clusters(jtem)[-2]:
                                # print(grapheme, 'p', jtem, item['name'])
                                extraString = '\emph{' + item + '} (' + item + ')'
                                results.append([place, grapheme, jtem, item, item, item, item, extraString])
                    else:
                        if len(vowel_clusters(jtem)) > 2:
                            if grapheme in vowel_clusters(jtem)[:-2]:
                                # print(grapheme, 'a', jtem, item['name'])
                                extraString = '\emph{'+item+'} ('+item+')'
                                results.append([place, grapheme, jtem, item, item, item, item, extraString])
            else:
                pass
    return results

def graphemeUPA_count(grapheme, place):
    return len(grapheme_query_v_UPA(grapheme, place))

def graphemeUPA_countUNIQ(grapheme, place):
    return len(grapheme_query_v_UPA_UNIQ(grapheme, place))

def vowel_grapheme_count(grapheme):
    results = 0
    # for item in all_loader:
    for item in corpus:
        queryList = item['name'].lower().split(' ')
        for jtem in queryList:
            for htem in vowel_clusters(jtem):
                if grapheme.lower() == htem.lower():
                    results += 1
    return results



def vowel_grapheme_countUNIQ(grapheme):
    results = 0
    # for item in all_loader:
    for item in UniQ:
        queryList = item.lower().split(' ')
        for jtem in queryList:
            for htem in vowel_clusters(jtem):
                if grapheme.lower() == htem.lower():
                    results += 1
    return results



def print_all_numbers(grapheme):
    return [vowel_grapheme_count(grapheme), graphemeUPA_count(grapheme, 'u'), len(sorted(grapheme_query_v_all(grapheme, 1, 'u'))), graphemeUPA_count(grapheme, 'p'), graphemeUPA_count(grapheme, 'a')]

def print_all_numbers_grapheme_index(grapheme):
    return [grapheme, vowel_grapheme_count(grapheme), graphemeUPA_count(grapheme, 'u'), len(sorted(grapheme_query_v_all(grapheme, 1, 'u'))), graphemeUPA_count(grapheme, 'p'), graphemeUPA_count(grapheme, 'a')]

def print_all_numbersUNIQ(grapheme):
    return [vowel_grapheme_countUNIQ(grapheme), graphemeUPA_countUNIQ(grapheme, 'u'), len(sorted(grapheme_query_v_allUNIQ(grapheme, 1, 'u'))), graphemeUPA_countUNIQ(grapheme, 'p'), graphemeUPA_countUNIQ(grapheme, 'a')]

def print_all_numbersMEAN(grapheme):
    return [(vowel_grapheme_count(grapheme) + vowel_grapheme_countUNIQ(grapheme))/2, (graphemeUPA_count(grapheme, 'u') + graphemeUPA_countUNIQ(grapheme, 'u'))/2, (len(sorted(grapheme_query_v_all(grapheme, 1, 'u')))+len(sorted(grapheme_query_v_allUNIQ(grapheme, 1, 'u'))))/2, (graphemeUPA_count(grapheme, 'p')+graphemeUPA_countUNIQ(grapheme, 'p'))/2, (graphemeUPA_count(grapheme, 'a')+graphemeUPA_countUNIQ(grapheme, 'a'))/2]

def print_all_numbersMINoverMAX(grapheme):
    total_count = [print_all_numbersUNIQ(grapheme)[0] / print_all_numbers(grapheme)[0] if print_all_numbers(grapheme)[0] > 0 else 'x']
    ultima = [print_all_numbersUNIQ(grapheme)[1] / print_all_numbers(grapheme)[1] if print_all_numbers(grapheme)[1] > 0 else 'x']
    mono = [print_all_numbersUNIQ(grapheme)[2] / print_all_numbers(grapheme)[2] if print_all_numbers(grapheme)[2] > 0 else 'x']
    penult = [print_all_numbersUNIQ(grapheme)[3] / print_all_numbers(grapheme)[3] if print_all_numbers(grapheme)[3] > 0 else 'x']
    antepenult = [print_all_numbersUNIQ(grapheme)[4] / print_all_numbers(grapheme)[4] if print_all_numbers(grapheme)[4] > 0 else 'x']
    return [grapheme, total_count[0], ultima[0], mono[0], penult[0], antepenult[0]]

def panMINoverMAXpprint(grapheme):
    print(', '.join(map(str,print_all_numbersMINoverMAX(grapheme))))

# print(panMINoverMAXpprint('â'))

def pAn_latex(grapheme):
    return "The grapheme manifests itself in \\numprint{" + str(print_all_numbers(grapheme)[0]) + "} instances; \\numprint{" + str(print_all_numbers(grapheme)[1]) + "} times in ult (of which \\numprint{" + str(print_all_numbers(grapheme)[2]) + "} are monosyllabics), \\numprint{" + str(print_all_numbers(grapheme)[3]) + "} in penult and \\numprint{" + str(print_all_numbers(grapheme)[4]) + "} in antepenult positions."



def pAn_latexUNIQ(grapheme):
    return "The grapheme manifests itself in \\numprint{" + str(print_all_numbers(grapheme)[0]) + "} instances; \\numprint{" + str(print_all_numbers(grapheme)[1]) + "} times in ult (of which \\numprint{" + str(print_all_numbers(grapheme)[2]) + "} are monosyllabics), \\numprint{" + str(print_all_numbers(grapheme)[3]) + "} in penult and \\numprint{" + str(print_all_numbers(grapheme)[4]) + "} in antepenult positions."

def categories(grapheme):
    result = []
    count = print_all_numbers(grapheme)[0]
    if count < 10:
        result.append('category I')
    elif count in range(11,101):
        result.append('category II')
    elif count in range(101,1000):
        result.append('category III')
    elif count in range(1001,10000):
        result.append('category IV')
    elif count in range(10001,100000):
        result.append('category V')
    elif count > 100000:
        result.append('category VI')
    return result



def pAn_latex_cat(grapheme):
    return "The "+ str(categories(grapheme)[0]) + " grapheme manifests itself in \\numprint{" + str(print_all_numbers(grapheme)[0]) + "} instances; \\numprint{" + str(print_all_numbers(grapheme)[1]) + "} times in ult (of which \\numprint{" + str(print_all_numbers(grapheme)[2]) + "} are monosyllabics), \\numprint{" + str(print_all_numbers(grapheme)[3]) + "} in penult and \\numprint{" + str(print_all_numbers(grapheme)[4]) + "} in antepenult positions."


# graphemes = ["ëi", "i'", "ia", "ie", "ih", "ii", "ij", "iu", "iä", "iè", "ié", "ië", "iö", "ïh", "o'", "oa", "oe", "oh", "oi", "oo", "ou", "oy", "oè", "oé"]
# graphemes = ["oë", "ôh'", "ö'", "öe", "öh", "u'", "ua", "ue", "uh", "ui", "uo", "uu", "uä", "ué", "uë", "uö", "üe", "üh", "ye"]
# graphemes = ["yä", "'eh''", "'ou", "'uo'", "aah", "aee", "aeh", "aei", "aeu", "aey", "aie", "ao'", "aoe", "aou", "au'", "aue", "auh", "aui", "e'h"]
# graphemes = ["e'i", "eae", "eee", "eeh", "ei'", "eih", "eij", "i'e", "i'è", "i'é", "ie'", "ieh", "iei", "iie", "ije", "ioe", "ièh", "iéh", "o'e"]
# graphemes = ["o'h", "o'i", "o'u", "oe'", "oeh", "oei", "oi'", "oie", "oih", "ooe", "ooh", "oou", "ou'", "oua", "oue", "ouh", "oui", "oéh", "u'a"]
graphemes = ["uoe"]
# graphemes = ["e'ih", "i'eh", "ie'e", "ie'h", "ieou", "oueh", "u'eh", "uo'h"]


for grapheme in graphemes:
    print(grapheme)
    print(pAn_latex(grapheme))
    print()



def consonant_start(consonant_cluster):
    c = consonant_cluster
    results = []
    for item in corpus:
        for j in item['name'].split():
            if j.lower().startswith(c):
                results.append([c,j,item['name'],item['section'],item['corpus']])
    return results

def consonant_end(consonant_cluster):
    c = consonant_cluster
    results = []
    for item in corpus:
        for j in item['name'].split():
            if j.lower().endswith(c):
                results.append([c,j,item['name'],item['section'],item['corpus']])
    return results

def consonant_inside(consonant_cluster):
    c = consonant_cluster
    results = []
    for item in corpus:
        for j in item['name'].lower().split():
            if c in j:
                # if j[0] != c and j[-1] != c:
                if j.lower().startswith(c) != True and j.lower().endswith(c) != True:

                    results.append([c,j,item['name'],item['section'],item['corpus']])
    return results

def query_c_contextt(c, v, direction):
    results = []
    for item in consonant_inside(c):
        pre = item[1].split(c)[0]
        fol = item[1].split(c)[1]
        if direction == 'pre':
            if v in pre[-1]:
                results.append([pre, c, fol, item[-4], item[-3], item[-2], item[-1]])
        elif direction == 'fol':
            if v in fol[0]:
                results.append([pre, c, fol, item[-4], item[-3], item[-2], item[-1]])
    return results



Da_list = []
# for item in all_loader:
for item in corpus:
    for v in vowel_clusters(item['name'].lower()):
        # if len(v) == 4:
        #     # print(v, vowel_clusters(item['name'].lower()), item['name'], item['corpus'])
        #     # print(v, item['name'], item['corpus'])
        #     continue
        if v not in Da_list:
            Da_list.append(v)

# print(len(Da_list))
# print(sorted(Da_list))

def grapheme_count_all_export(list_of_graphemes):
    print('GRAPHEME, TOTAL, ULTIMA, MONOSYLLABICS, PENULT, ANTEPENULT')
    for item in sorted(list_of_graphemes):
        # print(print_all_numbers_grapheme_index(item))
        print(', '.join(map(str, print_all_numbers_grapheme_index(item))))



# print(print_all_numbers("'a"))
# grapheme_count_all_export(Da_list)
# for item in sorted(Da_list):
#     print(item, vowel_grapheme_count(item))

# print(print_all_numbers('a'))


l1 = []
l2 = []
l3 = []
l4 = []
lplus = []

for item in sorted(Da_list):
    # print('\\paragraph{' + item + '}')
    if len(item) == 1:
        l1.append(item)
    elif len(item) == 2:
        l2.append(item)
    elif len(item) == 3:
        l3.append(item)
    elif len(item) == 4:
        l4.append(item)
    elif len(item) > 4:
        lplus.append(item)
#
# for item in l1:
#     print('\\paragraph{\\textless ' + item + '\\textgreater}')

# print(len(Da_list))


c_list = []
for item in corpus:
    for c in consonant_clusters(item['name'].lower()):
        if c not in c_list:
            c_list.append(c)

# print(*sorted(c_list), sep='\n')
# print(len(c_list))
lengths = []


c1 = []
c2 = []
c3 = []
c4 = []
c5 = []
c6 = []
c7 = []
cplus = []

for item in c_list:
    if len(item) == 1:
        c1.append(item)
    if len(item) == 2:
        c2.append(item)
    if len(item) == 3:
        c3.append(item)
    if len(item) == 4:
        c4.append(item)
    if len(item) == 5:
        c5.append(item)
    if len(item) == 6:
        c6.append(item)
    if len(item) == 7:
        c7.append(item)
    if len(item) > 7:
        cplus.append(item)

# print(c2)
querY = []
for item in c3:
    # if item[0] != item[1]:
    if 'ss' in item:
        querY.append(item)

# print(querY)
c = "uie"

# print([c+"ch" for c in 'bcdfghjklmnpqrstvwxz'])
# onset_count = 0
# midle_count = 0
# offset_count = 0
# for c in [c+"g" for c in 'bcdfghjklmnpqrstvwxz']:
#     onset_count += len(consonant_start(c))
#     # print(c)
#     print(c, len(consonant_start(c)), len(consonant_inside(c)), len(consonant_end(c)))
#     midle_count += len(consonant_inside(c))
#     # print(c)
#     # print(len(consonant_inside(c)))
#     offset_count += len(consonant_end(c))
#     # print(c)
#     # print(len(consonant_end(c)))
# print(onset_count)
# print(midle_count)
# print(offset_count)
# print(len(consonant_start(c)))
# print(len(consonant_inside(c)))
# print(len(consonant_end(c)))

# print(*consonant_start(c), sep='\n')

# print(*consonant_inside(c), sep='\n')

# print(*consonant_end(c), sep='\n')
# ghgh_count = 0
# for j in consonant_end(c):
#     if j[1].lower() == 'ob':
#         ghgh_count += 1

# print(ghgh_count)
# print(*query_c_contextt(c, 'e', 'fol'), sep='\n')


# print(len(consonant_start(c)))
# print(len(consonant_inside(c)))
# print(len(consonant_end(c)))
#
# print('The grapheme \guilsinglleft ' + c + '\guilsinglright\ occurs \\numprint{' + str(len(consonant_start(c))) + '} times at word onset, \\numprint{' + str(len(consonant_inside(c))) + '} times inside the word and \\numprint{' + str(len(consonant_end(c))) + '} times in word offset.')

# make if loop for length of vowel graph, index() gives you beginning of string, so you have to add 1
# per character that is more than 1 in graph.
# print(test_string.index('ue'))
# print(test_string[2])
#
# print()
#
# pre = test_string.index('ue') - 1
# mid = test_string.index('ue') + 1
# end = test_string.index('ue') + 1 + 1
#
# print(test_string[pre], test_string[mid], test_string[end])
#
# for v in sorted(vowel_list):
#     if len(v) == 1:
#         pre = test_string.index(v) - 1
#         vv = test_string.index(v)
#         end = test_string.index(v) + 1
#         print(test_string.index(vv-1) + test_string.index(vv-2), v, test_string.index(vv+1) + test_string.index(vv+2))
#     elif len(v) == 2:
#         pass
#     elif len(v) == 3:
#         pass
#     elif len(v) == 4:
#         pass
#
# return_list = []
# plural_list = []
# for item in microTopoAll:
#     lemma_word = item['name'].split()[-1].lower()
#     query = teststring.lower()
#     length = len(vowel_clusters(query))
#     if length == 1: # alternatively I could write an algorithm that specificly hands out the numers and I do not need
#         # to specify the length. So, if length = 3, that means I have a list of three vowel clusters, that are in the
#         # order that they were searched, hence len(vowel_clusters('Bruechtebaach')) = 3
#         # and vowel_clusters('Bruechtebaach') == ['ue', 'e', 'aa']. index[0] == 'ue' and so on.
#         # so, to access the specific clusters, I need:
#         # vowel_clusters('Bruechtebaach')[len(vowel_clusters('Bruechtebaach')) -1]
#         # better:
#         # vowel_clusters('Bruechtebaach')[length -1], and then length + 1
#         strip_word = query.lstrip(vowel_clusters(query)[0])
#         for v in vowel_list:
#             if v + strip_word == lemma_word:
#                 if lemma_word not in return_list:
#                     return_list.append(lemma_word)
# for item in return_list:
#     for jtem in microTopoAll:
#         lemma_word2 = jtem['name'].split()[-1].lower()
#         if item + 'en' == lemma_word2:
#             print(lemma_word2)

# for v in vowel_list:
#     for item in microTopoAll:
#         lemma_word = item['name'].split()[-1].lower()
#         if lemma_word.startswith(v + 'cht' + 'el'):
#             print(lemma_word)

'''Plurals:
So, with the example 'uecht' I have the plurals 'en' at the word boundary, or in front of another vowel or 'h' 
and 'e' in front of consonants that are not 'h' 
I got 'el' in 'aechtel', but is it a derivation of 'uecht'? Also in 'echtelgesbaum', hapax.

As derivation I have 'chen', and I know about 'gen' in other instances.
If I put everything together in a dict?
In any case, I would need to query first for the derivations and only then for the plurals, in order to catch
everything.
'''

morpho_dict = {'derivations':{},
               'plurals': [['en'], ['e']]}

def query_catcher(input_string):
    input_string = input_string.lower()
    results = []
    # loop_count = 0
    # while loop_count <= len(vowel_clusters(input_string)):
    #     # do something with query here, the idea was to look for alternations in all different query directions for
    #     # vowel clusters.
    #     loop_count += 1
    rest = input_string.lstrip(str(vowel_clusters(input_string)))
    for v in vowel_list:
        for item in microTopoAll:
            ref_name = item['name'].split()[-1].lower()
            if v + rest == ref_name:
                if ref_name not in results:
                    results.append(ref_name)
    for v in vowel_list:
        for item in microTopoAll:
            ref_name = item['name'].split()[-1].lower()
            # if v + rest + 'en' == ref_name:
            #     if ref_name not in results:
            #         results.append(ref_name)
            if str([v + rest + 'e' + c for c in ' nwhklmnpqrstbcdfg']) in ref_name:
                if ref_name not in results:
                    results.append(ref_name)
    return results

# print(query_catcher('uecht'))



# print('ue' + '-' + 'cht' + '-' + 'e' + str(''.join([c for c in ' nwhklmnpqrstbcdfg'])))
# print(['ue' + '-' + 'cht' + '-' + 'e' + '-' + n for n in ' nwhklmnpqrstbcdfg'])

def alterno(input_string): # works for monosyllabics, needs at least a vowel(cluster)
    input_string = input_string.lower()
    results = []
    vowel = vowel_clusters(input_string)
    c_clusters = input_string.split(vowel_clusters(input_string)[0])
    return c_clusters[0], vowel[0], c_clusters[1]


# print(vowel_clusters('gruechte'))
# print('gruecht'.split(vowel_clusters('gruecht')[0]))
# print(alterno('te'))

# for v in sorted(vowel_list):
#     if len(v) == 4:
#         print(r'\subparagraph{' + v + '}')
    # for item in microTopoAll:
    #     if v + 'h' in item['name']:
    #         print(v + 'h', ':', '\t', item['name'])

signs = ['R', 'o', 'm', 'e', 'n', 'b', 'ü', 's', 'c', 'h', 'i', ' ', 'J', 'k', 'M', 'l', 'u', 'r', 'D', 'd', 'w', 'g', 'H', 'a', 'E', 't', 'W', 'K', 'f', 'B', 'ö', 'z', 'G', 'L', 'S', 'p', 'é', 'C', 'à', 'Z', 'ë', 'ä', 'v', "'", 'A', 'P', 'I', 'F', 'U', 'y', 'T', 'O', 'N', 'Q', 'Ä', '-', 'Í', 'V', 'j', 'Ë', '2', 'x', 'q', '1', 'è', '.', 'ô', 'ê', '3', 'Ì', 'å', 'û', 'É', '(', ')', 'ï', 'ç', 'â', 'Å', 'Y', 'X', 'Û', '/', '&', 'Ü', 'Ö', '’', '‘', '0', 'À', 'Ç', 'Ô', '`']


#
# for item in sorted(Da_list):
#     # print(item)
#     print(item, print_all_numbers(item)[0])
#


# looking_for = "euhaue"
# positio = 'p'

# print(print_all_numbers(looking_for))
# print(print_all_numbersUNIQ(looking_for))
# # print(print_all_numbersMEAN(looking_for))
# # print(print_all_numbersMINoverMAX(looking_for))

# print(print_all_numbersMINoverMAX(looking_for))
# panMINoverMAXpprint(looking_for)
#
# for item in sorted(Da_list):
#     # print(item)
#     panMINoverMAXpprint(item)
# looking_for = "ä"
# print(pAn_latex(looking_for))
#
# print(*sorted(grapheme_query_v_all(looking_for, 2, positio)), sep='\n')
# print(vowel_grapheme_count(looking_for))

# print('------------------------------------------------------------------------------------------')
# print(*sorted(grapheme_query_v_UPA(looking_for, positio)), sep='\n')
# print(graphemeUPA_count(looking_for, positio))
