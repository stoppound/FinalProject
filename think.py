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
    lst1 = []
    lst2 = []
    lst3 = []
    lst4 = []
    for m in menu:
        num_count = 0
        for i in thing:
            if i in menu[m]:
                num_count += 1
        lst1.append((len(menu[m])-num_count, m))
    lst1.sort()
    # for i in thing:
    #     for m in menu:
    #         if m not in lst1:
    #             if i in menu[m]:
    #                
    output(lst1)


def output(out):
    for i in out:
        print(i)


def main():
    check = input()
    thing = []
    while check != 'end':
        thing.append(check)
        check = input()
    data(thing)
main()
