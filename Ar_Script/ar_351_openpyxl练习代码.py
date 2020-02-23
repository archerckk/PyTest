import openpyxl

wb=openpyxl.load_workbook('testData_冷启动_tinder.csv')
ws=wb.active()
for row in ws.rows:

    print(row)

