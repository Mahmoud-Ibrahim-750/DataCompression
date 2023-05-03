# Huffman Algorithm Implementation with console logs
# This implementation with the logs it provides is perfect if
# you want to understand how the algorithm works, while the
# other one at file [huffman.py] without "log" at the end
# is a clean implementation the just works without logging
# what happens behind the scenes
from queue import PriorityQueue
import time


class HuffmanNode:
    def __init__(self, char, freq, timestamp):
        self.char = char
        self.freq = freq
        self.timestamp = timestamp
        self.left = None  # left node
        self.right = None  # right node

    # less than operator
    def __lt__(self, other):
        # if two nodes have the same frequency, then the one with the smallest timestamp should be smaller
        if self.freq == other.freq:
            return self.timestamp > other.timestamp
        else:
            return self.freq < other.freq


# calculate how many times each character appears in the data
def get_frequency_dict(data):
    freq_dict = {}
    for char in data:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict


# print the tree (represented in a priority queue) at a particular time
# this function is only required to keep track of the built tree and has
# nothing to do with the result actually
def print_queue(queue, freq_dict):
    print("queue at the moment has:")
    temp_queue = PriorityQueue()
    while not queue.empty():
        node = queue.get()
        print(f"char: {node.char} freq: {freq_dict[node.char]}")
        temp_queue.put(node)

    while not temp_queue.empty():
        queue.put(temp_queue.get())

    if queue.qsize() == 1:
        node = queue.get()
        print(f"Character: {node.char}, Frequency: {freq_dict[node.char]}")
        queue.put(node)


# construct a tree starting from the frequency table generated at the beginning
# till the tree is fully build
def build_huffman_tree(freq_dict):
    pq = PriorityQueue()

    # add all characters to a tree
    current_time = time.time()
    for char, freq in freq_dict.items():
        node = HuffmanNode(char, freq, current_time)
        pq.put(node)
        current_time = time.time()

    # take two nodes with the lowest frequency and add them to the tree
    print("build the tree:")
    while pq.qsize() > 1:
        print_queue(pq, freq_dict)
        print()

        last_node = pq.get()
        pre_last_node = pq.get()
        print(f"last two nodes {last_node.char, last_node.freq}, {pre_last_node.char, pre_last_node.freq}")
        print()

        merged_node = HuffmanNode(pre_last_node.char + last_node.char, last_node.freq + pre_last_node.freq, time.time())
        merged_node.left = pre_last_node
        merged_node.right = last_node
        pq.put(merged_node)

        freq_dict[merged_node.char] = merged_node.freq

    print()

    # get the last node which is the root of the tree
    root = pq.get()
    return root


# traverse the tree nodes extracting the generated character codes
def traverse_tree(node, code_dict, code=""):
    # base condition: calling on a leaf node then calling on the left and right (None) stops
    if node is None:
        return

    # add/update the code of this character
    if node.char is not None:
        code_dict[node.char] = code

    # recursively call the function on the left and right child nodes
    traverse_tree(node.left, code_dict, code + "0")
    traverse_tree(node.right, code_dict, code + "1")


# using the mechanisms introduced above, encode the data
def huffman_encoding(data):
    freq_dict = get_frequency_dict(data)
    print(f"the frequency map: {freq_dict}")
    print()

    if len(freq_dict) == 1:
        code_dict = {list(freq_dict.keys())[0]: "0"}
    else:
        root = build_huffman_tree(freq_dict)
        print("tree built successfully")
        print(f"the last node char: {root.char} freq: {root.freq}")
        print()

        code_dict = {}
        traverse_tree(root, code_dict)

    # Filter the code dictionary to only include keys from the provided data
    code_dict = {key: char for key, char in code_dict.items() if key in data}

    print(code_dict)
    print()

    # for each character in the provided data, retrieve its corresponding
    # code and concatenate it to a string forming the compressed data
    encoded_data = "".join([code_dict[char] for char in data])

    return encoded_data, code_dict


# decode the encoded data again
def huffman_decoding(data, code_dict):
    # swap characters with their codes
    reversed_dict = {code: char for char, code in code_dict.items()}

    decoded_data = ""
    current_code = ""
    # for each bit in the encoded data, add the bit to the current code
    for bit in data:
        current_code += bit
        # then search for the current code in the codes map
        # if found, add the character associated with the code
        # to the decoded string and reset the code to begin
        # searching for another code
        if current_code in reversed_dict:
            char = reversed_dict[current_code]
            decoded_data += char
            current_code = ""

    return decoded_data


# this function provides the binary equivalent to the data that a typical computer system would generate
def binary_encode(text):
    code_dict = {}
    binary_text = ""
    for char in text:
        # use the built-in ord function to get the ASCII code for each character and then converts the ASCII code
        # to binary using the built-in bin function. The bin function returns a string representing the binary
        # value, with a prefix of '0b'. This prefix is removed by slicing the string starting from the 2nd character.
        # The resulting binary string is then zero-padded to 8 digits using the zfill() method to ensure that each
        # character is encoded in a consistent 8-bit format.
        binary_char = bin(ord(char))[2:].zfill(8)
        binary_text += binary_char
        # construct code map
        if char not in code_dict:
            code_dict[char] = binary_char

    return binary_text, code_dict


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    original_text = "aaaaaaaaaaaaaaabbbbbbbccccccddddddeeeee"
    uncompressed_output, fixed_length_codes = binary_encode(original_text)
    compressed_output, variable_length_codes = huffman_encoding(original_text)
    compression_ratio = ((len(compressed_output) / len(uncompressed_output)) * 100)

    print(f"original text: {original_text}")
    print(f"uncompressed binary representation: {uncompressed_output}")
    print(f"fixed-length codes used: {fixed_length_codes}")
    print(f"compressed binary representation: {compressed_output}")
    print(f"variable-length codes used: {variable_length_codes}")
    print(f"compression ratio: {round(compression_ratio, 2)}%")
