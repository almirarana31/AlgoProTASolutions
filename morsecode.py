def conversion(text):
    code = ({' ':'  ', 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.',
             'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..'
        ,'M':'--', 'N':'-.', 'O':'---', 'P': '.---.'
        ,'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-'
        ,'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', ',':'--.--',
             '.':'.-.-.-', '?':'..--..','0':'-----', '1':'.----', '2':'..---',
             '3':'...--', '4':'....-','5':'.....', '6':'-....','7':'--....', '8':'---..','9':'----.'})

    #create empty string
    morse_code = ""

    #for loop with if else conditonal to ensure character inputted is within dictionary
    for char in text:
        if char.upper() in code:
            morse_code += code[char.upper()]
        else:
            morse_code += ' '

    return morse_code

#input from user
text = input("Enter the string to be converted to Morse code:")
#print results by calling function
print(conversion(text))