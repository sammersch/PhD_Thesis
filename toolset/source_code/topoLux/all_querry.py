import itertools, re
from phoneticDistribution import vowel_clusters
import collections
# import cologne_phonetics
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

diachonic_dict = {'@': phoneme_dict_vowel['a'] + phoneme_dict_vowel['aa'] + phoneme_dict_vowel['uë'] +
                     phoneme_dict_vowel['oi'] + phoneme_dict_vowel['äu'] + phoneme_dict_vowel['ia'],
                  '€': phoneme_dict_vowel['e'] + phoneme_dict_vowel['ee'] + phoneme_dict_vowel['ae'] +
                     phoneme_dict_vowel['ë'] + phoneme_dict_vowel['i'] + phoneme_dict_vowel['ii'] +
                     phoneme_dict_vowel['ië'] + phoneme_dict_vowel['éi'] + phoneme_dict_vowel['äi'] +
                     phoneme_dict_vowel['ai'] + phoneme_dict_vowel['ui'] + phoneme_dict_vowel['ie'],
                  '0': phoneme_dict_vowel['o'] + phoneme_dict_vowel['oo'] + phoneme_dict_vowel['u'] +
                     phoneme_dict_vowel['uu'] + phoneme_dict_vowel['ëu'] + phoneme_dict_vowel['au'] +
                     phoneme_dict_vowel['iu'] + phoneme_dict_vowel['üë'] + phoneme_dict_vowel['ö'] +
                     phoneme_dict_vowel['öö'] + phoneme_dict_vowel['ü'] + phoneme_dict_vowel['üü'] +
                     phoneme_dict_vowel['â'] + phoneme_dict_vowel['ô']
                  } # 1=back vowel, 2=front vowels, 3=midfront (o,u)+div



def word_split(input_string):
    # v = re.compile('[\']*[oeüiuaöéàëäyíèôêìåûïâú]+[\']*[j]*[oeüiuaöéàëäyíèôêìåûïâú]*[h]*', re.I)
    # c = re.compile('[bcdfghjklmnpqrstvwxz]+', re.I)
    a = re.compile('[\']*[oeüiuaöéàëäyíèôêìåûïâú]+[\']*[j]*[oeüiuaöéàëäyíèôêìåûïâú]*[h]*|[bcdfghjklmnpqrstvwxz]+|[\s]*', re.I)
    return a.findall(input_string)[:-1]

# print(word_split('Bruechtebaach'))
# print(word_split('an der Burechtebaach'))

def string_querry_mini(input_string): # only works with unique keys and values.
    s = word_split(input_string)
    results = []
    for i in s:
        i1 = s.index(i)
        for k in mini_dict.keys():
            if i in mini_dict[k]:
                results.append([i, k])
                s[i1] = k
    return s


def get_all_keys(input_string):
    i = [[item] for item in word_split(input_string)]
    for cluster in i:
        for key in phoneme_dict_vowel.keys():
            if cluster[0] in phoneme_dict_vowel[key]:
                i[i.index(cluster)].append(key)
    return i


def get_all_values(input_string):
    i = [[item] for item in word_split(input_string)]
    for cluster in i:
        for key in phoneme_dict_vowel.keys():
            if cluster[0] in phoneme_dict_vowel[key]:
                # i[i.index(cluster)].append(phoneme_dict_vowel[key])
                for value in phoneme_dict_vowel[key]:
                    i[i.index(cluster)].append(value)
    return i


def get_all_diachronic(input_string): # to code into 3 vowel system for diachronic analysis.
    i = [[item] for item in word_split(input_string)]
    for cluster in i:
        slice = cluster[0]
        if slice in vowel_clusters(input_string):
            i[i.index(cluster)].clear()
        for key in diachonic_dict.keys():
            if slice in diachonic_dict[key]:
                # i[i.index(cluster)].clear()
                i[i.index(cluster)].append(key)
    return i


def get_all_possibillities(input_list): # manages to put together of all possibilities of the dict search.
    return [''.join(item) for item in itertools.product(*input_list)]

#
# print(get_all_possibillities(get_all_keys('uecht')))
# print(get_all_possibillities(get_all_values('bruechtebaach')))
# print(get_all_possibillities(get_all_diachronic('bruechtebaach')))
# print(get_all_possibillities(get_all_diachronic('uecht')))


def get_all_consonants(input_string):
    # for item in phoneme_dict_consonant['sh'] + phoneme_dict_consonant['s']:

    for key in phoneme_dict_consonant.keys():
        for value in phoneme_dict_consonant[key]:
            input_string = re.sub(value, key, input_string)

    # re.sub('(?<=[abc])[g]', 's', input_string)

    return input_string


    # ['sch', 'ch', 's', 'g', 'gh', 'scg']
# print(get_all_consonants('br@cht€b@ch'))
# print(get_all_consonants('databcgia'))



# def cologn_coder(input_string): # shall take input string after get_all_possibillities()
#     return cologne_phonetics.encode(input_string)[0][1]



# print(cologn_coder('bruechtebaach'))



