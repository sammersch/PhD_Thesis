from MicroTopoLoadAllData import microTopoAll


abc = 'aäbcdeéëèfghijklmnoöpqrstuüvwxyz'
simple_list = []



for item in microTopoAll:
    if item['name'].split()[-1] not in simple_list:
        if item['name'].split()[-1] == 'im':
            pass
        elif item['name'].split()[-1] == 'grusse':
            pass
        elif item['name'].split()[-1] == 'dem':
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
        elif item['name'].split()[-1] == 'champ':
            base_lemma = item['name'].split()[-3:-1]
        elif item['name'].split()[-1] == 'Aus':
            base_lemma = item['name'].split()[-2]
        elif item['name'].split()[-1] in '123':
            base_lemma = item['name'].split()[-2]
        elif item['name'].split()[-1] in abc.upper():
            base_lemma = item['name'].split()[-2]
        else:
            base_lemma = item['name'].split()[-1]
        simple_list.append(base_lemma)


simple_list_sorted = []

for letter in abc:
    for entry in simple_list:
        if str(entry).lower().startswith(letter):
            simple_list_sorted.append(entry)



def evidence_printer(file_name, list):
    with open(file_name + '.txt', 'w', encoding='utf-8') as printer:
        for item in list:
            printer.write('\n\n')
            printer.write('\\textbf{')
            printer.write(item.upper())
            printer.write('}')
            printer.write('\n')
            for jtem in microTopoAll:
                if jtem['name'].split()[-1] in '123':
                    if item.lower() == jtem['name'].split()[-2].lower():
                        printer.write(jtem['name'] + ' (' + jtem['section'] + ' / ' + jtem['adm_comm'] + '), ')
                else:
                    if item.lower() == jtem['name'].split()[-1].lower():
                        printer.write(jtem['name'] + ' (' + jtem['section'] + ' / ' + jtem['adm_comm'] + '), ')
    printer.close()


def evidence_printer_tex(file_name, list):
    with open(file_name + '.tex', 'w', encoding='utf-8') as printer:
        for letter in abc:
            # printer.write('\section*{')
            # printer.write(letter.upper())
            # printer.write(letter.lower())
            # printer.write('}')
            # printer.write('\\addcontentsline{toc}{section}{')
            # printer.write(letter.upper())
            # printer.write(letter.lower())
            # printer.write('}')


            try:
                test_list = []
                for item in simple_list_sorted:
                    if item.lower().startswith(letter.lower()):
                        test_list.append(item)
                test_list = sorted(test_list)
                # print(test_list[0] + ' - ' + test_list[-1])
            # except IndexError:
            #     pass


            # title_text = []
            #
            # for item in list:
            #     if item.lower().startswith(letter.lower()):
            #         title_text.append(item)

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

            for item in list:
                if item.lower().startswith(letter.lower()):
                    printer.write('\n\n')
                    printer.write('\\textbf{')
                    printer.write(item.upper())
                    printer.write('}')
                    printer.write('\n')
                    for jtem in microTopoAll:
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

# evidence_printer('SortedBelegbuch',simple_list_sorted)
evidence_printer_tex('namedInstances', simple_list_sorted)


# with open('AllNamesLemmatized.csv', 'w', encoding='utf-8') as BelPrint:
#     for item in simple_list_sorted:
#         for jtem in microTopoAll:
#             if item in jtem['name'].split():
#                 BelPrint.write(item)
#                 BelPrint.write(';')
#                 BelPrint.write(jtem['name'])
#                 BelPrint.write('\n')
# BelPrint.close()


# for letter in abc:
#     try:
#         test_list = []
#         for item in simple_list_sorted:
#             if item.lower().startswith(letter.lower()):
#                 test_list.append(item)
#         test_list = sorted(test_list)
#         print(test_list[0] + ' - ' + test_list[-1])
#     except IndexError:
#         print('IndexError occured')



# test_list = []
# for item in simple_list_sorted:
#     if item.lower().startswith('a'):
#         print(item)
#         test_list.append(item)
# print(test_list[0] + '-' + test_list[-1])