import mammoth
import openpyxl


def docx2html(docx_file):
    custom_styles = """ b => b.mark
                        u => u.initialism
                        p[style-name='Heading 1'] => h1.card
                        table => table.table.table-hover
                        """


    bootstrap_css = '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">'
    bootstrap_js = '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>'


    with open(docx_file, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file, style_map = custom_styles)
        html = result.value 

    return bootstrap_css + html + bootstrap_js


def preprocess_excel_table(excel_file): 
    wb = openpyxl.load_workbook(excel_file)

    worksheet = wb.worksheets[0]

    excel_data = list()
    for row in worksheet.iter_rows():
        row_data = list()
        for cell in row:
            row_data.append(str(cell.value))
        excel_data.append(row_data)
    
    return excel_data, worksheet