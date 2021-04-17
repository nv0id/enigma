from collections import defaultdict

def create_rotors(rotor_strings):
    rotor_dictionaries = []
    for j in rotor_strings:
        rotor_finished = {}
        for i in enumerate(j):
            rotor_finished[i[0]] = ord(i[1])-97
        rotor_dictionaries.append(rotor_finished)
    return rotor_dictionaries

def choose_rotor():
    one   = int(input("First Rotor: "))
    #ptr1  = int(input("Starting offest: "))
    two   = int(input("Second Rotor: "))
    #ptr2  = int(input("Starting offest: "))
    three = int(input("Thrid Rotor: "))
    #ptr3  = int(input("Starting offest: "))
    choices = [one, two, three]
    #pointers = [ptr1, ptr2, ptr3]

    #choices  = [1, 1, 1]
    pointers = [0, 0, 0]

    return choices, pointers

def encode(rotors, pointers, message):

    encoded_message = ""
    for i in rotors:
        print(i)

    for i in message:
        print(i)
        char_val = ord(i)-97
        print("OG: ", char_val)

        char_val = rotors[0].get(char_val+pointers[0])
        pointers = inc_ptr_0(pointers)
        print("1st:", char_val)

        char_val = rotors[1].get(char_val+pointers[1])
        pointers = inc_ptr_1(pointers)
        print("2nd: ", char_val)

        char_val = rotors[2].get(char_val+pointers[2])
        pointers = inc_ptr_2(pointers)
        print("3rd: ", char_val, "\n")

        encoded_message += chr(char_val+97)

    return encoded_message

        
def inc_ptr_0(pointers):
    pointers[0] += 1
    if pointers[0] == 26:
        pointers[0] = 0
        inc_ptr_1(pointers)

    return pointers

def inc_ptr_1(pointers):
    pointers[1] += 1
    if pointers[1] == 26:
        pointers[1] = 0
        inc_ptr_2(pointers)

    return pointers

def inc_ptr_2(pointers):
    pointers[2] +=1
    if pointers[2] == 26:
        pointers[2] = 0
    
    return pointers

if __name__ == "__main__":
    # execute only if run as a script
    #main()

    rotor_strings = ["ekmflgdqvzntowyhxuspaibrcj", "ajdksiruxblhwtmcqgznpyfvoe", 
                     "bdfhjlcprtxvznyeiwgakmusqo", "esovpzjayquirhxlnftgkdcmwb", 
                     "vzbrgityupsdnhlxawmjqofeck", "jpgvoumfyqbenhzrdkasxlictw", 
                     "nzjhgrcxmyswboufaivlpekqdt", "fkqhtlxocbjspdzramewniuygv"]

    rotors = create_rotors(rotor_strings)

    choices = choose_rotor()
    three_rotors = [rotors[choices[0][0]-1], rotors[choices[0][1]-1], rotors[choices[0][2]-1]]

    message = input("Enter Message: ").lower()

    print(encode(three_rotors, choices[1], message))

    


    