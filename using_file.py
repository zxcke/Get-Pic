#!/usr/bin/python
# Filename: using_file.py

poem = '''\
12345
Programming is fun
When the work is done
if you wanna make your work also fun:
use Python!




'''

f = file('poem.txt', 'w') # open for 'w'riting
f.write(poem) # write text to file
f.close() # close the file

f = file('poem.txt')
# if no mode is specified, 'r'ead mode is assumed by default
print '\n ###########print test############ \n'
nu = 1
while True:    
    line = f.readline()
    lenline = len(line) - 1
    if len(line) == 0: 
        break
    #print line,'This is the ', nu ,'line. It\'s ',lenline,'long \n'
    print nu,line
    nu = nu + 1
    # Notice comma to avoid automatic newline added by Python
f.close() # close the file
