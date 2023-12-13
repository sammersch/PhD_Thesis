act_actu_dict = []

with open('ACT_actuel_20140603_2.csv') as act:
    act = act.readlines()
    for l in act:
        _commune_section, _ur_plang, _aal_lieu_dit, _nei_lieu_dit, _haaptwuert, _nummer = l.split(';')
        # _nummer = _nummer.rstrip('\n')
        act_actu_dict.append(dict({'commune_section': _commune_section,
                               'ur_plang': _ur_plang,
                               'aal_lieu_dit': _aal_lieu_dit,
                               'nei_lieu_dit': _nei_lieu_dit,
                               'haaptwuert': _haaptwuert,
                               'nummer': _nummer.rstrip('\n')}))


up_counter = []
for item in act_actu_dict:
    if item['ur_plang'] == 'not_declared':
        pass
    else:
        up_counter.append(item['ur_plang'])

# print(len(up_counter))
# print(len(act_actu_dict))

# for item in act_actu_dict:
#     # if item['ur_plang'].startswith('hutton'):
#     # print(item['aal_lieu_dit'])
#     if item['aal_lieu_dit'] != '':
#         print(item['aal_lieu_dit'])