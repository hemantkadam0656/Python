import time

def vowelstr(str):
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    res = [i for i in str for j in vowels if i == j]
    res.reverse()
    strlist = [char for char in str]
    idx = 0
    for i in range(len(str)):
        for j in vowels:
            if str[i] == j:
                strlist[i] = res[idx]
                idx +=1
    result = ''.join(strlist)
    
    return result
    


    print(str)
    print(result)
    
    print(strlist)



start = time.perf_counter()
vowelstr("Aa")
End = time.perf_counter()
print(End - start)
