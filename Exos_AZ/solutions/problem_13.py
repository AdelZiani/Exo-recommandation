
def a(listname):
    length = len(listname)
    tmp = []
    for i in range(0,length-1):
        maximum = max(listname[i],listname[i+1])
        tmp.append(maximum)
    return tmp  

def max_in_list(abc):
    if len(abc) == 1:
        return abc[0]
    else:
        return max_in_list(a(abc))

ab = [3,7,98,34,12,14]
print(max_in_list(ab))
    


######################################################
###################### shortcut ######################
######################################################

def maximum(list_var):
    list_var.sort()
    return list_var[-1]
print(maximum(ab))
