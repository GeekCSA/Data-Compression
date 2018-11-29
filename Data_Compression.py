import math
import numpy as np


def find_self_dangling_suffix(S, T, same):
    s = set()

    if same == 1:
        if len(T) != set(T).__len__():
            s.add("2")  # 2 as epsilon
        S = T = set(T)

    for current in S:
        for word in T:
            if word.find(current) == 0 and current != word:
                index_finish_prefix = word.find(current) + len(current)
                dangling_suffix = word[index_finish_prefix:]
                if dangling_suffix == "":
                    s.add('2')
                s.add(dangling_suffix)
    return s

class CodeWords:
    def __init__(self, C, P):
        self.C = np.array(C)
        self.lenC = np.array([len(c) for c in C])
        self.P = np.array(P)

        if len(C) != len(P):
            raise Exception("size(C) != size(P)")
        if  sum(P) != 1:
            raise Exception("sum of p in P != 1")

    def E_C_P(self):
        return np.sum(self.lenC * self.P)

    def isUDCode(self):

        isUD = True

        dangling_set = find_self_dangling_suffix(self.C, self.C, 1)
        C_set = set(self.C)
        notOriginal = C_set | dangling_set
        dangling_size = len(dangling_set)

        while isUD == True:

            for c in dangling_set:
                if c in C_set:
                    isUD = False
                    break

            if "2" in dangling_set:
                isUD = False
                break

            dangling_set = find_self_dangling_suffix(notOriginal, notOriginal, 1)

            if dangling_size >= len(dangling_set):
                break

            notOriginal |= dangling_set

        return isUD

    def kraft(self):
        k = np.array([1/pow(2, lnc) for lnc in self.lenC])
        return np.sum(k)

    def entropy(self):
        logs = np.log(self.P)
        return -np.sum(self.P * logs)

    def isPrefixFree(self):
        for i in range(len(self.C)):
            for j in range(len(self.C)):
                word1 = self.C[i]
                word2 = self.C[j]

                if i != j and  word1.find(word2) == 0:
                    return False
        return True