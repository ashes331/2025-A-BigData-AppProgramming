import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

# matplotlib에서 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# ----------------- 설정 부분 -----------------
PROGRAMS_FILE = 'TV_Programs.csv'
GENRE_FILE = 'TV_Genre.csv'
# 프로그램 파일의 월 정보 컬럼 인덱스 (0부터 시작)
PROGRAMS_MONTH_COL_IDX = 31
# 프로그램 파일의 총 시청 시간 컬럼 인덱스
PROGRAMS_DATA_COL_IDX = 3


# ----------------- 데이터 로드 및 전처리 함수 (Program CSV 전용 수정) -----------------

def load_and_clean_data(file_name):
    """CSV 파일을 로드하고, 파일별 특성에 맞게 데이터를 정리하는 함수."""
    file_path = os.path.join(os.getcwd(), file_name)
    print(f"\n[INFO] 파일 로드 시작: {file_name}")

    try:
        # 1. 파일별 로딩 방식 분기
        if file_name == PROGRAMS_FILE:
            # Programs 파일: 첫 2행은 모집단/헤더 정보이므로 건너뛰고 (skiprows=2), 세 번째 행을 헤더(header=0)로 사용
            df = pd.read_csv(file_path, encoding='utf-8-sig', skiprows=2, header=0)

            # Programs 파일의 경우, 월 컬럼 이름이 유일하므로 인덱스로 지정
            month_col_name = df.columns[PROGRAMS_MONTH_COL_IDX]
            data_col_name = df.columns[PROGRAMS_DATA_COL_IDX]

            # 카테고리 체크용 컬럼 이름 통일
            df.rename(columns={df.columns[2]: 'Category_3_Check'}, inplace=True)

        elif file_name == GENRE_FILE:
            # Genre 파일: 첫 3행이 헤더이므로 skip하지 않고, 구분선 행만 제거
            df = pd.read_csv(file_path, encoding='utf-8-sig')
            df = df[~df.iloc[:, 0].astype(str).str.startswith('---')].copy()

            # Genre 파일의 경우, 월 컬럼은 마지막 컬럼
            month_col_name = df.columns[-1]
            # Genre 파일의 총 시청 시간 컬럼 (Index 2)
            data_col_name = df.columns[2]

            # 카테고리 체크용 컬럼 이름 통일
            df.rename(columns={df.columns[1]: 'Category_3_Check'}, inplace=True)

        else:
            print(f"[ERROR] 알 수 없는 파일: {file_name}")
            return None

        # 2. '월' 컬럼 처리
        df = df.dropna(subset=[month_col_name]).copy()
        df['월'] = df[month_col_name].astype(str).str.strip()
        df['월_순서'] = df['월'].str.replace('월', '').str.strip()
        df['월_순서'] = pd.to_numeric(df['월_순서'], errors='coerce')
        df = df.dropna(subset=['월_순서']).copy()

        # 3. 데이터 값 처리 (변환 실패 시 0으로 처리)
        df['Data_Value'] = pd.to_numeric(df[data_col_name], errors='coerce').fillna(0)

        # 첫 번째 컬럼을 'Category_Name'으로 통일
        df.rename(columns={df.columns[0]: 'Category_Name'}, inplace=True)

        print(f"[INFO] 시각화 기준 컬럼: '{data_col_name}' 사용. 월 컬럼: '{month_col_name}' 사용. 데이터 총 행 수: {len(df)}")

        if df.empty:
            print("[ERROR] 데이터 처리 후 유효한 행이 남아있지 않아 시각화 불가.")
            return None

        return df[['Category_Name', 'Category_3_Check', '월', '월_순서', 'Data_Value']]

    except FileNotFoundError:
        print(f"[ERROR] 파일을 찾을 수 없습니다: {file_path}")
        return None
    except Exception as e:
        print(f"[ERROR] 파일 처리 중 오류 발생 ({file_name}): {e}")
        return None


# ----------------- 시각화 함수 (월별 추이: 소계/총합계만 사용) -----------------

