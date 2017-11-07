#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import re


def main():
    filepaths = sys.argv[1].split(',')
    dependencySet = set()
    print(filepaths)

    for filepath in filepaths:
        print('Processing filepath: {}'.format(filepath))
        if not os.path.isfile(filepath):
            print('File path {} does not exist. Exiting...'.format(filepath))
            continue

        with open(filepath) as fp:
            cnt = 0
            for line in fp:
                matchObj = re.match(r'(.*):(.*):(.*):(.*):(.*)', line,
                                    re.M)
                if matchObj:
                    groupId = matchObj.group(1).split()[-1]
                    artifactId = matchObj.group(2)
                    version = matchObj.group(4)

                    # dependency = "{}:{}:{}".format(groupId, artifactId, version)

                    dependency = '{} ({})'.format(artifactId, version)
                    dependencySet.add(dependency)
                else:
                    cnt += 1

    allFiledDependencySet = set()
    allDepsFilePath = sys.argv[2]
    print('Processing filepath: {}'.format(allDepsFilePath))

    with open(allDepsFilePath) as fp:
        for line in fp:
            allFiledDependencySet.add(line.strip())

   # dependencySet = sorted(dependencySet)
   # allFiledDependencySet = sorted(allFiledDependencySet)

#    for element in dependencySet:
#        print(element)

#    for element in allFiledDependencySet:
#        print(element)

    needsToBefiled = set()
    print('########### Difference is ############')
    needsToBefiled = dependencySet.difference(allFiledDependencySet)
    needsToBefiled = sorted(needsToBefiled)

    for element in needsToBefiled:
        print(element)


if __name__ == '__main__':
    main()

			