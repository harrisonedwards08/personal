#Euler4

def isPalindrome(number):

    #reverse string

    variable1 = str(number)

    variable2 = variable1[::-1]

    #return palindrome or no
    if variable2 == variable1:
        
        return 1
        
    else:
        
        return 2


# control = 0
# while control == 0:
    
#     input1 = input("gimme numb: \n")
#     if input1 == "end":
#         break
#     else:
#         isPalindrome(input1)


dig1 = 100
dig2 = 100
palinput = 0
output2 = []

while dig1 < 1000:


    dig2 = 10
    while dig2 < 1000:

        palinput = dig1 * dig2

        print(f"palinput {palinput}, dig1 {dig1}, dig2 {dig2}")

        output1 = isPalindrome(palinput)
        if output1 == 1:
            output2.append(palinput)


        

        dig2 += 1
    dig1 += 1

print (output2)

output2.sort()
print (output2[-1])

