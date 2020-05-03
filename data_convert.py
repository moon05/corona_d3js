import csv
import pandas as pd

fields = ["Distname", "Division", "Geometry", "Shape Area", "Shape Leng",\
            "district_name", "Dist_code", "total_quarantine"]

df = pd.read_csv("./bd_covid.csv", skipinitialspace=True, usecols=fields)

districts = {"Khulna":0, "Chittagong":0, "Barisal": 0, "Sylhet": 0, \
            "Rangpur": 0, "Dhaka": 0, "Rajshahi": 0}

def summary_districts():
    for index, row in df.iterrows():
        if row["Division"] == "Khulna":
            districts["Khulna"] += row["total_quarantine"]
        elif row["Division"] == "Chittagong":
            districts["Chittagong"] += row["total_quarantine"]
        elif row["Division"] == "Barisal":
            districts["Barisal"] += row["total_quarantine"]
        elif row["Division"] == "Sylhet":
            districts["Sylhet"] += row["total_quarantine"]
        elif row["Division"] == "Rangpur":
            districts["Rangpur"] += row["total_quarantine"]
        elif row["Division"] == "Dhaka":
            districts["Dhaka"] += row["total_quarantine"]
        elif row["Division"] == "Rajshahi":
            districts["Rajshahi"] += row["total_quarantine"]


def write_tsv_file(name):
    with open(name+".tsv", "w", newline="") as f_output:
        tsv_output = csv.writer(f_output, delimiter='\t')
        tsv_output.writerow(["district", "number"])
        for key, val in districts.items():
            tsv_output.writerow([key, val])

def write_csv_file(name):
    with open(name+".csv", "w", newline="") as f_output:
        tsv_output = csv.writer(f_output, delimiter=',')
        tsv_output.writerow(["district", "number"])
        for key, val in districts.items():
            tsv_output.writerow([key, val])




summary_districts()

print (districts)
print (sum(districts.values()))

write_tsv_file("district_numbers")
