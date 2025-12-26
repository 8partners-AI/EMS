import streamlit as st
import pandas as pd
import plotly.express as px

# 1. 페이지 기본 설정 (무조건 최상단)
st.set_page_config(
    page_title="EMS QUANT AI",
    page_icon="📈",
    layout="wide",  # 화면을 넓게 사용 (필수)
    initial_sidebar_state="expanded"
)

# 2. 커스텀 CSS (디자인 디테일 잡기)
# ongkoo-ai 처럼 깔끔한 폰트와 헤더 스타일 적용
st.markdown("""
    <style>
        /* 전체 폰트 적용 (Pretendard, 없으면 Sans-serif) */
        html, body, [class*="css"] {
            font-family: 'Pretendard', 'Noto Sans KR', sans-serif;
        }
        /* 메인 타이틀 스타일 */
        h1 {
            color: #1E3A8A; /* 진한 남색 */
            font-weight: 700;
        }
        /* 데이터프레임 헤더 색상 */
        [data-testid="stDataFrame"] th {
            background-color: #F3F4F6;
            color: #374151;
        }
    </style>
""", unsafe_allow_html=True)

# 3. 데이터 로드 (캐싱을 통해 속도 향상)
@st.cache_data
def load_data():
    # 파일명이 매일 바뀌면 glob으로 찾는 로직이 필요하지만, 일단 예시 파일명 사용
    # 실제로는 이전에 알려드린 glob 코드를 쓰시면 됩니다.
    try:
        # 엑셀 파일이 없으면 임시 데이터 생성 (테스트용)
        df = pd.read_excel("EMS_US_Report.xlsx") 
    except:
        # 파일이 없을 경우를 대비한 더미 데이터 (에러 방지용)
        data = {
            '국면': ['저점 매수 영역', '저점 매수 영역', '고점 이후 하락', '상승 추세'],
            '섹터': ['이차전지', '반도체', '바이오', '자동차'],
            '종목명': ['에코프로', '삼성전자', '셀트리온', '현대차'],
            '등락률': [0.015, -0.005, 0.023, 0.010],
            'RS점수': [94, 88, 70, 92]
        }
        df = pd.DataFrame(data)
    return df

df = load_data()

# 4. 메인 화면 구성
st.title("📋 일일 섹터 및 종목 분석 리포트")
st.markdown("---") # 구분선

# (1) 시장 요약 지표 (Metrics) - 3단 컬럼
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="오늘의 추천 종목 수", value=f"{len(df)}개", delta="전일 대비 +2")
with col2:
    avg_score = df['RS점수'].mean() if 'RS점수' in df.columns else 0
    st.metric(label="평균 RS 점수", value=f"{avg_score:.1f}점", delta="-1.5")
with col3:
    top_sector = df['섹터'].value_counts().idxmax() if '섹터' in df.columns else "-"
    st.metric(label="주도 섹터", value=top_sector)

st.markdown("### 🎯 오늘의 스크리닝 요약")

# (2) 스타일이 적용된 데이터프레임 (핵심 기술)
# 등락률을 퍼센트로 보여주고, 색상 바를 추가함
st.dataframe(
    df,
    column_config={
        "종목명": st.column_config.TextColumn("종목명", help="종목의 이름입니다.", width="medium"),
        "등락률": st.column_config.NumberColumn(
            "등락률",
            help="전일 대비 등락률",
            format="%.2f%%", # 퍼센트 포맷
        ),
        "RS점수": st.column_config.ProgressColumn(
            "RS 강도",
            help="상대적 강도 점수 (0~100)",
            format="%d",
            min_value=0,
            max_value=100,
        ),
    },
    use_container_width=True, # 화면 너비 꽉 채우기
    hide_index=True # 인덱스 번호 숨기기
)

# (3) 하단 차트 (Plotly)
if '섹터' in df.columns and 'RS점수' in df.columns:
    st.markdown("### 📊 섹터별 RS 점수 비교")
    fig = px.bar(df, x='섹터', y='RS점수', color='국면', title="섹터별 모멘텀 분석")
    st.plotly_chart(fig, use_container_width=True)
