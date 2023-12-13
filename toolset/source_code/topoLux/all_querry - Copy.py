import itertools

from unique_list import UniQ
import re
from phoneticDistribution import vowel_clusters, Da_list

from corpus_load import corpus

phoneme_dict_vowel = {'a': ['a', "a'", 'aé', 'ea'],
                'aa': ['a', 'à', 'â', "'a", "a'", 'aa', 'ah', 'ao', 'aah'],
                'e': ['å', 'e', 'é', 'ë', 'eé', 'ëe'],
                'ee': ['ä', 'e', 'è', 'ê', 'ë', "'e", 'ae', 'ay', 'aä', 'aè', 'aé', 'aë'
                       "ä'", 'äe', 'äh', 'äi', 'ää', "e'", 'ea', 'ee', 'eh', 'ey', 'eè', 'eé'
                       "è'", 'èe', 'èh', 'ée', 'éh', 'éi', 'ëe', 'ëh', "'eh", 'aee', 'aeh', 'aey'],
                'ae': ['ä', 'e', 'è', "'e", 'ae', 'ai', 'aë', "ä'", 'äe'],
                'ë': ['å', 'e', 'è', 'ê', 'ë', 'í', 'ô', 'ö', "'e", "e'", 'ea', 'oe', "ö'"],
                'i': ['i', 'ì', 'í', 'ï', "i'", 'ije', 'oui'],
                'ii': ['i', 'y', 'ie', 'ih', 'ii', 'ij', 'ïh', 'ye', 'ieh', 'ièh', "ie'e"],
                'o': ['o'],
                'oo': ['o', 'ô', "'o", 'au', 'oh', 'oo', 'ôh', 'ooh'],
                'u': ['u', 'ou'],
                'uu': ["u'", 'uh', 'uu', "o'i", 'oou', 'ouh', "u'h", 'uee'],
                'ië': ["'e", "i'", 'ie', 'iè', 'ié', 'ië', 'iö', 'ye', 'yä', "i'e", "i'è", "i'é"
                       "ie'", 'ieh', 'ioe', 'ièh', 'iéh', "i'eh", "ie'h"],
                'uë': ["'o", 'eo', 'oè', 'oé', 'oë', "ö'", 'ue', 'uä', 'ué', 'uë', 'uö', "'ou"
                       "'uo", "o'e", "o'h", "o'i", 'oei', "oi'", 'oie', 'oih', 'oua', 'oue', 'ouh'
                       'oéh', "u'a", "u'e", "u'h", "u'é", "ue'", 'uoh', 'uou', "u'eh", "uo'h"],
                'éi': ['è', 'é', "'e", "e'", 'eè', 'èi', "é'", 'éi', "ë'", 'ëi', "'eh", 'aei'
                       'aey', "e'h", "e'i", "ei'", 'eih', 'eij', "é'i", 'éih', "e'ih"],
                'ëu': ["o'", 'ou', 'oë', "ao'", "o'e", "o'i", "o'u", "oe'", "ou'", 'oue', 'ouh'
                       "u'o", "uo'", 'oueh'],
                'oi': ['äu', 'eu', 'eü', 'oy', 'aeu', 'aue', 'aui'],
                'äi': ['ai', 'aï', 'äi', "e'", "ë'", 'ëi', 'aei', "e'i", "ei'", "ä'i", "äi'", "éi'"],
                'äu': ['au', 'àu', 'aou', "au'", 'aui'],
                'ai': ['ai', 'aj', 'aé', 'ei', 'ey', "ë'", 'eih', 'eij'],
                'au': ['ao', 'au', 'aoe', 'aou', 'auh', 'aou'],
                'ui': ['ui'],
                'ia': ['ea', 'ia'],
                'iu': ['iu', 'ieou'],
                'ie': ['iä', "i'e", "i'é", 'iei', 'iie'],
                'üë': ['üe'],
                'ö': ['ö', 'oe', 'oé', 'aeu', 'oeh'],
                'öö': ['ö', 'oë', 'öe', 'öh', 'ooe', 'oéh'],
                'ü': ['u', 'û', 'ü', 'ue', 'oui'],
                'üü': ['û', 'ü', 'ïh', 'üh', 'uee', 'ueh'],
                'â': ['ea'],
                'ô': ['ea']}

