import csv
from collections import Counter

with open('height-weight.csv', newline='')as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)    
new_data=[]
for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(n_num)

n=len(new_data) 
data=Counter(new_data)
md={
    "75-115":0,
    "115-145":0,
    "145-175":0

}

for height,occurence in data.items():
    if 75<float(height)<115:
        md["75-115"]+=occurence
    elif 115<float(height)<145:
        md["115-145"]+=occurence
    elif 145<float(height)<175:
        md["145-175"]+=occurence
mode_range,mode_occurence=0,0
for range, occurence in md.items():
    if occurence>mode_occurence:     
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode=float((mode_range[0]+mode_range[1])/2)                                   
print(f"{mode:2f}")