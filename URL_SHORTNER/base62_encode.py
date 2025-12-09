ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def encode_base62(num):
    if num == 0:
        return ALPHABET[0]
    base62 = []
    while num>0:
        num, rem = divmod(num, 62)
        base62.append(ALPHABET[rem])
    return "".join(reversed(base62))


print(encode_base62(10000))        