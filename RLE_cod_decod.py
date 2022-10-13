


f = open('my_txt_1.txt', 'r')
def rle_encode(f):
    encoding = ''
    prev_char = ''
    count = 1
    if not f: return ''
    for char in f:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding
decoding = open('my_txt_2', 'w')        
def rle_decode(decoding): 
    decode = '' 
    count = '' 
    for char in decoding: 
        if char.isdigit(): 
            count += char 
        else:  
            decode += char * int(count) 
            count = '' 
    return decode

encoded_val = rle_encode(f) 
print(encoded_val)
   
decoded_val = rle_decode(decoding) 
print(decoded_val)

 
      
