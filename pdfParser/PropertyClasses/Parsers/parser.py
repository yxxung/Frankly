import pandas as pd
import tabula

# 특정파일 CSV 변환

file = './data/money3.pdf'
df = tabula.read_pdf(file, pages='all')
tabula.convert_into(file, "money3.csv", output_format="csv", pages="all")

# 전체파일 Csv 변환
# tabula.convert_into_by_batch("./data/", lattice=True, output_format="csv", pages='all')


