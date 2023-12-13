from MicroTopoLoad import streetNames

counter = []
newp = []
for item in streetNames:
    if item['name'].lower().endswith('sel'): # promenade imp digue colonel caf nouv anc hl no rn r.n chal centre vie sal quai jardin devant camp ferm circuit cour rive ceinture z
            if 'de' in item['name'].split():
                continue
            elif 'du' in item['name'].split():
                continue
            elif "d'" in item['name']:
                continue
            elif 'principale' in item['name'].lower().split():
                continue
            elif 'neuve' in item['name'].lower().split():
                continue
            elif 'centrale' in item['name'].lower().split():
                continue
            elif 'haute' in item['name'].lower().split():
                continue
            elif 'basse' in item['name'].lower().split():
                continue
            elif 'longue' in item['name'].lower().split():
                continue
            elif 'des' in item['name'].split():
                continue
            else:
                # print(item['name'], ',', item['coordinates'][0][0], item['coordinates'][0][1])
                counter.append(item['name'])
    # print(item['name'].split()[0])
    if item['name'].split()[0] not in newp:
        newp.append(item['name'].split()[0])
print(len(counter))
# print(*newp, sep='\n')
print(*counter, sep='\n')

# for item in streetNames:
#     if 'pont' in item['name'].lower():
#         print(item)

print(len(streetNames))
print(len(newp))
print()


# ###### This is a list of names out of the 1278 in newp.
# Fraeschegaass
# Härewiss
# Dittegaass
# Dupontsgaessel
# Badensgaessel
# Schumanswee
# Marcel-Greischer-Strooss
# Mathessegaessel
# Witrysgaass
# Pierre-Risch-Strooss
# Fräschepéilchen
# Donatusgaessel
# Kinnekswee
# Tobiaswee