from openpyxl import Workbook
wb = Workbook() #새 워크북 생성
ws = wb.create_sheet() #새로운시트 기본 이름으로 생성
ws.title = "Nadosheet" 
wb.save("sample.xlsx")