import pdfplumber




table_settings = {
    "vertical_strategy" : "lines_strict",
    "horizontal_strategy" : "lines_strict"
}


f = open("parsed.txt",'w', encoding="UTF-8")


with pdfplumber.open(r'money/국회공보 제2022-31호(정기재산변동신고).pdf') as pdf:
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
