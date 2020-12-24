from openpyxl import Workbook
wb = Workbook() #새 워크북 생성
ws = wb.active #현재 활성화된 시트 가져오기
ws.title = "Nadosheet" 
wb.save("sample.xlsx")