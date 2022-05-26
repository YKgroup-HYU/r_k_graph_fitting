from src import fitting_r_k
from src import alter_csv

# Lumerical data(텍스트)를 csv로 변환
# 변환할 텍스트 파일 이름 입력
name_list = ['50', '150', '250', '350', '450', '550']
# 0이면 텍스트 제목 삭제(한번만 실행) or 1
alter_csv.txt_drop(1, name_list)
# 0이면 변환 or 1
alter_csv.convert(1)
# 파일의 파라미터 입력
name_list = ['50', '150', '250', '350', '450', '550']
# through, cross 경로 입력

fitting_r_k.file_path_th = '.\data_processing\ex\*through_E*.csv'
fitting_r_k.file_path_cr = '.\data_processing\ex\*cross_E*.csv'

# 그래프 피팅
fitting_r_k.run(name_list, fitting_r_k.r_value_list, fitting_r_k.k_value_list)