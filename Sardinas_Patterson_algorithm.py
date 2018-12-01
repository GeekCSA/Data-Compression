import Data_Compression as dc
from Huffman_Encoding import Huffman


def main():

    # C = ["11", "0"]
    # P = [0.5, 0.5]
    # new_code = dc.CodeWords(C, P)


    S = ['a', 'b', 'c', 'd', 'e', 'f']
    P = [0.11, 0.06, 0.04, 0.67, 0.07, 0.05]

    h = Huffman(S, P)
    print(h.C)
    print(h.P)
    print(h.E_C_P())
    print(h.kraft())
    print(h.entropy())
    print(h.isPrefixFree())
    print(h.isUDCode())



    # print(new_code.E_C_P())
    # print(new_code.kraft())
    # print(new_code.entropy())
    # print(new_code.isPrefixFree())
    # print(new_code.isUDCode())

if __name__ == '__main__':
    main()