import json, os, re
from MicroTopoLoad import microToponyms
from MicroTopoLoadAllData import microTopoAll




def SyntacticQuery(n, dict): # displays all microtoponyms with a syntactic length n.
    # min = 1, max = 7
    results = []
    for item in dict:
        if item["sequence_length"] == n:
            results.append(item['name'])
    return results


def SQueryPPrint(n, dict):
    print(*SyntacticQuery(n, dict), sep='\n')


def SyntacticQuery_ctrl(topo_dict, n): # displays all microtoponyms with a syntactic length n.
    # min = 1, max = 7
    # control version which can specify which dictionary to access.
    results = []
    for item in topo_dict:
        if item["sequence_length"] == n:
            results.append(item['microtoponym'])
    return results




def HowManyHave(n): # queries for how many items there are with a syntactic length n.
    # min = 1, max = 7
    return len(SyntacticQuery(n))


def HowManyHave_ctrl(topo_dict, n): # queries for how many items there are with a syntactic length n.
    # min = 1, max = 7
    # control version which can specify which dictionary to access.
    return len(SyntacticQuery_ctrl(topo_dict, n))


def CharacterLength(n): # querries for absolute character length in a microtoponym (i.e. any character!)
    # minimal length is 3, maximal length is 43. Spaces are not taken into account.
    results = []
    for item in micro_dict:
        if item["character_length"] == n:
            results.append(item["microtoponym"])
    return results



def CharacterLength_ctrl(topo_dict, n): # querries for absolute character length in a microtoponym (i.e. any character!)
    # minimal length is 3, maximal length is 43. Spaces are not taken into account.
    results = []
    for item in topo_dict:
        if item["character_length"] == n:
            results.append(item["microtoponym"])
    return results



# ---- UNDER DEVELOPMENT!!!----
def SortByCharaLength(): # not happy with that. output is not what I like, or better, there are forms in there I do
    # not like.
    results = []
    chara_length = 3
    # while chara_length < 34:
    #     for item in micro_dict:
    #         if item["character_length"] == chara_length:
    #             results.append(item["microtoponym"])
    #
    #             chara_length = chara_length + 1
    # if chara_length == 34: # anything bigger than 34 takes way too long to calculate. In fact, it seems not to stop!
    #     for item in micro_dict:
    #         if item["character_length"] >= chara_length:
    #             results.append(item["microtoponym"])
    #
    #             # chara_length = chara_length + 1
    while chara_length in range(3, 34):
        for item in micro_dict:
            # for chara_length in range(item["character_length"]): # Takes way too long to calculate!
            # if item["character_length"] == chara_length:  # This is an if loop, so it will only show one instance each time.
            results.append(item["microtoponym"])
            chara_length = chara_length + 1
    # for item in micro_dict:
    #     if item["character_length"] == 37:
    #         results.append(item["microtoponym"])
    #     if item["character_length"] == 38:
    #         results.append(item["microtoponym"])
    #     if item["character_length"] == 43:
    #         results.append(item["microtoponym"])


    return results
# ---- UNDER DEVELOPMENT!!!----


# print(*SortByCharaLength(), sep='\n')










# ---- UNDER DEVELOPMENT!!!----
def MainCharaLength(n): # queries for the length of the primary (semantically most relevant) element of a microtoponym.
    # It is assumed, due to germanic syntactical rules, that this primary element is also the last in sequence.
    results = []
    for item in micro_dict:
        if item["sequence_length"] > 1:
            new_item = re.split(" ", item["microtoponym"])
            if len(new_item[-1]) == n:
                results.append(item['microtoponym'])
        else:
            if item["character_length"] == n:
                results.append(item['microtoponym'])
    return results
# ---- UNDER DEVELOPMENT!!!----


# ---- UNDER DEVELOPMENT!!!----
def MaxCharaLength(n): # looks for the longuest character sequence in any syntactic element of a microtoponym.

    # Does not work yet!!!!
    results = []
    for item in micro_dict:
        if item["sequence_length"] > 1:
            new_item = re.split(" ", item["microtoponym"])
            for var in new_item[:-1]:
                if len(var) == n:
                    pass
                if len(var[:-1]) > len(new_item[-1]):
                    if len(new_item[-1]) == n:
                        pass


                    else:
                        if len(var) == n:
                            results.append(item['microtoponym'])
                else:
                    if len(new_item[-1]) == n:
                        results.append(item['microtoponym'])
        else:
            if item["character_length"] == n:
                results.append(item['microtoponym'])
    return results
# ---- UNDER DEVELOPMENT!!!----





def simplex(name):
    results = []
    for x in micro_dict:
        if name == x['microtoponym']:
            results.append(x['microtoponym'])
    return results

# print(simplex('Wangert'))

