# class Solution(object):
#     def maxProfit(prices):

#         difs = []        

#         for dif1 in prices:

#             for dif2 in prices:
                
#                 difs.append(dif1-dif2)

#                 print(f'dif1: {dif1}, dif2:{dif2}, difs entry: {dif1-dif2}')



class Solution2(object):
    def maxProfit(prices):

        difs = []        

        i = 0

        for i in range(len(prices)):

            j = i + 1

            while True:

                if j > len(prices)-1:
                    break

                else:
                    #print (f'price i: {prices[i]}, price j {prices[j]} ')

                    difs.append(prices[j] - prices[i])

                j += 1

            i +=1

        if max(difs) > 0:
            return max(difs)
        else:
            return 0








        

        

 

        


prices2 = [7,6,4,3,1]

prices = [7,1,5,3,6,4]
print(Solution2.maxProfit(prices2))