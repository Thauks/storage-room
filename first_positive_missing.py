def solution(A):
    positive = [n for n in A if n > 0]
    positive.sort()
    
    # setting the min on 1 as required
    min = 1
    #looping until we find the gap
    for n in positive:
        if(min < n):break # min found
        else:
            min=n+1
    
    return min