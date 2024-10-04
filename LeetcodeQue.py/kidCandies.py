# Kids With the Greatest Number of Candies
import time


class Solution:
   
    def kidsWithCandies(self, candies, extraCandies):
        time.sleep(4)
        max_num = max(candies)
        total_candy = []
        result = []

        for candy in candies:
            tot = candy + extraCandies
            total_candy.append(tot)
        
        for num in total_candy:
            if max_num > num:
                result.append("False")
            else:
                result.append("True")

             
        return result

start = time.perf_counter()
obj = Solution()
print(obj.kidsWithCandies([4,2,1,1,2], 1))
end = time.perf_counter()
print(end - start)



             
