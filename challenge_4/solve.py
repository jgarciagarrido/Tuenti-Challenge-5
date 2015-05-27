import base64


def split_in_bytes(bit_sequence):
    return [bit_sequence[i:i+8] for i in range(0, len(bit_sequence), 8)]


def get_slice_of_bytes(bytes, n_bits):
    bytes_slice = bytes[:n_bits]
    return split_in_bytes(bytes_slice), bytes[n_bits:]


def split_recipe(recipe):
    reverse = False
    if recipe[-1] == 'R':
        reverse = True
        recipe = recipe[:-1]
    endian = recipe[-1]
    n_bits = int(recipe[:-1])
    return n_bits, endian, reverse


def cook_bytes(bytes, recipe):
    n_bits, endian, reverse = split_recipe(recipe)
    bytes_slice, bytes = get_slice_of_bytes(bytes, n_bits)
    if endian == 'L':
        bytes_slice = bytes_slice[::-1]
    bit_slice = "".join(bytes_slice)
    if reverse:
        bit_slice = bit_slice[::-1]
    return long(bit_slice, 2), bytes

if __name__ == "__main__":
    number_base64 = raw_input()
    number_decoded = base64.decodestring(number_base64)
    bytes = "".join(map(lambda x: '{0:08b}'.format(ord(x)), number_decoded))

    cases = int(input())
    for i in xrange(cases):
        recipe = raw_input()
        cpu_number, bytes = cook_bytes(bytes, recipe)
        print cpu_number
