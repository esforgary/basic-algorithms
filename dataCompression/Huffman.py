import heapq
from collections import defaultdict

def huffman_encoding(data):
    freq = defaultdict(int)
    for char in data:
        freq[char] += 1

    heap = [[weight, [symbol, ""]] for symbol, weight in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        low = heapq.heappop(heap)
        high = heapq.heappop(heap)

        for pair in low[1:]:
            pair[1] = '0' + pair[1]
        for pair in high[1:]:
            pair[1] = '1' + pair[1]

        heapq.heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])

    huffman_code = dict(heapq.heappop(heap)[1:])
    encoded_data = "".join([huffman_code[char] for char in data])

    return encoded_data, huffman_code

def huffman_decoding(encoded_data, huffman_code):
    inv_huffman_code = {v: k for k, v in huffman_code.items()}

    decoded_data = ""
    i = 0
    while i < len(encoded_data):
        for j in range(i + 1, len(encoded_data) + 1):
            if encoded_data[i:j] in inv_huffman_code:
                decoded_data += inv_huffman_code[encoded_data[i:j]]
                i = j
                break

    return decoded_data

data = "hello world"
encoded_data, huffman_code = huffman_encoding(data)
print(encoded_data)

decoded_data = huffman_decoding(encoded_data, huffman_code)
print(decoded_data)
