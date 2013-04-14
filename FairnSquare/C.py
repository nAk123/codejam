def range(stop):
   i = 0
   while i < stop:
       yield i
       i += 1

def palcal(num):
    n = num
    rev = 0
    while num > 0:
        dig = num % 10
        rev = rev * 10 + dig
        num = num / 10
    if rev == n:
        return True
    else:
        return False

def sqrt(x):

    ans = 0
    while ans*ans < x:
        ans = ans + 1
    if ans*ans != x:
        return None
    else:
        return ans

def play(m, a, b):

    palindromes = [ x for x in m if palcal(x) ]
    root = [ sqrt(x) for x in palindromes ]
    fair = set ([ x for x in root if palcal(x) ])
    return len(fair)

if __name__ == "__main__":

    f = open('Output.txt','w')
    f.seek(0)
    with open('C-large-1.in') as sample:
        t = int(sample.readline())
        assert 1 <= t <= 10000
        for case in range(t):
            elements = sample.readline().strip('\n').split()
            N = int(elements[0])
            M = int(elements[1])
            assert 1 <= N <= 10 ** 14
            assert 1 <= M <= 10 ** 14
            matrix = [ N + x for x in range(M - N + 1)]
            l = play(matrix, N, M)
            f.write("Case #%d:"%(case+1) + " " + "%d\n"%l)
