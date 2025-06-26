def slot(lit: int, unlit: int, RCA_PS2: bool, full: str, battery: int, parallel: bool, right_serial: int, unlit_BOB: bool, serial_port: bool, serial_numlargest):   
    full_list = list(full)
    fibo = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    binary = {0: 0, 1: 1, 2: 1, 3: 2, 4: 1, 5: 2, 6: 2, 7: 3, 8: 1, 9: 2, 10: 2}
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    final =[]

    def all_slots(slot_num1, slot_num1_orig):    
        if slot_num1 == 2:
            slot_num1 = 5
        elif slot_num1 == 7:
            slot_num1 = 0
        slot_num1 = slot_num1 + lit - unlit
        if slot_num1 % 3 == 0:
            slot_num1 = slot_num1 + 4
        elif slot_num1 > 7:
            slot_num1 = slot_num1 * 2
        elif slot_num1 < 3 and slot_num1 % 2 == 0:
            slot_num1 = slot_num1 / 2
        elif RCA_PS2 == True:
            return slot_num1
        else:
            slot_num1 = slot_num1_orig + battery
        return slot_num1

    def slot_position1(slot_num2):
        right_num = int(full_list[1])
        if slot_num2 % 2 == 0 and slot_num2 > 5:
            slot_num2 = slot_num2 / 2
        elif any(ele == slot_num2 for ele in prime):
            slot_num2 = slot_num2 + right_serial
        elif parallel == True:
            slot_num2 = slot_num2 * -1
        elif right_num % 2 != 0:
            return slot_num2
        else:
            slot_num2 = slot_num2 - 2
        return slot_num2

    def slot_position2(slot_num3):
        if unlit_BOB == True:
            return slot_num3
        elif slot_num3 == 0:
            one_slot = int(full_list[0])
            slot_num3 = slot_num3 + one_slot
        elif any(ele == slot_num3 for ele in fibo):
            for i in range(len(fibo)):
                if fibo[i] == slot_num3:
                    slot_num3 = slot_num3 + fibo[i + 1]
                    break
        elif slot_num3 >= 7:
            slot_num3 = slot_num3 + 4
        else:
            slot_num3 = slot_num3 * 3
        return slot_num3

    def slot_position3(slot_num4,slot_num4_orig):
        if serial_port == True:
            slot_num4 = slot_num4 + serial_numlargest
        elif True == same_num(slot_num4_orig):
            return slot_num4
        elif slot_num4 >= 5:
            slot_num4 = binary.get(slot_num4_orig)
        else:
            slot_num4 = slot_num4 + 1
        return slot_num4

    def same_num(x):
        checklist = full_list
        checklist.pop()
        if any(int(ele) == x for ele in checklist):
            return True
        else:
            return False

    for x in range(len(full_list)):
        slot = x + 1
        slot_num_orig = int(full_list[x])
        slot_num = all_slots(slot_num_orig, slot_num_orig)
        print(slot_num)
        if slot == 1:
            slot_num = slot_position1(slot_num)
        elif slot == 2:
            slot_num = slot_position2(slot_num)
        elif slot == 3:
            slot_num = slot_position3(slot_num, slot_num_orig)
        else:
            print("Invalid slot number")
            break
        while slot_num > 9:
            slot_num = slot_num - 10
        while slot_num < 0:
            slot_num = slot_num + 10
        final.append(slot_num)
    return final
