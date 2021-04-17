from collections import defaultdict

def create_rotors(rotors):
    rotor_dictionaries = []
    for j in range(len(rotors)):
        rotor_finished = {}
        for i in enumerate(rotors[j]):
            rotor_finished[i] = ord(i)-65
        rotor_dictionaries.append(rotor_finished)
    return rotor_dictionaries



if __name__ == "__main__":
    # execute only if run as a script
    #main()
    rotor_strings = ["EKMFLGDQVZNTOWYHXUSPAIBRCJ", "AJDKSIRUXBLHWTMCQGZNPYFVOE", 
                     "BDFHJLCPRTXVZNYEIWGAKMUSQO", "ESOVPZJAYQUIRHXLNFTGKDCMWB", 
                     "VZBRGITYUPSDNHLXAWMJQOFECK", "JPGVOUMFYQBENHZRDKASXLICTW", 
                     "NZJHGRCXMYSWBOUFAIVLPEKQDT", "FKQHTLXOCBJSPDZRAMEWNIUYGV"]

    rotors = create_rotors(rotor_strings)
    for i in range(len(rotors)):
        print(rotors[i])
        
        
            
