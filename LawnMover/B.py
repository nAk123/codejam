def flagger(x, flag):
    n = len(x)
    if flag != 0:
        if x[1:] == x[:-1]:
            flag = 1
            return flag
        else:
            flag = 0
            return flag
    else:
        flag = 0
        return flag

def evaluate(m, x, y):

    flag = 1
    for i in range(x):
        if (i != 0 and i != x-1):
            if i % 2 == 0:
                temp = []
                for j in range(1, y):
                    temp.append(m[i][j])
                flag = flagger(temp, flag)
            else:
                temp = []
                for j in range(y-1):
                    temp.append(m[i][j])
                flag = flagger(temp, flag)

    if flag != 1:
        for i in range(x):
            if (i != 0 and i != x-1):
                if i % 2 == 0:
                    temp = []
                    for j in range(y-1):
                        temp.append(m[i][j])
                    flag = flagger(temp, flag)
                else:
                    temp = []
                    for j in range(1, y):
                        temp.append(m[i][j])
                    flag = flagger(temp, flag)

    if flag != 1:
        for i in range(y):
            if (i != 0 and i != y-1):
                if i % 2 == 1:
                    temp = []
                    for j in range(x-1):
                        temp.append(m[j][i])
                    flag = flagger(temp, flag)
                else:
                    temp = []
                    for j in range(1, x):
                        temp.append(m[j][i])
                    flag = flagger(temp, flag)

    if flag != 1:
        for i in range(y):
            if (i !=0 and i != y-1):
                if i % 2 == 1:
                    temp = []
                    for j in range(1, x):
                        temp.append(m[j][i])
                    flag = flagger(temp, flag)
                else:
                    temp = []
                    for j in range(x-1):
                        temp.append(m[j][i])
                    flag = flagger(temp, flag)

    return flag

if __name__ == "__main__":

    f = open('Out.txt','w')
    f.seek(0)
    with open('B-small-attempt1.in') as sample:
        t = int(sample.readline())
        assert 1 <= t <= 100
        for case in range(t):
            elements = sample.readline().strip('\n').split()
            N = int(elements[0])
            M = int(elements[1])
            matrix = [0 for x in xrange(N)]
            assert 1 <= N <= 10
            assert 1 <= M <= 10
            for n in range(N):
                row = sample.readline().strip('\n').split()
                elems = map(int, row)
                assert all(1 <= elem <= 2 for elem in elems)
                matrix[n] = elems
            flag = evaluate(matrix, N, M)
            if flag == 1:
                f.write("Case #%d:"%(case+1) + " " + "YES\n")
            else:
                f.write("Case #%d:"%(case+1) + " " + "NO\n")
