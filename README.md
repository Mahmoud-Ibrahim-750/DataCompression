# DataCompression
Data Compression is a Python package that provides implementations of several popular compression algorithms, including Huffman coding, Run-length encoding and Repetitive sequence suppression algorithm. These algorithms can be used to reduce the size of data files without losing any information.

## Installation

To install Data Compression, simply clone this repository to your desktop. It's recommended to use PyCharm IDE.


## Usage

I provided all examples that shows how can these implementations be used and I hope the examples are enough. However, I may have missed something so feel free to contribute to this repository if you want to improve it somehow.

## Contributing

I would love to have some contributions, So if you would like to contribute to Image Dithering, please follow these steps:

1. Fork the repository
2. Create a new branch
3. Make your changes and commit them
4. Push to the branch
5. Create a new pull request

## Examples

Here is an example, the output of the `repetitive_sequence_suppression.py` file is provided:
```
Test Case #1: No Repetition
Primitive Approach
original text: thisisatextwithnospaces
compressed output: rt1rh1ri1rs1ri1rs1ra1rt1re1rx1rt1rw1ri1rt1rh1rn1ro1rs1rp1ra1rc1re1rs1
decompression output: thisisatextwithnospaces
compression ratio: 300.0%

Enhanced Approach
original text: thisisatextwithnospaces
compressed output: thisisatextwithnospaces
decompression output: thisisatextwithnospaces
compression ratio: 100.0%

Test Case #2: Repetition
Primitive Approach
original text: aaaaaaaaaaaaaaabcccccccccdddddddddddddddeeeeeeefgghhhhhhhhhhiiiiii
compressed output: ra15rb1rc9rd15re7rf1rg2rh10ri6
decompression output: aaaaaaaaaaaaaaabcccccccccdddddddddddddddeeeeeeefgghhhhhhhhhhiiiiii
compression ratio: 45.45%

Enhanced Approach
original text: aaaaaaaaaaaaaaabcccccccccdddddddddddddddeeeeeeefgghhhhhhhhhhiiiiii
compressed output: ra15brc9rd15re7frg2rh10ri6
decompression output: aaaaaaaaaaaaaaabcccccccccdddddddddddddddeeeeeeefgghhhhhhhhhhiiiiii
compression ratio: 39.39%


Process finished with exit code 0

```
The two test cases show the great difference between the two approaches of the repetitive sequence suppression algorithm. The primitive approach gives three times more data when data has no repeated characters, while the enhanced one gives the same data where nothing can be done actually. For the second case with a lot of repeated characters, the primitive approach can deliver a 45.45% compression ratio, while the enhanced delivers 39.39%.

If you checked the outputs carefully, you will notice that the primitive approach insists on encoding each and every character, while the enhanced one only encodes the repeated ones, meaning that it only encodes when it's necessary.

## Contact
If you have any questions or comments, please feel free to contact the project owner, Mahmoud Ibrahim, at futuredream31@gmail.com.

Feel free to modify the content to fit your preferences and style.

## License
This code is licensed under the MIT License. See the LICENSE file for details. 
