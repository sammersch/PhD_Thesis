from MicroTopoLoad import microToponyms
from MicroTopoLoadAllData import microTopoAll




def geoJsonExporterSimple(lookupName, _dict):
    with open('JsonExport/Name/Name_' + lookupName + '.geojson', 'w', encoding='utf-8') as data_file:
        data_file.write('{"type" : "FeatureCollection", ')
        # data_file.write('"name": ' + str(lookupName) + ', ')
        # data_file.write('"crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:EPSG::2169" } }, ')
        data_file.write('"features" : [')
        for item in _dict:
            # if lookupName in item['name']:
            if lookupName.lower() in item['name'].lower():
                data_file.write('{"type":"Feature","geometry":{"type":"LineString","coordinates": ' )
                data_file.write(str(item['coordinates']))
                data_file.write('},"properties":{')
                data_file.write('"SHAPE.LEN":"')
                data_file.write(str(item['shape_length']))
                data_file.write('","OBJECTID": ')
                data_file.write(str(item['object_ID']))
                data_file.write(', "GROESSE" : 1, "FEATURELINK" : "", "LABEL" : "')
                data_file.write(str(item['name']))
                data_file.write('", "ANFINDEX" : "", "ENDINDEX" : "", "JUSTIFICATION" : "CH"}},')
        data_file.write(']}')

abc = 'aäbcdeéëfghijklmnoöpqrstuüövwxyz'

# requestString = 'Affe Maerel Ameisen Ames Bär Beer Baier Baumläuferchen Bibesch Biwesch Be Beien Honig Dachs Intges Inte Innen Esel Eil Ail Ell Echhel Uhl Eul Fock  Fisch Fesch Fresch Kröte Krotte Mouk Onk Fuhs Fous Fuse Fuss Hase Huse Hoise Hirz Hirsch Hierz Huhn Hahn Hühn Hinkel Hinger Poellen Zechen Hund Kater Kuder Katze Hons Hond Igel Kaefe Kaatz Koder Kockel Kuckuck Kuh Küh  Ochs Oisse Ranner Kalbe Kalwe Kribs Mauluf Moll Maulup Maus Mäus Meis Mücke Ferden Perd Pferd Kuob Kob Koib Doil Kre Kreh Kreckel Räup Reh Geis Geiß Bock Hermes Betschel Bitschen Kietz Schaf Hammel Laamert Wider Schwein Sau Bier Beiren Karmesch Dauw Kauter Daub Tier Thier Vieh Vogel Sänger Wolf Wuremt Wurmes'
#
# request = requestString.split()
# for item in request:
#     geoJsonExporterSimple(item, microTopoAll)


def geoJsonExporterSection(section, _dict): # This function has been upgraded so that it writes CRS to json file too.
    with open('JsonExport/Section/Section_' + section + '.geojson', 'w', encoding='utf-8') as data_file:
        data_file.write('{"type" : "FeatureCollection", ')
        data_file.write('"name": ' + str(section) + ', ')
        data_file.write('"crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:EPSG::2169" } }, ')
        data_file.write('"features" : [')
        for item in _dict:
            if item['section'] == section:
                data_file.write('{"type":"Feature","geometry":{"type":"LineString","coordinates": ' )
                data_file.write(str(item['coordinates']))
                data_file.write('},"properties":{')
                data_file.write('"SHAPE.LEN":"')
                data_file.write(str(item['shape_length']))
                data_file.write('","OBJECTID": ')
                data_file.write(str(item['object_ID']))
                data_file.write(', "GROESSE" : 1, "FEATURELINK" : "", "LABEL" : "')
                data_file.write(str(item['name']))
                data_file.write('", "ANFINDEX" : "", "ENDINDEX" : "", "JUSTIFICATION" : "CH"}},')
        data_file.write(']}')


def geoJsonExporterAdmComm(commune, _dict):
    with open('JsonExport/Commune/Commune_' + commune + '.geojson', 'w', encoding='utf-8') as data_file:
        data_file.write('{"type" : "FeatureCollection", ')
        data_file.write('"name": ' + str(commune) + ', ')
        data_file.write('"crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:EPSG::2169" } }, ')
        data_file.write('"features" : [')
        for item in _dict:
            if item['adm_comm'] == commune:
                data_file.write('{"type":"Feature","geometry":{"type":"LineString","coordinates": ')
                data_file.write(str(item['coordinates']))
                data_file.write('},"properties":{')
                data_file.write('"SHAPE.LEN":"')
                data_file.write(str(item['shape_length']))
                data_file.write('","OBJECTID": ')
                data_file.write(str(item['object_ID']))
                data_file.write(', "GROESSE" : 1, "FEATURELINK" : "", "LABEL" : "')
                data_file.write(str(item['name']))
                data_file.write('", "ANFINDEX" : "", "ENDINDEX" : "", "JUSTIFICATION" : "CH"}},')
        data_file.write(']}')

# geoJsonExporterSection('Larochette', microTopoAll)

# search_list = ['Barriere', 'Barrière', 'Berger', 'Driecht', 'Fähr', 'Gaas', 'Gass', 'Gäss', 'Keem', 'Kemecht', 'Kemel',
#                'Kemend', 'Kemicht', 'Kiem', 'Paad', 'Pad', 'Pfad', 'Pfaad', 'Pied', 'Fad', 'Pavé', 'Pawai', 'Renn',
#                'Ritt', 'Sperr', 'Stenge', 'Stras', 'Straß', 'Stroos', 'Stros', 'Strooß', 'Stroß', 'Umweg', 'ëmwe',
#                'ëmwé', 'Wé', 'Wee', 'Weg', 'Fahr', 'Furt', 'Stei', 'Kehr', 'Kéier', 'Bé', 'Bee', 'Biege', 'Scheub',
#                'Weiser', 'Poteau', 'Poto', 'Brück', 'Breck', 'Bréck', 'Steg', 'Hafen']
#
#
# search_list = ['Kräiz', 'Kreuz', 'Kreiz', 'Kreutz', 'Kréiz', 'Kreutz', 'Kruemm', 'Krümm', 'Kromm', 'Fur', 'Kritz',
#                'Kraiz', 'Kroem', 'Krätz', 'Krëmm', 'Kräitz']
# search_list = ['Paat', 'Pat', 'Béien']
# for item in search_list:
#     geoJsonExporterSimple(item, microTopoAll)
#
# for item in microTopoAll:
#     if 'paat' in item['name'].split()[-1].lower():
#         print(item['name'])