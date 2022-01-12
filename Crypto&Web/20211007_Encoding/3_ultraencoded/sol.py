#open the text file
with open('zero_one', 'r') as file:
    challenge = file.read()

#replace the zeros and ones in the numerical representation
challenge = challenge.replace('ZERO', '0').replace('ONE', '1').replace(' ','')
print(challenge)

#let see the length
print(len(challenge))

#since it is not a multiple of 8, we can't think that this is a series of ascii characters
result=''.join(chr(int(challenge[i*8:i*8+8],2)) for i in range(len(challenge)//8))
print(result)

#the last couple of characters are '==' ... it looks a base64
import base64
decoded = base64.b64decode(result).decode('ascii')
print(decoded)
