import re, json


wholeJson = [] # this is the full dictionary that is fed by act_pcn_toponymes_0 and act_pcn_toponymes_1
streetNames = [] # this is the control dictionary that is fed by act_pcn_toponymes_0
microToponyms = [] # this is the control dictionary that is fed by act_pcn_toponymes_1

with open('MicroTopoLoad/act_pcn_toponymes.geojson', encoding='utf-8') as data_file:

    data = json.load(data_file)

    for feature in data['act_pcn_toponymes_0']['features']:
        wholeJson.append(dict({"name" : feature['properties']['LABEL'],
                                "coordinates" : feature['geometry']['coordinates'],
                                "shape_length" : feature['properties']['SHAPE.LEN'],
                                "object_ID" : feature['properties']['OBJECTID'],
                                "character_length": len(re.sub(" ", "", feature['properties']['LABEL'])),
                                "sequence_length": len(feature['properties']['LABEL'].split())}))

        streetNames.append(dict({"name": feature['properties']['LABEL'],
                                 "coordinates": feature['geometry']['coordinates'],
                                 "shape_length" : feature['properties']['SHAPE.LEN'],
                                 "object_ID" : feature['properties']['OBJECTID'],
                                 "character_length": len(re.sub(" ", "", feature['properties']['LABEL'])),
                                 "sequence_length": len(feature['properties']['LABEL'].split())}))


    for feature in data['act_pcn_toponymes_1']['features']:
        wholeJson.append(dict({"name" : feature['properties']['LABEL'],
                                "coordinates" : feature['geometry']['coordinates'],
                                "shape_length" : feature['properties']['SHAPE.LEN'],
                                "object_ID" : feature['properties']['OBJECTID'],
                                "character_length": len(re.sub(" ", "", feature['properties']['LABEL'])),
                                "sequence_length": len(feature['properties']['LABEL'].split())}))

        microToponyms.append(dict({"name": feature['properties']['LABEL'],
                                   "coordinates": feature['geometry']['coordinates'],
                                   "shape_length" : feature['properties']['SHAPE.LEN'],
                                   "object_ID" : feature['properties']['OBJECTID'],
                                   "character_length": len(re.sub(" ", "", feature['properties']['LABEL'])),
                                   "sequence_length": len(feature['properties']['LABEL'].split())}))






