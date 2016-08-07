ans = 0
for x in xrange(10):
    for y in xrange(10):
        for z in xrange(10):
            if x == y and y == z:
                continue
            currNum = x*100 + y*10 + z
            #print currNum
            sumNum = y*100 + y*10 + y 
            if sumNum == currNum * 3:
                ans = sumNum
                print "****", ans, " ", currNum
                break
if ans == 0:
    print "Not found"
