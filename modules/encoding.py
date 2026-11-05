def text_to_binary(message):
    binary_data = ''.join(
        format(byte, '08b')
        for byte in message.encode('utf-8')
    )

    return [int(bit) for bit in binary_data]


def binary_to_text(bits):
    binary_string = ''.join(str(bit) for bit in bits)

    # Only complete 8-bit groups can form bytes
    complete_length = (len(binary_string) // 8) * 8
    binary_string = binary_string[:complete_length]

    byte_array = bytearray()

    for i in range(0, len(binary_string), 8):
        byte_value = int(binary_string[i:i + 8], 2)
        byte_array.append(byte_value)

    return byte_array.decode('utf-8', errors='replace')