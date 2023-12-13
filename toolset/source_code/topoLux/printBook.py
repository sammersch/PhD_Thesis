import os

from MicroTopoLoadAllData import microTopoAll

newItemList = []
newList = []
exceptionsList = []
# newListCut = []
for item in microTopoAll:
    if item['name'].split()[-1].islower():
        # newItem = item['name'].split()[-2]
        exceptionsList.append((item['name'], item['object_ID'], item['section'], item['adm_comm'], item['coordinateOne']))
        continue
    if item['name'].lower().startswith('zone indus'):
        newItem = item['name'].split()[-2]
    # elif item['name'].split()[-1].islower():
    #     newItem = item['name'].split()[-2]
    if item['name'].lower().split()[-1].startswith('d\''):
        newItem = item['name'].split()[-1].lstrip('d\'')
    else:
        newItem = item['name'].split()[-1]
    newItemList.append(newItem)
    newList.append((newItem, item['name'], item['object_ID'], item['section'], item['adm_comm'], item['coordinateOne']))



def print_by_letter(directory='perLetter'):
    if not os.path.exists('topoSearch/' + directory):
        os.makedirs('topoSearch/' + directory)
    firstCharas = []
    for jtem in newItemList:
        if jtem[0].lower() not in firstCharas:
            firstCharas.append(jtem[0].lower())

    for htem in firstCharas: # this generates several files according to the first letter of the semantic main element

        with open('topoSearch/' + directory + '/' + htem.upper() + '.csv', 'w', encoding='utf-8') as dump:
            dump.write('Lemma,Name,ObjectID,Section,Commune,Long,Lat\n')
            for item in sorted(newList):
                if item[0].lower().startswith(htem.lower()):
                    dump.write(str(item[0]) + ',' + str(item[1]) + ',' + str(item[2])+ ',' + str(item[3])+ ',' + str(item[4])+ ',' + str(item[5]).lstrip('[').rstrip(']') + '\n')
        dump.close()



def print_whole(file_name='All_Items'):
    with open('topoSearch/' + file_name + '.csv', 'w', encoding='utf-8') as dump:
        dump.write('Lemma,Name,ObjectID,Section,Commune,Long,Lat\n')
        for item in sorted(newList):
            dump.write(str(item[0]) + ',' + str(item[1]) + ',' + str(item[2])+ ',' + str(item[3])+ ',' + str(item[4])+ ',' + str(item[5]).lstrip('[').rstrip(']') + '\n')
    dump.close()


nubi = []

for item in newItemList:
    if item not in nubi:
        nubi.append(item)


KHG_Queryed = []
KVG_Queryed = []
Lemmata_Removed = []
Lemmata_Remaining = nubi
StrippedFromKHG = []
StrippedFromKVG = []


def KHGRemover(quEry):
    global KHG_Queryed
    global Lemmata_Removed
    global Lemmata_Remaining
    KHG_Queryed.append(quEry)
    for item in nubi:
        item = item.lstrip(' ')
        item = item.rstrip(' ')
        if item.lower().endswith(quEry.lower()):
            Lemmata_Removed.append(item)
            Lemmata_Remaining.remove(item)
    # return len(Lemmata_Removed), len(Lemmata_Remaining)
    # print(len(Lemmata_Removed), len(Lemmata_Remaining))



def KVGRemover(quEry):
    global KVG_Queryed
    global Lemmata_Removed
    global Lemmata_Remaining
    KVG_Queryed.append(quEry)
    for item in nubi:
        item = item.lstrip(' ')
        item = item.rstrip(' ')
        if item.lower().startswith(quEry.lower()):
            Lemmata_Removed.append(item)
            Lemmata_Remaining.remove(item)
    # return len(Lemmata_Removed), len(Lemmata_Remaining)
    # print(len(Lemmata_Removed), len(Lemmata_Remaining))


def KHG_as_KVG():
    global KVG_Queryed
    global KHG_Queryed
    global Lemmata_Removed
    global Lemmata_Remaining
    # KVG_Queryed.append(quEry)
    for jtem in KHG_Queryed:

        for item in nubi:
            item = item.lstrip(' ')
            item = item.rstrip(' ')
            if item.lower().startswith(jtem.lower()):
                Lemmata_Removed.append(item)
                Lemmata_Remaining.remove(item)
                KVG_Queryed.append(jtem)


def KVG_as_KHG():
    global KVG_Queryed
    global KHG_Queryed
    global Lemmata_Removed
    global Lemmata_Remaining
    # KVG_Queryed.append(quEry)
    for jtem in KVG_Queryed:

        for item in nubi:
            item = item.lstrip(' ')
            item = item.rstrip(' ')
            if item.lower().startswith(jtem.lower()):
                Lemmata_Removed.append(item)
                Lemmata_Remaining.remove(item)
                KHG_Queryed.append(jtem)





# write function: if item in name, if jtem in KHG, if item.endswith(jtem), item.rstrip(jtem)

def lemmaBySplitKHG():
    global StrippedFromKHG
    global KVG_Queryed
    global KHG_Queryed
    global Lemmata_Removed
    global Lemmata_Remaining
    for item in nubi:
        for jtem in KHG_Queryed:
            if item.endswith(jtem):
                StrippedFromKHG.append(str(item.rstrip(jtem)) + '\t\t--\t' + str(jtem))

# and vice versa for KVG
def lemmaBySplitKVG():
    global StrippedFromKVG
    global KVG_Queryed
    global KHG_Queryed
    global Lemmata_Removed
    global Lemmata_Remaining
    for item in nubi:
        for jtem in KVG_Queryed:
            if item.startswith(jtem):
                StrippedFromKVG.append(str(item.lstrip(jtem)) + '\t\t--\t' + str(jtem))


