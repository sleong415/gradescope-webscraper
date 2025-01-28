import csv
from bs4 import BeautifulSoup
from pprint import pprint
import numpy as np
import os


def parseExcludedTAs(file):
    excludedTAs = []

    with open(file, "r") as file:
        for line in file:
            name = line.strip()
            excludedTAs.append(name)

    print("excluded TAs:", excludedTAs)
    return excludedTAs

def countSubmissions(file):
    # Process submissions
    with open(file) as infile:
        soup = BeautifulSoup(infile, "html.parser")

    rows = [row for row in soup.find_all("tr")]
    # tas = {name: {count: 0, points: 0}}
    tas = {} 
    for row in rows:
        items = [item.text for item in row.find_all("td")]
        if len(items) > 2 and items[2]:
            name = items[2]
            points = items[4]
            tas[name] = tas.get(name, {"count": 0, "points": 0.0})
            tas[name]["count"] += 1

            if len(points) == 0:
                points = 0

            tas[name]["points"] += float(points)
    
    excludedTAs = parseExcludedTAs("./excludedTAs.txt")
    for ta in excludedTAs:
        if ta in tas:
            del tas[ta]

    return tas

def calculateStats(submissionDict):
     # tas = {name: {percent: 0}}
    tas = {}
    totalList = []
    for name in submissionDict:
        numGraded = submissionDict[name]["count"]
        points = submissionDict[name]["points"]

        average = round(points / numGraded, 4)
        tas[name] = {"avg_points": average}
        totalList.append(average)
    
    arr = np.array(totalList)
    mean = round(arr.mean(), 4)
    stdev = round(np.std(arr), 4)
    return tas, mean, stdev

def writeToCSV(tas, mean, stdev, newFile):
    taList = []

    for name in tas:
        formattedName = formatName(name)
        avg_points = tas[name]["avg_points"]
        taList.append([formattedName, avg_points])
    taList.sort()

    with open(newFile, "w", newline='') as fout:
        writer = csv.writer(fout)
        writer.writerows(taList)

def formatName(name):
    if "," in name:
        parts = name.split(",")
        name = f"{parts[1]} {parts[0]}".strip()
    return name

def main(semester, homework):
    submissionDict = countSubmissions(os.path.join(semester, (homework + ".html")))
    tas, mean, stDev = calculateStats(submissionDict)
    writeToCSV(tas, mean, stDev, "output.csv")
    print("mean:", mean)
    print("st dev:", stDev)
    
if __name__ == "__main__":
    main("spring2025", "hw1")
    
    
   