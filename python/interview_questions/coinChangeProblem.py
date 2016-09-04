import sys
def getMinCount(total, coins):
    counts = [0] * (total+1)
    coinsSolutions = [0] * (total+1)
    coinsUsed = []

    for i in range(total+1):
        count = sys.maxint
        for j in range(len(coins)):
            if i - coins[j] >= 0:
                if count > counts[i-coins[j]]:
                    coinsSolutions[i] = coins[j]
                count = min(count, counts[i-coins[j]])

        if count < sys.maxint:
            counts[i] = count + 1

    coinsUsed = getMinCoinDenominations(total, coinsSolutions)
    print "amt=%s, coins=%s, counts=%s, coinsSolutions=%s, minCount=%s coinsUsed=%s" % \
            (total, coins, counts, coinsSolutions, counts[total], coinsUsed)
    return counts[total], coinsUsed

def getMinCoinDenominations(total, coinsSolutions):
    coinsUsed = []
    nextIndex = total
    while coinsSolutions[nextIndex] > 0:
        coinsUsed.append(coinsSolutions[nextIndex])
        nextIndex = nextIndex - coinsSolutions[nextIndex]
    return coinsUsed

def main():
    coins = [1,3,9,10]

    for amt in [3, 1, 9, 15, 69]:
        count, coinsUsed = getMinCount(amt, coins)

if __name__ == "__main__":
    main()


