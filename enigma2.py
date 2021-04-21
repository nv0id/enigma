def choose_rotor():
    #one   = int(input("Left Rotor: "))
    #ptr1  = int(input("Left Ring setting: "))
    #two   = int(input("Middle Rotor: "))
    #ptr2  = int(input("Middle Ring setting: "))
    #three = int(input("Right Rotor: "))
    #ptr3  = int(input("Right Ring setting: "))
    #choices = [one, two, three]
    #offset = [ptr1, ptr2, ptr3]

    # fastest to slowest
    choice_rotors  = [3, 2, 1]
    R_settings = [0, 0, 0]
    #input of letters, make lowercase and then turn to ints, a = 0
    starting_letters = [0, 0, 0]


    return choice_rotors, R_settings, starting_letters

def setup(rotors, R_settings):
    return rotors

def encode(rotors_encoding_strings, starting_letters, notches, message, reflector):
    encoded_message = ""
    rotations = [0, 0, 0]
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rotor_positions = [alphabet, alphabet, alphabet]

    #turn rotors to match starting letters.
    for n,i in enumerate(rotor_positions):
        rotors_encoding_strings[n] = i[starting_letters[n]:]+i[:starting_letters[n]]

    for i in message:
        rotor_positions = move_rotors(rotor_positions, notches)
        
        print("---------")
        for zaxs in rotor_positions:
            print(zaxs)
        print(reflector)
        print("\n")

        print("OG:", i)
        
        

    """
    Index i and find() alphabet letter.
    Index alphabet letter to rotors_encoding_strings.
    Find() encoded letter in alphabet string.
    Next rotor. 
    """


    encoded_message += chr(char_val+97)
        
    print("\n")

    return encoded_message

def move_rotors(rotors, notches):
    #move 1st rotors, check for notch. repeat for next 2.
    rotors[0] = rotors[0][1:]+rotors[0][0]
    
    if rotors[0][0] ==  notches[0]:
        rotors[1] = rotors[1][1:]+rotors[1][0]
        if rotors[1][0] == notches[1]:
            rotors[2] = rotors[2][1:]+rotors[2][0]
    return rotors


if __name__ == "__main__":
    # execute only if run as a script
                    # I turn 17, II turn 5, III turn 22, IV turn 10,  V turn  26
    rotor_strings = ["ekmflgdqvzntowyhxuspaibrcj", "ajdksiruxblhwtmcqgznpyfvoe", 
                     "bdfhjlcprtxvznyeiwgakmusqo", "esovpzjayquirhxlnftgkdcmwb", 
                     "vzbrgityupsdnhlxawmjqofeck"]
                     # "jpgvoumfyqbenhzrdkasxlictw", "nzjhgrcxmyswboufaivlpekqdt", "fkqhtlxocbjspdzramewniuygv"]
    rotor_notches = ["r", "f", "w", "k", "a"]

    reflector_B = "yruhqsldpxngokmiebfzcwvjat"

    choices = choose_rotor()
    three_rotors = [rotor_strings[choices[0][0]-1], rotor_strings[choices[0][1]-1], rotor_strings[choices[0][2]-1]]
    three_notches = [rotor_notches[choices[0][0]-1], rotor_notches[choices[0][1]-1], rotor_notches[choices[0][2]-1]]
    starting_letters = choices[2]
    message = input("Enter Message: ").lower()

    setup(three_rotors, choices[1])

    print(encode(three_rotors, starting_letters, three_notches, message, reflector_B))
