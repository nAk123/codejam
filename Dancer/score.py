def gentriplet(scores, s, p, n):
    temp = 0
    cutoff = 0
    for score in scores:
        rem = score%n
        quo = score/n
        if rem == 0:
            if quo >= p:
                triplet = (quo, quo, quo)
                cutoff += 1
            else:
                if (temp < s and quo+1>=p):
                    temp = temp + 1
                    triplet = (quo-1, quo, quo+1)
                    cutoff += 1
                else:
                    triplet = (quo, quo, quo)
        else:
            if (quo + 1) >= p:
                if rem == 1:
                    triplet = (quo, quo, quo+1)
                else:
                    triplet = (quo, quo+1, quo+1)
                cutoff += 1
            else:
                if (temp<s and rem == 2 and quo+2 >= p):
                    temp = temp + 1
                    triplet = (quo, quo, quo + 2)
                    cutoff += 1
                else:
                    if rem == 1:
                        triplet = (quo, quo, quo+1)
                    else:
                        triplet = (quo, quo+1, quo+1)
        #print triplet
    #print cutoff
    return cutoff

def evalfile():
    f = open('B-small-practice.in', 'r+')
    f.seek(0)
    count = 0
    f2 = open('Output.txt','w')
    f2.seek(0)
    for line in f:
        if count > 0:
            inlist = [int(x) for x in line.split()]
            n = inlist[0]
            s = inlist[1]
            p = inlist[2]
            scores = inlist[3:]
            qualified = gentriplet(scores, s, p, n)
            print "Case #%d:"%count + " " + "%d"%qualified + "\n"
            f2.write("Case #%d:"%count + " " + "%d"%qualified + "\n")
        count = count + 1

if __name__ == "__main__":
    evalfile()
