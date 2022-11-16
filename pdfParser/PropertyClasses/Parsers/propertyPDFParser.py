'''
@Author 최제현
@date 22/1/07

tokenize를 위해 구분자 변경
@date 22/08/01

pdf

'''


import pdfplumber
import os

class PropertyPDFParser:

    def propertyPDFParse(self, pdfDir, txtDir):
        table_settings = {
            "vertical_strategy" : "lines_strict",
            "horizontal_strategy" : "lines_strict",
            "keep_blank_chars": True,
            "text_tolerance": 1,
            "text_x_tolerance": 1
        }

        # pdfDir = 'D:\code\Frankly\pdfParser\PropertyClasses\moneyPDF'
        #
        # txtDir = 'D:\code\Frankly\pdfParser\PropertyClasses\moneyTXT'


        # pdfDir = 'E:\work\Frankly\pdfParser\PropertyClasses\Parsers\moneyPDF'

        # txtDir = 'E:\work\Frankly\pdfParser\PropertyClasses\Parsers\moneyTXT'

        # pdfDir = dir + '/moneyPDF'
        #
        # txtDir = dir + '/moneyTXT'


        fileList = os.listdir(pdfDir)



        for fileName in fileList:
            txtName = txtDir+ "/" + fileName.replace(".pdf","") + ".txt"

            f = open(txtName,'w', encoding="UTF-8")
            with pdfplumber.open(pdfDir+"/"+fileName) as pdf:

                # page = pdf.pages[1]
                # im = page.to_image(resolution=150)
                # im.reset().debug_tablefinder(table_settings).save("./debug.PNG", format="PNG")

                # PDF에서 테이블 추출
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
