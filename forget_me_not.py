def forget_me_not(serial: str, number: str, unlit_car: bool, unlit: int, lit: int, serial_port: bool):
    """
    This function calculates a final list of digits based on the input serial number and module numbers.
    It considers various conditions such as unlit indicators, lit indicators, and the presence of a serial port.
    """
    final = []
    intial = list(number)
    serial_num_list = []
    modules = len(intial)
    
    def serial_list()->None:
        global serial_list
        #global serial_num_list
        global serial_num_largest
        global serial_num_smallest_odd
        serial_list = list(serial)
        for i in serial_list:
            if i.isdigit():
                serial_num_list.append(int(i))
        serial_num_largest = serial_num_list[0]
        for i in serial_num_list:
            if i > serial_num_largest:
                serial_num_largest = i
        serial_num_smallest_odd = 10
        for i in serial_num_list:
            if i % 2 != 0 and i < serial_num_smallest_odd:
                serial_num_smallest_odd = i
        if serial_num_smallest_odd == 10:
            serial_num_smallest_odd = 9

    def combiner(first_digit, num):
        com_digit = int(first_digit) + int(num)
        com_list = list(str(com_digit))
        return com_list[-1]

    def first_digit():
        first_digit = intial[0]
        if unlit_car == True:
            num = 2
        elif unlit > lit:
            num = 7
        elif unlit == 0:
            num = lit
        else:
            num = serial_list[-1]
        return combiner(first_digit, num)

    def second_digit():
        second_digit = intial[1]
        if len(serial_num_list) >= 3 and serial_port == True:
            num = 3
        elif (int(final[0]) % 2) == 0:
            num = int(final[0]) + 1
        else:
            num = int(final[0]) - 1
        return combiner(second_digit, num)

    def all_others(i):
        digit = int(intial[i])
        if int(final[i-1]) == 0 or int(final[i-2]) == 0:
            num = serial_num_largest
        elif (int(final[i - 1]) % 2) == 0 and (int(final[i - 2]) % 2) == 0:
            num = serial_num_smallest_odd
        else:
            num = int(final[i - 1]) + int(final[i - 2])
            com_list = list(str(num))
            num = com_list[0]
        return combiner(digit, num) 

    serial_list()
    final.append(first_digit())
    final.append(second_digit())
    for i in range(modules - 2):
        final.append(all_others(i + 2))

    return final