# # print(len(nubi))
# KHGRemover('gruecht')
# KHGRemover('gracht')
# KHGRemover('groicht')
# KHGRemover('uecht')
# KHGRemover('acht')
# KHGRemover('oicht')
# KHGRemover('brill')
# KHGRemover('haff')
# KHGRemover('weg')
# KHGRemover('wies')
# KHGRemover('busch')
# KHGRemover('bach')
# KHGRemover('berg')
# KHGRemover('hoecht')
# KHGRemover('feld')
# KHGRemover('dell')
# KHGRemover('delt')
# KHGRemover('heck')
# KHGRemover('bour')
# KHGRemover('garten')
# KHGRemover('hof')
# KHGRemover('pesch')
# KHGRemover('millen')
# KHGRemover('gasse')
# KHGRemover('wroch')
# KHGRemover('waach')
# KHGRemover('wis')
# KHGRemover('kréiz')
# KHGRemover('wiesen')
# KHGRemover('bärig')
# KHGRemover('haed')
# KHGRemover('gärtchen')
# KHGRemover('grof')
# KHGRemover('mühle')
# KHGRemover('felder')
# KHGRemover('hecken')
# KHGRemover('schmelz')
# KHGRemover('bësch')
# KHGRemover('graecht')
# KHGRemover('sack')
# KHGRemover('gründchen')
# KHGRemover('driesch')
# KHGRemover('dorf')
# KHGRemover('laecher')
# KHGRemover('bungert')
# KHGRemover('haeuser')
# KHGRemover('bruck')
# KHGRemover('garten')
# KHGRemover('stück')
# KHGRemover('aak')
# KHGRemover('bongert')
# KHGRemover('baumchen')
# KHGRemover('busch')
# KHGRemover('kopp')
# KHGRemover('buesch')
# KHGRemover('heid')
# KHGRemover('langent')
# KHGRemover('baeumchen')
# KHGRemover('apfelbaum')
# KHGRemover('lach')
# KHGRemover('lei')
# KHGRemover('berg')
# KHGRemover('knap')
# KHGRemover('hals')
# KHGRemover('mauer')
# KHGRemover('boesch')
# KHGRemover('wois')
# KHGRemover('feldchen')
# KHGRemover('büsch')
# KHGRemover('schleidchen')
# KHGRemover('bour')
# KHGRemover('kaulen')
# KHGRemover('bësch')
# KHGRemover('gart')
# KHGRemover('deltchen')
# KHGRemover('driescher')
# KHGRemover('wee')
# KHGRemover('bur')
# KHGRemover('loch')
# KHGRemover('bierg')
# KHGRemover('kaul')
# KHGRemover('gruef')
# KHGRemover('birebam')
# KHGRemover('grond')
# KHGRemover('dréischer')
# KHGRemover('dalt')
# KHGRemover('wiss')
# KHGRemover('wues')
# KHGRemover('dréisch')
# KHGRemover('dall')
# KHGRemover('holz')
# KHGRemover('broch')
# KHGRemover('baach')
# KHGRemover('köpchen')
# KHGRemover('weg')
# KHGRemover('floerchen')
# KHGRemover('haischen')
# KHGRemover('gruendchen')
# KHGRemover('haeuschen')
# KHGRemover('dörner')
# KHGRemover('weiler')
# KHGRemover('häuschen')
# KHGRemover('land')
# KHGRemover('lay')
# KHGRemover('wald')
# KHGRemover('bäumchen')
# KHGRemover('pfad')
# KHGRemover('paat')
# KHGRemover('hiwel')
# KHGRemover('flur')
# KHGRemover('wangert')
# KHGRemover('schleidgen')
# KHGRemover('grundchen')
# KHGRemover('felder')
# KHGRemover('bueschelchen')
# KHGRemover('hoff')
# KHGRemover('gaarden')
# KHGRemover('bourn')
# KHGRemover('wangerten')
# KHGRemover('griecht')
# KHGRemover('strasse')
# KHGRemover('bach')
# KHGRemover('stueck')
# KHGRemover('kreuz')
# KHGRemover('heck')
# KHGRemover('bierg')
# KHGRemover('dränk')
# KHGRemover('hoehe')
# KHGRemover('band')
# KHGRemover('feld')
# KHGRemover('wohs')
# KHGRemover('wenkel')
# KHGRemover('püllen')
# KHGRemover('huebel')
# KHGRemover('deel')
# KHGRemover('hofen')
# KHGRemover('pull')
# KHGRemover('grund')
# KHGRemover('bruch')
# KHGRemover('thal')
# KHGRemover('pehlen')
# KHGRemover('thael')
# KHGRemover('dell')
# KHGRemover('moir')
# KHGRemover('bergen')
# KHGRemover('bitt')
# KHGRemover('kapp')
# KHGRemover('moor')
# KHGRemover('bärig')
# KHGRemover('pohl')
# KHGRemover('baum')
# KHGRemover('peschen')
# KHGRemover('grund')
# KHGRemover('knaepchen')
# KHGRemover('floos')
# KHGRemover('riecht')
# KHGRemover('griécht')
# KHGRemover('weeg')
# KHGRemover('paad')
# KHGRemover('huewen')
# KHGRemover('drüsch')
# KHGRemover('winkel')
# KHGRemover('tal')
# KHGRemover('knapp')
# KHGRemover('muehle')
# KHGRemover('aecker')
# KHGRemover('hooh')
# KHGRemover('berger')
# KHGRemover('buesch')
# KHGRemover('haus')
# KHGRemover('brück')
# KHGRemover('woos')
# KHGRemover('ahl')
# KHGRemover('knöpgen')
# KHGRemover('birchen')
# KHGRemover('muehle')
# KHGRemover('schleid')
# KHGRemover('dahl')
# KHGRemover('woas')
# KHGRemover('knaeppchen')
# KHGRemover('weiherchen')
# KHGRemover('baeumchen')
# KHGRemover('wasser')
# KHGRemover('zoll')
# KHGRemover('kreutz')
# KHGRemover('peesch')
# KHGRemover('delt')
# KHGRemover('ställen')
# KHGRemover('riédgen')
# KHGRemover('kummer')
# KHGRemover('wies')
# KHGRemover('chleid')
# KHGRemover('groiht')
# KHGRemover('looch')
# KHGRemover('weyer')
# KHGRemover('brätchen')
# KHGRemover('baeumen')
# KHGRemover('berech')
# KHGRemover('hiwel')
# KHGRemover('kraezer')
# KHGRemover('broch')
# KHGRemover('knopf')
# KHGRemover('aul')
# KHGRemover('auel')
# KHGRemover('biereg')
# KHGRemover('buedem')
# KHGRemover('muehlen')
# KHGRemover('säif')
# KHGRemover('gritt')
# KHGRemover('stücker')
# KHGRemover('hoelzer')
# KHGRemover('dellchen')
# KHGRemover('mörchen')
# KHGRemover('grächt')
# KHGRemover('büch')
# KHGRemover('kamp')
# KHGRemover('houscht')
# KHGRemover('steg')
# KHGRemover('buch')
# KHGRemover('platz')
# KHGRemover('wisen')
# KHGRemover('köppchen')
# KHGRemover('mühl')
# KHGRemover('wasser')
# KHGRemover('weiher')
# KHGRemover('dierchen')
# KHGRemover('schlaedchen')
# KHGRemover('schläd')
# KHGRemover('weihern')
# KHGRemover('dréischter')
# KHGRemover('burn')
# KHGRemover('schleidchen')
# KHGRemover('bouren')
# KHGRemover('héicht')
# KHGRemover('gaart')
# KHGRemover('thaell')
# KHGRemover('grëndchen')
# KHGRemover('pillen')
# KHGRemover('waeldchen')
# KHGRemover('diérchen')
# KHGRemover('furt')
# KHGRemover('wieschen')
# KHGRemover('fels')
# KHGRemover('bur')
# KHGRemover('boden')
# KHGRemover('gintz')
# KHGRemover('buren')
# KHGRemover('kopf')
# KHGRemover('schleiden')
# KHGRemover('haart')
# KHGRemover('flass')
# KHGRemover('weiher')
# KHGRemover('plon')
# KHGRemover('hischtgen')
# KHGRemover('buedem')
# KHGRemover('steg')
# KHGRemover('wäldgen')
# KHGRemover('kämpgen')
# KHGRemover('faad')
# KHGRemover('lee')
# KHGRemover('reech')
# KHGRemover('fenn')
# KHGRemover('mühl')
# KHGRemover('pesch')
# KHGRemover('schlaedchen')
# KHGRemover('loecher')
# KHGRemover('schleidchen')
# KHGRemover('bann')
# KHGRemover('aker')
# KHGRemover('knöpchen')
# KHGRemover('kräiz')
# KHGRemover('koll')
# KHGRemover('buch')
# KHGRemover('gaart')
# KHGRemover('bosch')
# KHGRemover('rueder')
# KHGRemover('hoeh')
# KHGRemover('dällt')
# KHGRemover('boden')
# KHGRemover('grächt')
# KHGRemover('grâcht')
# KHGRemover('knopp')
# KHGRemover('juenkt')
# KHGRemover('kreutz')
# KHGRemover('kopf')
# KHGRemover('weiher')
# KHGRemover('burg')
# KHGRemover('waeldchen')
# KHGRemover('hiewen')
# KHGRemover('hurt')
# KHGRemover('pelt')
# KHGRemover('reech')
# KHGRemover('bich')
# KHGRemover('knipp')
# KHGRemover('tomm')
# KHGRemover('boechel')
# KHGRemover('wäldchen')
# KHGRemover('weltchen')
# KHGRemover('weier')
# KHGRemover('knupp')
# KHGRemover('grouf')
# KHGRemover('schleiddchen')
# KHGRemover('riéch')
# KHGRemover('schnack')
# KHGRemover('dällt')
# KHGRemover('rueder')
# KHGRemover('gewan')
# KHGRemover('ritt')
# KHGRemover('ley')
# KHGRemover('knoeppchen')
# KHGRemover('dickt')
# KHGRemover('haar')
# KHGRemover('pullen')
# KHGRemover('kiel')
# KHGRemover('gruf')
# KHGRemover('staellchen')
# KHGRemover('schleed')
# KHGRemover('dellchen')
# KHGRemover('looch')
# KHGRemover('schloss')
# KHGRemover('lambicht')
# KHGRemover('eck')
# KHGRemover('hoerchen')
# KHGRemover('schlaed')
# KHGRemover('maierchen')
# KHGRemover('ginst')
# KHGRemover('dellt')
# KHGRemover('scheedchen')
# KHGRemover('dorn')
# KHGRemover('delchen')
# KHGRemover('héicht')
# KHGRemover('knäppchen')
# KHGRemover('mühlen')
# KHGRemover('grëndchen')
# KHGRemover('kreuz')
# KHGRemover('pad')
# KHGRemover('kämmchen')
# KHGRemover('kamp')
# KHGRemover('därchen')
# KHGRemover('kräiz')
# KHGRemover('kirch')
# KHGRemover('muehlen')
# KHGRemover('lae')
# KHGRemover('auel')
# KHGRemover('houscht')
# KHGRemover('béchel')
# KHGRemover('bierken')
# KHGRemover('stein')
# KHGRemover('krätz')
# KHGRemover('laeah')
# KHGRemover('laeh')
# KHGRemover('wies')
# KHGRemover('gaas')
# KHGRemover('haard')
# KHGRemover('howen')
# KHGRemover('biirchen')
# KHGRemover('päsch')
# KHGRemover('wiss')
# KHGRemover('stiedchen')
# KHGRemover('gass')
# KHGRemover('lächelchen')
# KHGRemover('rääch')
# KHGRemover('äärd')
# KHGRemover('grënnchen')
# KHGRemover('bÍsch')
# KHGRemover('stack')
# KHGRemover('stuecker')
# KHGRemover('stécker')
# KHGRemover('schleeden')
# KHGRemover('miirchen')
# KHGRemover('kailchen')
# KHGRemover('bäämchen')
# KHGRemover('duerf')
# KHGRemover('nascht')
# KHGRemover('holtz')
# KHGRemover('wee')
# KHGRemover('uwänner')
# KHGRemover('hiel')
# KHGRemover('gäertchen')
# KHGRemover('géieren')
# KHGRemover('gaass')
# KHGRemover('buerg')
# KHGRemover('steen')
# KHGRemover('strachen')
# KHGRemover('mound')
# KHGRemover('millen')
# KHGRemover('äcker')
# KHGRemover('bond')
# KHGRemover('buurg')
# KHGRemover('weier')
# KHGRemover('bäm')
# KHGRemover('sank')
# KHGRemover('feldgen')
# KHGRemover('rei')
# KHGRemover('gut')
# KHGRemover('baemchen')
# KHGRemover('lä')
# KHGRemover('bruch')
# KHGRemover('schett')
# KHGRemover('stän')
# KHGRemover('hoh')
# KHGRemover('stell')
# KHGRemover('Muehl')
# KHGRemover('steltchen')
# KHGRemover('lai')
# KHGRemover('leh')
# KHGRemover('kapelle')
# KHGRemover('stadt')
# KHGRemover('petz')
# KHGRemover('schet')
# KHGRemover('roeder')
# KHGRemover('burn')
# KHGRemover('hag')
# KHGRemover('ploentgen')
# KHGRemover('knob')
# KHGRemover('caut')
# KHGRemover('mäuerchen')
# KHGRemover('gleicht')
# KHGRemover('nack')
# KHGRemover('patz')
# KHGRemover('pescher')
# KHGRemover('stell')
# KHGRemover('scheidchen')
# KHGRemover('reis')
# KHGRemover('heidchen')
# KHGRemover('gewann')
# KHGRemover('hoppescht')
# KHGRemover('thaelchen')
# KHGRemover('béiwen')
# KHGRemover('hierchen')
# KHGRemover('ak')
# KHGRemover('haltz')
# KHGRemover('fad')
# KHGRemover('dränken')
# KHGRemover('briet')
# KHGRemover('ofen')
# KHGRemover('pil')
# KHGRemover('kehr')
# KHGRemover('daerchen')
# KHGRemover('tränk')
# KHGRemover('stecker')
# KHGRemover('kiesgen')
# KHGRemover('buodem')
# KHGRemover('bam')
# KHGRemover('kaeulchen')
# KHGRemover('grunn')
# KHGRemover('mehl')
# KHGRemover('hau')
# KHGRemover('halchen')
# KHGRemover('steinchen')
# KHGRemover('stoppeln')
# KHGRemover('buchen')
# KHGRemover('büsch')
# KHGRemover('weiser')
# KHGRemover('furt')
# KHGRemover('deld')
# KHGRemover('glecht')
# KHGRemover('scheid')
# KHGRemover('kellerchen')
# KHGRemover('loechelchen')
# KHGRemover('schnäpchen')
# KHGRemover('breis')
# KHGRemover('gaertchen')
# KHGRemover('rech')
# KHGRemover('hart')
# KHGRemover('boewen')
# KHGRemover('seit')
# KHGRemover('flass')
# KHGRemover('scheed')
# KHGRemover('ville')
# KHGRemover('béchel')
# KHGRemover('grond')
# KHGRemover('daen')
# KHGRemover('wénkel')
# KHGRemover('hoehl')
# KHGRemover('schesser')
# KHGRemover('bierg')
# KHGRemover('mouer')
# KHGRemover('spronk')
# KHGRemover('këpp')
# KHGRemover('mier')
# KHGRemover('schwanz')
# KHGRemover('schleedchen')
# KHGRemover('muer')
# KHGRemover('säitert')
# KHGRemover('panz')
# KHGRemover('dällchen')
# KHGRemover('bierchen')
# KHGRemover('stall')
# KHGRemover('schënner')
# KHGRemover('brich')
# KHGRemover('kiemert')
# KHGRemover('hëlzchen')
# KHGRemover('bech')
# KHGRemover('rausch')
# KHGRemover('stéck')
# KHGRemover('land')
# KHGRemover('schock')
# KHGRemover('matt')
# KHGRemover('längten')
# KHGRemover('deelen')
# KHGRemover('dällchen')
# KHGRemover('schläden')
# KHGRemover('äppelchen')
# KHGRemover('spéisser')
# KHGRemover('wénkel')
# KHGRemover('päärchen')
# KHGRemover('fur')
# KHGRemover('fouer')
# KHGRemover('längt')
# KHGRemover('stall')
# KHGRemover('scheier')
# KHGRemover('gewännchen')
# KHGRemover('bréck')
# KHGRemover('grond')
# KHGRemover('rued')
# KHGRemover('ställchen')
# KHGRemover('feldern')
# KHGRemover('mer')
# KHGRemover('stee')
# KHGRemover('häärchen')
# KHGRemover('stäerz')
# KHGRemover('rätchen')
# KHGRemover('lácher')
# KHGRemover('héien')
# KHGRemover('schlag')
# KHGRemover('däärchen')
# KHGRemover('liller')
# KHGRemover('Aa')
# KHGRemover('bämercher')
# KHGRemover('bëschelchen')
# KHGRemover('päerchen')
# KHGRemover('fiirzchen')
# KHGRemover('wasen')
# KHGRemover('stall')
# KHGRemover('hanz')
# KHGRemover('pont')
# KHGRemover('klapp')
# KHGRemover('géier')
# KHGRemover('satzéng')
# KHGRemover('léi')
# KHGRemover('hölzchen')
# KHGRemover('sang')
# KHGRemover('haufen')
# KHGRemover('zock')
# KHGRemover('wesch')
# KHGRemover('wiese')
# KHGRemover('jenkt')
# KHGRemover('aal')
# KHGRemover('mond')
# KHGRemover('spreit')
# KHGRemover('kohsselt')
# KHGRemover('birk')
# KHGRemover('banert')
# KHGRemover('ae')
# KHGRemover('bechel')
# KHGRemover('bürchen')
# KHGRemover('kuost')
# KHGRemover('frehn')
# KHGRemover('püllchen')
# KHGRemover('héight')
# KHGRemover('raedchen')
# KHGRemover('büschen')
# KHGRemover('herr')
# KHGRemover('fahrt')
# KHGRemover('pütz')
# KHGRemover('poul')
# KHGRemover('ratt')
# KHGRemover('beer')
# KHGRemover('mann')
# KHGRemover('ber')
# KHGRemover('bouch')
# KHGRemover('mühle')
# KHGRemover('stengchen')
# KHGRemover('büschelchen')
# KHGRemover('röder')
# KHGRemover('garbe')
# KHGRemover('thalchen')
# KHGRemover('buren')
# KHGRemover('nast')
# KHGRemover('pat')
# KHGRemover('hoven')
# KHGRemover('fuert')
# KHGRemover('strooss')
# KHGRemover('büscher')
# KHGRemover('gënst')
# KHGRemover('kuosten')
# KHGRemover('kaempgen')
# KHGRemover('rieder')
# KHGRemover('boidem')
# KHGRemover('bichelchen')
# KHGRemover('gredchen')
# KHGRemover('scheierchen')
# KHGRemover('thomm')
# KHGRemover('biedem')
# KHGRemover('drëf')
# KHGRemover('trëf')
# KHGRemover('hauf')
# KHGRemover('kuir')
# KHGRemover('büschel')
# KHGRemover('kessel')
# KHGRemover('dar')
# KHGRemover('bëscher')
# KHGRemover('kascht')
# KHGRemover('uuscht')
# KHGRemover('fëls')
# KHGRemover('fuer')
# KHGRemover('wäert')
# KHGRemover('äerd')
# KHGRemover('beemchen')
# KHGRemover('plaz')
# KHGRemover('bërg')
# KHGRemover('zohl')
# KHGRemover('flouer')
# KHGRemover('récker')
# KHGRemover('péilchen')
# KHGRemover('beem')
# KHGRemover('bännchen')
# KHGRemover('äker')
# KHGRemover('maart')
# KHGRemover('hoecht')
# KHGRemover('gaard')
# KHGRemover('zéien')
# KHGRemover('teil')
# KHGRemover('draff')
# KHGRemover('dang')
# KHGRemover('béch')
# KHGRemover('wëlt')
# KHGRemover('atzéngen')
# KHGRemover('männchen')
# KHGRemover('sprénger')
# KHGRemover('rauschen')
# KHGRemover('wäert')
# KHGRemover('ruechten')
# KHGRemover('wand')
# KHGRemover('määssen')
# KHGRemover('sterz')
# KHGRemover('onner')
# KHGRemover('fiels')
# KHGRemover('strachen')
# KHGRemover('flesschen')
# KHGRemover('wehr')
# KHGRemover('losen')
# KHGRemover('root')
# KHGRemover('bochen')
# KHGRemover('nohl')
# KHGRemover('bäum')
# KHGRemover('bichel')
# KHGRemover('loechelgen')
# KHGRemover('erdchen')
# KHGRemover('schaeppchen')
# KHGRemover('born')
# KHGRemover('hausen')
# KHGRemover('gronn')
# KHGRemover('bood')
# KHGRemover('lecker')
# KHGRemover('sprung')
# KHGRemover('wirtgen')
# KHGRemover('tref')
# KHGRemover('tuch')
# KHGRemover('traenk')
# KHGRemover('eckert')
# KHGRemover('richt')
# KHGRemover('haeding')
# KHGRemover('jengt')
# KHGRemover('brenner')
# KHGRemover('brüsch')
# KHGRemover('ginz')
# KHGRemover('gröndchen')
# KHGRemover('hälchen')
# KHGRemover('birchen')
# KHGRemover('delltchen')
# KHGRemover('muehlech')
# KHGRemover('koellchen')
# KHGRemover('drait')
# KHGRemover('knapp')
# KHGRemover('stuhl')
# KHGRemover('huef')
# KHGRemover('hirk')
# KHGRemover('buescher')
# KHGRemover('bick')
# KHGRemover('big')
# KHGRemover('mullen')
# KHGRemover('schleckt')
# KHGRemover('hëlz')
# KHGRemover('gruewen')
# KHGRemover('kaeppchen')
# KHGRemover('wéngerten')
# KHGRemover('berge')
# KHGRemover('heed')
# KHGRemover('griet')
# KHGRemover('loh')
# KHGRemover('heiden')
# KHGRemover('bënner')
# KHGRemover('daer')
# KHGRemover('kies')
# KHGRemover('baach')
# KHGRemover('wuurzel')
# KHGRemover('waasser')
# KHGRemover('taart')
# KHGRemover('zap')
# KHGRemover('rei')
# KHGRemover('bicht')
# KHGRemover('drenk')
# KHGRemover('stübchen')
# KHGRemover('gall')
# KHGRemover('au')
# KHGRemover('ecker')
# KHGRemover('berreg')
# KHGRemover('bilt')
# KHGRemover('hepp')
# KHGRemover('fuurt')
# KHGRemover('saang')
# KHGRemover('stécken')
# KHGRemover('groif')
# KHGRemover('eker')
# KHGRemover('grietchen')
# KHGRemover('stoppelen')
# KHGRemover('Dälchen')
# KHGRemover('lach')
# KHGRemover('ecker')
# KHGRemover('heed')
# KHGRemover('schledgen')
# KHGRemover('bau')
# KHGRemover('aasch')
# KHGRemover('båsch')
# KHGRemover('kiirten')
# KHGRemover('leeferchen')
# KHGRemover('schoul')
# KHGRemover('schend')
# KHGRemover('stach')
# KHGRemover('dëmpel')
# KHGRemover('spalt')
# KHGRemover('schlicht')
# KHGRemover('bréil')
# KHGRemover('drisch')
# KHGRemover('busc')
# KHGRemover('pëtz')
# KHGRemover('drëff')
# KHGRemover('poull')
# KHGRemover('griefchen')
# KHGRemover('al')
# KHGRemover('gof')
# KHGRemover('lousen')
# KHGRemover('affen')
# KHGRemover('wéngert')
# KHGRemover('kneppchen')
# KHGRemover('bam')
# KHGRemover('erd')
# KHGRemover('kraitz')
# KHGRemover('gert')
# KHGRemover('nësser')
# KHGRemover('wiesselen')
# KHGRemover('beien')
# KHGRemover('bois')
# KHGRemover('iechtchen')
# KHGRemover('gäschen')
# KHGRemover('kaemmchen')
# KHGRemover('buecher')
# KHGRemover('krëpp')
# KHGRemover('mierchen')
# KHGRemover('sprong')
# KHGRemover('poirt')
# KHGRemover('kaulen')
# KHGRemover('kierten')
# KHGRemover('häuser')
# KHGRemover('zung')
# KHGRemover('bett')
# KHGRemover('juck')
# KHGRemover('schisser')
# KHGRemover('knöppchen')
# KHGRemover('brék')
# KHGRemover('kaempchen')
# KHGRemover('gründgen')
# KHGRemover('wiss')
# KHGRemover('knop')
# KHGRemover('staat')
# KHGRemover('acker')
# KHGRemover('jentchen')
# KHGRemover('schlaff')
# KHGRemover('kleppen')
# KHGRemover('lécker')
# KHGRemover('raecher')
# KHGRemover('felden')
# KHGRemover('wier')
# KHGRemover('gruet')
# KHGRemover('neppchen')
# KHGRemover('bont')
# KHGRemover('stég')
# KHGRemover('äertchen')
# KHGRemover('bäumen')
# KHGRemover('bongerten')
# KHGRemover('këp')
# KHGRemover('lieder')
# KHGRemover('zeilchen')
# KHGRemover('diéren')
# KHGRemover('siedel')
# KHGRemover('réck')
# KHGRemover('weid')
# KHGRemover('widdem')
# KHGRemover('pëllchen')
# KHGRemover('guard')
# KHGRemover('hëtzelt')
# KHGRemover('stronck')
# KHGRemover('kiem')
# KHGRemover('houlz')
# KHGRemover('ruet')
# KHGRemover('atzéngen')
# KHGRemover('däerchen')
# KHGRemover('brillchen')
# KHGRemover('flues')
# KHGRemover('grouwen')
# KHGRemover('haiser')
# KHGRemover('éngen')
# KHGRemover('reih')
# KHGRemover('lo')
# KHGRemover('noss')
# KHGRemover('leechen')
# KHGRemover('leien')
# KHGRemover('ber')
# KHGRemover('bändchen')
# KHGRemover('fuerten')
# KHGRemover('heide')
# KHGRemover('käulchen')
# KHGRemover('maark')
# KHGRemover('schmëtt')
# KHGRemover('kreiz')
# KHGRemover('fang')
# KHGRemover('singer')
# KHGRemover('rodt')
# KHGRemover('lësch')
# KHGRemover('ingen')
# KHGRemover('knippchen')
# KHGRemover('loosen')
# KHGRemover('ruoder')
# KHGRemover('jon')
# KHGRemover('riech')
# KHGRemover('marjall')
# KHGRemover('wisschen')
# KHGRemover('muergen')
# KHGRemover('weed')
# KHGRemover('gruendchen')
# KHGRemover('botter')
# KHGRemover('strach')
# KHGRemover('brëschtchen')
# KHGRemover('kirt')
# KHGRemover('iwwer')
# KHGRemover('fleisch')
# KHGRemover('repper')
# KHGRemover('bréch')
# KHGRemover('hienert')
# KHGRemover('weën')
# KHGRemover('riedgen')
# KHGRemover('neelchen')
# KHGRemover('kiirfech')
# KHGRemover('bäume')
# KHGRemover('pand')
# KHGRemover('mauerchen')
# KHGRemover('säit')
# KHGRemover('leien')
# KHGRemover('gläich')
# KHGRemover('kaaf')
# KHGRemover('brach')
# KHGRemover('buerger')
# KHGRemover('bant')
# KHGRemover('weed')
# KHGRemover('dall')
# KHGRemover('dorref')
# KHGRemover('schlass')
# KHGRemover('uecht')
# KHGRemover('hiwwelen')
# KHGRemover('fëls')
# KHGRemover('waldes')
# KHGRemover('kirel')
# KHGRemover('wënkel')
# KHGRemover('éng')
# KHGRemover('kraiz')
# KHGRemover('uet')
# KHGRemover('brillen')
# KHGRemover('strach')
# KHGRemover('kielen')
# KHGRemover('laachen')
# KHGRemover('rolen')
# KHGRemover('fären')
# KHGRemover('helz')
# KHGRemover('betten')
# KHGRemover('bännen')
# KHGRemover('harden')
# KHGRemover('hënner')
# KHGRemover('bréch')
# KHGRemover('art')
# KHGRemover('kroll')
# KHGRemover('jans')
# KHGRemover('gärten')
# KHGRemover('koepchen')
# KHGRemover('resch')
# KHGRemover('knup')
# KHGRemover('bösch')
# KHGRemover('ho')
# KHGRemover('heckercher')
# KHGRemover('bierger')
# KHGRemover('meeschter')
# KHGRemover('junken')
# KHGRemover('uewen')
# KHGRemover('stronk')
# KHGRemover('furen')
# KHGRemover('wissen')
# KHGRemover('driisch')
# KHGRemover('driésch')
# KHGRemover('dreesch')
# KHGRemover('koist')
# KHGRemover('kehl')
# KHGRemover('dierfer')
# KHGRemover('dörfer')
# KHGRemover('winckel')
# KHGRemover('dange')
# KHGRemover('récken')
# KHGRemover('barack')
# KHGRemover('dael')
# KHGRemover('hënnescht')
# KHGRemover('bödem')
# KHGRemover('bääm')
# KHGRemover('breech')
# KHGRemover('belz')
# KHGRemover('bels')
# KHGRemover('beltz')
# KHGRemover('biidchen')
# KHGRemover('heimicht')
# KHGRemover('gaalgen')
# KHGRemover('gäert')
# KHGRemover('galgen')
# KHGRemover('gemein')
# KHGRemover('gemeng')
# KHGRemover('greecht')
# KHGRemover('grouw')
# KHGRemover('grow')
# KHGRemover('greet')
# KHGRemover('gruend')
# KHGRemover('höh')
# KHGRemover('hëlp')
# KHGRemover('jan')
# KHGRemover('kach')
# KHGRemover('kiirb')
# KHGRemover('kiirch')
# KHGRemover('kiirt')
# KHGRemover('koemp')
# KHGRemover('köp')
# KHGRemover('stucker')
# KHGRemover('mill')
# KHGRemover('moulin')
# KHGRemover('moul')
# KHGRemover('muhl')
# KHGRemover('gewaan')
# KHGRemover('kläpper')
# KHGRemover('wiesen')
# KHGRemover('piertchen')
# KHGRemover('ocht')
# KHGRemover('oocht')
# KHGRemover('paesch')
# KHGRemover('pelz')
# KHGRemover('stellchen')
# KHGRemover('mies')
# KHGRemover('reiser')
# KHGRemover('räis')
# KHGRemover('uechten')
# KHGRemover('weit')
# KHGRemover('rücken')
# KHGRemover('knuppen')
# KHGRemover('haisercher')
# KHGRemover('stucken')
# KHGRemover('strunk')
# KHGRemover('struenk')
# KHGRemover('këllchen')
# KHGRemover('bam')
# KHGRemover('baum')
#
#
#
# # KHGRemover('')
# # abc = 'aäbcdeéëfghijklmnoöpqrstuüvwxyz'
# #
# KVGRemover('Hasen')
# KVGRemover('Bodem')
# KVGRemover('Akescht')
# KVGRemover('Feier')
# KVGRemover('Jenck')
# KVGRemover('Geis')
# KVGRemover('Fous')
# KVGRemover('Faul')
# KVGRemover('Lay')
# KVGRemover('Wolf')
# KVGRemover('Wolef')
# KVGRemover('Huese')
# KVGRemover('Erd')
# KVGRemover('Ack')
# KVGRemover('Af')
# KVGRemover('Ag')
# KVGRemover('Ap')
# KVGRemover('Alf')
# KVGRemover('Al')
# KVGRemover('Ar')
# KVGRemover('Atz')
# KVGRemover('As')
# KVGRemover('Aärd')
# KVGRemover('Äis')
# KVGRemover('Äs')
# KVGRemover('Äl')
# KVGRemover('Baack')
# KVGRemover('Baak')
# KVGRemover('Biirk')
# KVGRemover('Baer')
# KVGRemover('Batter')
# KVGRemover('Batz')
# KVGRemover('Beng')
# KVGRemover('Beck')
# KVGRemover('Bark')
# KVGRemover('Banz')
# KVGRemover('Besch')
# KVGRemover('Bid')
# KVGRemover('Bill')
# KVGRemover('Bins')
# KVGRemover('Binz')
# KVGRemover('Bis')
# KVGRemover('Bock')
# KVGRemover('Bleil')
# KVGRemover('Boech')
# KVGRemover('Boels')
# KVGRemover('Boeltz')
# KVGRemover('Boelz')
# KVGRemover('Boeck')
# KVGRemover('Boed')
# KVGRemover('Bom')
# KVGRemover('Bop')
# KVGRemover('Bréng')
# KVGRemover('Bréim')
# KVGRemover('Breid')
# KVGRemover('Bréich')
# KVGRemover('Bréim')
# KVGRemover('Bréin')
# KVGRemover('Bët')
# KVGRemover('Dief')
# KVGRemover('Dir')
# KVGRemover('Diir')
# KVGRemover('Doer')
# KVGRemover('Dräi')
# KVGRemover('Duck')
# KVGRemover('Dud')
# KVGRemover('Déif')
# KVGRemover('Eil')
# KVGRemover('Echer')
# KVGRemover('Eder')
# KVGRemover('Eech')
# KVGRemover('Eis')
# KVGRemover('Ell')
# KVGRemover('Els')
# KVGRemover('Eltz')
# KVGRemover('Elt')
# KVGRemover('Enk')
# KVGRemover('Enn')
# KVGRemover('Ensch')
# KVGRemover('Folk')
# KVGRemover('Gees')
# KVGRemover('Gehaan')
# KVGRemover('Gehan')
# KVGRemover('Gehr')
# KVGRemover('Grouss')
# KVGRemover('Em')
# KVGRemover('Heim')
# KVGRemover('Ham')
# KVGRemover('Han')
# KVGRemover('Hund')
# KVGRemover('Hung')
# KVGRemover('Hun')
# KVGRemover('Back')
# KVGRemover('Behk')
# KVGRemover('Bend')
# KVGRemover('Beir')
# KVGRemover('Baesch')
# KVGRemover('Beis')
# KVGRemover('Bier')
# KVGRemover('Biir')
# KVGRemover('Birck')
# KVGRemover('Birb')
# KVGRemover('Bir')
# KVGRemover('Bouner')
# KVGRemover('Brom')
# KVGRemover('Demp')
# KVGRemover('Diel')
# KVGRemover('Däich')
# KVGRemover('Hond')
# KVGRemover('Wäiss')
# KVGRemover('Kuel')
# KVGRemover('Kirch')
# KVGRemover('Seif')
# KVGRemover('toem')
# KVGRemover('thoem')
# KVGRemover('Bir')
# KVGRemover('Apfel')
#
# # KVGRemover('')
# # abc = 'aäbcdeéëfghijklmnoöpqrstuüvwxyz'
#
#
#
# KHG_as_KVG()
# KVG_as_KHG()
# #
# lemmaBySplitKHG()
# lemmaBySplitKVG()



