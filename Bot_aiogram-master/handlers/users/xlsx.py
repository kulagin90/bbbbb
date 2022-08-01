import xlsxwriter
from parser import poisk


def writer(parametr):
    book = xlsxwriter.Workbook(r'auto.xlsx')
    page = book.add_worksheet('автомобили')

    row = 0
    column = 0

    page.set_column('A:A', 50)
    page.set_column('B:B', 50)
    #page.set_column('C:C', 20)
    #page.set_column('D:D', 50)
    #page.set_column('E:E', 50)
    #page.set_column('F:F', 50)

    for item in parametr():
        page.write(row, column, item[0])
        page.write(row, column + 1, item[1])
        #page.write(row, column + 2, item[2])
        #page.write(row, column + 3, item[3])
        #page.write(row, column + 4, item[4])
        #page.write(row, column + 5, item[5])
        row += 1

    book.close()


writer(poisk)
