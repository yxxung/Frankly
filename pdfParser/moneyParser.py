import pdfplumber
import os



table_settings = {
    "vertical_strategy" : "lines_strict",
    "horizontal_strategy" : "lines_strict",
    "keep_blank_chars": True,
    "text_tolerance": 1.5,
    "text_x_tolerance": 1.5
}

pdfDir = './moneyPDF'
fileList = os.listdir(pdfDir)

txtDir = './moneyTXT'

for fileName in fileList:
    txtName = txtDir+ "/" + fileName.replace(".pdf","") + ".txt"

    f = open(txtName,'w', encoding="UTF-16")
    with pdfplumber.open(pdfDir+"/"+fileName) as pdf:
        # page = pdf.pages[1]
        # im = page.to_image(resolution=150)
        # im.reset().debug_tablefinder(table_settings).save("./debug.PNG", format="PNG")
        for pdf_page in pdf.pages:
            try:
                table = pdf_page.extract_table(table_settings)
                str1 = ['|'.join(list(filter(None, line))) for line in table]
                str2 = [str.replace("\n"," ") for str in str1]
                str3 = '\n'.join(str2)
                f.write(str3+'\n')
                # f.write(str3)
            except Exception as e:
                print(e)

    f.close
