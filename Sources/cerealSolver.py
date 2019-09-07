#import modueles
#import os
import csv

#open the csv
#cerealCSV=os.path.join("..","cereal.csv")
cerealCSV="../cereal.csv"

with open(cerealCSV,"r", encoding="UTF-8") as file:
    #create my csv.reader
    csvreader=csv.reader(file,delimiter=",")
    csvheader=next(csvreader)
    print(f"The header is:{csvheader}")

    #iterate rows (for loop)
    for row in csvreader:   
        #if statement (if the cereal contains 5 more grams of fiber, print)
        if float(row[7])>=5:
            print(row)


#print row if condition meets
