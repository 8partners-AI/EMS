import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import os
import sys

# 페이지 설정
st.set_page_config(
    page_title="8Partners Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 사이드바 네비게이션
st.sidebar.title("📊 8Partners")
st.sidebar.markdown("---")

# 메인 메뉴
menu = st.sidebar.selectbox(
    "메인 메뉴",
    ["🏠 Home", "🇰🇷 한국장", "🇺🇸 미국장", "📈 분석", "⚙️ 설정"]
)

# Home 페이지
if menu == "🏠 Home":
    st.title("🏠 8Partners Dashboard")
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
        if st.button("🇰🇷 한국장 분석", use_container_width=True):
            st.session_state.menu = "🇰🇷 한국장"
            st.rerun()
    
    with col2:
        if st.button("🇺🇸 미국장 분석", use_container_width=True):
            st.session_state.menu = "🇺🇸 미국장"
            st.rerun()
    
    with col3:
        if st.button("📈 데이터 분석", use_container_width=True):
            st.session_state.menu = "📈 분석"
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

# 한국장 페이지
elif menu == "🇰🇷 한국장":
    st.title("🇰🇷 한국장 분석")
    st.markdown("---")
    
    # 서브 메뉴
    submenu = st.tabs(["📊 종목 분석", "📈 업종별 수익률", "🔥 급등주", "📋 관심종목"])
    
    with submenu[0]:  # 종목 분석
        st.subheader("📊 종목 분석")
        
        # 검색 및 필터
        col1, col2, col3 = st.columns(3)
        
        with col1:
            search_term = st.text_input("종목명 검색", placeholder="예: 삼성전자")
        
        with col2:
            market = st.selectbox("시장", ["전체", "코스피", "코스닥", "코넥스"])
        
        with col3:
            sort_by = st.selectbox("정렬 기준", ["시가총액", "등락률", "거래량"])
        
        # 샘플 데이터
        sample_data = pd.DataFrame({
            "종목명": ["삼성전자", "SK하이닉스", "LG에너지솔루션", "NAVER", "카카오"],
            "현재가": [75000, 150000, 450000, 180000, 55000],
            "등락률": [2.5, -1.2, 3.8, 0.5, -2.1],
            "거래량": [12500000, 3500000, 850000, 2100000, 5800000],
            "시가총액": [4500000, 1100000, 1050000, 280000, 120000]
        })
        
        st.dataframe(sample_data, use_container_width=True, hide_index=True)
        
        # 차트
        if st.checkbox("차트 표시"):
            st.line_chart(sample_data.set_index("종목명")[["현재가", "등락률"]])
    
    with submenu[1]:  # 업종별 수익률
        st.subheader("📈 업종별 수익률")
        
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
    
    with submenu[2]:  # 급등주
        st.subheader("🔥 급등주")
        
        timeframe = st.selectbox("시간대", ["당일", "1주일", "1개월"])
        
        hot_stocks = pd.DataFrame({
            "종목명": ["A기업", "B기업", "C기업", "D기업", "E기업"],
            "현재가": [15000, 25000, 35000, 45000, 55000],
            "등락률": [15.5, 12.3, 10.8, 9.2, 8.5],
            "거래량": [5000000, 3200000, 2800000, 2100000, 1800000],
            "시가총액": [150000, 250000, 350000, 450000, 550000]
        })
        
        st.dataframe(hot_stocks, use_container_width=True, hide_index=True)
    
    with submenu[3]:  # 관심종목
        st.subheader("📋 관심종목")
        
        watchlist = st.multiselect(
            "관심종목 선택",
            ["삼성전자", "SK하이닉스", "LG에너지솔루션", "NAVER", "카카오", "현대차", "기아", "POSCO홀딩스"],
            default=["삼성전자", "SK하이닉스"]
        )
        
        if watchlist:
            watchlist_data = pd.DataFrame({
                "종목명": watchlist,
                "현재가": [75000, 150000, 450000, 180000, 55000, 250000, 120000, 450000],
                "등락률": [2.5, -1.2, 3.8, 0.5, -2.1, 1.5, 2.3, 0.8],
                "거래량": [12500000, 3500000, 850000, 2100000, 5800000, 1200000, 2100000, 850000]
            })
            
            st.dataframe(watchlist_data, use_container_width=True, hide_index=True)

# 미국장 페이지
elif menu == "🇺🇸 미국장":
    st.title("🇺🇸 미국장 분석")
    st.markdown("---")
    
    # 서브 메뉴
    submenu = st.tabs(["📊 종목 분석", "📈 섹터별 수익률", "🔥 급등주", "💼 포트폴리오"])
    
    with submenu[0]:  # 종목 분석
        st.subheader("📊 종목 분석")
        
        # 검색 및 필터
        col1, col2, col3 = st.columns(3)
        
        with col1:
            search_term = st.text_input("종목명/Ticker 검색", placeholder="예: AAPL, Apple")
        
        with col2:
            sector = st.selectbox("섹터", ["전체", "Technology", "Healthcare", "Finance", "Consumer", "Energy"])
        
        with col3:
            sort_by = st.selectbox("정렬 기준", ["시가총액", "등락률", "거래량"])
        
        # 샘플 데이터
        us_stocks = pd.DataFrame({
            "Ticker": ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA"],
            "회사명": ["Apple", "Microsoft", "Google", "Amazon", "NVIDIA"],
            "현재가": [175.50, 380.25, 142.30, 145.80, 485.20],
            "등락률": [1.2, -0.5, 2.1, 0.8, 3.5],
            "거래량": [45000000, 28000000, 32000000, 38000000, 52000000],
            "시가총액": [2800000, 2800000, 1800000, 1500000, 1200000]
        })
        
        st.dataframe(us_stocks, use_container_width=True, hide_index=True)
        
        # 차트
        if st.checkbox("차트 표시"):
            st.line_chart(us_stocks.set_index("Ticker")[["현재가", "등락률"]])
    
    with submenu[1]:  # 섹터별 수익률
        st.subheader("📈 섹터별 수익률")
        
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
    
    with submenu[2]:  # 급등주
        st.subheader("🔥 급등주")
        
        timeframe = st.selectbox("시간대", ["당일", "1주일", "1개월"])
        
        hot_stocks = pd.DataFrame({
            "Ticker": ["TSLA", "AMD", "META", "NFLX", "PYPL"],
            "회사명": ["Tesla", "AMD", "Meta", "Netflix", "PayPal"],
            "현재가": [245.50, 125.80, 320.25, 450.60, 65.30],
            "등락률": [8.5, 6.2, 5.8, 4.9, 4.2],
            "거래량": [85000000, 45000000, 38000000, 28000000, 25000000]
        })
        
        st.dataframe(hot_stocks, use_container_width=True, hide_index=True)
    
    with submenu[3]:  # 포트폴리오
        st.subheader("💼 포트폴리오")
        
        portfolio = st.multiselect(
            "포트폴리오 종목 선택",
            ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "TSLA", "META", "NFLX"],
            default=["AAPL", "MSFT", "GOOGL"]
        )
        
        if portfolio:
            portfolio_data = pd.DataFrame({
                "Ticker": portfolio,
                "회사명": ["Apple", "Microsoft", "Google", "Amazon", "NVIDIA", "Tesla", "Meta", "Netflix"],
                "현재가": [175.50, 380.25, 142.30, 145.80, 485.20, 245.50, 320.25, 450.60],
                "등락률": [1.2, -0.5, 2.1, 0.8, 3.5, 8.5, 5.8, 4.9],
                "보유수량": [100, 50, 75, 60, 30, 40, 25, 20],
                "평가금액": [17550, 19012.5, 10672.5, 8748, 14556, 9820, 8006.25, 9012]
            })
            
            st.dataframe(portfolio_data, use_container_width=True, hide_index=True)
            
            # 총 평가금액
            total_value = portfolio_data["평가금액"].sum()
            st.metric("총 평가금액", f"${total_value:,.2f}")

# 분석 페이지
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

# 설정 페이지
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
        <p>© 2024 8Partners. All rights reserved.</p>
    </div>
    """,
    unsafe_allow_html=True
)
