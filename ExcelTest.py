import pandas
import xlrd

workbook = xlrd.open_workbook('ItemIndex.xlsx')
worksheet = workbook.sheet_by_name('NameIDType')

print(worksheet.cell(1,0).value)
