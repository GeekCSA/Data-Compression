import Data_Compression as dc

def main():
    # The code-words
    C = ["11", "0"]
    P = [0.5, 0.5]

    new_code = dc.CodeWords(C, P)

    # print(new_code.E_C_P())
    # print(new_code.kraft())
    # print(new_code.entropy())
    # print(new_code.isPrefixFree())
    # print(new_code.isUDCode())

if __name__ == '__main__':
    main()