phoneme_dict_consonant = {'b': ['b', 'bb'],
                          'p': ['b', 'p', 'pp'],
                          'd': ['d', 'dd'],
                          't': ['d', 't', 'tt', 'th', 'dt'],
                          'g': ['g', 'gg', 'gh'],
                          'k': ['g', 'gh', 'k', 'kk', 'ck', 'cck', 'ch'],
                          'h': ['h'],
                          'x': ['ch'],
                          'j': ['g', 'j', 'jh'],
                          'sh': ['sch', 'ch', 's', 'g', 'gh', 'scg'],
                          'tsh': ['g', 'ch', 'tch', 'tsch', 'j'],
                          's': ['s', 'ss'],
                          'dz': ['ds', 'dz'],
                          'ts': ['ds', 'dz', 'z', 'tz', 'ts'],
                          'f': ['f', 'ff', 'v', 'ph', 'w'],
                          'v': ['w', 'ww', 'v'],
                          'r': ['r', 'rr', 'rh'],
                          'l': ['l', 'll'],
                          'm': ['m', 'mm', 'mmm'],
                          'n': ['n', 'nn', 'nnn'],
                          'ng': ['ng', 'n', "ng'", 'ngh', 'ngg'],
                          'y': ['j', 'y', 'g'],
                          'w': ['u', 'w']}

mini_dict = {'a': ['a', "a'", 'aé', 'ea', 'a', 'à', 'â', "'a", "a'", 'aa', 'ah', 'ao', 'aah'],
             'e': ['å', 'e', 'é', 'ë', 'eé', 'ëe', 'ä', 'e', 'è', 'ê', 'ë', "'e", 'ae', 'ay', 'aä', 'aè', 'aé', 'aë',
                   "ä'", 'äe', 'äh', 'äi', 'ää', "e'", 'ea', 'ee', 'eh', 'ey', 'eè', 'eé',"è'", 'èe', 'èh', 'ée', 'éh',
                   'éi', 'ëe', 'ëh', "'eh", 'aee', 'aeh', 'aey', 'ä', 'e', 'è', "'e", 'ae', 'ai', 'aë', "ä'", 'äe'],
             'i': ['i', 'ì', 'í', 'ï', "i'", 'ije', 'oui', 'i', 'y', 'ie', 'ih', 'ii', 'ij', 'ïh', 'ye', 'ieh', 'ièh',
                   "ie'e"],
             'o': ['o', 'ô', "'o", 'au', 'oh', 'oo', 'ôh', 'ooh'],
             'u': ["u'", 'uh', 'uu', 'ou', "o'i", 'oou', 'ouh', "u'h", 'uee'],
             'ië': ["'e", "i'", 'ie', 'iè', 'ié', 'ië', 'iö', 'ye', 'yä', "i'e", "i'è", "i'é"
                       "ie'", 'ieh', 'ioe', 'ièh', 'iéh', "i'eh", "ie'h"],
             'uë': ["'o", 'eo', 'oè', 'oé', 'oë', "ö'", 'ue', 'uä', 'ué', 'uë']}

mini_vowel = {'a': phoneme_dict_vowel['a'] + phoneme_dict_vowel['aa'],
              'o': phoneme_dict_vowel['o'] + phoneme_dict_vowel['oo'],
              'u': phoneme_dict_vowel['u'] + phoneme_dict_vowel['uu'],
              'e': phoneme_dict_vowel['e'] + phoneme_dict_vowel['ee'],
              'i': phoneme_dict_vowel['i'] + phoneme_dict_vowel['ii']}



# for i in mini_vowel.keys():
#     for j in ['gr', 'aa', 'cht']:
#         if j in mini_vowel[i]:
#             print(j, i)
#
# print(vowel_clusters('Bruchtebaach'))
#
# query_string = 'Bruechtebaach'
# for item in vowel_clusters(query_string):
#     print(query_string, item, query_string.split(item))

def word_split(input_string):
    # v = re.compile('[\']*[oeüiuaöéàëäyíèôêìåûïâú]+[\']*[j]*[oeüiuaöéàëäyíèôêìåûïâú]*[h]*', re.I)
    # c = re.compile('[bcdfghjklmnpqrstvwxz]+', re.I)
    a = re.compile('[\']*[oeüiuaöéàëäyíèôêìåûïâú]+[\']*[j]*[oeüiuaöéàëäyíèôêìåûïâú]*[h]*|[bcdfghjklmnpqrstvwxz]+', re.I)
    return a.findall(input_string)

# print(word_split('bruechtebahch'))

t = word_split('bruechtebaach')

