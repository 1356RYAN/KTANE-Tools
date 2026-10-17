import math
def morsematics(serial, battery, lit_list, unlit_list, received):
    letter_number_translate = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,
                               "M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}

    number_letter_translate = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K",12:"L",
                               13:"M",14:"N",15:"O",16:"P",17:"Q",18:"R",19:"S",20:"T",21:"U",22:"V",23:"W",24:"X",25:"Y",26:"Z"}

    letter_morse_translate = {"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---",
                              "K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-",
                              "U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--.."}
    
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23]

    def normalize_letter_pair() -> None:
            letter_pair[0] = (letter_pair[0] - 1) % 26 + 1
            letter_pair[1] = (letter_pair[1] - 1) % 26 + 1

    def letter_pair_number(serial) -> None:
        global letter_pair
        letter_pair = list(serial[3:5])
        for i, char in enumerate(letter_pair):
            if char.isalpha():
                letter_pair[i] = letter_number_translate[char.upper()]
            else:
                letter_pair[i] = int(char)

    def indicator_match(lit_list, unlit_list, received) -> None:
        received_list = list(received.upper())
        for char in received_list:
            letter_pair[0] += (" ".join(lit_list)).count(char)
        for char in received_list:
            letter_pair[1] += (" ".join(unlit_list)).count(char)

    def sum_pair() -> None:
        if math.sqrt(letter_pair[0] + letter_pair[1]) % 1 == 0:
            letter_pair[0] += 4
        else:
            letter_pair[1] -= 4

    def largest_recieved(received) -> None:
        largest = 0
        for char in received:
            if letter_number_translate[char.upper()] > largest:
                largest = letter_number_translate[char.upper()]

        letter_pair[0] += largest

    def prime_square_batteries_recieved(received) -> None:
        for char in received:
            if letter_number_translate[char.upper()] in prime_numbers:
                letter_pair[0] -= prime_numbers[prime_numbers.index(letter_number_translate[char.upper()])]
                normalize_letter_pair()

        for char in received:
            if math.sqrt(letter_number_translate[char.upper()]) % 1 == 0:
                letter_pair[1] -= letter_number_translate[char.upper()]
                normalize_letter_pair()

        if battery > 0:
            for char in received:
                if letter_number_translate[char.upper()] % battery == 0:
                    letter_pair[0] -= letter_number_translate[char.upper()]
                    letter_pair[1] -= letter_number_translate[char.upper()]
                    normalize_letter_pair()


    letter_pair_number(serial)
    indicator_match(lit_list, unlit_list, received)
    normalize_letter_pair()
    sum_pair()
    normalize_letter_pair()
    largest_recieved(received)
    normalize_letter_pair()
    prime_square_batteries_recieved(received)
    normalize_letter_pair()

    if letter_pair[0] > letter_pair[1]:
        return letter_morse_translate[number_letter_translate[(letter_pair[0] - letter_pair[1]) % 27]]

    elif letter_pair[1] > letter_pair[0]:
        return letter_morse_translate[number_letter_translate[(letter_pair[1] + letter_pair[0]) % 27]]
    else:
        return letter_morse_translate[number_letter_translate[letter_pair[0] % 27]]

if __name__ == "__main__":
    serial = input("Enter the serial number: ")
    battery = int(input("Enter the number of batteries: "))
    lit_list = input("Enter the lit indicators (space-separated): ").split(" ")
    unlit_list = input("Enter the unlit indicators (space-separated): ").split(" ")
    while True:
        received = input("Enter the received letters: ")
        result = morsematics(serial, battery, lit_list, unlit_list, received)

        print(f"The result is: {result}")
