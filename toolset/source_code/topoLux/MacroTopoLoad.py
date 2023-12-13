import re
# import pandas


# use pandas to read the excell file.



topo_dict = [] # a dictionary of toponyms. Is outside of function so all functions can access it.

# with open("MacroTopoLoad/localites_et_lieux_avec_coordonnees_v2017-4.xls", "r") as evidence: # opens the .txt file that has the linguistic data in it.
#     # Here the data about macrotoponymy from the data.public.lu is used. The excel file was transformed in a tab
#     # separated values txt file which is then read. Every line contains the following data of a certain macrotoponym;
#     # the official name, the luxembourgish name, the name of the administrative commune, the name of the cadastral
#     # commune or district, a y coordinate, an x coordinate, a longitude and a latitude.
#     for line in evidence.readlines():
#         line = line.split()
#         official_name, dialect_name, adm_comm2, cad_comm2, y_co2, x_co2, long2, lat2 = tuple(line) # splits the results
#         # in a tuple so that every item can be read and accessed separately
#         long2 = re.sub(',', '.', long2)
#         lat2 = re.sub(',', '.', lat2)
#         topo_dict.append(dict({"OfficialName": official_name,
#                                "DialectName": dialect_name,
#                                "AdministrativeCommune": adm_comm2,
#                                "CadastralCommune": cad_comm2,
#                                "YCoordinate": y_co2,
#                                "XCoordinate": x_co2,
#                                "Longitude": long2,
#                                "Latitude": lat2})) # topo_dict is appended by the data of the tuple as created before.

