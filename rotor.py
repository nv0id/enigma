from collections import defaultdict

def create_rotors(rotor_strings):
    rotor_dictionaries = []
    for j in rotor_strings:
        rotor_finished = {}
        for i in enumerate(j):
            rotor_finished[i[0]+1] = ord(i[1])-96
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
    #offset = [ptr1, ptr2, ptr3]

    #choices  = [1, 1, 1]
    offset = [0, 0, 0]

    return choices, offset

def encode(rotors, offset, message, notches):

    encoded_message = ""
    for i in rotors:
        print(i)

    for i in message:
        print(i)
        char_val = ord(i)-96
        print("OG: ", char_val)

        char_val = rotors[0].get(char_val+offset[0])
        print("1st:", char_val)

        char_val = rotors[1].get(char_val+offset[1])
        print("2nd: ", char_val)

        char_val = rotors[2].get(char_val+offset[2])
        print("3rd: ", char_val, "\n")


        offset = inc_ptr_0(offset, notches)
        encoded_message += chr(char_val+96)

    return encoded_message

        
def inc_ptr_0(offset, notches):
    #two check: 1) if notch +1 to next rotor in sequence
    #           2) if on 26 next value to 27.





    offset[0] += 1
    if offset[0] == 27:
        offset[0] = 0
        offset[1] += 1
        if offset[1] == 27:
            offset[1] = 0
            offset[2] +=1
            if offset[2] == 27:
                offset[2] = 0

    return offset

if __name__ == "__main__":
    # execute only if run as a script
    #main()
            # I turn 17, II turn 5, III turn 22, IV turn 10,  V turn  26,
    rotor_strings = ["ekmflgdqvzntowyhxuspaibrcj", "ajdksiruxblhwtmcqgznpyfvoe", 
                     "bdfhjlcprtxvznyeiwgakmusqo", "esovpzjayquirhxlnftgkdcmwb", 
                     "vzbrgityupsdnhlxawmjqofeck"]
                     # "jpgvoumfyqbenhzrdkasxlictw", "nzjhgrcxmyswboufaivlpekqdt", "fkqhtlxocbjspdzramewniuygv"]
    rotor_notches = [17, 5, 22, 10, 26]

    rotors = create_rotors(rotor_strings)

    choices = choose_rotor()
    three_rotors = [rotors[choices[0][0]-1], rotors[choices[0][1]-1], rotors[choices[0][2]-1]]
    three_notches = [rotor_notches[choices[0][0]-1], rotor_notches[choices[0][1]-1], rotor_notches[choices[0][2]-1]]

    message = input("Enter Message: ").lower()

    print(encode(three_rotors, choices[1], message, three_notches))

    


    