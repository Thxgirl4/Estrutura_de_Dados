# Two Pointer - Tecnica para ser usada em Strings
# Reverse words

class Solution:
    def reverseWords(selfself, s):
        res = ''
        l, r = 0, 0
        while r < len(s): # enquanto r for menor q o array
            if s[r] !=' ': # se for algo diferente q um espaço em branco
                r += 1 # ++1
            else:
                res += s[l:r + 1][::-1] #
                r += 1
                l = r
        res +=' '
        res += s[l:r + 2][::-1]
        return res[1:]
