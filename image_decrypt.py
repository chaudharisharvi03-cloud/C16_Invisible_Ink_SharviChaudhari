from PIL import Image
im = Image.open("secret.png")
ima=im.convert("RGB")
pixels = list(ima.getdata())
all_bits = []
for p in pixels:
    all_bits.append(p[2] % 2)
message = ""
for i in range(0, len(all_bits), 8):
    byte_bits = all_bits[i:i+8]
    if len(byte_bits) < 8: 
        break
    char_code = int("".join(map(str, byte_bits)), 2)
    if char_code == 255: 
        break
    if 32 <= char_code <= 126:
        message += chr(char_code)
    if len(message) > 10:
        break
print("Extracted text:", message)