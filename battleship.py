letter_translate = {"A":"A","B":"B","C":"C","D":"D","E":"E","F":"A","G":"B","H":"C","I":"D","J":"E","K":"A","L":"B","M":"C","N":"D","O":"E","P":"A","Q":"B","R":"C","S":"D","T":"E","U":"A","V":"B","W":"C","X":"D","Y":"E","Z":"A"}
letter_num_translate = {1:"A",2:"B",3:"C",4:"D",5:"E"}
serial_num = str(input("Input the Serial Number:"))
serial_num_list = []
serial_let_list = []
final_pair_list = []
def serial_num_to_lists(serial_num)->None:
    global serial_num_list
    global serial_let_list
    serial_tot_list = list(serial_num)
    for i in serial_tot_list:
        if i.isdigit():
            serial_num_list.append(i)
        else:
            serial_let_list.append(i)

def pairs(serial_num_list,serial_let_list)->None:
    global final_pair_list
    if len(serial_num_list) > len(serial_let_list):
        pair_amount = len(serial_let_list)
    else:
        pair_amount = len(serial_num_list)
    for i in range(pair_amount):
        letter = serial_let_list[i]
        number = int(serial_num_list[i])
        letter = letter_translate[letter]
        while number > 5:
            number = number - 5
        while number < 1:
            number = number + 5
        final_pair_list.append(letter + str(number))

def final_pair():
    ports = int(input("Input the amount of Ports:"))
    indicator = int(input("Input the amount of Indicators:"))
    batteries = int(input("Input the amount of Batteries:"))
    while ports > 5:
        ports = ports - 5
    while ports < 1:
        ports = ports + 5
    letter = letter_num_translate[ports]
    number =  indicator + batteries
    while number > 5:
        number = number - 5
    while number < 1:
        number = number + 5
    final_pair_list.append(letter + str(number))
serial_num_to_lists(serial_num)
pairs(serial_num_list,serial_let_list)
final_pair()
print(final_pair_list)