from math import inf
def romanToInt(s):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sumroman=0
        lastint=inf
        for x in s:
            if lastint<roman[x]:
                sumroman=sumroman-((lastint)*2)+roman[x]
                lastint=roman[x]
            else:
                lastint=roman[x]
                sumroman+=roman[x]
        return sumroman
def intToRoman(n):
        if n<=0:
            return ''
        data=[(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),
              (90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
        res=[]
        for v,sym in data:
            if n==0:
                break
            k=n//v
            if k:
                res.append(sym*k)
                n-=v*k
        return ''.join(res)
roman_tests = ["IV", "IX", "XLII", "XCIX", "MMXXIII"] 
print([(s,x) for x2 in roman_tests for s in [romanToInt(x2)]  for x in [intToRoman(s)] ])

