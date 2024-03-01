import csv
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import numpy as np
import os


def countSubmissions(campusFile, onlineFile):
    # Process campus/hybrid submissions
    with open(campusFile) as infile:
        soup = BeautifulSoup(infile, "html.parser")

    rows = [row for row in soup.find_all("tr")]
    # tas = {name: {count: 0, section: "O"}}
    tas = {} 
    for row in rows:
        items = [item.text for item in row.find_all("td")]
        if len(items) > 2 and items[2]:
            name = items[2]
            tas[name] = tas.get(name, {"count": 0, "section": "C"})
            tas[name]["count"] += 1
    
    # Process online submissions
    with open(onlineFile) as infile:
        soup = BeautifulSoup(infile, "html.parser")

    rows = [row for row in soup.find_all("tr")]
    for row in rows:
        items = [item.text for item in row.find_all("td")]
        if len(items) > 2 and items[2]:
            name = items[2]
            tas[name] = tas.get(name, {"count": 0, "section": "O"})
            tas[name]["count"] += 1
    return tas

def countEfficiencies(campusFile, onlineFile):
    # Process campus/hybrid submissions
    with open(campusFile) as infile:
        soup = BeautifulSoup(infile, "html.parser")

    rows = [row for row in soup.find_all("tr")]
    # tas = {name: {count: 0, section: "O"}}
    tas = {} 
    for row in rows:
        items = [item.text for item in row.find_all("td")]
        if len(items) > 3 and items[3]:
            name = items[3]
            tas[name] = tas.get(name, {"count": 0, "section": "C"})
            tas[name]["count"] += 1
    
    # Process online submissions
    with open(onlineFile) as infile:
        soup = BeautifulSoup(infile, "html.parser")

    rows = [row for row in soup.find_all("tr")]
    for row in rows:
        items = [item.text for item in row.find_all("td")]
        if len(items) > 3 and items[3]:
            name = items[3]
            tas[name] = tas.get(name, {"count": 0, "section": "O"})
            tas[name]["count"] += 1
    return tas

def calculateStats(submissionDict, efficiencyDict):
     # tas = {name: {percent: 0, section: "O"}}
    tas = {}
    totalList = []
    for name in submissionDict:
        numGraded = submissionDict[name]["count"]
        if name in efficiencyDict.keys():
            numEfficient = efficiencyDict[name]["count"]
        else:
            numEfficient = 0
        percent = round(numEfficient / numGraded, 4)
        section = submissionDict[name]["section"]
        tas[name] = {"percent": percent, "section": section}
        totalList.append(percent)
    
    arr = np.array(totalList)
    mean = round(arr.mean(), 4)
    stdev = round(np.std(totalList), 4)
    return tas, mean, stdev

def writeToCSV(tas, mean, stdev, newFile):
    campusList = []
    onlineList = []

    for name in tas:
        formattedName = formatName(name)
        percent = tas[name]["percent"]
        if tas[name]["section"] == "C":
            campusList.append([formattedName, percent])
        else:
            onlineList.append([formattedName, percent])
    campusList.sort()

    with open(newFile, "w") as fout:
        writer = csv.writer(fout)
        writer.writerows(campusList)
        writer.writerow([])
        writer.writerows(onlineList)

def formatName(name):
    if "," in name:
        parts = name.split(",")
        name = f"{parts[1]} {parts[0]}".strip()
    return name

def main(semester, homework):
    submissionDict = countSubmissions(os.path.join(semester, homework, "campusSubmissions.html"),
                                      os.path.join(semester, homework, "onlineSubmissions.html"))
    efficiencyDict = countEfficiencies(os.path.join(semester, homework, "campusEfficiency.html"),
                                      os.path.join(semester, homework, "onlineEfficiency.html"))
    tas, mean, stDev = calculateStats(submissionDict, efficiencyDict)
    writeToCSV(tas, mean, stDev, "output.csv")

    
if __name__ == "__main__":
    main("spring2024", "hw5")
    
    
   