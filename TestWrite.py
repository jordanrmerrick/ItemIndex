import pandas
from openpyxl import load_workbook

with pandas.ExcelWriter('ItemIndex.xlsx', engine='openpyxl') as writer:
    writer.book = load_workbook('ItemIndex.xlsx')
    data_filtered.to_excel(writer,"NameIDType", cols=['Diff1', 'Diff2'])