# UniqueLemmata = []
# OnlyKVG = []
# OnlyKHG = []
#
# for item in KHG_Queryed:
#     if item not in KVG_Queryed:
#         OnlyKHG.append(item)
#
# for item in KVG_Queryed:
#     if item not in KHG_Queryed:
#         OnlyKVG.append(item)



# print(*Lemmata_Remaining, sep='\n')

# print('\n\n\n')

# print("KHG queryed:\t" + str(len(KHG_Queryed)))
# print("KVG queryed:\t" + str(len(KVG_Queryed)))
# print("Lemmata removed:\t" + str(len(Lemmata_Removed)))
# print("Lemmata remaining:\t" + str(len(Lemmata_Remaining)))
# print("Obtained by stripping KHG:\t" + str(len(StrippedFromKHG)))
# print("Obtained by stripping KVG:\t" + str(len(StrippedFromKVG)))
# print('--Begin Writing--')
# with open('All3G.txt', 'w', encoding='utf-8') as newWriter: # way too slow
#
#     print('--Starting first for loop--')
#
#     for item in sorted(KHG_Queryed):
#         # for ktem in sorted(KVG_Queryed):
#         # for jtem in newItemList:
#         for jtem in microTopoAll:
#             if item.lower() == jtem['name'].split()[-1].lower():
#                 newWriter.write('{} : {}  -  {} (COMMUNE {}, CANTON {}) : {}\n'.format('Simplex', item.upper(), jtem['section'], jtem['adm_comm'], jtem['canton'], jtem['name']))
#
#     print('--Starting second for loop--')
#
#     for ktem in sorted(KVG_Queryed):
#         # for jtem in newItemList:
#         for jtem in microTopoAll:
#             if ktem.lower() == jtem['name'].split()[-1].lower():
#                 # newWriter.write('{} : {}  -  {}\n'.format('Simplex', ktem, jtem))
#                 newWriter.write('{} : {}  -  {} (COMMUNE {}, CANTON {}) : {}\n'.format('Simplex', item.upper(), jtem['section'], jtem['adm_comm'], jtem['canton'], jtem['name']))
#
#     print('--Starting third for loop--')
#
#     for item in sorted(KHG_Queryed):
#         # for jtem in newItemList:
#         for jtem in microTopoAll:
#             if jtem['name'].split()[-1].lower().endswith(item):
#                 # newWriter.write('{} : {}  -  {}\n'.format('KHG', item, jtem))
#                 newWriter.write('{} : {}  -  {} (COMMUNE {}, CANTON {}) : {}\n'.format('Simplex', item.upper(), jtem['section'], jtem['adm_comm'], jtem['canton'], jtem['name']))
#
#     print('--Starting fourth for loop--')
#
#     for ktem in sorted(KVG_Queryed):
#         # for jtem in newItemList:
#         for jtem in microTopoAll:
#             if jtem['name'].split()[-1].lower().startswith(ktem):
#                 # newWriter.write('{} : {}  -  {}\n'.format('KVG', ktem, jtem))
#                 newWriter.write('{} : {}  -  {} (COMMUNE {}, CANTON {}) : {}\n'.format('Simplex', item.upper(), jtem['section'], jtem['adm_comm'], jtem['canton'], jtem['name']))
#
#                 # if item.lower() == jtem.split()[-1].lower():
#                 #     newWriter.write('{} : {}  -  {}\n'.format('Simplex', item, jtem))
#                 # elif ktem.lower() == jtem.split()[-1].lower():
#                 #     newWriter.write('{} : {}  -  {}\n'.format('Simplex', ktem, jtem))
#                 # elif jtem.split()[-1].lower().endswith(item):
#                 #     newWriter.write('{} : {}  -  {}\n'.format('KHG', item, jtem))
#                 # elif jtem.split()[-1].lower().startswith(ktem):
#                 #     newWriter.write('{} : {}  -  {}\n'.format('KVG', ktem, jtem))
#     print('--Stop Writing--')
# newWriter.close()

