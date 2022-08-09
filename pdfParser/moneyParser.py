import pdfplumber

f = open("parsed.txt",'w', encoding="UTF-8")


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
            str1 = ['|'.join(list(filter(None, line))) for line in table]
            str2 = [str.replace("\n","") for str in str1]
            str3 = '\n'.join(str2)
            f.write(str3+'\n')
            # f.write(str3)
        except Exception as e:
            print(e)

f.close
