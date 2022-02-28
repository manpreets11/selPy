import openpyxl



def readExcel_returnTuples(self):
        wb = openpyxl.load_workbook("../TestData/TestData.xlsx")
        sh = wb['LoginData']
        sheet_cells = []
        for rows in sh.iter_rows():
            row_cells = []
            for cell in rows:
                row_cells.append(cell.value)
            sheet_cells.append(tuple(row_cells))
        return sheet_cells