# print('\n\n\n')

# print("Only KVG:\t" + str(len(OnlyKVG)))
# print("Only KHG:\t" + str(len(OnlyKHG)))
# print("Unique Lemmata:\t" + str(len(UniqueLemmata)))

# print('\n\n\n')

# print(*StrippedFromKHG, sep='\n')

# print('\n\n\n')

# print(*StrippedFromKVG, sep='\n')

# print('--END--')


#
# with open('LemmataQueryed.txt', 'w', encoding='utf-8') as qUERy:
#     for item in sorted(Lemmata_Queryed):
#         qUERy.write(item + '\n')
# qUERy.close()
#
# with open('LemmataRemoved.txt', 'w', encoding='utf-8') as rEMOVe:
#     for item in sorted(Lemmata_Removed):
#         rEMOVe.write(item + '\n')
# rEMOVe.close()
#
# with open('LemmataRemaining.txt', 'w', encoding='utf-8') as rEMAIn:
#     for item in sorted(Lemmata_Remaining):
#         rEMAIn.write(item + '\n')
# rEMAIn.close()

abc = 'aäbcdeéëfghijklmnoöpqrstuüvwxyz'
def LemmataRemainingDump(name):
    with open(name + '.txt', 'w', encoding='utf-8') as rEMAIn:
        for jtem in abc:
            rEMAIn.write(jtem.upper() + '\n')
            for item in sorted(Lemmata_Remaining):
                if item.lower().startswith(jtem):
                    rEMAIn.write(item + ', ')
            rEMAIn.write('\n\n')
    rEMAIn.close()


