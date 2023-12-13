

cnra_load = []
with open('cnra/cnra_up.csv', encoding='utf-8') as cabernet:
    pinot = cabernet.readlines()
    for item in pinot:
        elbling = item.rstrip('\n')
        rivaner = elbling.split(',')

        cnra_load.append(dict({'name': rivaner[0],
                                'section': rivaner[1],
                                'adm_comm': rivaner[2]}))
cabernet.close()

