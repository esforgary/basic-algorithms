def compress(uncompressed):
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256
    result = []
    w = ''
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            dictionary[wc] = next_code
            next_code += 1
            w = c
    if w:
        result.append(dictionary[w])
    return result


def decompress(compressed):
    dictionary = {i: chr(i) for i in range(256)}
    next_code = 256
    result = []
    w = chr(compressed.pop(0))
    result.append(w)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == next_code:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result.append(entry)
        dictionary[next_code] = w + entry[0]
        next_code += 1
        w = entry
    return ''.join(result)


uncompressed_data = 'TOBEORNOTTOBEORTOBEORNOT'
compressed_data = compress(uncompressed_data)
print(compressed_data)  # [84, 79, 66, 69, 79, 82, 78, 79, 84, 256, 258, 260, 265, 259, 261]
decompressed_data = decompress(compressed_data)
print(decompressed_data)  # TOBEORNOTTOBEORTOBEORNOT