def LemmataRemovedDump(name):
    with open(name + '.txt', 'w', encoding='utf-8') as rEMAIn:
        for jtem in abc:
            rEMAIn.write(jtem.upper() + '\n')
            for item in sorted(Lemmata_Removed):
                if item.lower().startswith(jtem):
                    rEMAIn.write(item + ', ')
            rEMAIn.write('\n\n')
    rEMAIn.close()


def KHGQueryedDump(name):
    with open(name + '.txt', 'w', encoding='utf-8') as rEMAIn:
        for jtem in abc:
            rEMAIn.write(jtem.upper() + '\n')
            for item in sorted(KHG_Queryed):
                if item.lower().startswith(jtem):
                    rEMAIn.write(item + ', ')
            rEMAIn.write('\n\n')
    rEMAIn.close()


def KVGQueryedDump(name):
    with open(name + '.txt', 'w', encoding='utf-8') as rEMAIn:
        for jtem in abc:
            rEMAIn.write(jtem.upper() + '\n')
            for item in sorted(KVG_Queryed):
                if item.lower().startswith(jtem):
                    rEMAIn.write(item + ', ')
            rEMAIn.write('\n\n')
    rEMAIn.close()


def KHGQueryedDumpRectified(name):
    newKHG = []
    for ktem in KHG_Queryed:
        if ktem not in newKHG:
            newKHG.append(ktem)
    with open(name + '.txt', 'w', encoding='utf-8') as rEMAIn:
        for jtem in abc:
            rEMAIn.write(jtem.upper() + '\n')
            for item in sorted(newKHG):
                if item.lower().startswith(jtem):
                    rEMAIn.write(item + ', ')
            rEMAIn.write('\n\n')
    rEMAIn.close()


def KVGQueryedDumpRectified(name):
    newKVG = []
    for ktem in KVG_Queryed:
        if ktem not in newKVG:
            newKVG.append(ktem)
    with open(name + '.txt', 'w', encoding='utf-8') as rEMAIn:
        for jtem in abc:
            rEMAIn.write(jtem.upper() + '\n')
            for item in sorted(newKVG):
                if item.lower().startswith(jtem):
                    rEMAIn.write(item + ', ')
            rEMAIn.write('\n\n')
    rEMAIn.close()



def DerivationRemover(name):
    derivList = []
    newKHG = []
    for item in KHG_Queryed:
        if item not in newKHG:
            newKHG.append(item)
    for jtem in newKHG:
        for ktem in newKHG:
            # if jtem == ktem:
            #     continue
            if ktem.startswith(jtem):
                derivList.append(jtem + ': ' + ktem)
    with open(name + '.txt', 'w', encoding='utf-8') as rEMAIn:
        for ltem in abc:
            rEMAIn.write(ltem.upper() + '\n')
            for mtem in sorted(derivList):
                if mtem.lower().startswith(ltem):
                    rEMAIn.write(mtem + '\n')
            rEMAIn.write('\n\n')
    rEMAIn.close()



# LemmataRemainingDump('LRmain1')
# LemmataRemovedDump('LRmov1')
# KHGQueryedDumpRectified('KHGQuer')
# KVGQueryedDumpRectified('KVGQuer')
# DerivationRemover('deriMove')

# with open('topoSearch/NewItemList.txt', 'w', encoding='utf-8') as dump:
#     for item in sorted(nubi):
#
#         dump.write(item + '\n')
# dump.close()
# print('--start process--')
# allQueries = []
# # print('--load KVG into allQueries--')
# for item in KVG_Queryed:
#     if item not in allQueries:
#         allQueries.append(item)
# # print('--load KHG into allQueries--')
# for item in KHG_Queryed:
#     if item not in allQueries:
#         allQueries.append(item)
#
# # print('--opening file for writing--')


# with open('AllTopoBook.txt', 'w', encoding='utf-8') as newWriter:
#     newWriter.write('EXTRACTIONES NUMERISATA AUTMATISATA\n\nTOPONYMIA LUXEMBURGENSIS\n\nMICROTOPONYMIA\n\n\n')
#     print('--Starting lemma in allQueries loop--')
#     for lemma in sorted(allQueries):
#         newWriter.write('\n\n')
#         newWriter.write(lemma.upper())
#         newWriter.write('\n')
#         newWriter.write('-' * len(lemma))
#         newWriter.write('\n\n')
#
#         sIMPLEx = []
#         kAFAUGe = []
#         kAHAGe = []
#         simCount = 0
#         KVGCount = 0
#         KHGCount = 0
#         print('--Starting microtopoall loop--')
#         for fullName in microTopoAll:
#             print('--querying for simplex--')
#             if lemma.lower() == fullName['name'].split()[-1].lower():
#                 simCount += 1
#                 sIMPLEx.append([fullName['name'], fullName['section'], fullName['adm_comm'], fullName['canton'], fullName['coordinateOne']])
#             # print('--querying for KVG--')
#             elif fullName['name'].split()[-1].lower().startswith(lemma.lower()):
#                 KVGCount += 1
#                 kAFAUGe.append([fullName['name'], fullName['section'], fullName['adm_comm'], fullName['canton'], fullName['coordinateOne']])
#             # print('--querying for KHG--')
#             elif fullName['name'].split()[-1].lower().endswith(lemma.lower()):
#                 KHGCount += 1
#                 kAHAGe.append([fullName['name'], fullName['section'], fullName['adm_comm'], fullName['canton'], fullName['coordinateOne']])
#         # print('There are {} simplicia for lemma {}'.format(str(simCount), lemma))
#         # print('There are {} kvg for lemma {}'.format(str(KVGCount), lemma))
#         # print('There are {} khg for lemma {}'.format(str(KHGCount), lemma))
#         # print('--end of microtopoall loop')
#         # print('--start writing to file--')
#         newWriter.write('FREQUENCY\t')
#         newWriter.write(str(simCount + KVGCount + KHGCount))
#         newWriter.write('\n\n')
#         newWriter.write('MORPHOLOGY\n')
#         newWriter.write('SIMPLEX\t')
#         newWriter.write(str(simCount))
#         newWriter.write('\t')
#         for simplex in sIMPLEx:
#             newWriter.write(simplex[0].split()[-1])
#             newWriter.write(', ')
#         newWriter.write('\t')
#         newWriter.write('KVG\t')
#         newWriter.write(str(KVGCount))
#         newWriter.write('\t')
#         for kvg in kAFAUGe:
#             newWriter.write(kvg[0].split()[-1])
#             newWriter.write(', ')
#         newWriter.write('\t')
#         newWriter.write('KHG\t')
#         newWriter.write(str(KHGCount))
#         newWriter.write('\t')
#         for khg in kAHAGe:
#             newWriter.write(khg[0].split()[-1])
#             newWriter.write(', ')
#         newWriter.write('\n\n')
#         newWriter.write('LOCATION\n')
#         for simplex in sIMPLEx:
#             # newWriter.write('{} (COMMUNE {}, CANTON {}): NAME {} AT {}.'.format(simplex[1], simplex[2], simplex[3], simplex[0], simplex[4])) # 12304
#             newWriter.write('{} ({}, {}): {}.'.format(simplex[1], simplex[2], simplex[3], simplex[0])) # 12304
#             newWriter.write('\n')
#         for kvg in kAFAUGe:
#             # newWriter.write('{} (COMMUNE {}, CANTON {}): NAME {} AT {}.'.format(kvg[1], kvg[2], kvg[3], kvg[0], kvg[4]))
#             newWriter.write('{} ({}, {}): {}.'.format(kvg[1], kvg[2], kvg[3], kvg[0]))
#             newWriter.write('\n')
#         for khg in kAHAGe:
#             # newWriter.write('{} (COMMUNE {}, CANTON {}): NAME {} AT {}.'.format(khg[1], khg[2], khg[3], khg[0], khg[4]))
#             newWriter.write('{} ({}, {}): {}.'.format(khg[1], khg[2], khg[3], khg[0]))
#             newWriter.write('\n')
#
#     newWriter.write('\n\n\nFINIS ITERATIONIS')
# newWriter.close()

