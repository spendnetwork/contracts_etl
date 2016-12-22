import xlrd
import csv
import pandas

with xlrd.open_workbook('C:\\Users\\Kiere\\Desktop\\Work Experience\\ContractsRegisters\\Central Government\\Central Government Contract Registers\\DepartmentforTransport.xls') as wb:
	sh = wb.sheet_by_name('Business Unit')
	with open('C:\\Users\\Kiere\\Desktop\\Work Experience\\ContractsRegisters\\Central Government\\csvFiles\\DepartmentforTransport1.csv', 'wb') as f:
		c = csv.writer(f)
		for r in range(sh.nrows):
			c.writerow(sh.row_values(r))
		for r in range (sh.ncols):	
			c.writecol(sh.col_values(r))
			
			


			



			
			

			

			
			

			
