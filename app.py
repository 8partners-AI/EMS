import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import os
import sys

# 페이지 설정
st.set_page_config(
    page_title="EMS QUANT AI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS 스타일링
st.markdown("""
<style>
    /* 사이드바 스타일 개선 */
    [data-testid="stSidebar"] {
        background-color: #fafafa;
    }
    
    /* 메뉴 버튼 스타일 */
    .stButton > button {
        width: 100%;
        border-radius: 0.25rem;
        border: none;
        padding: 0.5rem 1rem;
        text-align: left;
        font-weight: 400;
        transition: all 0.2s ease;
        background-color: transparent;
        color: #262730;
        margin-bottom: 0.25rem;
    }
    
    .stButton > button:hover {
        background-color: rgba(0, 0, 0, 0.05);
    }
    
    /* Primary 버튼 (선택된 메뉴) */
    .stButton > button[kind="primary"] {
        background-color: rgba(0, 0, 0, 0.08);
        font-weight: 500;
    }
    
    /* 섹션 제목 스타일 */
    .sidebar h3 {
        font-size: 0.875rem;
        font-weight: 600;
        color: #262730;
        margin-top: 1.5rem;
        margin-bottom: 0.75rem;
        text-transform: none;
    }
    
    /* 사이드바 제목 */
    .sidebar h1 {
        font-size: 1.5rem;
        font-weight: 700;
        color: #262730;
        margin-bottom: 1rem;
    }
    
    /* 구분선 숨기기 */
    hr {
        display: none;
    }
    
    /* Expander 스타일 */
    .streamlit-expanderHeader {
        font-size: 0.875rem;
        font-weight: 600;
        color: #262730;
    }
</style>
""", unsafe_allow_html=True)

# 사이드바 네비게이션
st.sidebar.markdown("""
<div style='font-size: 1.5rem; font-weight: 700; color: #262730; margin-bottom: 1rem;'>
EMS QUANT AI
</div>
""", unsafe_allow_html=True)

# 세션 상태 초기화
if 'selected_page' not in st.session_state:
    st.session_state.selected_page = "🏠 Home"

# 메인 메뉴 섹션
st.sidebar.markdown("### 메인 메뉴")
if st.sidebar.button("🏠 Home", use_container_width=True, key="menu_home",
                    type="primary" if st.session_state.selected_page == "🏠 Home" else "secondary"):
    st.session_state.selected_page = "🏠 Home"
    st.rerun()

# 한국장 섹션 (드롭다운)
with st.sidebar.expander("### 한국장", expanded=True):
    kr_menu_items = [
        ("📄 일일 리포트", "📄 일일 리포트"),
        ("💯 EMS스코어", "💯 EMS스코어"),
        ("📊 섹터 모니터링", "📊 섹터 모니터링"),
        ("📈 섹터별 수익률", "📈 섹터별 수익률"),
        ("🔍 종목 스크리닝", "🔍 종목 스크리닝")
    ]
    
    for label, page in kr_menu_items:
        if st.button(label, use_container_width=True, key=f"kr_{page}",
                    type="primary" if st.session_state.selected_page == page else "secondary"):
            st.session_state.selected_page = page
            st.rerun()

# 미국장 섹션 (드롭다운)
with st.sidebar.expander("### 미국장", expanded=True):
    us_menu_items = [
        ("💯 EMS스코어", "💯 EMS스코어 (US)"),
        ("📊 섹터 모니터링", "📊 섹터 모니터링 (US)"),
        ("📈 섹터별 수익률", "📈 섹터별 수익률 (US)"),
        ("🔍 종목 스크리닝", "🔍 종목 스크리닝 (US)")
    ]
    
    for label, page in us_menu_items:
        if st.button(label, use_container_width=True, key=f"us_{page}",
                    type="primary" if st.session_state.selected_page == page else "secondary"):
            st.session_state.selected_page = page
            st.rerun()

# 현재 선택된 페이지
menu = st.session_state.selected_page

# Home 페이지
if menu == "🏠 Home":
    st.title("EMS OVERVIEW")
    st.markdown("---")
    
    # 주요 지표
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("한국장 종목 수", "2,847", "↑ 12")
    
    with col2:
        st.metric("미국장 종목 수", "5,234", "↑ 45")
    
    with col3:
        st.metric("오늘 거래량", "1.2조원", "↑ 5.3%")
    
    with col4:
        st.metric("시스템 상태", "정상", "✓")
    
    st.markdown("---")
    
    # 빠른 접근
    st.subheader("🚀 빠른 접근")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📄 일일 리포트", use_container_width=True):
            st.session_state.selected_page = "📄 일일 리포트"
            st.rerun()
    
    with col2:
        if st.button("📊 섹터 모니터링", use_container_width=True):
            st.session_state.selected_page = "📊 섹터 모니터링"
            st.rerun()
    
    with col3:
        if st.button("🔍 종목 스크리닝", use_container_width=True):
            st.session_state.selected_page = "🔍 종목 스크리닝"
            st.rerun()
    
    st.markdown("---")
    
    # 최근 활동
    st.subheader("📊 최근 활동")
    
    activity_data = pd.DataFrame({
        "시간": pd.date_range(start=datetime.now().date(), periods=5, freq="-1D"),
        "활동": ["한국장 데이터 업데이트", "미국장 분석 완료", "보고서 생성", "시스템 점검", "데이터 백업"],
        "상태": ["완료", "완료", "완료", "완료", "완료"]
    })
    
    st.dataframe(activity_data, use_container_width=True, hide_index=True)

# 한국장 - 일일 리포트
elif menu == "📄 일일 리포트":
    st.title("📄 일일 리포트")
    st.markdown("---")
    st.info("일일 리포트 기능 개발 중입니다.")
    
# 한국장 - EMS스코어
elif menu == "💯 EMS스코어":
    st.title("💯 EMS스코어")
    st.markdown("---")
    st.info("EMS스코어 기능 개발 중입니다.")

# 한국장 - 섹터 모니터링
elif menu == "📊 섹터 모니터링":
    st.title("📊 섹터 모니터링")
    st.markdown("---")
    
    sector_data = pd.DataFrame({
        "업종": ["반도체", "2차전지", "IT서비스", "은행", "증권", "화학", "바이오", "자동차"],
        "수익률": [5.2, 3.8, 2.1, -0.5, 1.2, 4.5, 6.2, 2.8],
        "종목수": [45, 32, 28, 12, 15, 38, 52, 25]
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.dataframe(sector_data, use_container_width=True, hide_index=True)
    
    with col2:
        st.bar_chart(sector_data.set_index("업종")["수익률"])

# 한국장 - 섹터별 수익률
elif menu == "📈 섹터별 수익률":
    st.title("📈 섹터별 수익률")
    st.markdown("---")
    
    period = st.selectbox("기간", ["1일", "1주", "1개월", "3개월", "6개월", "1년"])
    
    sector_data = pd.DataFrame({
        "업종": ["반도체", "2차전지", "IT서비스", "은행", "증권", "화학", "바이오", "자동차"],
        "수익률": [5.2, 3.8, 2.1, -0.5, 1.2, 4.5, 6.2, 2.8],
        "종목수": [45, 32, 28, 12, 15, 38, 52, 25]
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.dataframe(sector_data, use_container_width=True, hide_index=True)
    
    with col2:
        st.bar_chart(sector_data.set_index("업종")["수익률"])

# 한국장 - 종목 스크리닝
elif menu == "🔍 종목 스크리닝":
    st.title("🔍 종목 스크리닝")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        search_term = st.text_input("종목명 검색", placeholder="예: 삼성전자")
    
    with col2:
        market = st.selectbox("시장", ["전체", "코스피", "코스닥", "코넥스"])
    
    with col3:
        sort_by = st.selectbox("정렬 기준", ["시가총액", "등락률", "거래량"])
    
    sample_data = pd.DataFrame({
        "종목명": ["삼성전자", "SK하이닉스", "LG에너지솔루션", "NAVER", "카카오"],
        "현재가": [75000, 150000, 450000, 180000, 55000],
        "등락률": [2.5, -1.2, 3.8, 0.5, -2.1],
        "거래량": [12500000, 3500000, 850000, 2100000, 5800000],
        "시가총액": [4500000, 1100000, 1050000, 280000, 120000]
    })
    
    st.dataframe(sample_data, use_container_width=True, hide_index=True)

# 미국장 - EMS스코어
elif menu == "💯 EMS스코어 (US)":
    st.title("💯 EMS스코어 (미국장)")
    st.markdown("---")
    st.info("미국장 EMS스코어 기능 개발 중입니다.")

# 미국장 - 섹터 모니터링
elif menu == "📊 섹터 모니터링 (US)":
    st.title("📊 섹터 모니터링 (미국장)")
    st.markdown("---")
    
    sector_data = pd.DataFrame({
        "섹터": ["Technology", "Healthcare", "Finance", "Consumer", "Energy", "Industrial", "Materials", "Utilities"],
        "수익률": [3.2, 2.8, 1.5, 2.1, -0.8, 1.8, 2.5, 0.9],
        "종목수": [125, 98, 85, 72, 45, 68, 52, 38]
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.dataframe(sector_data, use_container_width=True, hide_index=True)
    
    with col2:
        st.bar_chart(sector_data.set_index("섹터")["수익률"])

# 미국장 - 섹터별 수익률
elif menu == "📈 섹터별 수익률 (US)":
    st.title("📈 섹터별 수익률 (미국장)")
    st.markdown("---")
    
    period = st.selectbox("기간", ["1일", "1주", "1개월", "3개월", "6개월", "1년"])
    
    sector_data = pd.DataFrame({
        "섹터": ["Technology", "Healthcare", "Finance", "Consumer", "Energy", "Industrial", "Materials", "Utilities"],
        "수익률": [3.2, 2.8, 1.5, 2.1, -0.8, 1.8, 2.5, 0.9],
        "종목수": [125, 98, 85, 72, 45, 68, 52, 38]
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.dataframe(sector_data, use_container_width=True, hide_index=True)
    
    with col2:
        st.bar_chart(sector_data.set_index("섹터")["수익률"])

# 미국장 - 종목 스크리닝
elif menu == "🔍 종목 스크리닝 (US)":
    st.title("🔍 종목 스크리닝 (미국장)")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        search_term = st.text_input("종목명/Ticker 검색", placeholder="예: AAPL, Apple")
    
    with col2:
        sector = st.selectbox("섹터", ["전체", "Technology", "Healthcare", "Finance", "Consumer", "Energy"])
    
    with col3:
        sort_by = st.selectbox("정렬 기준", ["시가총액", "등락률", "거래량"])
    
    us_stocks = pd.DataFrame({
        "Ticker": ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA"],
        "회사명": ["Apple", "Microsoft", "Google", "Amazon", "NVIDIA"],
        "현재가": [175.50, 380.25, 142.30, 145.80, 485.20],
        "등락률": [1.2, -0.5, 2.1, 0.8, 3.5],
        "거래량": [45000000, 28000000, 32000000, 38000000, 52000000],
        "시가총액": [2800000, 2800000, 1800000, 1500000, 1200000]
    })
    
    st.dataframe(us_stocks, use_container_width=True, hide_index=True)

# 기존 분석 페이지 (호환성을 위해 유지)
elif menu == "📈 분석":
    st.title("📈 데이터 분석")
    st.markdown("---")
    
    # 파일 업로드
    uploaded_file = st.file_uploader(
        "데이터 파일 업로드 (CSV, Excel)",
        type=['csv', 'xlsx', 'xls']
    )
    
    if uploaded_file is not None:
        try:
            # 파일 확장자에 따라 읽기
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            
            st.success(f"✅ 파일이 성공적으로 로드되었습니다! ({len(df)} 행)")
            
            # 데이터 미리보기
            st.subheader("📋 데이터 미리보기")
            st.dataframe(df.head(20), use_container_width=True)
            
            # 데이터 통계
            st.subheader("📊 데이터 통계")
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**기본 정보**")
                st.write(f"- 총 행 수: {len(df):,}")
                st.write(f"- 총 열 수: {len(df.columns)}")
                st.write(f"- 결측치: {df.isnull().sum().sum():,}")
            
            with col2:
                st.write("**데이터 타입**")
                dtype_df = pd.DataFrame({
                    "컬럼명": df.dtypes.index,
                    "데이터 타입": df.dtypes.values
                })
                st.dataframe(dtype_df, use_container_width=True, hide_index=True)
            
            # 수치형 데이터 통계
            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
            if numeric_cols:
                st.subheader("📈 수치형 데이터 통계")
                st.dataframe(df[numeric_cols].describe(), use_container_width=True)
                
                # 차트 선택
                chart_type = st.selectbox(
                    "차트 유형 선택",
                    ["선 그래프", "막대 그래프", "히스토그램", "산점도"]
                )
                
                if chart_type == "선 그래프":
                    selected_col = st.selectbox("컬럼 선택", numeric_cols)
                    st.line_chart(df[selected_col])
                
                elif chart_type == "막대 그래프":
                    selected_col = st.selectbox("컬럼 선택", numeric_cols)
                    st.bar_chart(df[selected_col])
                
                elif chart_type == "히스토그램":
                    selected_col = st.selectbox("컬럼 선택", numeric_cols)
                    st.hist_chart(df[selected_col])
                
                elif chart_type == "산점도":
                    x_col = st.selectbox("X축 컬럼", numeric_cols)
                    y_col = st.selectbox("Y축 컬럼", numeric_cols)
                    if x_col != y_col:
                        st.scatter_chart(df[[x_col, y_col]])
        
        except Exception as e:
            st.error(f"❌ 파일 로드 중 오류가 발생했습니다: {str(e)}")
    else:
        st.info("👆 위에서 데이터 파일을 업로드해주세요.")

# 기존 설정 페이지 (호환성을 위해 유지)
elif menu == "⚙️ 설정":
    st.title("⚙️ 설정")
    st.markdown("---")
    
    # 사용자 설정
    st.subheader("👤 사용자 설정")
    
    username = st.text_input("사용자 이름", value="관리자")
    email = st.text_input("이메일", value="admin@8partners.co.kr")
    language = st.selectbox("언어", ["한국어", "English", "日本語"])
    
    if st.button("💾 설정 저장"):
        st.success("✅ 설정이 저장되었습니다!")
    
    st.markdown("---")
    
    # 시스템 설정
    st.subheader("🔧 시스템 설정")
    
    auto_refresh = st.checkbox("자동 새로고침", value=False)
    if auto_refresh:
        refresh_interval = st.slider("새로고침 간격 (초)", 10, 300, 60)
    
    theme = st.selectbox("테마", ["라이트", "다크", "시스템 기본값"])
    
    st.markdown("---")
    
    # 정보
    st.subheader("ℹ️ 시스템 정보")
    st.write(f"- Streamlit 버전: {st.__version__}")
    st.write(f"- Python 버전: {sys.version.split()[0]}")
    st.write(f"- 현재 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# 푸터
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray;'>
        <p>© 2024 EMS QUANT AI. All rights reserved.</p>
    </div>
    """,
    unsafe_allow_html=True
)
