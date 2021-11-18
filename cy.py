#This is My Project!!!

def funnyValues(n,W,wt,val):
    if n == 0 or W == 0 :
        return 0
  
    if (wt[n-1] > W):
        return funnyValues(n-1, W, wt, val) 
    else:                               
        return max(val[n-1] + funnyValues(n-1,W-wt[n-1],wt,val),
                   funnyValues(n-1,W,wt,val))
  
#initializing in main
val = [60, 120, 100]
wt = [20, 30, 10]
W = 50
n = len(val)
print (funnyValues(n, W, wt, val))