import pdfplumber
f = open("parsed.txt",'w')


table_settings = {
    "vertical_strategy" : "lines_strict",
    "horizontal_strategy" : "lines_strict"
}


with pdfplumber.open(r'./money2.pdf') as pdf:
    # page = pdf.pages[1]
    # im = page.to_image(resolution=150)
    # im.reset().debug_tablefinder(table_settings).save("./debug.PNG", format="PNG")
    for pdf_page in pdf.pages:
        try:
            table = pdf_page.extract_table(table_settings)
            # str = ','.join(table)
            print(str)

        except Exception as e:
            print(e)

f.close
