CRC_16 = '11000000000000101'
GENERATOR_POLYNOMIAL = CRC_16


def remove_insignificant_bits(m: str) -> str:
    if len(m) < 2:
        return m

    while len(m) > 0 and m[0] != '1':
        m = m[1:]
    return m


def xor(s: str, t: str) -> str:
    s = int(s, base=2)
    t = int(t, base=2)
    result = bin(s ^ t)

    return result[2:]  # remove 0b


def crc(m: str, polynomial: str, is_checking=False):
    p_degree = len(polynomial)

    if not is_checking:
        for _ in range(p_degree - 1):
            m = m + '0'

    bits_to_divide = ''
    bits_to_divide += m[:p_degree]
    bits_to_divide = remove_insignificant_bits(bits_to_divide)
    m = m[p_degree:]

    while len(m) > 0:
        while len(bits_to_divide) < p_degree and len(m) > 0:
            bits_to_divide += m[0]
            bits_to_divide = remove_insignificant_bits(bits_to_divide)
            m = m[1:]

        if len(bits_to_divide) == p_degree:
            bits_to_divide = xor(bits_to_divide, polynomial)

    while len(bits_to_divide) < p_degree:
        bits_to_divide = '0' + bits_to_divide

    rest = bits_to_divide
    return rest


def sender(message, polynomial):
    p_degree = len(polynomial) - 1
    rest = crc(message, polynomial)

    return message + rest[-p_degree:]


def receiver(message, polynomial):
    rest = crc(message, polynomial, True)
    return rest


if __name__ == '__main__':
    print(sender('011101010011101001110010110101100010', GENERATOR_POLYNOMIAL))
