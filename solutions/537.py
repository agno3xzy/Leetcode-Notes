class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a = self.getPart(a)
        b = self.getPart(b)
        complex1 = a[0]*b[0]+(-1)*b[1]*a[1]
        complex2 = a[0]*b[1]+a[1]*b[0]
        return str(complex1)+'+'+str(complex2)+'i'
    def getPart(self, str):
        if '+-' in str:
            str = str[:str.find('+-')]+'-'+str[str.find('+-')+2:]
        if '-' in str:
            minusIndex = str.rfind('-')
            if minusIndex != 0:
                return [int(str[:minusIndex]),int(str[minusIndex:len(str)-1])]
        str = str.split('+')
        if str[1] == 'i':
            str[1] = '1'
            return [int(str[0]),int(str[1])]
        stri = str[1]
        stri = stri[:len(stri)-1]
        return [int(str[0]), int(stri)]


if __name__ == '__main__':
    s = Solution()
    print(s.complexNumberMultiply("-2+-2i", "3-4i"))


'''
2+i
2-i
-2+i
-2+i

-2-6i
'''
