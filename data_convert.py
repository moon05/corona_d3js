import csv
import pandas as pd

fields = ["Distname", "Division", "Geometry", "Shape Area", "Shape Leng",\
            "district_name", "Dist_code", "total_quarantine"]

df = pd.read_csv("./csv_data/bd_covid.csv", skipinitialspace=True, usecols=fields)

divisions = {"Khulna":0, "Chittagong":0, "Barisal": 0, "Sylhet": 0, \
            "Rangpur": 0, "Dhaka": 0, "Rajshahi": 0, "Mymensingh": 0}

districts = {}

def summary_divisions():
    for index, row in df.iterrows():
        if row["Division"] == "Khulna":
            divisions["Khulna"] += row["total_quarantine"]
        elif row["Division"] == "Mymensingh":
            divisions["Dhaka"] += row["total_quarantine"]    
        elif row["Division"] == "Chittagong":
            divisions["Chittagong"] += row["total_quarantine"]
        elif row["Division"] == "Barisal":
            divisions["Barisal"] += row["total_quarantine"]
        elif row["Division"] == "Sylhet":
            divisions["Sylhet"] += row["total_quarantine"]
        elif row["Division"] == "Rangpur":
            divisions["Rangpur"] += row["total_quarantine"]
        elif row["Division"] == "Dhaka":
            divisions["Dhaka"] += row["total_quarantine"]
        elif row["Division"] == "Rajshahi":
            divisions["Rajshahi"] += row["total_quarantine"]


def summary_districts():
    dist_names = list(set(df.Distname))
    t_dict = {key: 0 for key in dist_names}
    for index, row in df.iterrows():
        print (row["Distname"], row["total_quarantine"])
        t_dict[row["Distname"]] += row["total_quarantine"]
    global districts
    districts = t_dict
    


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

print (sum(districts.values()))

write_tsv_file("district_numbers")
