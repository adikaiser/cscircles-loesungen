starting_time = input()   
D = int(input())   
H = int(starting_time[0:2]) 
M = int(starting_time[3:5]) 

if D + M > 59:  
    H = H + (D + M) // 60   
    M = (D + M) % 60  
    if len(str(M)) == 1:   
        M = '0' + str(M)   
    if H > 23:  
        H = H % 24
        if len(str(H)) == 1:  
           H = '0' + str(H)   
print(str(H) + ':' + str(M))