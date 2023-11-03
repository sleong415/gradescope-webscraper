import requests
from bs4 import BeautifulSoup
from pprint import pprint
import numpy as np

def countSubmissions(filename):
    with open(filename) as infile:
        soup = BeautifulSoup(infile, "html.parser")

    rows = [row for row in soup.find_all("tr")]
    tas = {}
    for row in rows:
        items = [item.text for item in row.find_all("td")]
        if len(items) > 2 and items[2]:
            name = items[2]
            count = tas.get(name, 0)
            tas[name] = count + 1
        else:
            continue
    return tas

def countEfficiencies(filename):
    with open(filename) as infile:
        soup = BeautifulSoup(infile, "html.parser")
    rows = [row for row in soup.find_all("tr")]
    tas = {}
    for row in rows:
        items = [item.text for item in row.find_all("td")]
        if len(items) > 3 and items[3]:
            name = items[3]
            count = tas.get(name, 0)
            tas[name] = count + 1
        else:
            continue
    return tas

def calculateStats(submissionDict, efficiencyDict):
    tas = {}
    totalList = []
    for name in submissionDict:
        numGraded = submissionDict[name]
        numEfficient = efficiencyDict.get(name, 0)
        percent = round(numEfficient / numGraded, 4)
        tas[name] = percent
        totalList.append(percent)
    
    arr = np.array(totalList)
    mean = round(arr.mean(), 4)
    stdev = round(np.std(totalList), 4)
    return tas, mean, stdev

def writeToExcel(tas, mean, stdev):


    
if __name__ == "__main__":
    submissionDict = countSubmissions("submissions.html")
    efficiencyDict = countEfficiencies("efficiency.html")
    tas, mean, stdev = calculateStats(submissionDict, efficiencyDict)
    writeToExcel(tas, mean, stdev)
    
    
   