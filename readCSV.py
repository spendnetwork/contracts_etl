import csv


with open('NorthSummersetContractsRegister.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter='/')
    for row in readCSV:
        print(row)
        print(row[0])
        

        

        


	
