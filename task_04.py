
def RLE_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''

    for i in data:
        if i != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = i
        else:
            count += 1

    else:
        encoding += str(count) + prev_char
        return encoding


encoded_val = RLE_encode('AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE')
print(encoded_val)


def RLE_decode(data):
    decode = ''
    count = ''
    for i in data:
        if i.isdigit():
            count += i
        else:
            decode += i * int(count)
            count = ''
    return decode


decoder_val = RLE_decode(encoded_val)
print(decoder_val)
