import random
import pandas
import xlrd

book = xlrd.open_workbook('ItemIndex.xlsx')
worksheet = book.sheet_by_name('ItemName')

fcharacters = worksheet.cell(1,1).value
fone = fcharacters[:1]

npart = worksheet.cell(0,1).value
nlimit = npart[:2]

rnumber = (random.randint(0,500) + random.randint(0,500) + random.randint(0,500))

print(fone + nlimit + str(rnumber))


#This is the check to find how many cells are filled. It is reliant on the specific column (0) being used
def CheckCells():
    workbook = xlrd.open_workbook('ItemIndex.xlsx')
    sheet = workbook.sheet_by_name('ItemName')
    colvalues = sheet.col_values(0)

    for i in colvalues:
        if i != '':
            print('Item Found')
        else:
            break


CheckCells()