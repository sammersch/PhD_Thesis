import re, json


with open('AllNewTopo/microtoponymsVillages.geojson', encoding='utf-8') as data_file:

    data = json.load(data_file)

    for feature in data['features'][0]['properties']['LABEL']:
        print(data['features'][0]['properties']['LABEL'])
        # wholeJson.append(dict({"name" : feature['properties']['LABEL'],
        #                        "coordinates" : feature['geometry']['coordinates'],
        #                        "shape_length" : feature['properties']['SHAPE.LEN'],
        #                        "object_ID" : feature['properties']['OBJECTID'],
        #                        "character_length": len(re.sub(" ", "", feature['properties']['LABEL'])),
        #                        "sequence_length": len(feature['properties']['LABEL'].split())}))
        #
        # streetNames.append(dict({"name": feature['properties']['LABEL'],
        #                          "coordinate_set": feature['geometry']['coordinates'],
        #                          "shape_length" : feature['properties']['SHAPE.LEN'],
        #                          "object_ID" : feature['properties']['OBJECTID'],
        #                          "character_length": len(re.sub(" ", "", feature['properties']['LABEL'])),
        #                          "sequence_length": len(feature['properties']['LABEL'].split())}))
