"""think"""
def data(thing):
    menu = {'Khao Phad Mhoo':['rice','pork','egg'],
            'Khao Phad kai':['rice','chicken','egg'],
            'Mhoo Phad Kratiem':['pork','garlic'],
            'kai Phad Kratiem':['chicken','garlic'],
            'Mhoo Phad Kra Phrao':['pork','basil'],
            'kai Phad Kra Phrao':['chicken','basil'],
            'Mama Phad Mhoo':['mama','pork','egg'],
            'Mama Phad kai':['mama','chicken','egg'],
            'Mhoo Phad Nam Plar':['pork','fish sauce'],
            'kai Phad Nam Plar':['chicken','fish sauce'],
            'Panaeng Mhoo':['pork','panaeng curry','coconut milk','red chilli'],
            'Panaeng kai':['chicken','panaeng curry','coconut milk','red chilli'],
            'Fakthong Phad Khai':['pumpkin','egg','garlic'],
            'Khai Palo':['egg','tofu','palo','garlic']
            }
    lst = []
    for m in menu:
        num_count = 0
        for i in thing:
            if i in menu[m]:
                num_count += 1
        lst.append((len(menu[m])-num_count, m))
    lst.sort()
    output(lst)


def output(out):
    all_lst = []
    # lst = [[] for _ in range(10)]
    # for i in out:
        # if i[0] == 0:
        #     lst[0].append(i[1])
        # elif i[0] == 1:
        #     lst[1].append(i[1])
        # elif i[0] == 2:
        #     lst[2].append(i[1])
        # elif i[0] == 3:
        #     lst[3].append(i[1])
        # elif i[0] == 4:
        #     lst[4].append(i[1])
        # elif i[0] == 5:
        #     lst[5].append(i[1])
        # elif i[0] == 6:
        #     lst[6].append(i[1])
        # elif i[0] == 7:
        #     lst[7].append(i[1])
        # elif i[0] == 8:
        #     lst[8].append(i[1])
        # elif i[0] == 9:
        #     lst[9].append(i[1])
        # elif i[0] == 10:
        #     lst[10].append(i[1])
    lst0 = []
    lst1 = []
    lst2 = []
    lst3 = []
    lst4 = []
    lst5 = []
    lst6 = []
    lst7 = []
    lst8 = []
    lst9 = []
    lst10 = []
    for i in out:
        if i[0] == 0:
            lst0.append(i[1])
        elif i[0] == 1:
            lst1.append(i[1])
        elif i[0] == 2:
            lst2.append(i[1])
        elif i[0] == 3:
            lst3.append(i[1])
        elif i[0] == 4:
            lst4.append(i[1])
        elif i[0] == 5:
            lst5.append(i[1])
        elif i[0] == 6:
            lst6.append(i[1])
        elif i[0] == 7:
            lst7.append(i[1])
        elif i[0] == 8:
            lst8.append(i[1])
        elif i[0] == 9:
            lst9.append(i[1])
        elif i[0] == 10:
            lst10.append(i[1])
    num = 0
    lst_ans = []
    while num != 10:
        num += 1
        print(num, out[num-1][1])
        lst_ans.append(out[num-1][1])

    choose = int(input("NUMBER:"))
    while not(1 <= choose <= 10):
        choose = int(input("NUMBER:"))

    num = 0
    count = 1
    while count != 11:
        count += 1
        num += 1
        if num == choose:
            print(out[num-1][1])




def main():
    print("egg    rice    pork    chicken    coconut    ")
    check = input("MATERIAL:")
    thing = []
    while check != 'end':
        thing.append(check)
        check = input("MATERIAL:")
    data(thing)
main()
