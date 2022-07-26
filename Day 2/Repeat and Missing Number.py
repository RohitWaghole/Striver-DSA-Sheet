# T.C. -> O(N)
# S.C. -> O(N)

def missingAndRepeating(arr, n):
    l = [0]*n
    for i in arr:
        l[i-1]+=1
    missing, repeat = -1,-1
    for i in range(len(l)):
        if l[i]==0:
            missing = i+1
        if l[i]>=2:
            repeat = i+1
    return [missing, repeat]
  
 ############################################################

# T.C. -> O(N)
# S.C. -> O(1)

def missingAndRepeating(arr, n):
    
    s = n*(n+1)//2
    sq = n*(n+1)*(2*n+1)//6
    s -= sum(arr)
    for i in arr:
        sq -= i**2
    
    missing = (s+sq//s)//2
    repeating = missing - s
    return [missing, repeating]
  
############################################################

# T.C. -> O(N)
# S.C. -> O(1)

def missingAndRepeating(arr, n):
    
    x = 0
    for i in arr:
        x^=i
    for i in range(1,n+1):
        x^=i
    set_bit_no = x & ~(x-1)
    a,b = 0,0
    for i in range(n):
        if arr[i]&set_bit_no:
            a^=arr[i]
        else:
            b^=arr[i]
    for i in range(1,n+1):
        if i&set_bit_no:
            a^=i
        else:
            b^=i
    c = 0
    for i in arr:
        if a==i:
            c+=1
    if c==0:
        return [a,b]
    return [b,a]
