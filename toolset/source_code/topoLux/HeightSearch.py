from MicroTopoHeightLoad import microTopoHeight


queryList = []

AboveFiveH = []
FourFifty = []
FourUptoFifty = []
ThreeFifty = []
ThreeUpToFifty = []
TwoFifty = []
TwoUpToFifty = []
OneFiftyUpToTwo= []
BelowOneFifty = []
Other = []


for item in microTopoHeight:
    # if item['heightM'] not in queryList:
    #     queryList.append(item['heightM'])
    if item['heightCM'] >= 50000:
        AboveFiveH.append([item['name'], item['heightCM']])
    elif item['heightCM'] in range(45000, 50000):
        FourFifty.append([item['name'], item['heightCM']])
    elif item['heightCM'] in range(40000, 45000):
        FourUptoFifty.append([item['name'], item['heightCM']])
    elif item['heightCM'] in range(35000, 40000):
        ThreeFifty.append([item['name'], item['heightCM']])
    elif item['heightCM'] in range(30000, 35000):
        ThreeUpToFifty.append([item['name'], item['heightCM']])
    elif item['heightCM'] in range(25000, 30000):
        TwoFifty.append([item['name'], item['heightCM']])
    elif item['heightCM'] in range(20000, 25000):
        TwoUpToFifty.append([item['name'], item['heightCM']])
    elif item['heightCM'] in range(15000, 20000):
        OneFiftyUpToTwo.append([item['name'], item['heightCM']])
    elif item['heightCM'] < 15000:
        BelowOneFifty.append([item['name'], item['heightCM']])
    else:
        Other.append([item['name'], item['heightCM']])


sortedList = sorted(queryList)

print('\nThere are {} place names with the following distribution by height:\n'.format(str(len(microTopoHeight))))

print('Above 500 m are \t\t\t\t\t\t\t\t' + str(len(AboveFiveH)) + '\t\tplace names.')
print('Between 450 up to but not including 500 m are \t' + str(len(FourFifty)) + '\tplace names.')
print('Between 400 up to but not including 450 m are \t' + str(len(FourUptoFifty)) + '\tplace names.')
print('Between 350 up to but not including 400 m are \t' + str(len(ThreeFifty)) + '\tplace names.')
print('Between 300 up to but not including 350 m are \t' + str(len(ThreeUpToFifty)) + '\tplace names.')
print('Between 250 up to but not including 300 m are \t' + str(len(TwoFifty)) + '\tplace names.')
print('Between 200 up to but not including 250 m are \t' + str(len(TwoUpToFifty)) + '\tplace names.')
print('Between 150 up to but not including 200 m are \t' + str(len(OneFiftyUpToTwo)) + '\tplace names.')
print('Below 150 m are \t\t\t\t\t\t\t\t' + str(len(BelowOneFifty)) + '\t\tplace names.\n')

print('\nCount of all these: {} instances.'.format(str(len(AboveFiveH) +
                                                       len(FourFifty) +
                                                       len(FourUptoFifty) +
                                                       len(ThreeFifty) +
                                                       len(ThreeUpToFifty) +
                                                       len(TwoFifty) +
                                                       len(TwoUpToFifty) +
                                                       len(OneFiftyUpToTwo) +
                                                       len(BelowOneFifty))))

print('\nThere are {} instances that were not parsed.\n\n'.format(str(len(Other))))


# with open('HeightDistribution.txt', 'w', encoding='utf-8') as writer:
#     writer.write('There are {} place names with the following distribution by height:\n\n'.
#                  format(str(len(microTopoHeight))))
#     writer.write('Above 500 m are \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t' + str(len(AboveFiveH)) + '\t\tplace names.\n')
#     writer.write('Between 450 up to but not including 500 m are \t' + str(len(FourFifty)) + '\tplace names.\n')
#     writer.write('Between 400 up to but not including 450 m are \t' + str(len(FourUptoFifty)) + '\tplace names.\n')
#     writer.write('Between 350 up to but not including 400 m are \t' + str(len(ThreeFifty)) + '\tplace names.\n')
#     writer.write('Between 300 up to but not including 350 m are \t' + str(len(ThreeUpToFifty)) + '\tplace names.\n')
#     writer.write('Between 250 up to but not including 300 m are \t' + str(len(TwoFifty)) + '\tplace names.\n')
#     writer.write('Between 200 up to but not including 250 m are \t' + str(len(TwoUpToFifty)) + '\tplace names.\n')
#     writer.write('Between 150 up to but not including 200 m are \t' + str(len(OneFiftyUpToTwo)) + '\tplace names.\n')
#     writer.write('Below 150 m are \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t' + str(len(BelowOneFifty)) + '\t\tplace names.\n\n')
#     writer.write('\nCount of all these: {} instances.'.format(str(len(AboveFiveH) +
#                                                                   len(FourFifty) +
#                                                                   len(FourUptoFifty) +
#                                                                   len(ThreeFifty) +
#                                                                   len(ThreeUpToFifty) +
#                                                                   len(TwoFifty) +
#                                                                   len(TwoUpToFifty) +
#                                                                   len(OneFiftyUpToTwo) +
#                                                                   len(BelowOneFifty))))
#     writer.write('\n\n\nThere are {} instances that were not parsed.\n\n\n'.format(str(len(Other))))
#     writer.write('--End of Iteration--\n')
# writer.close()

