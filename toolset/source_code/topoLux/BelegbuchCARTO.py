from CartoLoad import cartoLoad
from MicroTopoLoadAllData import microTopoAll
from BusStopLoad import busStops


abc = 'aäbcdeéëèfghijklmnoöpqrstuüvwxyz'
simple_list = []
simple_list2 = []


for item in cartoLoad:
    if item['name'].split()[-1] not in simple_list:
        if item['nature'] == 'Village':
            pass
        elif item['nature'] == 'Commune':
            pass
        elif item['name'] == '(B)':
            pass
        elif item['name'] == '(Dunkrodt)':
            pass
        elif item['name'].split()[-1].startswith('d\''):
            temp = item['name'].split()[-1]
            base_lemma = temp[2:]
        elif item['name'].split()[-1].startswith('l\''):
            temp = item['name'].split()[-1]
            base_lemma = temp[2:]
        elif item['name'].split()[-1].startswith('z\''):
            temp = item['name'].split()[-1]
            base_lemma = temp[2:]
        else:
            base_lemma = item['name'].split()[-1]
        simple_list.append(base_lemma)



for item in sorted(simple_list):
    if item.startswith('('):
        pass
    elif item.startswith(')'):
        pass
    else:
        simple_list2.append(item)



simple_list_sorted = simple_list2

#
# for letter in abc:
#     for entry in simple_list:
#         if str(entry).lower().startswith(letter):
#             simple_list_sorted.append(entry)







def evidence_printer_tex(file_name):
    with open(file_name + 'CARTO.tex', 'w', encoding='utf-8') as printer:
        for letter in abc:

            try:
                test_list = []
                for item in simple_list_sorted:
                    if item.lower().startswith(letter.lower()):
                        test_list.append(item)
                test_list = sorted(test_list)


                printer.write('\section*{')
                printer.write(test_list[0])
                printer.write(' - ')
                printer.write(test_list[-1])
                printer.write('}\n')
                printer.write('\\addcontentsline{toc}{section}{')
                printer.write(test_list[0])
                printer.write(' - ')
                printer.write(test_list[-1])
                printer.write('}\n')
            except IndexError:
                pass

            for item in simple_list2:
                if item.lower().startswith(letter.lower()):
                    printer.write('\n\n')
                    printer.write('\\textbf{')
                    printer.write(item.upper())
                    printer.write('}')
                    printer.write('\n')
                    for jtem in cartoLoad:
                        if jtem['name'].split()[-1] in '123':
                            if item.lower() == jtem['name'].split()[-2].lower():
                                printer.write(jtem['name'] + ' (' + jtem['section'] + ' / ' + jtem['adm_comm'] + '), ')
                        else:
                            if item.lower() == jtem['name'].split()[-1].lower():
                                printer.write(jtem['name'] + ' (' + jtem['section'] + ' / ' + jtem['adm_comm'] + '), ')
                    printer.write('\n')
            printer.write('\n')
        printer.write('\n')
    printer.close()



# evidence_printer_tex('namedInstances')

