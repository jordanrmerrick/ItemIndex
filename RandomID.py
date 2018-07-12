import random
import pandas
import xlrd
import xlwt

workbook = xlrd.open_workbook('ItemIndex.xlsx')
worksheet = workbook.sheet_by_name('NameIDType')

firstcharacter = worksheet.cell(1,1).value
firstone = firstcharacter[:1]

input = worksheet.cell(1,0).value
output = ""
for i in input.upper().split():
    output += i[0]
firsttwo = output[:2]

randomnumber = (random.randint(0,500) + random.randint(0,500) + random.randint(0,500))

print(firstone + firsttwo + str(randomnumber)) # This will be replaced with a way to export this to Excel

#There needs to be a way to check if the ID is identical to any other ID in the system

df = pandas.DataFrame({'UID': ['CNC1239', 'SADJ2102', 'SADJ319']})
writer = pandas.ExcelWriter('ItemIndex.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='NameIDType')
writer.save()