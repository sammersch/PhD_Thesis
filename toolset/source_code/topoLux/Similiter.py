from MicroTopoLoadAllData import microTopoAll
import re

def vowel_wrapper(word):
    # returns vowels and vowelclusters as 0.
    word = word.lower()
    word = re.sub('0+', '0', re.sub(str([i for i in 'aeiouáäéèëüö']), '0', word))
    return word

def dental_wrapper(word):
    # returns dentals to 2.
    word = word.lower()
    word = re.sub('2+', '2', re.sub(str([i for i in 'dt']), '2', word))
    return word

def double_remover(word):
    # removes doubles
    word = word.lower()
    word = re.sub(r'([a-z])\1+', r'\1', word)
    return word

def plosive_wrapper(word):
    # removes doubles
    word = word.lower()
    word = re.sub('3+', '3', re.sub(str([i for i in 'bp']), '3', word))
    return word

def simplifier(word):
    word = word.lower()
    word = double_remover(word)
    word = dental_wrapper(word)
    word = vowel_wrapper(word)
    word = plosive_wrapper(word)
    return word.upper()

print(simplifier('dellt'))

def similiter(word, test_list):
    results = []
    word = list(word.lower())
    for item in test_list:
        complie_word = []
        item_list = list(item.lower())
        if len(word) == len(item_list):
            for i in range(len(word)):
                if word[i] == item_list[i]:
                    complie_word.append(word[i])
                else:
                    complie_word.append('-')
        results.append(''.join(complie_word))
        if len(word) < len(item_list):
            for i in range(len(word)):
                if word[i] == item_list[i]:
                    complie_word.append(word[i])
                else:
                    complie_word.append('-')
            complie_word.append('@')
            # if len(list_word) < len(item_list):
            #     filler = '-' * (len(item_list)-len(list_word))
            #     complie_word.append(filler)
        results.append(''.join(complie_word))
    # return ''.join(complie_word)
    return results

print(similiter('Dell', ['Dall', 'Delt', 'Däll', 'Dällchen']))


# test_list = ['Dall', 'Delt', 'Däll', 'Dällchen']
#
# test_word = 'Dell'
#
# list_word = list(test_word.lower())
#
# for item in test_list:
#     complie_word = []
#     item_list = list(item.lower())
#     if len(list_word) == len(item_list):
#         for i in range(len(list_word)):
#             if list_word[i] == item_list[i]:
#                 complie_word.append(list_word[i])
#             else:
#                 complie_word.append('-')
#     elif len(list_word) < len(item_list):
#         for i in range(len(list_word)):
#             if list_word[i] == item_list[i]:
#                 complie_word.append(list_word[i])
#             else:
#                 complie_word.append('-')
#         complie_word.append('@')
#         # if len(list_word) < len(item_list):
#         #     filler = '-' * (len(item_list)-len(list_word))
#         #     complie_word.append(filler)
#     print(''.join(complie_word))
#
#
#
#
simple_list = []
for item in microTopoAll:
    word = item['name'].split()[-1]
    simple_list.append(word)

# for item in simple_list:
#     print(simplifier(item))
#
