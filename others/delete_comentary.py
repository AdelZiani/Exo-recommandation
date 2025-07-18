import sys
import os

args = sys.argv

if(len(args) < 4 ):
    print("Not enough arguments please put the PATH and the pattern for the files Name and the number of files")
    exit(1)

#PATH = args[1]

def delete_commentary(file):
    comment = False
    content = ""
    f = open(file, 'r')
    line = f.readline()
    longCommentary = False
    cache = ""
    while line != "":
        commentary = False
        for char in line:
            delete = False
            if char == '#':
                commentary = True
                tmp = False
            if char == '\"' or char =="\'":
                if len(cache) < 2:
                    cache += char
                    tmp = True
                else:
                    print(longCommentary)
                    longCommentary = not longCommentary
                    cache = ""
                    tmp = False
                    delete = True
            else:
                tmp = False
            if (not commentary) and (not longCommentary) and (not tmp) and (not delete):
                content += cache
                content +=char 
                cache = "" 
        line = f.readline()
    f.close()
    f = open(file, "w")
    f.write(content)
    f.close()



#for i in range(2, args[3]):
#    delete_commentary(PATH + args[2]+ str(i)+".py")

delete_commentary("comm.py")