# with open('myLemmataReverseALL.txt', 'w', encoding='utf-8') as yamYam:
#     # for jtem in abc:
#     # yamYam.write(jtem.upper())
#     # yamYam.write('\n')
#     newsss = allQueries
#     newsss.sort(key=len)
#     newsss.reverse()
#     for item in newsss:
#         # if item.lower().startswith(jtem.lower()):
#             yamYam.write(item)
#             yamYam.write('\n')
#     yamYam.write('\n\n')
# yamYam.close()



# newQueries = []
# for item in allQueries:
#     bItem = item.rstrip('chen')
#     newQueries.append([bItem, item])
# print(*newQueries,sep='\n')
#
#
# newsss = allQueries
# newsss.sort(key=len)
# newsss.reverse()
# print(newsss)
#
# lemma_dict = {}

# Title: Vun Äppeltaart bis Schnuddelmier.
lemma_dict = []
with open('LemBaTa.txt', 'r', encoding='utf-8') as basicLemmata:
    readLem = basicLemmata.read()
    readLem = readLem.split('\n')
    for item in readLem:
        item = item.split()
        lemma_dict.append(dict({'lemma':item[0], 'variant': item[1]}))


lemma_first = []
for item in lemma_dict:
    if item['lemma'] not in lemma_first:
        lemma_first.append(item['lemma'])







def Belegbuch(title):
    allQueries = []
    # print('--load KVG into allQueries--')
    for item in KVG_Queryed:
        if item not in allQueries:
            allQueries.append(item)
    # print('--load KHG into allQueries--')
    for item in KHG_Queryed:
        if item not in allQueries:
            allQueries.append(item)
    with open(title + '.txt', 'w', encoding='utf-8') as newWriter:
        newWriter.write('EXTRACTIONES NUMERISATA AUTMATISATA\n\nTOPONYMIA LUXEMBURGENSIS\n\nMICROTOPONYMIA\n\n\n')
        # print('--Starting lemma in allQueries loop--')
        for lemma in sorted(allQueries):
            newWriter.write('\n\n')
            newWriter.write(lemma.upper())
            newWriter.write('\n')
            newWriter.write('-' * len(lemma))
            newWriter.write('\n\n')

            sIMPLEx = []
            kAFAUGe = []
            kAHAGe = []
            simCount = 0
            KVGCount = 0
            KHGCount = 0
            # print('--Starting microtopoall loop--')
            for fullName in microTopoAll:
                # print('--querying for simplex--')
                if lemma.lower() == fullName['name'].split()[-1].lower():
                    simCount += 1
                    sIMPLEx.append([fullName['name'], fullName['section'], fullName['adm_comm'], fullName['canton'], fullName['coordinateOne']])
                # print('--querying for KVG--')
                elif fullName['name'].split()[-1].lower().startswith(lemma.lower()):
                    KVGCount += 1
                    kAFAUGe.append([fullName['name'], fullName['section'], fullName['adm_comm'], fullName['canton'], fullName['coordinateOne']])
                # print('--querying for KHG--')
                elif fullName['name'].split()[-1].lower().endswith(lemma.lower()):
                    KHGCount += 1
                    kAHAGe.append([fullName['name'], fullName['section'], fullName['adm_comm'], fullName['canton'], fullName['coordinateOne']])
            # print('There are {} simplicia for lemma {}'.format(str(simCount), lemma))
            # print('There are {} kvg for lemma {}'.format(str(KVGCount), lemma))
            # print('There are {} khg for lemma {}'.format(str(KHGCount), lemma))
            # print('--end of microtopoall loop')
            # print('--start writing to file--')
            newWriter.write('FREQUENCY\t')
            newWriter.write(str(simCount + KVGCount + KHGCount))
            newWriter.write('\n\n')
            newWriter.write('MORPHOLOGY\n')
            newWriter.write('SIMPLEX\t')
            newWriter.write(str(simCount))
            newWriter.write('\t')
            for simplex in sIMPLEx:
                newWriter.write(simplex[0].split()[-1])
                newWriter.write(', ')
            newWriter.write('\t')
            newWriter.write('KVG\t')
            newWriter.write(str(KVGCount))
            newWriter.write('\t')
            for kvg in kAFAUGe:
                newWriter.write(kvg[0].split()[-1])
                newWriter.write(', ')
            newWriter.write('\t')
            newWriter.write('KHG\t')
            newWriter.write(str(KHGCount))
            newWriter.write('\t')
            for khg in kAHAGe:
                newWriter.write(khg[0].split()[-1])
                newWriter.write(', ')
            newWriter.write('\n\n')
            newWriter.write('LOCATION\n')
            for simplex in sIMPLEx:
                # newWriter.write('{} (COMMUNE {}, CANTON {}): NAME {} AT {}.'.format(simplex[1], simplex[2], simplex[3], simplex[0], simplex[4])) # 12304
                newWriter.write('{} ({}, {}): {}.'.format(simplex[1], simplex[2], simplex[3], simplex[0])) # 12304
                newWriter.write('\n')
            for kvg in kAFAUGe:
                # newWriter.write('{} (COMMUNE {}, CANTON {}): NAME {} AT {}.'.format(kvg[1], kvg[2], kvg[3], kvg[0], kvg[4]))
                newWriter.write('{} ({}, {}): {}.'.format(kvg[1], kvg[2], kvg[3], kvg[0]))
                newWriter.write('\n')
            for khg in kAHAGe:
                # newWriter.write('{} (COMMUNE {}, CANTON {}): NAME {} AT {}.'.format(khg[1], khg[2], khg[3], khg[0], khg[4]))
                newWriter.write('{} ({}, {}): {}.'.format(khg[1], khg[2], khg[3], khg[0]))
                newWriter.write('\n')

        newWriter.write('\n\n\nFINIS ITERATIONIS')
    newWriter.close()


def topoBook(title):

    with open(title + '.txt', 'w', encoding='utf-8') as newWriter:
        newWriter.write('EXTRACTIONES NUMERISATA AUTMATISATA\n\nTOPONYMIA LUXEMBURGENSIS\n\nMICROTOPONYMIA\n\n\n')
        # print('--Starting lemma in allQueries loop--')
        for lemma in sorted(lemma_first):
            newWriter.write('\n\n')
            newWriter.write(lemma.upper())
            newWriter.write('\n')
            newWriter.write('-' * len(lemma))
            newWriter.write('\n\n')

            variants = []
            for lemAll in lemma_dict:
                if lemAll['lemma'] == lemma:
                    variants.append(lemAll['variant'])



            sIMPLEx = []
            SIMPsimple = []
            kAFAUGe = []
            KVGsimple = []
            kAHAGe = []
            KHGsimple = []
            simCount = 0
            KVGCount = 0
            KHGCount = 0

            newWriter.write('VARIATIONS:\n')
            variaCount = 0
            for varia in variants:
                variaCount += 1
                newWriter.write(varia.lower())
                if varia != variants[-1]:
                    newWriter.write(', ')

            # print('--Starting microtopoall loop--')
                for fullName in microTopoAll:
                    # print('--querying for simplex--')
                    if varia.lower() == fullName['name'].split()[-1].lower():
                        simCount += 1
                        sIMPLEx.append([fullName['name'], fullName['section'], fullName['adm_comm'], fullName['canton'], fullName['coordinateOne']])
                        if varia not in SIMPsimple:
                            SIMPsimple.append(varia)
                    # print('--querying for KVG--')
                    elif fullName['name'].split()[-1].lower().startswith(varia.lower()):
                        KVGCount += 1
                        kAFAUGe.append([fullName['name'], fullName['section'], fullName['adm_comm'], fullName['canton'], fullName['coordinateOne']])
                        if varia not in KVGsimple:
                            KVGsimple.append(varia)
                    # print('--querying for KHG--')
                    elif fullName['name'].split()[-1].lower().endswith(varia.lower()):
                        KHGCount += 1
                        kAHAGe.append([fullName['name'], fullName['section'], fullName['adm_comm'], fullName['canton'], fullName['coordinateOne']])
                        if varia not in KHGsimple:
                            KHGsimple.append(varia)
            # print('There are {} simplicia for lemma {}'.format(str(simCount), lemma))
            # print('There are {} kvg for lemma {}'.format(str(KVGCount), lemma))
            # print('There are {} khg for lemma {}'.format(str(KHGCount), lemma))
            # print('--end of microtopoall loop')
            # print('--start writing to file--')
            newWriter.write('\n\nFREQUENCY: ')
            newWriter.write(str(simCount + KVGCount + KHGCount))
            newWriter.write(' instances')
            newWriter.write('\n\n')
            newWriter.write('MORPHOLOGY:\n')
            if simCount != 0:
                newWriter.write('SIMPLEX, ')
                if simCount == 1:
                    # newWriter.write(str(simCount) + ' instance in the variation: ')
                    newWriter.write(str(simCount) + ' instance')
                else:
                    # newWriter.write(str(simCount) + ' instances in the variations: ')
                    newWriter.write(str(simCount) + ' instances')
                # newWriter.write('\t')
                if len(SIMPsimple) == 1:
                    newWriter.write(' in the variation: ')
                else:
                    newWriter.write(' in the variations: ')
            for simplex in SIMPsimple:
                # newWriter.write(simplex[0].split()[-1])
                newWriter.write(simplex.lower())
                if simplex != SIMPsimple[-1]:
                    newWriter.write(', ')
            if simCount != 0:
                newWriter.write('\n')
            if KVGCount != 0:
                # newWriter.write('\n')
                newWriter.write('KVG, ')
                if KVGCount == 1:
                    newWriter.write(str(KVGCount) + ' instance')
                else:
                    newWriter.write(str(KVGCount) + ' instances')
                # newWriter.write('\t')
                if len(KVGsimple) == 1:
                    newWriter.write(' in the variation: ')
                else:
                    newWriter.write(' in the variations: ')
            for kvg in KVGsimple:
                # newWriter.write(kvg[0].split()[-1])
                newWriter.write(kvg.lower())
                if kvg != KVGsimple[-1]:
                    newWriter.write(', ')
            if KVGCount != 0:
                newWriter.write('\n')
            if KHGCount != 0:
                # newWriter.write('\n')
                newWriter.write('KHG, ')
                if KHGCount == 1:
                    newWriter.write(str(KHGCount) + ' instance')
                else:
                    newWriter.write(str(KHGCount) + ' instances')
                # newWriter.write('\t')
                if len(KHGsimple) == 1:
                    newWriter.write(' in the variation: ')
                else:
                    newWriter.write(' in the variations: ')
            for khg in KHGsimple:
                # newWriter.write(khg[0].split()[-1])
                newWriter.write(khg.lower())
                if khg != KHGsimple[-1]:
                    newWriter.write(', ')
            newWriter.write('\n\n')
            newWriter.write('LOCATION:\n')
            for simplex in sIMPLEx:
                # newWriter.write('{} (COMMUNE {}, CANTON {}): NAME {} AT {}.'.format(simplex[1], simplex[2], simplex[3], simplex[0], simplex[4])) # 12304
                newWriter.write('{} ({}, {}): {}.'.format(simplex[1], simplex[2], simplex[3], simplex[0])) # 12304
                newWriter.write('\n')
            for kvg in kAFAUGe:
                # newWriter.write('{} (COMMUNE {}, CANTON {}): NAME {} AT {}.'.format(kvg[1], kvg[2], kvg[3], kvg[0], kvg[4]))
                newWriter.write('{} ({}, {}): {}.'.format(kvg[1], kvg[2], kvg[3], kvg[0]))
                newWriter.write('\n')
            for khg in kAHAGe:
                # newWriter.write('{} (COMMUNE {}, CANTON {}): NAME {} AT {}.'.format(khg[1], khg[2], khg[3], khg[0], khg[4]))
                newWriter.write('{} ({}, {}): {}.'.format(khg[1], khg[2], khg[3], khg[0]))
                newWriter.write('\n')

        newWriter.write('\n\n\nFINIS ITERATIONIS')
    newWriter.close()

