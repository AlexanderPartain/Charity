#python3

with open("ciphertext", "rb", buffering=4096) as intext: # reads in ciphertext and key file, ciphertext needs to be changed to command line
    text = intext.read()
with open("key", "rb", buffering=4096) as inkey:
    key = inkey.read()

keycode = [chr(q) for q in key] # changes binary int of file to ascii character
w = 0
while w < len(key):
    keycode[w] = ord(keycode[w]) # converts to ascii value
    keycode[w] = bin(keycode[w]) # binary conversion
    w += 1

textcode = [chr(r) for r in text]
e = 0
while e < len(text):
    textcode[e] = ord(textcode[e])
    textcode[e] = bin(textcode[e])
    e += 1

y = 0
decode = []
while y < len(text):
    decode.append(chr(int(textcode[y], 2) ^ int(keycode[y], 2))) #XOR of two lists to make final list
    y += 1
decode = ''.join(decode)

print(decode)

