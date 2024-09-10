import openpyxl
def read_excel(filename,row,col):
    workbook1 = openpyxl.load_workbook(filename)
    sheet = workbook1.active
    cell = sheet.cell(row=row, column=col)
    print(cell.value)
read_excel('read_data.xlsx',row=4,col=1)
