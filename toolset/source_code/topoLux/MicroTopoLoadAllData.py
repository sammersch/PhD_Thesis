import re, json



microTopoAll = [] # this is the dictionary that is fed by nameSectionShape, which was generated from the shape files
                  # LIM_SECTION and act_pcn_toponymes_1:

with open('MicroTopoLoadAllData/nameSectionShape.geojson', encoding='utf-8') as data_file:

    data = json.load(data_file)

    for feature in data['features']:
        if feature['properties']['LABEL'] == None:
            # print('found a None')
            continue
        else:
            namedInstance = feature['properties']['LABEL']
            namedInstance = re.sub('\n', ' ', namedInstance)
            namedInstance.rstrip('3')
            namedInstance.rstrip('2')
            namedInstance.rstrip('1')
            microTopoAll.append(dict({"name": namedInstance,
                                     "object_ID" : feature['properties']['OBJECTID'],
                                     "canton" : feature['properties']['join_CANTON'],
                                     "district" : feature['properties']['join_DISTRICT'],
                                     "section" : feature['properties']['join_SECTION'],
                                     "cad_comm" : feature['properties']['join_COMMUNE_CA'],
                                     "code_comm" : feature['properties']['join_CODE_COMMU'],
                                     "adm_comm" : feature['properties']['join_COMMUNE_AD'],
                                     "code_vill" : feature['properties']['join_CODE'],
                                     "distance" : feature['properties']['join_CODE_COMMU'],
                                     "shape_length" : feature['properties']['SHAPE_LEN'],
                                     # these are the elements that are inside the GEOJson file under 'properties'
                                     "coordinates" : feature['geometry']['coordinates'],
                                     "coordinateOne" : feature['geometry']['coordinates'][0],
                                     "coordinateTwo" : feature['geometry']['coordinates'][1],
                                     # these are the elements that are inside the GEOJson file under 'geometry'
                                     "character_length": len(re.sub(" ", "", str(feature['properties']['LABEL']))),
                                     "sequence_length": len(str(feature['properties']['LABEL']).split())
                                      # these are the elements that are calculated from the ['properties']['LABEL'], they
                                      # are total length of characters in the toponym and syntactic length of the toponym.
                                      }))
    data_file.close()


# for item in microTopoAll:

    # if item['section'].startswith('Harlange'):
        # print(item['section'])
    # if 'jock' in item['name'].lower():
    #     if item['name'].endswith('dell'):
    #     print(item['name'])
#     if 'galgen' in item['name'].lower():
#         print(item['name'] + ":\t" + item['section'])

# for item in microTopoAll:
#     if item['section'].startswith('Hesp'):
#         # if len(item['name'].split()) > 1:
#         if item['name'].split()[-1].startswith('G'):
#             print(item['name'] + ":\t" + item['section'])

# articles = ['d\'', 'dem', 'den', 'die', 'der', 'am', 'beim']
# # to catch articles and hopefully induce knowledge about gender. Enhance this further!
# for item in microTopoAll:
#    for art in articles:
#        if art in item['name'].split():
#         print(art + ":  " + item['name'] + ":\t" + item['section'])

# with open('MicroTopoLoadAllData/nameSectionShape.geojson', encoding='utf-8') as data_file:
#
#     data = data_file.read()
#     print(data)

    # for feature in data['features']:
    #     if feature['properties']['LABEL'] == None:
    #         # print('found a None')
    #         continue
    #     else:
    #         microTopoAll.append(dict({"name": feature['properties']['LABEL'],
    #                                   "object_ID" : feature['properties']['OBJECTID'],
    #                                   "canton" : feature['properties']['join_CANTON'],
    #                                   "district" : feature['properties']['join_DISTRICT'],
    #                                   "section" : feature['properties']['join_SECTION'],
    #                                   "cad_comm" : feature['properties']['join_COMMUNE_CA'],
    #                                   "code_comm" : feature['properties']['join_CODE_COMMU'],
    #                                   "adm_comm" : feature['properties']['join_COMMUNE_AD'],
    #                                   "code_vill" : feature['properties']['join_CODE'],
    #                                   "distance" : feature['properties']['join_CODE_COMMU'],
    #                                   "shape_length" : feature['properties']['SHAPE_LEN'],
    #                                   # these are the elements that are inside the GEOJson file under 'properties'
    #                                   "coordinates" : feature['geometry']['coordinates'],
    #                                   "coordinateOne" : feature['geometry']['coordinates'][0],
    #                                   "coordinateTwo" : feature['geometry']['coordinates'][1],
    #                                   # these are the elements that are inside the GEOJson file under 'geometry'
    #                                   "character_length": len(re.sub(" ", "", str(feature['properties']['LABEL']))),
    #                                   "sequence_length": len(str(feature['properties']['LABEL']).split())
    #                                   # these are the elements that are calculated from the ['properties']['LABEL'], they
    #                                   # are total length of characters in the toponym and syntactic length of the toponym.
    #                                   }))
    # data_file.close()

# extraList = []
# el2 = []
# for item in microTopoAll:
#     if item['sequence_length'] > 1:
#         short = item['name'].split()[:-1]
#         for i in short:
#             if i not in extraList:
#                 extraList.append(i)
#                 if i.islower():
#                     if i not in el2:
#                         el2.append(i)


# print(len(extraList))
# print(len(el2))
# # print(*sorted(extraList), sep='\n')
# print(*sorted(el2), sep='\n')


# for item in microTopoAll:
#     if 'follmillen' in item['name'].lower():
#         print(item['name'], item['section'])