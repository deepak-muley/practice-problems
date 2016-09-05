import sys
def getMaxSumSubArray(arr):
    currSum = 0
    maxSum = -sys.maxint
    subArr = []
    maxSumSubArr = []
    for currIndex in range(len(arr)):
        if currSum <= 0:
            currSum = arr[currIndex]
            subArr = [currSum]
        else:
            currSum += arr[currIndex]
            subArr.append(arr[currIndex])

        if maxSum < currSum:
            maxSum = currSum
            maxSumSubArr = subArr[:]

    return maxSum, maxSumSubArr

def main():
    arr = [-1, -2, 3, 4, -1]
    print getMaxSumSubArray(arr)

    arr = [-5, -2, -3, -4, -1]
    print getMaxSumSubArray(arr)

    arr = [5, 2, 3, 4, 1]
    print getMaxSumSubArray(arr)

if __name__ == "__main__":
    main()


