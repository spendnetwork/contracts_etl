# coding=utf-8
import pandas


src = 'C:\\Users\\Kiere\\Desktop\\Work Experience\\ContractsRegisters\\Central Government\\Central Government Contract Registers\\DepartmentforTransport.xls'
dst = 'C:\\Users\\Kiere\\Desktop\\Work Experience\\ContractsRegisters\\Central Government\\csvFiles\\DepartmentforTransport1.csv'
# src = "/home/sim/SpendNetwork/contracts/ContractsRegisters/Central Government/Central Government Contract Registers/DepartmentforTransport.xls"
# dst = "/home/sim/SpendNetwork/contracts/ContractsRegisters/Central Government/Central Government Contract Registers/DepartmentforTransport.csv"

pandas_dataframe = pandas.read_excel(src, sheetname='Business Unit')
print(pandas_dataframe)
pandas_dataframe.to_csv(dst)

