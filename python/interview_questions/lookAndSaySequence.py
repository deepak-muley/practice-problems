
def generateLookAndSay(startChar, n):
    las = [str(startChar)]
    index = 0
    while index < n-1:
        currItem = las[index]
        nextItem = ''
        currCharCount = 1
        currChar = currItem[0]
        for c in currItem[1:]:
            if c != currChar:
                nextItem += str(currCharCount)+currChar
                currChar = c
                currCharCount = 1
            else:
                currCharCount += 1
        nextItem += str(currCharCount)+currChar
        las.append(nextItem)
        index += 1
    print "startChar=%s, total=%s, seq=%s" % (startChar, n, las)
    return las


def main():
    print generateLookAndSay(1, 2)
    print generateLookAndSay(1, 3)
    print generateLookAndSay(1, 5)
    print generateLookAndSay(1, 10)

if __name__ == "__main__":
    main()


