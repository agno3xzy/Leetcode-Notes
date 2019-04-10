import operator

class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        numpattern = []
        patternlist = []
        anspatternnum = []
        anspatternlist = []
        anslist = []
        for i in range(len(pattern)):
            if  pattern[i] not in patternlist:
                patternlist.append(pattern[i])
                numpattern.append(patternlist.index(pattern[i]))
            else:
                numpattern.append(patternlist.index(pattern[i]))

        for ans in words:
            if len(ans) != len(pattern):
                pass
            else:
                anspatternnum = []
                anspatternlist = []
                for i in range(len(ans)):
                    if ans[i] not in anspatternlist:
                        anspatternlist.append(ans[i])
                        anspatternnum.append(anspatternlist.index(ans[i]))
                    else:
                        anspatternnum.append(anspatternlist.index(ans[i]))
                if operator.eq(numpattern,anspatternnum):
                    anslist.append(ans)
        return anslist
    def better_solution(self,words, pattern):
        def match(word):
            m1, m2 = {}, {}
            for w, p in zip(word, pattern):
                if w not in m1: m1[w] = p
                if p not in m2: m2[p] = w
                if (m1[w], m2[p]) != (p, w):
                    return False
            return True

        return filter(match, words)
    def better_solution2(self, words, pattern):
        def match(word):
            P = {}
            for x, y in zip(pattern, word):
                if P.setdefault(x, y) != y:
                    return False
            return len(set(P.values())) == len(P.values())

        return filter(match, words)


