# Repetitive Sequence Suppression Algorithm
import re  # regular expression

# This algorithm has a significant draw back which is for a data with no repetitions
# it produces compressed data larger than the original data and this is shown in
# the functions ending with "primitive" word. However, we can just approach differently
# to solve such a problem and this is shown in the functions with the same name as
# the last two but without the "primitive" keyword.

# I put a test case to show the difference, check it out!


def suppress_repetitive_sequence(sequence):
    result = ""  # Initialize an empty string to store the suppressed sequence
    count = 1  # Initialize a counter to keep track of the length of the current repetitive sequence
    for i in range(1, len(sequence)):
        # If the current element is equal to the previous element, increase the counter
        if sequence[i] == sequence[i - 1]:
            count += 1
        else:  # If the current element is not equal to the previous element
            if count >= 2:  # If the length of the current sequence is greater than 1
                # mark the occurrence of the repeated element along with the count
                result += "".join(f"r{sequence[i - 1]}{count}")
            else:  # If the length of the current repetitive sequence is NOT greater than 1
                # just append the character to the result string
                result += "".join(sequence[i - count:i])
            count = 1  # Reset the counter for the next sequence

    # the last character or sequence (as no character next to the last one)
    if count >= 2:  # If the length of the current sequence is greater than 1
        # mark the occurrence of the repeated element along with the count
        result += "".join(f"r{sequence[-1]}{count}")
    else:  # If the length of the current repetitive sequence is NOT greater than 1
        # just append the character to the result string
        result += "".join(sequence[len(sequence) - count:])

    return result  # Return the resulting sequence


def decompress_sequence(compressed_sequence):
    result = ""  # Initialize an empty string to store the decompressed sequence
    # Use regular expression to find all occurrences of the compressed repetitive sequences
    # this returns a list of tuples of characters and their occurrence times
    matches = re.findall(r'r(\w)(\d+)', compressed_sequence)
    start_index = 0
    for match in matches:
        char, count = match  # get character and count from tuple
        # find where this character relies on in the sequence
        index = compressed_sequence.find(f"r{char}{count}", start_index)
        # Append any characters before the current repetitive sequence to the result
        result += compressed_sequence[start_index:index]
        # Append the sequence repeated to the result
        result += char * int(count)
        # move the start index next to the repeated sequence flag
        start_index = index + len(f"r{char}{count}")
    # Append any remaining characters after the last repetitive sequence to the result
    result += compressed_sequence[start_index:]
    return result


def suppress_repetitive_sequence_primitive(sequence):
    result = ""  # Initialize an empty string to store the suppressed sequence
    count = 1  # Initialize a counter to keep track of the length of the current repetitive sequence
    for i in range(1, len(sequence)):
        # If the current element is equal to the previous element, increase the counter
        if sequence[i] == sequence[i - 1]:
            count += 1
        else:  # If the current element is not equal to the previous element
            # mark the occurrence of the repeated element along with the count
            result += "".join(f"r{sequence[i - 1]}{count}")
            count = 1  # Reset the counter for the next sequence

    # the last character or sequence (as no character next to the last one)
    # mark the occurrence of the repeated element along with the count
    result += "".join(f"r{sequence[-1]}{count}")

    return result  # Return the resulting sequence


def decompress_sequence_primitive(compressed_sequence):
    result = ""  # Initialize an empty string to store the decompressed sequence
    # Use regular expression to find all occurrences of the compressed repetitive sequences
    # this returns a list of tuples of characters and their occurrence times
    matches = re.findall(r'r(\w)(\d+)', compressed_sequence)
    start_index = 0
    for match in matches:
        char, count = match  # get character and count from tuple
        # find where this character relies on in the sequence
        index = compressed_sequence.find(f"r{char}{count}", start_index)
        # Append any characters before the current repetitive sequence to the result
        result += compressed_sequence[start_index:index]
        # Append the sequence repeated to the result
        result += char * int(count)
        # move the start index next to the repeated sequence flag
        start_index = index + len(f"r{char}{count}")
    # Append any remaining characters after the last repetitive sequence to the result
    result += compressed_sequence[start_index:]
    return result


if __name__ == '__main__':
    # The two test cases show the great difference between the two approaches
    # the primitive approach gives 3 times more data when data has no repeated characters
    # while the enhanced one gives the same data where nothing can be done actually
    # for the second case with a lot of repeated characters the primitive approach
    # can deliver 45.45% compression ratio while the enhanced delivers 39.39%

    # if you checked the outputs carefully you will notice that the primitive approach
    # insists on encoding each and every character while the enhanced one only encodes
    # the repeated ones meaning that it only encodes when it's necessary

    # Test cases
    print("Test Case #1: No Repetition")
    no_repetition_text = "thisisatextwithnospaces"
    # primitive approach
    prim_compressed_output1 = suppress_repetitive_sequence_primitive(no_repetition_text)
    prim_compression_ratio1 = ((len(prim_compressed_output1) / len(no_repetition_text)) * 100)
    prim_decompressed_output1 = decompress_sequence_primitive(prim_compressed_output1)

    print("Primitive Approach")
    print(f"original text: {no_repetition_text}")
    print(f"compressed output: {prim_compressed_output1}")
    print(f"decompression output: {prim_decompressed_output1}")
    print(f"compression ratio: {round(prim_compression_ratio1, 2)}%")
    print()

    # enhanced approach
    compressed_output1 = suppress_repetitive_sequence(no_repetition_text)
    compression_ratio1 = ((len(compressed_output1) / len(no_repetition_text)) * 100)
    decompressed_output1 = decompress_sequence(compressed_output1)

    print("Enhanced Approach")
    print(f"original text: {no_repetition_text}")
    print(f"compressed output: {compressed_output1}")
    print(f"decompression output: {decompressed_output1}")
    print(f"compression ratio: {round(compression_ratio1, 2)}%")
    print()

    print("Test Case #2: Repetition")
    repetition_text = "aaaaaaaaaaaaaaabcccccccccdddddddddddddddeeeeeeefgghhhhhhhhhhiiiiii"
    # primitive approach
    prim_compressed_output2 = suppress_repetitive_sequence_primitive(repetition_text)
    prim_compression_ratio2 = ((len(prim_compressed_output2) / len(repetition_text)) * 100)
    prim_decompressed_output2 = decompress_sequence_primitive(prim_compressed_output2)

    print("Primitive Approach")
    print(f"original text: {repetition_text}")
    print(f"compressed output: {prim_compressed_output2}")
    print(f"decompression output: {prim_decompressed_output2}")
    print(f"compression ratio: {round(prim_compression_ratio2, 2)}%")
    print()

    # enhanced approach
    compressed_output2 = suppress_repetitive_sequence(repetition_text)
    compression_ratio2 = ((len(compressed_output2) / len(repetition_text)) * 100)
    uncompressed_output2 = decompress_sequence(compressed_output2)

    print("Enhanced Approach")
    print(f"original text: {repetition_text}")
    print(f"compressed output: {compressed_output2}")
    print(f"decompression output: {uncompressed_output2}")
    print(f"compression ratio: {round(compression_ratio2, 2)}%")
    print()
