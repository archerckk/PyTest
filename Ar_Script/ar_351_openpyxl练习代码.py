import openpyxl
from openpyxl.styles import Font,Alignment,numbers

# wb=openpyxl.load_workbook('test_data.xlsx')

wb=openpyxl.Workbook()
ws=wb.active
# ws_list=wb.sheetnames
# print(ws_list)
# ws=wb['数值说明']

title_list=['标题1','标题2','标题3']
value_list=[(1,2,3),(1,2,3),(23445,4.45454323,0.45435313)]

font_title=Font(size=13,bold=True)
alignment=Alignment(horizontal='center',vertical='center')


ws.append(title_list)

for row in ws.iter_rows():
    for i in row:
        i.font=font_title
        i.alignment=alignment

for i in value_list:
    ws.append(i)

for row in ws.iter_rows():
    for i in row:
        i.alignment=alignment
        i.number_format=numbers.FORMAT_GENERAL


wb.save('test_code.xlsx')