# topoBook('Belegbuch')

KVGExceptions = {'Aa': ['aal','aaner', 'aspel', 'aart', 'Aarbecht', 'Aaz', 'aak', 'Assel', 'Arnecht', 'aes', 'ael',
                        'aas', 'aecker', 'aex', 'aetz', 'aehs', 'aechel', 'aegel', 'Aarbel', 'Aang', 'Aehl', 'Aepchen',
                        'Aet', 'Aechtchen', 'Aechtel', 'Aedem', 'Aech', 'Aez', 'Aegen', 'Aechen', 'Aegen', 'aehl'],
                 'Aak': ['aker', 'acker', 'Akescht', 'Braak'],

                 'Au': ['aul', 'aus', 'auel', 'auch', 'auch']}
KHGExceptions = {'Aa': ['gaa', 'lae'],
                 'Aak': ['schaak', 'braak', 'waak', 'plak', 'wak', 'brak', 'plaak', 'stak', 'stack', 'schack', 'back',
                         'krack', 'brack'],
                 'Aasch': ['baasch', 'faasch', 'laaschter', 'laschtert', 'Baaschtert'],
                 'Aechel': ['BAechel', 'Kraechel', 'Heichel'],
                 'Ael': ['Dael', 'thael', 'Haal', 'Staal', 'Kehl', 'Hoehl', 'Nehl', 'Hiehl', 'Stehl', 'Gesehl', 'Kiehl',
                         'mehl', 'muehl'],
                 'Aes': ['Maes', 'Saes', 'Gaes', 'chaes', 'paesch', 'Baesch', 'Maesch', 'Waesch'],
                 'Aetz': ['PLaetz', 'Batz', 'platz', 'katz', 'patz'],
                 'Aker': ['stuecker', 'stecker', 'boecker', 'iecker', 'klecker', 'lecker', 'specker', 'decker',
                          'becker', 'leker', 'läcker', 'boecker', 'ieker', 'jeker', 'stäcker'],
                 'Akesch': ['Baakescht'],
                 'Assel': ['Grassel', 'Hassel', 'Haassel', 'Rassel', 'Fassel', 'Maassel', 'Kaassel', 'Kassel'],
                 'Au': ['hau', 'bau', 'frau', 'rau'],
                 'Aul': ['kaul', 'paul', 'theil', 'treil', 'bleil', 'steil', 'teil', 'Daul', 'Gaul', 'Beil']}






def BelegeAZ(title, AZ):
    with open(title + '.txt', 'w', encoding='utf-8') as newWriter:
        # newWriter.write('LEMMATA ONYMATE PLUS PLUS')
        # print('--Starting lemma in allQueries loop--')
        newWriter.write('\\section*{')
        newWriter.write(AZ.upper())
        newWriter.write(AZ.lower())
        newWriter.write('}')
        for lemma in sorted(lemma_first):
            for letter in AZ:
                # newWriter.write('\\section{')
                # newWriter.write(letter.upper())
                # newWriter.write(letter.lower())
                # newWriter.write('}')
                newWriter.write('\n\n\n')
                if lemma.lower().startswith(letter.lower()):
                    newWriter.write('\n\n')
                    # newWriter.write('\\begin {description} \n')
                    # newWriter.write('\\item [')
                    # newWriter.write(lemma.upper())
                    # newWriter.write(']')
                    newWriter.write('\\begin {description} \n')
                    newWriter.write('\\item [')
                    newWriter.write('\\subsection*{')
                    newWriter.write(lemma.upper())
                    newWriter.write('}')
                    newWriter.write(']')
                    # newWriter.write('\n')
                    # newWriter.write('-' * len(lemma))
                    newWriter.write('\n\n')

                    variants = []
                    for lemAll in lemma_dict:
                        if lemAll['lemma'] == lemma:
                            variants.append(lemAll['variant'])


                    sIMPLEx = []
                    SIMPsimple = []
                    kAFAUGe = []
                    kAFAUGeExcept = []
                    KVGsimple = []
                    kAHAGe = []
                    kAHAGeExcept = []
                    KHGsimple = []
                    simCount = 0
                    KVGCount = 0
                    KHGCount = 0

                    ExceptionCount = 0

                    cartoCount = 0
                    histoCount = 0
                    secundoCount = 0
                    # newWriter.write('\\begin{description} [align=right, labelwidth=3cm] \n')

                    newWriter.write('\\begin{description} \n')
                    newWriter.write('\\item [ ]')
                    newWriter.write('\\item [Variations] ')
                    newWriter.write('\\begin{enumerate*} ')
                    variaCount = 0
                    for varia in variants:
                        variaCount += 1
                        newWriter.write('\item ')
                        newWriter.write(varia)
                        # if varia != variants[-1]:
                            # newWriter.write(', ')



                        for fullName in microTopoAll:
                            if varia.lower() == fullName['name'].split()[-1].lower():
                                simCount += 1
                                sIMPLEx.append([fullName['name'], fullName['section'], fullName['adm_comm'],
                                                fullName['canton'], fullName['coordinateOne']])
                                if varia not in SIMPsimple:
                                    SIMPsimple.append(varia)
                            elif fullName['name'].split()[-1].lower().startswith(varia.lower()):
                                kAFAUGe.append([fullName['name'], fullName['section'], fullName['adm_comm'],
                                                fullName['canton'], fullName['coordinateOne']])
                                for item in KVGExceptions.keys():
                                    for x in KVGExceptions[item]:
                                        if fullName['name'].split()[-1].lower().startswith(x.lower()):
                                            ExceptionCount += 1
                                            # KVGCount -= 1
                                            kAFAUGeExcept.append([fullName['name'], fullName['section'],
                                                                  fullName['adm_comm'], fullName['canton'],
                                                                  fullName['coordinateOne']])
                                if varia not in KVGsimple:
                                    KVGsimple.append(varia)
                            elif fullName['name'].split()[-1].lower().endswith(varia.lower()):
                                # for y in KHGExceptions[lemma]:
                                #     if fullName['name'].split()[-1].lower().endswith(y.lower()):
                                #         continue
                                    # else:

                                # KHGCount += 1
                                kAHAGe.append([fullName['name'], fullName['section'], fullName['adm_comm'],
                                               fullName['canton'], fullName['coordinateOne']])
                                for jtem in KHGExceptions.keys():
                                    for y in KHGExceptions[jtem]:
                                        if fullName['name'].split()[-1].lower().endswith(y.lower()):
                                            ExceptionCount += 1
                                            # KHGCount -= 1
                                            kAHAGeExcept.append([fullName['name'], fullName['section'],
                                                                 fullName['adm_comm'], fullName['canton'],
                                                                 fullName['coordinateOne']])
                                if varia not in KHGsimple:
                                    KHGsimple.append(varia)

                        # for cartoname in cartoset:
                        #     # same as above

                        # for stop in busstops:
                        #     # same as above

                        # for oldlemma in histoset:
                        #     # same as above

                        # for secondary in secndLit:
                        #     # same as above

                    newWriter.write('\\end{enumerate*}\n')
                    newKVG = []
                    newKHG = []

                    for item in kAFAUGe:
                        if item not in kAFAUGeExcept:
                            newKVG.append(item)
                            KVGCount += 1

                    for item in kAHAGe:
                        if item not in kAHAGeExcept:
                            newKHG.append(item)
                            KHGCount += 1

                    newWriter.write('\\item [Morphologie] ')
                    # newWriter.write('\n')
                    if simCount != 0:
                        newWriter.write('Simplex in ')
                        if simCount == 1:
                            # newWriter.write(str(simCount) + ' instance in the variation: ')
                            newWriter.write(str(simCount) + ' instance')
                        else:
                            # newWriter.write(str(simCount) + ' instances in the variations: ')
                            newWriter.write(str(simCount) + ' instances')
                        # newWriter.write('\t')
                        if len(SIMPsimple) == 1:
                            newWriter.write(' in the variation: ')
                        else:
                            newWriter.write(' in the variations: ')
                        newWriter.write('\\begin{enumerate*} \n')
                    for simplex in SIMPsimple:
                        # newWriter.write(simplex[0].split()[-1])
                        newWriter.write('\\item ')
                        newWriter.write(simplex)
                        if simplex != SIMPsimple[-1]:
                            newWriter.write(', ')
                    if simCount != 0:
                        newWriter.write('\\end{enumerate*} ')
                        # newWriter.write('\n')
                    if KVGCount != 0:
                        # newWriter.write('\n')
                        newWriter.write('. ')
                        newWriter.write('Primary compounding element in ')
                        if KVGCount == 1:
                            newWriter.write(str(KVGCount) + ' instance')
                        else:
                            newWriter.write(str(KVGCount) + ' instances')
                        # newWriter.write('\t')
                        if len(KVGsimple) == 1:
                            newWriter.write(' in the variation: ')
                        else:
                            newWriter.write(' in the variations: ')
                        newWriter.write('\\begin{enumerate*}')
                    for kvg in KVGsimple:
                        # newWriter.write(kvg[0].split()[-1])
                        newWriter.write('\\item ')
                        newWriter.write(kvg)
                        if kvg != KVGsimple[-1]:
                            newWriter.write('\n')
                    if KVGCount != 0:
                        # newWriter.write('\n')
                        newWriter.write('. ')
                        newWriter.write('\\end{enumerate*} \n')
                    if KHGCount != 0:
                        newWriter.write('\n')
                        newWriter.write('Final compounding element in ')
                        if KHGCount == 1:
                            newWriter.write(str(KHGCount) + ' instance')
                        else:
                            newWriter.write(str(KHGCount) + ' instances')
                        # newWriter.write('\t')
                        if len(KHGsimple) == 1:
                            newWriter.write(' in the variation: ')
                        else:
                            newWriter.write(' in the variations: ')
                        newWriter.write('\\begin{enumerate*} \n')
                    for khg in KHGsimple:
                        # newWriter.write(khg[0].split()[-1])
                        newWriter.write('\\item ')
                        newWriter.write(khg)
                        if khg != KHGsimple[-1]:
                            newWriter.write('\n')
                    if KHGCount != 0:
                        newWriter.write('\\end{enumerate*} \n')
                    # newWriter.write('\n\n')

                    newWriter.write('\\item [Location] ')
                    for simplex in sIMPLEx:
                        # newWriter.write('{} (COMMUNE {}, CANTON {}): NAME {} AT {}.'.format(simplex[1], simplex[2], simplex[3], simplex[0], simplex[4])) # 12304
                        newWriter.write('{}: {}. '.format(simplex[1].upper(), simplex[0])) # 12304
                        # newWriter.write('\n')
                    for kvg in newKVG:
                        # newWriter.write('{} (COMMUNE {}, CANTON {}): NAME {} AT {}.'.format(kvg[1], kvg[2], kvg[3], kvg[0], kvg[4]))
                        newWriter.write('{}: {}. '.format(kvg[1].upper(), kvg[0]))
                        # newWriter.write('\n')
                    for khg in newKHG:
                        # newWriter.write('{} (COMMUNE {}, CANTON {}): NAME {} AT {}.'.format(khg[1], khg[2], khg[3], khg[0], khg[4]))
                        newWriter.write('{}: {}. '.format(khg[1].upper(), khg[0]))
                        # newWriter.write('\n')
                    newWriter.write('')

                    newWriter.write('\\item [Explanation] Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.')

                    newWriter.write('\\item [Literature] ')
                    newWriter.write('LOD s.v. X, LWB Bd. X Sp. X, WLM X, LLU X, ')
                    newWriter.write('RHWb X, LothWb X, ElsWb X, ')
                    newWriter.write('Nnd Wb X, ndl Wb X, Fries Wb X, Duden s.v. X, DWDS s.v. X, Grimm Bd. X Col. X, GrandRobert Bd. X Col. X, ')
                    newWriter.write('AWB X. Y, Splett X. Y, Schuetzeichel X. Y, MWB X. Y, Lexer X. Y, ')
                    newWriter.write('EWA X. Y, FEW X. Y, REW X. Y')

                    newWriter.write('')
                    newWriter.write('\n')
                    newWriter.write('\\end {description}\n')
                    newWriter.write('\\end {description}\n')
        # newWriter.write('\\end {description}\n')




        # newWriter.write('\n\n\nFINIS ITERATIONIS')
    newWriter.close()
    with open(title + '_Exceptions.txt', 'w', encoding='utf-8') as ExceptionWriter:
        ExceptionWriter.write('Exceptions extracted\n\n\n')
        ExceptionWriter.write('KVG Exceptions:\n\n')
        for i in kAFAUGeExcept:
            ExceptionWriter.write(str(i[0]) + ': ' + str(i[1]) + '.\n')
        ExceptionWriter.write('\n\n')
        ExceptionWriter.write('KHG Exceptions:\n\n')
        for j in kAHAGeExcept:
            ExceptionWriter.write(str(j[0]) + ': ' + str(j[1]) + '.\n')
        ExceptionWriter.write('\n\n')
        ExceptionWriter.write('--End of file--')
    ExceptionWriter.close()

