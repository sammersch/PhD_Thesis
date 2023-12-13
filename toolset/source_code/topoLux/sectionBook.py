from MicroTopoLoadAllData import microTopoAll
from CartoLoad import cartoLoad

abc = 'aäbcdeéëèfghijklmnoöpqrstuüvwxyz'
section_list = []
abundant_list = []
adm_list = []




for i in microTopoAll:
    abundant_list.append((i['section'] + ':\t' + i['adm_comm'] + ':\t' + i['canton']))
    if i['section'] not in section_list:
        section_list.append(i['section'])


for j in abundant_list:
    if j not in adm_list:
        adm_list.append(j)


section_list = sorted(section_list)
adm_list = sorted(adm_list)


#######################################################################################
#### The following is for the loader for the carto data ###############################
#######################################################################################







def sectionbook_plotter_tex():
    with open('sectionBookPlotter.tex', 'w', encoding='utf-8') as plotter:



        for location in adm_list:
            section, commune, canton = location.split(':\t')

            plotter.write('\section*{')
            plotter.write(section)
            plotter.write(', Commune ')
            plotter.write(commune)
            plotter.write('}')

            # \addtocounter{section}{1}
            plotter.write('\\addcontentsline{toc}{section}{')
            plotter.write(section)
            plotter.write(', Commune ')
            plotter.write(commune)
            plotter.write('}')
            # plotter.write('}')

            plotter.write('\n\n')

            name_list = []
            for item in microTopoAll:
                if item['section'] == section and item['adm_comm'] == commune:
                    name_list.append(item['name'].split()[-1])
            name_list = sorted(name_list)
            for name in name_list:
                for item in microTopoAll:
                    if item['section'] == section and item['adm_comm'] == commune:
                        if name in item['name']:
                            if len(item['name'].split()) > 1:
                                plotter.write(' '.join(item['name'].split()[:-1]))
                                plotter.write(' ')
                                plotter.write('{\\large\\textbf{')
                                plotter.write(str(item['name'].split()[-1][0]))
                                plotter.write('}}')
                                plotter.write(str(item['name'].split()[-1][1:]))
                                plotter.write(', ')
                            else:
                                plotter.write('{\\large\\textbf{')
                                plotter.write(item['name'][0])
                                plotter.write('}}')
                                plotter.write(item['name'][1:])
                                plotter.write(', ')
            plotter.write('\n\n')

        # plotter.write('\\end{document}')
    plotter.close()


####################################################################
#### Parser for carto data #########################################
####################################################################


def sectionbook_plotter_carto():
    with open('sectionBookPlotterCarto.txt', 'w', encoding='utf-8') as plotter:
        for location in admlist_carto:
            section, commune = location.split(':\t')
            plotter.write(section)
            plotter.write(', Commune ')
            plotter.write(commune)
            plotter.write('\n')
            plotter.write('-' * len(section + ', Commune ' + commune))
            plotter.write('\n\n')
            name_list = []
            for item in cartoLoad:
                if item['section'] == section and item['adm_comm'] == commune:
                    name_list.append(item['name'].split()[-1])
            name_list = sorted(name_list)
            for name in name_list:
                for item in cartoLoad:
                    if item['section'] == section and item['adm_comm'] == commune:
                        if name in item['name']:
                            plotter.write(item['name'])
                            plotter.write(', ')
            plotter.write('\n\n')
            plotter.write('-' * 60)
            plotter.write('\n\n')
    plotter.close()


def sectionbook_plotter_tex_carto():
    with open('sectionBookPlotterCarto.tex', 'w', encoding='utf-8') as plotter:

        # plotter.write('\\documentclass[10pt,a4paper]{book}')
        # plotter.write('\n')
        # plotter.write('\\usepackage[utf8]{inputenc}')
        # plotter.write('\n')
        # plotter.write('\\usepackage[english]{babel}')
        # plotter.write('\n')
        # plotter.write('\\usepackage{amsmath}')
        # plotter.write('\n')
        # plotter.write('\\usepackage{amsfonts}')
        # plotter.write('\n')
        # plotter.write('\\usepackage{amssymb}')
        # plotter.write('\n')
        # plotter.write('\\usepackage[left=2cm,right=2cm,top=2cm,bottom=2cm]{geometry}')
        # plotter.write('\n')
        # plotter.write('\\author{Sam Mersch}')
        # plotter.write('\n')
        # plotter.write('\\begin{document}')
        # plotter.write('\n')

        for location in admlist_carto:
            section, commune, canton = location.split(':\t')

            plotter.write('\section*{')
            plotter.write(section)
            plotter.write(', Commune ')
            plotter.write(commune)
            plotter.write('}')

            # \addtocounter{section}{1}
            plotter.write('\\addcontentsline{toc}{section}{')
            plotter.write(section)
            plotter.write(', Commune ')
            plotter.write(commune)
            plotter.write('}')
            # plotter.write('}')

            plotter.write('\n\n')

            name_list = []
            for item in cartoLoad:
                if item['section'] == section and item['adm_comm'] == commune:
                    name_list.append(item['name'].split()[-1])
            name_list = sorted(name_list)
            for name in name_list:
                for item in cartoLoad:
                    if item['section'] == section and item['adm_comm'] == commune:
                        if name in item['name']:
                            if len(item['name'].split()) > 1:
                                plotter.write(' '.join(item['name'].split()[:-1]))
                                plotter.write(' ')
                                plotter.write('{\\large\\textbf{')
                                plotter.write(str(item['name'].split()[-1][0]))
                                plotter.write('}}')
                                plotter.write(str(item['name'].split()[-1][1:]))
                                plotter.write(', ')
                            else:
                                plotter.write('{\\large\\textbf{')
                                plotter.write(item['name'][0])
                                plotter.write('}}')
                                plotter.write(item['name'][1:])
                                plotter.write(', ')
            plotter.write('\n\n')

        # plotter.write('\\end{document}')
    plotter.close()



# sectionbook_plotter()
# sectionbook_plotter_tex()
