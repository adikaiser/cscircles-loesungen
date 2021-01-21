needle = input()  
haystack = input() 
counter = 0  
for a in range(0, len(haystack) - 1):
    if haystack[a:len(needle) + a] == needle:
        counter += 1  
print(counter)