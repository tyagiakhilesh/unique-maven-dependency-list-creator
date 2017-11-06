import sys  
import os
import re

def main():  
   filepath = sys.argv[1]
   mavenDependecyListRegex = '(.*):(.*):(.*):(.*):(.*)'

   if not os.path.isfile(filepath):
       print("File path {} does not exist. Exiting...".format(filepath))
       sys.exit()

   with open(filepath) as fp:
       cnt = 0
       for line in fp:
           print("line {} contents {}".format(cnt, line))
           matchObj = re.match(r'(.*):(.*):(.*):(.*):(.*)', line, re.M)
           if matchObj: 
               print("matchObj.group(1) : {}".format(matchObj.group(1))) 
               print("matchObj.group(2) : {}".format(matchObj.group(2)))
               print("matchObj.group(3) : {}".format(matchObj.group(3)))
               print("matchObj.group(4) : {}".format(matchObj.group(4)))
               print("matchObj.group(5) : {}".format(matchObj.group(5)))
           else:
               print("No match!!")
               cnt += 1

if __name__ == '__main__':  
   main()