# print(t)
# #
# print(t.index('ue'))
#
# t[1] = [t[1]]
# t[1].append('o')
#
# print(t)
# #
# t[1].append('oo')
# #
# print(t)

# for item in mini_dict.keys():
#     # print(item)
#     for jtem in t:
#         if item == jtem:
#             print(jtem, item)



# d = t
#
# print(d)
# d = [[item] for item in d]
# print(d)

# # print(d)
# results= []
# for i in d:
#     # print(i, d.index(i))
#     i1 = d.index(i)
#     # r1 = []
#     # r1.append(i)
#     for k in mini_dict.keys():
#         if i in mini_dict[k]:
#             results.append(i)
#             results.append(k)
#             # r1.append(k)
#             d[i1] = k
#     # print(r1)
#     # d[i1] = r1
# print(d)

#### this works if there are no disambiguities in the dict,
#### meaning keys and values are unique. So it might work for
#### a generalised dict.

# what if I use word_split and v_cluster together, open everything in word_split but use specifically v_cluster
# to access the vowels only. Then I query for all possible variations? Computing time ould be too big?

# print(Da_list)

# for i in d:
#     if i in vowel_clusters('bruechtebahch'):
#         i1 = d.index(i)
#         for k in mini_dict.keys():
#             if i in mini_dict[k]:
#                 d[i1] = k
#     # print(d)
# print('##########    TEST ENVIRONMENT    ##########')
# test_word = 'bruechtebaach'
# test_list = [[item] for item in word_split(test_word)]
# print(vowel_clusters(test_word))

# print()
# VG = ['ue']
#
# print(list(VG))
#
# if list(VG)[0] in vowel_clusters(test_word):
#     print('yes')
#
# print()

# for i in test_list:
#     print(i, test_list.index(i), [w for w in vowel_clusters(test_word) if w == i[0]])
    # for j in vowel_clusters(test_word):
    #     print(j)
        # if i in j:
        #     print(i)
        #     i1 = test_list.index(i)
        #     print(i1, i)
        #     for k in mini_dict.keys():
        #         if i in mini_dict[k]:
        #             d[i1] = k
    # print(d)



def string_querry_mini(input_string):
    s = word_split(input_string)
    for i in s:
        i1 = s.index(i)
        # print(i1)
        for k in mini_dict.keys():
            # intermitted = [i, k]
            # print(intermitted)
            if i in mini_dict[k]:
                intermitted = ['8', i, k]
                print(i1, intermitted)
                for graph in mini_dict[k]:
                    intermitted.append(graph)
                s[i1] = intermitted
            else:
                s[i1] = [i]
    return s

print(string_querry_mini('bruechtebaach'))
print()

# print(mini_dict['uë'])



def string_querry_big(input_string):
    s = word_split(input_string)
    for i in s:
        i1 = s.index(i)
        for k in phoneme_dict_vowel.keys():
            intermitted = [i, k]
            if i in phoneme_dict_vowel[k]:
                for graph in phoneme_dict_vowel[k]:
                    intermitted.append(graph)
                s[i1] = intermitted
            else:
                s[i1] = [i]
    return s






# print(list(itertools.product(*string_querry_mini('bruechtebaach'))))
print([''.join(item) for item in itertools.product(*string_querry_mini('bruechtebaach'))])
print(len(list(itertools.product(*string_querry_mini('bruechtebaach')))))
print([''.join(item) for item in itertools.product(*string_querry_big('bruechtebaach'))])
print(len(list(itertools.product(*string_querry_big('bruechtebaach')))))



# test_list = [['br'], ['ue', 'uë'], ['cht'], ['ë', 'e'], ['b'], ['a', 'aa'], ['ch']]
#
# print(list(itertools.product(*test_list)))
#
#
# for item in itertools.product(*test_list):
#     print(''.join(item))
#
# print([''.join(item) for item in itertools.product(*test_list)])
#
# print(len(list(itertools.product(*test_list))))








# combinations = []  # Kaarels multi line version
#
# def combine(terms, accum):
#     last = (len(terms) == 1)
#     n = len(terms[0])
#     for i in range(n):
#         item = accum + terms[0][i]
#         if last:
#             combinations.append(item)
#         else:
#             combine(terms[1:], item)
#
#
# >>> a = [['ab','cd','ef'],['12','34','56']]
# >>> combine(a, '')
# >>> print(combinations)
# ['ab12', 'ab34', 'ab56', 'cd12', 'cd34', 'cd56', 'ef12', 'ef34', 'ef56']