#
# def compare(input_string):
#     # change = word_split(input_string)
#     # print(change)
#     results = []
#     change = get_all_diachronic(input_string.lower())
#     # print(change)
#     change = get_all_possibillities(change)
#     # print(change)
#     for variant in change:
#         for instance in corpus:
#             for sub_i in get_all_possibillities(get_all_diachronic(instance['name'].lower())):
#                 if variant == sub_i:
#                     # print(input_string, variant, instance['name'])
#                     if instance['name'] not in results:
#                         results.append(instance['name'])
#                 elif sub_i.startswith(variant):
#                     if instance['name'] not in results:
#                         results.append(instance['name'])
#                 elif sub_i.endswith(variant):
#                     if instance['name'] not in results:
#                         results.append(instance['name'])
#                 elif variant in sub_i:
#                     if instance['name'] not in results:
#                         results.append(instance['name'])
#     return results


hgf = 'uecht'
# print(*compare(hgf), sep='\n')
#
# print(len(compare(hgf)))
#
# print(compare(hgf))

# print(get_all_values(hgf))
# print(get_all_possibillities(get_all_values(hgf)))

# def compare_vowels(input_string):
#     results = []
#     for possibility in get_all_possibillities(get_all_values(input_string)):
#         for instance in corpus:
#             if possibility == instance['name'].lower():
#                 adding = [possibility, 'exact', instance['name']]
#                 if adding not in results:
#                     results.append(adding)
#             elif instance['name'].lower().startswith(possibility):
#                 adding = [possibility, 'start', instance['name']]
#                 if adding not in results:
#                     results.append(adding)
#             elif instance['name'].lower().endswith(possibility):
#                 adding = [possibility, 'end', instance['name']]
#                 if adding not in results:
#                     results.append(adding)
#             elif possibility in instance['name'].lower():
#                 adding = [possibility, 'within', instance['name']]
#                 if adding not in results:
#                     results.append(adding)
#     return results


# print(len(compare_vowels('uecht')))
# print(*compare_vowels('uecht'), sep='\n')
# for item in compare_vowels('uecht'):
#     if 'exact' in item:
#         print(item)

def get_all_by_phoneme(phoneme):
    results = []
    for grapheme in phoneme_dict_vowel[phoneme]:
        for item in corpus:
            if grapheme in vowel_clusters(item['name']):
                results.append([grapheme, item['name'], item['section'], item['corpus']])
    return results


def get_all_contexts(phoneme):
    '''Query for all contexts of a vowel phoneme, will return immediate context as in consonant cluster. Takes arg phoneme'''
    results = []
    for grapheme in phoneme_dict_vowel[phoneme]:
        for item in corpus:
            if grapheme in word_split(item['name']):
                if grapheme == word_split(item['name'])[0]:
                    pre = ' '
                else:
                    pre = word_split(item['name'])[word_split(item['name']).index(grapheme) - 1]
                if grapheme == word_split(item['name'])[-1]:
                    post = ' '
                else:
                    post = word_split(item['name'])[word_split(item['name']).index(grapheme) + 1]
                context = [pre.lower(), grapheme, post]
                if context not in results:
                    results.append(context)
    return results

def get_context_pre(phoneme):
    '''Query for consonant context preceding vowel phoneme. Takes arg phoneme. Uses get_all_contexts.'''
    # return [item[0] for item in get_all_contexts(phoneme)]
    results = []
    for item in get_all_contexts(phoneme):
        if item[0] not in results:
            results.append(item[0])
    return results

def get_context_post(phoneme):
    '''Query for consonant context following vowel phoneme. Takes arg phoneme. Uses get_all_contexts.'''
    # return [item[-1] for item in get_all_contexts(phoneme)]
    results = []
    for item in get_all_contexts(phoneme):
        if item[-1] not in results:
            results.append(item[-1])
    return results

def get_context_post_single(phoneme):
    '''Query for consonant context following vowel phoneme. Takes arg phoneme. Uses get_all_contexts.'''
    # return [item[-1] for item in get_all_contexts(phoneme)]
    results = []
    for item in get_all_contexts(phoneme):
        if item[-1][0] == '':
            continue
        if item[-1][0] not in results:
            results.append(item[-1][0])
    return results

def get_specific_post_context(phoneme, context):
    results = []
    for grapheme in phoneme_dict_vowel[phoneme]:
        for item in corpus:
            if grapheme in word_split(item['name']):
                if grapheme + context in item['name']:
                    results.append([phoneme, grapheme, context, item['name']])
    return results

# print(get_context_pre('a'))
# print(len(get_context_pre('a')))
# print(sorted(get_context_pre('a')))
#
# print(get_context_post('a'))
# print(len(get_context_post('a')))
# print(sorted(get_context_post('a')))
# print(sorted(get_context_post_single('a')))
# for item in corpus:
#     if 'ab' in item['name'].lower():
#         print(item)

# print(*get_all_by_phoneme('e'), sep='\n')
# print(*get_specific_post_context('o', 'm'), sep='\n')

