import re


r = "(hi|hello|hey)[ ]*([a-z]*)"

print(re.match(r, 'Hello Tanisha', flags=re.IGNORECASE))
# print(re.match(r, 'Hello TanishaPandey', flags=re.IGNORECASE))
# print(re.match(r, 'Hello Tanisha Pandey', flags=re.IGNORECASE))
# <_sre.SRE_Match object; span=(0, 10), match='Hello Rosa'>

# print(re.match(r, "hi ho, hi ho, it's off to work ...", flags=re.IGNORECASE))
# print(re.match(r, "hi ho, hi ho, it's off to work ...", flags=re.IGNORECASE))
# <_sre.SRE_Match object; span=(0, 5), match='hi ho'>

# re.match(r, "hey, what's up", flags=re.IGNORECASE)
# # <_sre.SRE_Match object; span=(0, 3), match='hey>
#
# test_string = 'THis is my first sentence. Tanisha turned into Voldemort. I will try to put in many misstakess. And what efs evs evs. Voldemort is back. Voldemort is nice. Voldemort is Tanisha. '
# # print(test_string)
#
# t0 = test_string.split('. ')
#
# l = "(voldemort|tanisha)[ ]*([a-z]*)[ ]*([a-z]*)"
#
# m = "(voldemort|tanisha|sam|lotti|victor)"
# pattern_list = ['voldemort', 'tanisha', 'victor']
# for sentence in t0:
    # print(re.findall(m, sentence, flags=re.IGNORECASE))
    # for pattern in pattern_list:
    #     if pattern in sentence.lower():
    #         print(pattern.upper(), sentence)


# for sentence in t0:
#     print(re.match(l, sentence, flags=re.IGNORECASE))
#     # print(sentence)
#     # print("looks for sentence starts Vdude")
#     # if sentence.lower().startswith('voldemort'):
#     #     print(sentence)
#     # print("looks for any sentence with Vdude")
#     # if 'voldemort' in sentence.lower():
#     #     print(sentence)
#     # print('looks for senctence start Vdude with re')
# print(re.match(l, sentence, flags=re.IGNORECASE))
#     print(re.findall(m, sentence, flags=re.IGNORECASE))


print('Tanisha\nis\nVoldemort')
print(r'Tanisha\nis\nVoldemort')

print(input()*400)