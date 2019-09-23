# csv2xml.py
# Convert all CSV files in a given (using command line argument) folder to XML.
# FB - 20120523
# First row of the csv files must be the header!

# example CSV file: myData.csv
# id,code name,value
# 36,abc,7.6
# 40,def,3.6
# 9,ghi,6.3
# 76,def,99

import sys
import os
import csv
xmlFile = 'myData.xml'
csvFile = 'myData.csv'
csvData = csv.reader(open(csvFile))
xmlData = open(xmlFile, 'w')
xmlData.write('<?xml version="1.0" encoding="UTF-8"?>' + "\n")
xmlData.write('<testcases>' + "\n")
# there must be only one top-level tag
rowNum = 0
for row in csvData:
    if rowNum == 0:
        tags = row
        # replace spaces w/ underscores in tag names
        for i in range(len(tags)):
            tags[i] = tags[i].replace(' ', '_')
    else: 
        xmlData.write('<testcase '+tags[0]+'="'+row[0] +'">'+ "\n")
        tag_length = len(tags)
        for i in range (tag_length-1):
            if(tags[i+1]=='actions'):
                xmlData.write('<steps>' + "\n")
                xmlData.write('<step>' + "\n")
                xmlData.write('<step_number>1</step_number>' + "\n")
                xmlData.write('<' + tags[i+1] + '>' + row[i+1] + '</' + tags[i+1] + '>' + "\n")
            elif(tags[i+1]=='expectedresults'):
                xmlData.write('<' + tags[i+1] + '>' + row[i+1] + '</' + tags[i+1] + '>' + "\n")
                xmlData.write('</step>' + "\n")
                xmlData.write('</steps>' + "\n")
            else:
                xmlData.write('<' + tags[i+1] + '>' + row[i+1] + '</' + tags[i+1] + '>' + "\n")

        xmlData.write('</testcase>' + "\n")                
    rowNum +=1
xmlData.write('</testcases>' + "\n")
xmlData.close()