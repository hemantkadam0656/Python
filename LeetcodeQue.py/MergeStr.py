def gcdivisor(str1, str2):
    min_str = min(str1, str2, key=len)
    max_str = max(str1, str2, key=len)
   
    res = []

    if len(str1) == len(str2):
        if str1 == str2: 
            res.append(str1[0])
            for idx in range(1, len(str1)):
                if str1[idx]== str1[0]:
                    break
                else:
                    res.append(str1[idx])            
        else:
            return ""
        result = ''.join(res)
        return result
   
    if len(min_str) != len(max_str): 
        res.append(max_str[0])
        for i in range(1,len(max_str)):           
            if i < len(min_str) and min_str[i] == max_str[i]:
                if max_str[i] == res[0]:
                    break
                else:
                   res.append(max_str[i])  
            else:
                break
        result = ''.join(res)

    n = len(result)
    substr = []
    substr1 = [] 

    for ele in range(0,len(max_str),n):        
        substr.append(max_str[ele:ele+n])
    
    for ele in range(0,len(min_str),n):
        substr1.append(min_str[ele:ele+n])
    
    count = 0 
    cnt = 0
    for value in substr:
        if value == result:
            count +=1
        
    for val in substr1:
        if val == result:
            cnt +=1

    if count == len(substr) and  cnt == len(substr1):
        return substr[-1]
    else:
        return f""   

gcd = gcdivisor("ABABABAB", "EFAB")
print(gcd)