def KVG(KVG): # Kompositionsvorderglied; needs a specified dictionary outside of the
    # function. Is looking for the front element of a composition, indexing the official name of the macrotoponym.
    results = []
    for x in micro_dict:
        # if x['microtoponym'] == KVG:
        #     continue
        if x['microtoponym'].startswith(KVG) == True:
            results.append(x['microtoponym'])

    return results

# print(*KVG('Wangert'), sep='\n')
# print('-' * 40)

def KHG(KHG): # Kompositionshinterglied; needs a specified dictionary outside of the
    # function. Is looking for the front element of a composition, indexing the official name of the macrotoponym.
    # Up to now, there is a minor bug in this function. If the query is capitalized, the results will be different
    # syntactic units where the query is the last. So this bug actually returns the queried word in a simplex, but in a
    # syntactic unit higher than 1.
    # If the query is in minuscules, the function returns morphological KHG.
    results = []
    for x in micro_dict:
        if x['microtoponym'].endswith(KHG) == True:
            results.append(x['microtoponym'])

    return results

# print(*KHG('bësch'), sep='\n')



def nameLookUp(name): # needs a specified dictionary outside of the function.
    # Is looking for any microtoponym with name in it.
    results = []
    for x in micro_dict:
        if name.lower() in x['microtoponym'].lower():
            results.append(x['microtoponym'])

    return results


def HowManyAre(name):
    return len(nameLookUp(name))


# print(*nameLookUp('Wangert'), sep="\n")
# print(HowManyAre("Wangert"))








def nameLookUpCoor(name): # needs a specified dictionary outside of the function.
    # Is looking for any microtoponym with name in it.
    # returns a dictionary
    results = []
    for x in micro_dict:
        if name.lower() in x['microtoponym'].lower():
            # results.append({'name': x['microtoponym'], 'coorset': x['coordinate_set']})
            results.append('{} {}'.format(x['microtoponym'], x['coordinate_set']))
    return results


# print(*nameLookUpCoor('Frauen'), sep='\n')






def nameLookUp_syntax(name, syntactic_length=None): # needs a specified dictionary outside of the function.
    # Is looking for any microtoponym with name in it.
    # syntactic_length restricts the search to any such microtoponyms that have n syntactic units.
    # min=1, max=7. If not specified (or None), syntactic_length is set to all possible lengths.
    results = []
    for x in micro_dict:
        if syntactic_length is None:
            if name.lower() in x['microtoponym'].lower():
                results.append(x['microtoponym'])
        else:
            if syntactic_length == x['sequence_length']:
                if name.lower() in x['microtoponym'].lower():
                    results.append(x['microtoponym'])
    return results


# print(*nameLookUp_syntax('Wangert', 3), sep='\n')
# print(*nameLookUp_syntax('Bësch', 1), sep='\n')




def HowManyAre_syntax(name, syntactic_length):
    return len(nameLookUp_syntax(name, syntactic_length))

# print(HowManyAre_syntax('Wangert', 3))


# ----Under construction!----
def nameLookUp_morphology(name, syntactic_length, morphology=None): # looks for correlation of syntactic length and
    # morphological build.
    # syntactic_length: min=1, max=7.
    # morphology: args: simplex, KVG, KHG.
    # results = []
    # if morphology is None:
    #     results.append(nameLookUp_syntax(name, syntactic_length))
    # else:
    # for item in micro_dict:
    #     if syntactic_length == item['sequence_length']:
    # if morphology == simplex:
    # new_input = nameLookUp_syntax(name, syntactic_length).split()
    # return simplex(new_input)
    # if simplex(nameLookUp_syntax(name, syntactic_length)) is True:
    # for item in micro_dict:
    #     if syntactic_length == item['sequence_length']:
    #         if name.lower() in item['microtoponym'].lower():
    #             if name == item['microtoponym']:
    #                 results.append(item['microtoponym'])

    # else:
    #     return 'Simplex Error, Will Robinson'
    # elif morphology == KVG:
    #     # new_input = nameLookUp_syntax(name, syntactic_length).split()
    #     # return KVG(new_input)
    #     # return KVG(name)
    #     for item in micro_dict:
    #         if syntactic_length == item['sequence_length']:
    #             return KVG(name)
    # elif morphology == KHG:
    #     # new_input = nameLookUp_syntax(name, syntactic_length).split()
    #     # return KHG(new_input)
    #     # return KHG(name)
    #     for item in micro_dict:
    #         if syntactic_length == item['sequence_length']:
    #             return KHG(name)
    # else:
    #     return 'Error, Error, Will Robinson'

    # if nameLookUp_syntax(name, syntactic_length) is True:
    # if morphology == 'simplex':
    #     return simplex(nameLookUp_syntax(name, syntactic_length))
    # if morphology == 'KVG':
    #     return KVG(nameLookUp_syntax(name, syntactic_length))
    # if morphology == 'KHG':
    #     return KHG(nameLookUp_syntax(name, syntactic_length))
    # if morphology is None:
    #     return nameLookUp_syntax(name, syntactic_length)


    if morphology == 'simplex':
        # put in intersection of simplex(name) and nameLookUp_Syntax(name, n)
        for i in  nameLookUp_syntax(name, syntactic_length): # and simplex(name):
            return simplex(i)
    if morphology == 'KVG':
        for i in nameLookUp_syntax(name, syntactic_length): # and KVG(name):
            return KVG(i)
    if morphology == 'KHG':
        for i in nameLookUp_syntax(name, syntactic_length): # and KHG(name):
            return KHG(i)
    if morphology is None:
        return nameLookUp_syntax(name, syntactic_length)

    # return results
