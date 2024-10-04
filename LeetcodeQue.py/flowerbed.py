import time

time.time()
def canPlaceFlowers(flowerbed, n): 
        res = [0] + flowerbed + [0]
        print(res)
        for i in range(1, len(res)- 1):
                print(i)
                if res[i-1] == 0 and res[i] == 0 and res[i+1] == 0:
                        res[i] = 1
                        n -= 1
                        print(res)
                        print(n)
        if n <= 0:
                return True
        else:
                return False
                

obj = canPlaceFlowers([0,0,1], 2)
print(obj)                        
        