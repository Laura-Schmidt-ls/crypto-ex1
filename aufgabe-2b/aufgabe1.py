"""
Abgabe zu Aufgabe 1-2

Laura Schmidt
Andreas Schneider
"""

# Array k (result from 2a)
kArray = [66, 76, 71, 73, 85, 78, 73, 77, 83, 85, 68, 68, 75, 74, 75, 83, 68, 68, 77, 69, 77, 71, 84, 65, 76, 83, 77, 68, 66, 65, 73, 68, 82, 78, 90, 83, 77, 73, 83, 69, 75, 66, 71, 84, 85, 75, 80, 85]

# helper method to perform calculation
def decode(character, index):
    c = ord(character) # convert to ascii
    m = (c - kArray[index]) % 128 # m = c - k mod 128
    return chr(m) # reconvert m and return

decoded = ""
# saves char index in cipher.txt
i = 0

# open file and perform decode for each char
with open("cipher.txt","r") as f:
    for line in f:
        for char in line:
            decoded = decoded + decode(char, i % 48) # i mod 48 is normalized index to access k (overflow prevention)
            i += 1

print(decoded)

# output to file
outFile = open("decoded.txt", 'w')
outFile.write(decoded)
outFile.close()

"""
Result shows Garfield

                 __ __
               ,;::\::\
             ,'/' `/'`/
         _\,7 '.,-'.-':.
        -./"'  7    :  :\/,
         :7.  ,:____;__; :-
         :"  ( .`-*'o*',);
          \.. ` `---'`' /
           `7._..-   _.'
           ,;  .     `.
          /"'| |       \
         ::. ) :        7
         |" (   \       |
         :.(_,  :       ;
          \'`-'_/      /
           `:..   , _,'
            |,|  : |
            |`|  | |
            |,|  | |
        ,--.;`|  | '..--.
       /;' "' ;  '..--. ))
       \:.___(___   ) ))'
              SSt`-'-''
"""
