import re


with open('BusStopLoad/busStopsLux.txt', encoding='utf-8') as busStops:
    stops = busStops.read()

stopList = stops.split('; \n')

listOfStops = []
for item in stopList:
    dump = re.sub('id=A=1@O=', '',
                  re.sub('@X=', '; ',
                      re.sub('@Y=', '; ',
                             re.sub('@L=', '; ',
                                    re.sub('@B=', '; ',
                                           re.sub('1@p=', '',
                                                  re.sub('@U=', '', item)))))))
    new_list = dump.split('; ')
    # if ',' not in new_list[0]:
    #     pass
    # else:
    #
    name, Long, Lat, Xco, Yco = new_list
    if ',' in name:
        listOfStops.append(dict({'loc': name.split(',')[0],
                                 'name': name.split(',')[1],
                                 'Xcoordinate': Xco,
                                 'YCoordinate': Yco,
                                 'Longitude': Long,
                                 'Latitude': Lat}))

    # listOfStops.append(dict({'name': name,
    #                          'Xcoordinate': Xco,
    #                          'YCoordinate': Yco,
    #                          'Longitude': Long,
    #                          'Latitude': Lat}))



busStopLoad = []

with open('BusStopLoad/busStopsLuxEdit.txt', encoding='utf-8') as busStops:
    stops = busStops.read()

stopList2 = stops.split('; \n')

# listOfStops = []
for item in stopList2:
    dump = re.sub('id=A=1@O=', '',
                  re.sub('@X=', '; ',
                      re.sub('@Y=', '; ',
                             re.sub('@U=82@L=', '; ',
                                    re.sub('@B=1@p=', '; ', item)))))
    # print(dump)
    new_list = dump.split('; ')
    # print(new_list)
    # # if ',' not in new_list[0]:
    # #     pass
    # # else:
    # #
    name, Long, Lat, Xco, Yco = new_list
    # if ',' in name:
    if ',' in name:
        busStopLoad.append(dict({'section': re.sub('\ufeff', '', name.split(',')[0]), # adds section name to dict
        # busStopLoad.append(dict({'loc': name.split(',')[0],
                                 'name': name.split(',')[1], # adds toponym to dict
                                 'X': Xco, # adds x coordinate to dict
                                 'Y': Yco, # adds y coordinate to dict
                                 'Long': Long, # adds longitude to dict
                                 'Lat': Lat})) # adds latitude to dict




# print(busStopLoad)
print(busStopLoad)