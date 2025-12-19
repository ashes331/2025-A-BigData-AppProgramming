import pandas as pd
import glob
import os
import re

# 1. 파일 경로를 지정합니다. (사용자님이 알려주신 경로)
folder_path = r'C:\Users\SAMSUNG\OneDrive\바탕 화면\대학\대학 과제\2학년(2025)\2학기\빅데이터응용프로그래밍\기말\csv1'
all_files = glob.glob(os.path.join(folder_path, "*.csv"))

# 최종적으로 합쳐질 데이터프레임과 구분선을 담을 리스트
all_data_with_separators = []

print(f"🔎 지정된 폴더에서 총 {len(all_files)}개의 CSV 파일을 찾았습니다.")

# 2. 각 파일을 순서대로 읽고 구분선을 삽입합니다.
for file_name in all_files:
    base_file_name = os.path.basename(file_name)

    # 월 정보 추출 (예: '1월', '7월')
    match = re.search(r'(\d+)월', base_file_name)
    month_info = match.group(0) if match else 'Unknown Data'

    try:
        # 파일 로드: 세 번째 줄을 헤더(header=2)로, 첫 두 줄은 건너뛰기(skiprows=[0, 1])
        df = pd.read_csv(
            file_name,
            header=2,
            encoding='cp949',  # 윈도우 한글 파일 인코딩
            skiprows=[0, 1]
        )

        # 합쳐진 데이터 분석을 위해 '월' 컬럼을 추가 (구분선 행에는 빈 값으로 남겨둠)
        df['월'] = month_info

        # 🌟 3. 월별 구분선 (Separator Row) 생성 🌟
        cols = df.columns.tolist()  # 데이터프레임의 모든 컬럼 이름
        separator_text = f'--- {month_info} 데이터 시작 ({len(df)}행) ---'

        # 첫 번째 컬럼에만 구분 문구를 넣고 나머지는 빈 값으로 채웁니다.
        # 이렇게 해야 최종 CSV에서 구분선 행이 깔끔하게 보입니다.
        separator_data = {cols[0]: [separator_text],
                          **{col: [''] for col in cols[1:]}}

        df_separator = pd.DataFrame(separator_data, columns=cols)

        # 4. 구분선과 해당 월의 데이터를 리스트에 순서대로 추가
        all_data_with_separators.append(df_separator)
        all_data_with_separators.append(df)

        print(f"  ✅ 로드 및 구분선 삽입 성공: {base_file_name}")

    except Exception as e:
        # 인코딩 오류 발생 시 로그를 남기고 건너뜁니다.
        print(f"  ❌ 파일 로드 실패 ({base_file_name}): {e} -> 이 파일은 건너뜁니다.")

# 5. 구분선이 포함된 모든 데이터를 하나로 합칩니다.
if all_data_with_separators:
    combined_df = pd.concat(all_data_with_separators, axis=0, ignore_index=True)

    # 6. 최종 CSV 파일로 저장합니다.
    output_file_name = 'combined_with_visual_separation.csv'
    combined_df.to_csv(os.path.join(folder_path, output_file_name), index=False, encoding='utf-8-sig')

    print("\n-----------------------------------------------------")
    print(f"🎉 모든 파일이 **구분선과 함께** 합쳐져 '{output_file_name}'으로 저장되었습니다!")
    print(f"저장 위치: {folder_path}")
    print("-----------------------------------------------------")
else:
    print("⚠️ 합칠 수 있는 유효한 데이터 파일이 없습니다.")