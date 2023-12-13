import re, json



cartoLoad = [] # this is the dictionary that is fed by nameSectionShape, which was generated from the shape files
                  # LIM_SECTION and act_pcn_toponymes_1:

with open('CartoLoad/cartoALL.geojson', encoding='utf-8') as data_file:

    data = json.load(data_file)

    for feature in data['features']:
        if feature['properties']['TOPONYME'] == None:
            # print('found a None')
            continue
        else:
            cartoLoad.append(dict({"name": feature['properties']['TOPONYME'],
                                     "object_ID" : feature['properties']['OBJECTID'],
                                     "nature" : feature['properties']['NATURE'],
                                     "primedi" : feature['properties']['PRIMEDI'],
                                     "canton": feature['properties']['CANTON'],
                                     "district": feature['properties']['DISTRICT'],
                                     "section": feature['properties']['SECTION'],
                                     "cad_comm": feature['properties']['COMMUNE_CA'],
                                     "code_comm": feature['properties']['CODE_COMMU'],
                                     "adm_comm": feature['properties']['COMMUNE_AD'],
                                     "code_vill": feature['properties']['CODE'],
                                     # these are the elements that are inside the GEOJson file under 'properties'
                                     "coordinates" : feature['geometry']['coordinates'],
                                     # these are the elements that are inside the GEOJson file under 'geometry'
                                     "character_length": len(re.sub(" ", "", str(feature['properties']['TOPONYME']))),
                                     "sequence_length": len(str(feature['properties']['TOPONYME']).split())
                                      # these are the elements that are calculated from the ['properties']['LABEL'], they
                                      # are total length of characters in the toponym and syntactic length of the toponym.
                                      }))
    data_file.close()
# ['Lieu-dit', 'Petit lieu-dit', 'Maison isolée', 'Village', 'Bois, mont', 'Quartier, groupe de maisons', 'Forêt, montagne', 'Commune']
# slength = []
