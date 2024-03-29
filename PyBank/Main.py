import os
import csv
import sys

'''Find the File Path of Budget_data.csv'''
filepath = os.path.join('Resources', 'budget_data.csv')

'''Declare all variables and assign their values'''
Sum = 0
i = 0
Difference = 0
last = 867884
Increase = 0
Increase_Data = ""
Decrease_Data = ""
Decrease = 0
Total_Difference = 0
Difference_Percentage = 0

'''Red csv file: Budget_data.csv'''
with open(filepath, newline='') as Budget:
    Budget_Reader = csv.reader(Budget, delimiter=',')
    Budget_Header = next(Budget_Reader)
    '''Put into dictionary when find New Budget name'''
    '''Calculate total, times, and difference each loop'''
    for row in Budget_Reader:
        Sum = Sum + int(row[1])
        Difference = int(row[1]) - last
        Total_Difference += Difference
        if Difference > Increase:
            Increase = Difference
            Increase_Data = str(row[0])
        if Difference < Decrease:
            Decrease = Difference
            Decrease_Data = str(row[0])
        i = i + 1
        last = int(row[1])
Difference_Percentage = round((Total_Difference / (i-1)), 2)

'''write output to both text files and terminal'''
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

'''print output to terminal'''
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {i}")
print(f"Total: ${Sum}")
print(f"Average  Change: ${Difference_Percentage}")
print(f"Greatest Decrease in Profits: {Increase_Data} ({Increase})")
print(f"Greatest Increase in Profits: {Decrease_Data} ({Decrease})")




