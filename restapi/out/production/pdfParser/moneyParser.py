import pdfplumber
f = open("parsed.txt",'w')

with pdfplumber.open(r'money.pdf') as pdf:
    for pdf_page in pdf.pages:
        try:
            f.write(pdf_page.extract_text())
        except Exception as e:
            print(e)

f.close
