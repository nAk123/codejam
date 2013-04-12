# Process the string so that a code is generated for string assignment
def process(code, str1, str2):

    for s1,s2 in zip(str1,str2):
        if s1.isalpha():
            #print s1,s2
            x = ord(s1) - ord('a')
            #print x
            if x>0:
                code = code[:x] + s2 + code[(x+1):]
    return code

def readfile(code):

    f = open('A-small-practice.in', 'r+')
    f.seek(0)
    f2 = open('Output.txt','w')
    f2.seek(0)
    count = 0
    for line in f:
        lingo = ""
        #print line
        if count > 0:
            for l in line:
                if l.isalpha():
                    x = ord(l) - ord('a')
                    #print x
                    lingo = lingo + code[x]
                else:
                    lingo = lingo + " "
            print "Case #%d:"%count + " " + lingo
            f2.write("Case #%d:"%count + " " + lingo + "\n")
        count += 1

if __name__ == "__main__":

    code = "y_______________z________q"
    #code = code[:(ord('z')-ord('a'))] + 'q' + code[(ord('z')-ord('a')+1):]
    #code = code[:(ord('o')-ord('a'))] + 'e' + code[(ord('o')-ord('a')+1):]
    #code = code[:(ord('a')-ord('a'))] + 'y' + code[(ord('a')-ord('a')+1):]
    #print code
    #process(source, target)
    code = process(code,"ejp mysljylc kd kxveddknmc re jsicpdrysi","our language is impossible to understand")
    #print code
    code = process(code, "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","there are twenty six factorial possibilities")
    #print code
    code = process(code, "de kr kd eoya kw aej tysr re ujdr lkgc jv","so it is okay if you want to just give up")
    #print code
    #print len(code)
    readfile(code)
