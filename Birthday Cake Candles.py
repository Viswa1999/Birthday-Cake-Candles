def birthdayCakeCandles(candles):
    # Write your code here
    candles.sort()
    candles.reverse()
    n=len(candles)
    count=0
    for i in range(0,n):
        if(candles[0]==candles[i]):
            count+=1
        
    return count