

def choose_rotor():
    #one   = int(input("First Rotor: "))
    #ptr1  = int(input("Starting offest: "))-1
    #two   = int(input("Second Rotor: "))
    #ptr2  = int(input("Starting offest: "))-1
    #three = int(input("Thrid Rotor: "))
    #ptr3  = int(input("Starting offest: "))-1
    #choices = [one, two, three]
    #offset = [ptr1, ptr2, ptr3]

    choices  = [1, 2, 3]
    offset = [0, 0, 0]

    return choices, offset

def encode(rotors, offset, notches, message, reflector):
    
    encoded_message = ""
    
    #inital rotor setup
    for n,i in enumerate(rotors):
        rotors[n] = i[offset[n]:]+i[:offset[n]]
    
    print("\n")
    
    for i in message:
        print("OG: ", i )
        rotors = move_rotors(rotors, notches)
        char_val = ord(i)-97
        for j in rotors:
            print("Fro:", chr(char_val+97))
            char_val = ord(j[char_val])-97
            print("Chr:", chr(char_val+97))
            print("\n")
        
        char_val = ord(reflector[char_val])-97
        print("ChR:", chr(char_val+97))
        
        for j in reversed(rotors):
            char_val = ord(j[char_val])-97
            print("Chr:", chr(char_val+97))

        print("\nNext")
        for zaxs in rotors:
            print(zaxs)
        print(reflector)
        print("\n")

        
        encoded_message += chr(char_val+97)
    
    return encoded_message

def move_rotors(rotors, notches):
    #move 1st rotors, check for notch. repeat for next 2.
    rotors[0] = rotors[0][1:]+rotors[0][0]
    
    if rotors[0][0] ==  notches[0]:
        rotors[1] = rotors[1][1:]+rotors[1][0]
        if rotors[1][0] == notches[1]:
            rotors[2] = rotors[2][1:]+rotors[2][0]

    return rotors

# AS BI EF GJ HX LZ NO PW QT UV
def plugboard(setting,input_letter):
    setting = setting.split(" ")
    for i in setting:
        if setting[i][0] == input_letter.upper():
            return setting[i][1].lower()


if __name__ == "__main__":
    # execute only if run as a script
    #main()
            # I turn 17, II turn 5, III turn 22, IV turn 10,  V turn  26,
    rotor_strings = ["ekmflgdqvzntowyhxuspaibrcj", "ajdksiruxblhwtmcqgznpyfvoe", 
                     "bdfhjlcprtxvznyeiwgakmusqo", "esovpzjayquirhxlnftgkdcmwb", 
                     "vzbrgityupsdnhlxawmjqofeck"]
                     # "jpgvoumfyqbenhzrdkasxlictw", "nzjhgrcxmyswboufaivlpekqdt", "fkqhtlxocbjspdzramewniuygv"]
    rotor_notches = ["s", "i", "u", "u", "v"]

    reflector_B = "yruhqsldpxngokmiebfzcwvjat"

    choices = choose_rotor()
    three_rotors = [rotor_strings[choices[0][0]-1], rotor_strings[choices[0][1]-1], rotor_strings[choices[0][2]-1]]
    three_notches = [rotor_notches[choices[0][0]-1], rotor_notches[choices[0][1]-1], rotor_notches[choices[0][2]-1]]

    message = input("Enter Message: ").lower()
    print("\n")
    print(encode(three_rotors, choices[1], three_notches, message, reflector_B))
