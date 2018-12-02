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

The compression quality is measured according to the ![](https://latex.codecogs.com/gif.latex?%5Cfrac%7Bbits%7D%7Bcharacter%7D) ratio marked in [](https://latex.codecogs.com/gif.latex?E%28C%2CP%29%20%3D%20%5Csum_%7Bi%20%3D%200%7D%5E%7Bn%7D%20%5Cleft%28p_i*%7Cc_i%7C%5Cright%29) where $p_i$ is the probability that the word $i$ will appear in the text and $|c_i|$ is the length of the word The code representing the $i$ character. Encoding is best considered if $$E(C, P) = H(P) = -\sum_{i = 1}^{n}{p_i*log_2(p_i)}$$.

One of the known compression methods is Huffman Encoding, which always manages to construct a minimum encoding that always exists for this encoding that is equal to $H(P)$.

Dependencies:
* Python 3.6
* heapq
* numpy 1.15.4

List of files:
* Data_Compression.py - Contains a class named CodeWords that represents any encoding.
    This class has several methods that calculate all kinds of metrics on the code such as $E(C, P)$ and $H(P)$.

* Huffman_Encoding.py - Contains a class that encapsulates certain characters and their probabilities (appearing in text) calculates the Huffman code.
