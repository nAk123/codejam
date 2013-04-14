# Process the string so that a code is generated for charecter assignment as per googlerese
def process(code, str1, str2):

    for s1,s2 in zip(str1,str2):
        if s1.isalpha():
            x = ord(s1) - ord('a')
            if x>0:
                code = code[:x] + s2 + code[(x+1):]
    return code

#Read the input file and write the translated sentences to an output file
def readfile(code):

    f = open('A-small-practice.in', 'r+')
    f.seek(0)
    f2 = open('Output.txt','w')
    f2.seek(0)
    count = 0
    for line in f:
        lingo = ""
        if count > 0:
            for l in line:
                if l.isalpha():
                    x = ord(l) - ord('a')
                    lingo = lingo + code[x]
                else:
                    lingo = lingo + " "
            print "Case #%d:"%count + " " + lingo
            f2.write("Case #%d:"%count + " " + lingo + "\n")
        count += 1

if __name__ == "__main__":

    code = "y_______________z________q"
    #process(source, target)
    code = process(code,"ejp mysljylc kd kxveddknmc re jsicpdrysi","our language is impossible to understand")
    code = process(code, "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","there are twenty six factorial possibilities")
    code = process(code, "de kr kd eoya kw aej tysr re ujdr lkgc jv","so it is okay if you want to just give up")
    readfile(code)
