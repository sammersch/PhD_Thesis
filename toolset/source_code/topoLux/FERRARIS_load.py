
FERRARIS_data = [] # toponyme;usage;village;fiche

with open('FERRARIS_load/Fdata.csv', encoding='utf-8') as cabernet:
    pinot = cabernet.readlines()
for item in pinot:
    elbling = item.rstrip('\n')
    name, usage, section, fiche = elbling.split(',')
    FERRARIS_data.append(dict({'name': name,
                          'section': section,
                          'usage': usage,
                          'fiche': fiche}))
cabernet.close()