# ----Under construction!----


# print(*nameLookUp('roden'), sep="\n")
# print()
# print(HowManyAre_syntax("Bongert", 1))
# print()


# print('=' * 40)
# print(nameLookUp_morphology("Wangert", 5, 'KVG')) # This seems only to work with syntactic length of 1.
# print(*nameLookUp_morphology("bësch", 2, KVG), sep='\n') # This does not seem to work yet, as it seems to ignore the
# queried syntactic length.










# def writeGeojson(name):
#     # data is a dictionary not yet encoded.
#     with open('query.geojson', 'w', encoding='utf-8') as output_file:
#         json.dump(data, output_file)

# print(nameLookUpCoor('Bongert'))




def NameLookUpGEOJson(name, _data_file): # Does this actually work? I would need to be able to format it so that the right input
    # is always selected. But how does that work with that many curly brackets?
    pass
    # results = []
# first dump to json file: this can only happen once!
#     {
#         "act_pcn_toponymes_0": {
#             "type": "FeatureCollection",
#             "features": [

# # then the for loop, it inserts every instances to the json file.
#
#     for x in micro_dict:
#         if name.lower() in x['microtoponym'].lower():
#             results.append('{} {}'.format(x['microtoponym'], x['coordinate_set']))
#             return results
# {
# 	"microtop_NameLookUp" : {
# 		"type" : "FeatureCollection",
# 		"features" : [
#
# {
# 				"type" : "Feature",
# 				"geometry" : {
# 					"type" : "LineString",
# 					"coordinates" : [
# 						[ 5.7529837128488088, 49.809752975261524 ],
# 						[ 5.7531353595761159, 49.809759652432064 ]
# 					]
# 				},
# 				"properties" : {
# 					"SHAPE.LEN" : 10.940702268136199,
# 					"OBJECTID" : 7920,
# 					"GROESSE" : 1,
# 					"FEATURELINK" : "",
# 					"LABEL" : "Route d'Arlon",
# 					"ANFINDEX" : "",
# 					"ENDINDEX" : "",
# 					"JUSTIFICATION" : "CH"
# 				}
# 			},
#
# # Then the loop will end and the end of the json file has to be written, so that it works.
#
# ]
# 	}
# }
#
#
# # gotta see then...

#
#     data_feed = {}
#
#     data_feed['microtop_output'] = []
#     data_feed['microtop_output']['features'] = []
#     data_feed['microtop_output']['features']['properties'] = []
#     data_feed['microtop_output']['features']['properties']['LABEL'] = []
#     data_feed['microtop_output']['features']['geometry'] = []
#     data_feed['microtop_output']['features']['geometry']['coordinates'] = []
#
#
#     for item in micro_dict:
#         if name == item['microtoponym']:
#             data_feed['microtop_output']['features']['properties']['LABEL'].append({'microtoponym': item['microtoponym']})
#
#             data_feed['microtop_output']['features']['geometry']['coordinates'].append({'coordinates': item['coordinate_set']})
#
#
#
#     with open(_data_file, 'w') as outfile:
#         json.dump(data_feed, outfile)
#
#
#
# # NameLookUpGEOJson('Wangert', 'data_feed_wangert.geojson') # does not work :(:(:(:(:(:(:(
#
#
#
#
# for item in micro_dict:
#     names = item['microtoponym']
#     splitNames = names.split()
#
#
# # print(*micro_dict, sep='\n')
#
# search_dict = []
#
# with open('geoportail/act_pcn_toponymes.geojson', encoding='utf-8') as data_file:
#
#     data = json.load(data_file)
#
#     for feature in data['act_pcn_toponymes_0']['features']:
#         search_dict.append(feature['properties']['LABEL'])
#
#     for feature in data['act_pcn_toponymes_1']['features']:
#         search_dict.append(feature['properties']['LABEL'])
#
#
# topo_set = set(search_dict)
# dict_string = str(search_dict)
# split_string = dict_string.split()
#
#


# look into collections!
#
# import collections
#
# creatures = ['Jinn', 'Ghoul', 'Jinn', 'Angel', 'Ifrit', 'Ghoul', 'Buraq', 'Jinn']
# print(collections.Counter(creatures))