def plot_monthly_trend(df, title):
    """
    월별 총 합계를 막대 그래프로 시각화하는 함수.
    '소계' 또는 '총합계'가 포함된 행만 사용합니다.
    """

    # 🌟 '소계' 또는 '총합계'가 포함된 행만 명확하게 필터링
    df_totals = df[
        (df['Category_Name'].astype(str).str.contains('총합계|소계', na=False, regex=True)) |
        (df['Category_3_Check'].astype(str).str.contains('소계|Total', na=False, regex=True))
        ].copy()

    if df_totals.empty:
        print(f"[WARN] '{title}' 데이터에서 '소계'/'총합계' 행을 찾을 수 없어 월별 추이를 그릴 수 없습니다.")
        return

        # 월별로 그룹화하여 합계를 구합니다.
    df_grouped = df_totals.groupby('월_순서')['Data_Value'].sum().reset_index()
    df_grouped = df_grouped.sort_values(by='월_순서')

    # 그래프 시각화 시작
    plt.figure(figsize=(10, 6))
    month_labels = [f"{int(m)}월" for m in df_grouped['월_순서']]

    plt.bar(month_labels, df_grouped['Data_Value'], color='#3498db')

    plt.title(f'월별 총 시청 시간 추이 (소계 기준) ({title})', fontsize=15)
    plt.xlabel('월', fontsize=12)
    plt.ylabel('총 시청 시간 (합계)', fontsize=12)

    # Y축에 콤마 포맷 적용
    formatter = plt.FuncFormatter(lambda x, pos: f'{x:,.0f}')
    plt.gca().yaxis.set_major_formatter(formatter)

    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


# ----------------- 시각화 함수 (상위 항목) -----------------

def plot_top_categories(df, title):
    """전체 기간 동안 상위 10개 항목을 파이 차트로 시각화하는 함수 (개별 항목만 필터링)"""

    # '소계'나 '총합계' 행은 제외하고 개별 항목만 필터링합니다.
    df_filtered = df[
        ~df['Category_Name'].astype(str).str.contains('총합계|소계|Total|nan', na=False, regex=True) &
        ~df['Category_3_Check'].astype(str).str.contains('소계|Total|nan', na=False, regex=True)
        ].copy()

    if df_filtered.empty:
        print(f"[WARN] '{title}' 데이터에서 개별 항목을 찾을 수 없어 상위 항목 비율을 그릴 수 없습니다.")
        return

    category_sum = df_filtered.groupby('Category_Name')['Data_Value'].sum().sort_values(ascending=False)

    top_n = 10
    top_categories = category_sum.head(top_n)

    other_sum = category_sum[top_n:].sum()
    if other_sum > 0:
        top_categories['기타'] = other_sum

    plt.figure(figsize=(12, 10))
    wedges, texts, autotexts = plt.pie(top_categories.values,
                                       labels=top_categories.index,
                                       autopct='%1.1f%%',
                                       startangle=90,
                                       wedgeprops={'edgecolor': 'white', 'linewidth': 1})

    plt.setp(autotexts, size=10, weight="bold", color="white")
    plt.setp(texts, size=10)

    plt.title(f'전체 기간 상위 {top_n}개 항목 비율 ({title})', fontsize=15)
    plt.tight_layout()
    plt.show()


# ----------------- 메인 실행 부분 -----------------

if __name__ == '__main__':

    print("====================== 데이터 시각화 시작 ======================")

    # 1. 프로그램별 시각화 (Program File)
    df_programs = load_and_clean_data(PROGRAMS_FILE)
    if df_programs is not None:
        print("\n================== 1. 프로그램별 시각화 결과 ==================")
        plot_monthly_trend(df_programs, "TV 프로그램")
        plot_top_categories(df_programs, "TV 프로그램")

    # 2. 장르별 시각화 (Genre File)
    df_genre = load_and_clean_data(GENRE_FILE)
    if df_genre is not None:
        print("\n==================== 2. 장르별 시각화 결과 ====================")
        plot_monthly_trend(df_genre, "TV 장르")
        plot_top_categories(df_genre, "TV 장르")

    print("\n[INFO] 모든 시각화 창이 닫히면 프로그램이 종료됩니다.")