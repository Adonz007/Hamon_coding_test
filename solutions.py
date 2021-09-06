def customSort(n):
    length_of_n=len(n)
    for i in range(length_of_n-1,-1,-1):
        for j in range(0,i):
            if(n[j]>=n[j+1]):
                n[j],n[j+1]=n[j+1],n[j]
    return n


def biggest(n):
    if len(n)!=0:
        return customSort(n)[-1]
    return None

def biggest2(n):
    length_of_n=len(n)
    if length_of_n!=0:
        if length_of_n>2:
            return customSort(n)[-2:]
        return customSort(n)
    return None
def biggestn(n,m):
    length_of_n=len(n)
    if length_of_n!=0:
        if length_of_n>=m:
            return customSort(n)[-m:]
        return customSort(n)
    return None


print(biggestn([3,1,7,2,10,7,9],10))