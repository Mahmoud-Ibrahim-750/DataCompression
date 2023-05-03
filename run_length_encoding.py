# Run-Length Encoding Algorithm

def rl_encode(sequence):
    result = []  # Initialize an empty list to store encoded data
    count = 1  # Initialize a counter to keep track of the length of the current repetitive sequence
    for i in range(1, len(sequence)):
        # If the current element is equal to the previous element, increase the counter
        if sequence[i] == sequence[i - 1]:
            count += 1
        else:  # If the current element is not equal to the previous element
            if count >= 2:  # If the length of the current sequence is greater than 1
                # mark the occurrence of the repeated element along with the count
                result.append((sequence[i - 1], count))
            else:  # If the length of the current repetitive sequence is NOT greater than 1
                # just append the character to the result string
                result.append((sequence[i - count:i], 1))
            count = 1  # Reset the counter for the next sequence

    # the last character or sequence (as no character next to the last one)
    if count >= 2:  # If the length of the current sequence is greater than 1
        # mark the occurrence of the repeated element along with the count
        result.append((sequence[-1], count))
    else:  # If the length of the current repetitive sequence is NOT greater than 1
        # just append the character to the result string
        result.append((sequence[len(sequence) - count:], 1))

    return result  # Return the resulting sequence


def rl_decode(compressed_sequence):
    result = ""  # Initialize an empty string to store the decompressed sequence
    for data_tuple in compressed_sequence:
        char, count = data_tuple  # get character and repeat count
        result += char * count  # repeat the character
    return result


if __name__ == '__main__':
    original_text = "aaaaaaaaaaaaaaabbbbbbbccccccddddddeeeeefghiiiiii"
    compressed_output = rl_encode(original_text)
    compression_ratio = ((len(compressed_output) * 2 / len(original_text)) * 100)  # 2 for the char. and num.
    uncompressed_output = rl_decode(compressed_output)

    print(f"original text: {original_text}")
    print(f"compressed output: {compressed_output}")
    print(f"decompression output: {uncompressed_output}")
    print(f"compression ratio: {round(compression_ratio, 2)}%")
