

IVV_load = [] # commune;localité;section;lieu-dit;page

with open('IVV_load/VinyardsPRE.csv', encoding='utf-8') as cabernet:
    pinot = cabernet.readlines()
for item in pinot:
    elbling = item.rstrip('\n')
    adm_comm, section, sNR, name, page = elbling.split(';')
    IVV_load.append(dict({'name': name,
                          'section': section,
                          'adm_comm': adm_comm,
                          'sectionNumber': sNR,
                          'page': page}))
cabernet.close()

# print(len(IVV_load))
