from MicroTopoLoadAllData import microTopoAll

import lingpy

whatDistricts = []
diekirch = []
luxembourg = []
grevenmacher = []
#
# for item in microTopoAll:
#     if item['district'] == 'Diekirch':
#         new_name = item['name'].split()[-1]
#         if new_name not in diekirch:
#             diekirch.append(new_name)
#     if item['district'] == 'Luxembourg':
#         new_name = item['name'].split()[-1]
#         if new_name not in luxembourg:
#             luxembourg.append(new_name)
#     if item['district'] == 'Grevenmacher':
#         new_name = item['name'].split()[-1]
#         if new_name not in grevenmacher:
#             grevenmacher.append(new_name)
#
# print('Dikierch has how many? ' + str(len(diekirch)))
# print('Luxembourg has how many? ' + str(len(luxembourg)))
# print('Grevenmacher has how many ? ' + str(len(grevenmacher)))
# print()
#
# only_diekirch = []
# for item in diekirch:
#     if item not in luxembourg:
#         if item not in grevenmacher:
#             only_diekirch.append(item)
#
# print('Only in Diekirch: ' + str(len(only_diekirch)))
#
#
# only_luxembourg = []
# for item in luxembourg:
#     if item not in diekirch:
#         if item not in grevenmacher:
#             only_luxembourg.append(item)
#
# print('Only in Luxemourg: ' + str(len(only_luxembourg)))
#
# only_grevenmacher = []
# for item in grevenmacher:
#     if item not in diekirch:
#         if item not in luxembourg:
#             only_grevenmacher.append(item)
#
# print('Only in Grevenmacher: ' + str(len(only_grevenmacher)))
#
# all_in_common = []
# for item in diekirch:
#     if item in luxembourg:
#         if item in grevenmacher:
#             all_in_common.append(item)
#
# print('All in common are: '+ str(len(all_in_common)))
#
# print(*sorted(all_in_common), sep='\n')

new_list = []
for i in microTopoAll:
    new_list.append(i['name'].split()[-1])


print(len(new_list))
print(len(set(new_list)))

# for i in microTopoAll:
#     if 'weg' in i['name']:
#         print(i['name'], ':\t', i['section'])

for i in microTopoAll:
    if 'ingen' in i['name']:
        print(i['name'], ':\t', i['section'])