def Belege(title):
    with open(title + '.txt', 'w', encoding='utf-8') as newWriter:
        newWriter.write('LEMMATA ONYMATE')
        # print('--Starting lemma in allQueries loop--')
        for lemma in sorted(lemma_first):
            newWriter.write('\n\n')
            newWriter.write(lemma.upper())
            newWriter.write('\n')
            newWriter.write('-' * len(lemma))
            newWriter.write('\n\n')

            variants = []
            for lemAll in lemma_dict:
                if lemAll['lemma'] == lemma:
                    variants.append(lemAll['variant'])



            sIMPLEx = []
            SIMPsimple = []
            kAFAUGe = []
            KVGsimple = []
            kAHAGe = []
            KHGsimple = []
            simCount = 0
            KVGCount = 0
            KHGCount = 0

            newWriter.write('VARIATIONS:\t')
            variaCount = 0
            for varia in variants:
                variaCount += 1
                newWriter.write(varia)
                if varia != variants[-1]:
                    newWriter.write(', ')

                # print('--Starting microtopoall loop--')
                for fullName in microTopoAll:
                    # print('--querying for simplex--')
                    if varia.lower() == fullName['name'].split()[-1].lower():
                        simCount += 1
                        sIMPLEx.append([fullName['name'], fullName['section'], fullName['adm_comm'],
                                        fullName['canton'], fullName['coordinateOne']])
                        if varia not in SIMPsimple:
                            SIMPsimple.append(varia)
                    # print('--querying for KVG--')
                    elif fullName['name'].split()[-1].lower().startswith(varia.lower()):
                        KVGCount += 1
                        kAFAUGe.append([fullName['name'], fullName['section'], fullName['adm_comm'],
                                        fullName['canton'], fullName['coordinateOne']])
                        if varia not in KVGsimple:
                            KVGsimple.append(varia)
                    # print('--querying for KHG--')
                    elif fullName['name'].split()[-1].lower().endswith(varia.lower()):
                        KHGCount += 1
                        kAHAGe.append([fullName['name'], fullName['section'], fullName['adm_comm'],
                                       fullName['canton'], fullName['coordinateOne']])
                        if varia not in KHGsimple:
                            KHGsimple.append(varia)
            # print('There are {} simplicia for lemma {}'.format(str(simCount), lemma))
            # print('There are {} kvg for lemma {}'.format(str(KVGCount), lemma))
            # print('There are {} khg for lemma {}'.format(str(KHGCount), lemma))
            # print('--end of microtopoall loop')
            # print('--start writing to file--')
            # newWriter.write('\n\nFREQUENCY: ')
            # newWriter.write(str(simCount + KVGCount + KHGCount))
            # newWriter.write(' instances')
            # newWriter.write('\n\n')
            # newWriter.write('MORPHOLOGY:\n')
            newWriter.write('\n')
            if simCount != 0:
                newWriter.write('SIMPLEX, ')
                if simCount == 1:
                    # newWriter.write(str(simCount) + ' instance in the variation: ')
                    newWriter.write(str(simCount) + ' instance')
                else:
                    # newWriter.write(str(simCount) + ' instances in the variations: ')
                    newWriter.write(str(simCount) + ' instances')
                # newWriter.write('\t')
                if len(SIMPsimple) == 1:
                    newWriter.write(' in the variation: ')
                else:
                    newWriter.write(' in the variations: ')
            for simplex in SIMPsimple:
                # newWriter.write(simplex[0].split()[-1])
                newWriter.write(simplex)
                if simplex != SIMPsimple[-1]:
                    newWriter.write(', ')
            if simCount != 0:
                newWriter.write('\n')
            if KVGCount != 0:
                # newWriter.write('\n')
                newWriter.write('KVG, ')
                if KVGCount == 1:
                    newWriter.write(str(KVGCount) + ' instance')
                else:
                    newWriter.write(str(KVGCount) + ' instances')
                # newWriter.write('\t')
                if len(KVGsimple) == 1:
                    newWriter.write(' in the variation: ')
                else:
                    newWriter.write(' in the variations: ')
            for kvg in KVGsimple:
                # newWriter.write(kvg[0].split()[-1])
                newWriter.write(kvg)
                if kvg != KVGsimple[-1]:
                    newWriter.write(', ')
            if KVGCount != 0:
                newWriter.write('\n')
            if KHGCount != 0:
                # newWriter.write('\n')
                newWriter.write('KHG, ')
                if KHGCount == 1:
                    newWriter.write(str(KHGCount) + ' instance')
                else:
                    newWriter.write(str(KHGCount) + ' instances')
                # newWriter.write('\t')
                if len(KHGsimple) == 1:
                    newWriter.write(' in the variation: ')
                else:
                    newWriter.write(' in the variations: ')
            for khg in KHGsimple:
                # newWriter.write(khg[0].split()[-1])
                newWriter.write(khg)
                if khg != KHGsimple[-1]:
                    newWriter.write(', ')
            newWriter.write('\n\n')
            newWriter.write('LOCATION:\n')
            for simplex in sIMPLEx:
                # newWriter.write('{} (COMMUNE {}, CANTON {}): NAME {} AT {}.'.format(simplex[1], simplex[2], simplex[3], simplex[0], simplex[4])) # 12304
                newWriter.write('{}: {}. '.format(simplex[1].upper(), simplex[0])) # 12304
                # newWriter.write('\n')
            for kvg in kAFAUGe:
                # newWriter.write('{} (COMMUNE {}, CANTON {}): NAME {} AT {}.'.format(kvg[1], kvg[2], kvg[3], kvg[0], kvg[4]))
                newWriter.write('{}: {}. '.format(kvg[1].upper(), kvg[0]))
                # newWriter.write('\n')
            for khg in kAHAGe:
                # newWriter.write('{} (COMMUNE {}, CANTON {}): NAME {} AT {}.'.format(khg[1], khg[2], khg[3], khg[0], khg[4]))
                newWriter.write('{}: {}. '.format(khg[1].upper(), khg[0]))
                # newWriter.write('\n')

        newWriter.write('\n\n\nFINIS ITERATIONIS')
    newWriter.close()

# Belege('Belege')
# BelegeAZ('BelegeDEF', 'def')
# BelegeAZ('BelegeGHI', 'ghi')
# BelegeAZ('BelegeJKL', 'jkl')
# BelegeAZ('BelegeMNO', 'mno')
# BelegeAZ('BelegePQR', 'pqr')
# BelegeAZ('BelegeSTU', 'stu')
# BelegeAZ('BelegeVWXYZ', 'vwxyz')
# BelegeAZ('TestLATEX_A2', 'a')