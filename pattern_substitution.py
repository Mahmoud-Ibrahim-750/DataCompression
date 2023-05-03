# Pattern Substitution Algorithm

# This example involves the usage of one pattern
# which is not the best case, but for the
# educational purpose it does the trick
def ps_encode(sequence, patterns_list):
    result = sequence  # take a copy to work on it
    for data_tuple in patterns_list:  # for each data tuple in the list
        pattern, substitution = data_tuple  # get the pattern and its alternative
        result = result.replace(pattern, substitution)  # replace each occurrence
    return result  # finally, return the result sequence after all replacements


def ps_decode(compressed_sequence, patterns_list):
    result = compressed_sequence  # take a copy to work on it
    for data_tuple in patterns_list:
        pattern, substitution = data_tuple
        result = result.replace(substitution, pattern)  # replace substitutions with their patters again
    return result


if __name__ == '__main__':
    example_patterns = [('and', '&'), ('friends', '$f')]  # this is just an example
    original_text = "My friends and I went for a walk and had some fun and I enjoyed being with my friends"
    compressed_output = ps_encode(original_text, example_patterns)
    compression_ratio = ((len(compressed_output) / len(original_text)) * 100)
    uncompressed_output = ps_decode(compressed_output, example_patterns)

    print(f"original text: {original_text}")
    print(f"compressed output: {compressed_output}")
    print(f"decompression output: {uncompressed_output}")
    print(f"compression ratio: {round(compression_ratio, 2)}%")
