import csv
import json

csv_file = "./csv_data/bd_covid.csv"
json_file = "./bd_covid.json"

items = []


with open(csv_file) as csvFile:
    csvReader = csv.DictReader(csvFile)
    
    for rows in csvReader:
        print (rows)
        data = {}
        dist, qNum = rows["\ufeffDistname"], rows["total_quarantine"]
        data["district"], data["cases"] = dist, qNum
        items.append(data)
finalData = {"cases": "cases", "district": "district", "items": items}

with open(json_file, "w") as jsonFile:
    jsonFile.write(json.dumps(finalData, indent=4))