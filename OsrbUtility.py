import sys  
import os
import re

def main():  
   filepath = sys.argv[1]
   mavenDependecyListRegex = '(.*):(.*):(.*):(.*):(.*)'

   if not os.path.isfile(filepath):
       print("File path {} does not exist. Exiting...".format(filepath))
       sys.exit()

   dependencySet = set()

   with open(filepath) as fp:
       cnt = 0
       for line in fp:
           matchObj = re.match(r'(.*):(.*):(.*):(.*):(.*)', line, re.M)
           if matchObj:
               groupId = matchObj.group(1).split()[-1]
               artifactId = matchObj.group(2)
               version = matchObj.group(4)
               dependency = "{}:{}:{}".format(groupId, artifactId, version)
               dependencySet.add(dependency)
           else:
               cnt += 1

   dependencySet = sorted(dependencySet)
   print(dependencySet)

if __name__ == '__main__':  
   main()
