import os
import csv
import sys

filepath = os.path.join('Resources', 'election_data.csv')
i = 0
count = 0
value = 0
Max_Number = 0
Winner = ""
New_Dic = {}

with open(filepath, newline='') as Election:
    Election_Reader = csv.reader(Election, delimiter=',')
    Budget_Header = next(Election_Reader)
    for row in Election_Reader:
        if not row[2] in New_Dic:
            New_Dic.update({row[2]: 0})
        if row[2] in New_Dic:
            value = int(New_Dic[row[2]]) + 1
            New_Dic.update({row[2]: value})
        count += 1

for key in New_Dic:
    if New_Dic[key] > Max_Number:
        Max_Number = New_Dic[key]
        Winner = key
class Tee(object):
    def __init__(self, *files):
        self.files = files
    def write(self, obj):
        for f in self.files:
            f.write(obj)
            f.flush()
    def flush(self) :
        for f in self.files:
            f.flush()

f = open('out.txt', 'w')
original = sys.stdout
sys.stdout = Tee(sys.stdout, f)

print("Election Results")
print("-------------------------")
print(F"Total Votes: {count}")
print("-------------------------")
for key in New_Dic:
    print(f"{key}: {round(New_Dic[key]*100/count, 3)}00%  ({New_Dic[key]})")
print("-------------------------")
print(f"Winner: {Winner}")
print("-------------------------")


