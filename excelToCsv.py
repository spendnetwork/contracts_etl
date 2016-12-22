import xlrd
import csv
import pandas

src = 'C:\\Users\\Kiere\\Desktop\\Work Experience\\ContractsRegisters\\Central Government\\Central Government Contract Registers\\DepartmentforTransport.xls'
dst = 'C:\\Users\\Kiere\\Desktop\\Work Experience\\ContractsRegisters\\Central Government\\csvFiles\\DepartmentforTransport1.csv'
# src = "/home/sim/SpendNetwork/contracts/ContractsRegisters/Central Government/Central Government Contract Registers/DepartmentforTransport.xls"
# dst = "/home/sim/SpendNetwork/contracts/ContractsRegisters/Central Government/Central Government Contract Registers/DepartmentforTransport.csv"


with xlrd.open_workbook(src) as wb:
    sh = wb.sheet_by_name('Business Unit')
    with open(dst, 'wb') as f:
        c = csv.writer(f)
        for r in range(sh.nrows):
            c.writerow(sh.row_values(r))
        for r in range (sh.ncols):
            c.writecol(sh.col_values(r))


