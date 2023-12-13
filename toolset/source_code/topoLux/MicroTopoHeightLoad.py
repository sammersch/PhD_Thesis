import re, json



microTopoHeight = [] # this is the dictionary that is fed by nameSectionShape, which was generated from the shape files
# LIM_SECTION and act_pcn_toponymes_1:

with open('MicroTopoHeightLoaD/NamesAndHeights.geojson', encoding='utf-8') as data_file:

    data = json.load(data_file)

    for feature in data['features']:
        if feature['properties']['LABEL'] == None:
            # print('found a None')
            continue
        else:
            microTopoHeight.append(dict({"name": feature['properties']['LABEL'],
                                      "object_ID" : feature['properties']['OBJECTID'],
                                      # "canton" : feature['properties']['join_CANTON'],
                                      # "district" : feature['properties']['join_DISTRICT'],
                                      # "section" : feature['properties']['join_SECTION'],
                                      # "cad_comm" : feature['properties']['join_COMMUNE_CA'],
                                      # "code_comm" : feature['properties']['join_CODE_COMMU'],
                                      # "adm_comm" : feature['properties']['join_COMMUNE_AD'],
                                      # "code_vill" : feature['properties']['join_CODE'],
                                      # "distance" : feature['properties']['join_CODE_COMMU'],
                                      # "shape_length" : feature['properties']['SHAPE_LEN'],
                                      "heightCM" : int(feature['properties']['dhmtc0121']),
                                      "heightM" : int(feature['properties']['dhmtc0121'])/100,
                                      # these are the elements that are inside the GEOJson file under 'properties'
                                      "coordinates" : feature['geometry']['coordinates'],
                                      "coordinateOne" : feature['geometry']['coordinates'][0],
                                      "coordinateTwo" : feature['geometry']['coordinates'][1]#,
                                      # these are the elements that are inside the GEOJson file under 'geometry'
                                      # "character_length": len(re.sub(" ", "", str(feature['properties']['LABEL']))),
                                      # "sequence_length": len(str(feature['properties']['LABEL']).split())
                                      # these are the elements that are calculated from the ['properties']['LABEL'], they
                                      # are total length of characters in the toponym and syntactic length of the toponym.
                                      }))
    data_file.close()
