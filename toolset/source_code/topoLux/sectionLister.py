
big_list = [] # CANTON,DISTRICT,SECTION,COMMUNE_AD
with open('sectionCantonAll.csv', encoding='utf-8') as data_file:
    lines = data_file.readlines()
    for line in lines:
        line = line.rstrip('\n')
        # print(line.split(','))
        # canton, district, section, commune = line.split(',')
        canton = line.split(',')[0]
        district = line.split(',')[1]
        section = line.split(',')[2]
        commune = line.split(',')[3]
        big_list.append(dict({'section': section,
                              'commune': commune,
                              'canton': canton,
                              'district': district}))
# print(big_list)
print(len(big_list))

count_isOffYes = 0
count_isOffNo = 0
sectionBigNo = []

sections0 = []
sections = []
sectionsSigma = []
with open('sections.csv', encoding='utf-8') as data_file:
    lines = data_file.readlines()
    for line in lines:
        lin0 = line.rstrip('\n')
        # print(lin.split(';'))
        lin = lin0.split(';')
        is_official = lin[3]
        # print(is_official)
        section_official = lin[2]
        section_lb = lin[4]
        commune = lin[0]
        # sections0.append([section_official, section_lb, commune])
        sectionsSigma.append([section_official, section_lb, commune, [item['canton'] for item in big_list if item['commune']==commune], [item['district'] for item in big_list if item['commune']==commune]])
        for item in big_list:
            if commune == item['commune']:
                # if commune == item['commune']:
                #     sections.append([section_official, section_lb, commune, item['canton'], item['district']])
                if [section_official, section_lb, commune, item['canton'], item['district']] not in sections:
                    sections.append([section_official, section_lb, commune, item['canton'], item['district']])
            # else:
            #     sections.append([section_official, section_lb, commune, '', ''])
        if is_official == 'OUI':
            count_isOffYes += 1
        #     for item in big_list:
        #         if section_official == item['section']:
        #             if commune == item['commune']:
        #                 sections.append([section_official, section_lb, commune, item['canton'], item['district']])
        #         else:
        #             if section_official not in sectionBigNo:
        #                 sectionBigNo.append(section_official)
        # else:
        #     count_isOffNo += 1



# print(sections)
# print('len sections:', len(sections))
# print('len sections0:', len(sections0))
# print('len sectionsSigma:', len(sectionsSigma))
# print('count_isOffYes:', count_isOffYes)
# print('count_isOffNo:', count_isOffNo)
# print('count_isOffYesNO:', count_isOffNo+count_isOffYes)
# print('len sectionBigNo:', len(sectionBigNo))
# print(sectionBigNo)
# print(*sections0, sep='\n')
# print(*sectionsSigma, sep='\n')
# print(*sections, sep='\n')
for item in sections:
    print(item[0] + ' & ' + item[1] + ' & ' + item[2] + ' & ' + item[3] + ' & ' + item[4] + r' \\ \hline ')