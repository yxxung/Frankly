import pandas as pd
import tabula

# 특정파일 CSV 변환
#
# file = './data/제367회(임) 본회의 출결현황.pdf'
# df = tabula.read_pdf(file, pages='all')
# tabula.convert_into(file, "367output.csv", output_format="csv", pages="all")

# 전체파일 Csv 변환
tabula.convert_into_by_batch("./data/", lattice=True, output_format="csv", pages='all')
