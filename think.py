"""think"""
def data(thing):
    menu = {'Khao Phad Mhoo':['rice','pork','egg'],
            'Khao Phad Mhoo':['rice','chicken','egg'],
            'Mhoo Phad Kratiem':['pork','garlic'],
            'Ghai Phad Kratiem':['chicken','garlic'],
            'Mhoo Phad Kra Phrao':['pork','basil'],
            'Ghai Phad Kra Phrao':['chicken','basil'],
            'Mama Phad Mhoo':['mama','pork','egg'],
            'Mama Phad Ghai':['mama','chicken','egg'],
            'Mhoo Phad Nam Plar':['pork','fish sauce'],
            'Ghai Phad Nam Plar':['chicken','fish sauce'],
            'Panaeng Mhoo':['pork','panaeng curry','coconut milk','red chilli'],
            'Panaeng Ghai':['chicken','panaeng curry','coconut milk','red chilli'],
            'Fuck Tong Phad Khai':['pumpkin','egg','garlic'],
            'Khai Palo':['egg','tofu','palo','garlic']
            }
    for i in thing:
        for var in menu:
            if i in menu[var]:
                print(menu[var])
def main():
    check = input()
    thing = []
    while check != 'end':
        thing.append(check)
        check = input()
    data(thing)
main()
