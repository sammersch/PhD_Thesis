

ADL_load = [] # Commune actuelle,Village,Lieux-dits,Nature de culture,page

with open('ADL_load/ADLsmall.csv', encoding='utf-8') as cabernet:
    pinot = cabernet.readlines()
for item in pinot:
    elbling = item.rstrip('\n')
    adm_comm, section, name, usage, page = elbling.split(',')
    ADL_load.append(dict({'name': name,
                          'section': section,
                          'adm_comm': adm_comm,
                          'usage': usage,
                          'page': page}))
cabernet.close()

