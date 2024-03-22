class Solution(object):
    def romanToInt(s):
        output = 0
        trans = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
  
        prev = 10000000
        for i in range (len(s)):
            
            transint = (trans[s[i]])
            if transint > prev:
                output -= prev
                output = output + (transint - prev)
                print(f"whacked out. output:{output}, transint:{transint}, prev: {prev}")
                continue

            output += transint
            print (f'output is {output}')
            prev = transint
        print(f"final output is {output}")




    romanToInt('MCMXCIV')