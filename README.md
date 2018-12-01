introduction:
Data compression is a field in computer science that focuses on the various methods of compressing data (text files, audio, etc.).
 Data compression has many applications, such as:
* Save space
* Reduce IO operations
* Cryptography

Data compression is divided into two parts compression of data and decoding of compression.

The compression stage consists of three parts:

1. Modeling - learning about the information structure that needs to be compressed.
2. Statistical collection - on the information that needs to be compressed.
3. Encoding - the stage that performs the compression itself.

The decoding stage consists of the same three steps but in reverse order.

The compression quality is measured according to the bit / character ratio marked in ECP .... Encoding is best considered if ECP = H (P) = \ sum.


One of the known compression methods is Huffman Encoding, which always manages to construct a minimum encoding that always exists for this encoding that is equal to H (P).




Dependencies:
* Python 3.6
* heapq
* numpy 1.15.4

List of files:
Data_Compression.py - Contains a class named CodeWords that represents any encoding.
This class has several methods that calculate all kinds of metrics on the code such as ECP ... and H (P

Huffman_Encoding.py - Contains a class that encapsulates certain characters and their probabilities (appearing in text) calculates the Huffman code