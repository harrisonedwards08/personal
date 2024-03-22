def solution(numbers):
    
    finalarray = []
    i = 0
    for i in range (len(numbers)-2):
        
        a = numbers[i]
        b = numbers[i+1]
        c = numbers[i+2]
        
        
            
        if a < b > c or a> b < c:
            finalarray.append(1)
        else:
            finalarray.append(0)
        
        
    return finalarray



numb1 = [1,2,1]

numb2 = [1,2,3]

numb3 = [2,4,5,4]


print(solution(numb1))

print(solution(numb2))

print(solution(numb3))