import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import os
import sys

# HTTP → HTTPS 자동 리다이렉트 (8partners.co.kr 도메인 최적화)
# JavaScript를 사용하여 클라이언트 측에서 리다이렉트 수행
st.markdown("""
<script>
(function() {
    // 현재 프로토콜이 HTTP인 경우 HTTPS로 리다이렉트
    if (window.location.protocol === 'http:') {
        var httpsUrl = window.location.href.replace('http://', 'https://');
        // 8partners.co.kr 도메인인 경우에만 리다이렉트
        if (window.location.hostname === '8partners.co.kr' || 
            window.location.hostname.includes('8partners.co.kr')) {
            window.location.replace(httpsUrl);
        }
    }
})();
</script>
""", unsafe_allow_html=True)

# 페이지 설정
st.set_page_config(
    page_title="EMS QUANT AI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS 스타일링 - Pretendard/Noto Sans KR 폰트 및 전체 스타일
st.markdown("""
<style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css');
    
    /* 전체 폰트 설정 */
    * {
        font-family: 'Pretendard', 'Noto Sans KR', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }
    
    /* Streamlit 기본 요소 숨기기 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* 메인 콘텐츠 영역 */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
        max-width: 100%;
    }
    
    /* 사이드바 스타일 */
    [data-testid="stSidebar"] {
        background-color: #fafafa;
        padding: 1.5rem 1rem;
    }
    
    /* 사이드바 타이틀 */
    .sidebar .sidebar-content h1 {
        font-size: 1.5rem;
        font-weight: 700;
        color: #262730;
        margin-bottom: 1.5rem;
        padding-bottom: 0.5rem;
    }
    
    /* 섹션 제목 스타일 */
    .sidebar h3 {
        font-size: 0.75rem;
        font-weight: 600;
        color: #262730;
        margin-top: 1.5rem;
        margin-bottom: 0.75rem;
        text-transform: none;
        letter-spacing: 0.02em;
    }
    
    /* 첫 번째 섹션 (메인 메뉴) */
    .sidebar h3:first-of-type {
        margin-top: 0;
        margin-bottom: 0.5rem;
        font-size: 0.75rem;
    }
    
    /* Expander 완전 커스터마이징 */
    .streamlit-expanderHeader {
        font-size: 0.75rem !important;
        font-weight: 600 !important;
        color: #262730 !important;
        padding: 0.5rem 0 !important;
        margin-bottom: 0.5rem !important;
        background-color: transparent !important;
        border: none !important;
    }
    
    .streamlit-expanderHeader:hover {
        background-color: transparent !important;
    }
    
    /* Expander 아이콘 숨기기 및 커스터마이징 */
    .streamlit-expanderHeader svg {
        display: none !important;
    }
    
    /* Material Icons 텍스트 숨기기 */
    .streamlit-expanderHeader .material-icons,
    .streamlit-expanderHeader [class*="material-icons"],
    .streamlit-expanderHeader span[class*="icon"] {
        display: none !important;
        visibility: hidden !important;
    }
    
    /* keyboard_arrow 같은 텍스트 숨기기 */
    .streamlit-expanderHeader::after {
        content: "▼";
        float: right;
        font-size: 0.7rem;
        color: #666;
        margin-left: 0.5rem;
    }
    
    /* Expander 열림 상태 */
    .streamlit-expanderHeader[aria-expanded="true"]::after {
        content: "▼";
    }
    
    /* Expander 닫힘 상태 */
    .streamlit-expanderHeader[aria-expanded="false"]::after {
        content: "▶";
    }
    
    .streamlit-expanderContent {
        padding: 0 !important;
        margin-top: 0 !important;
    }
    
    /* Expander 내부 버튼 스타일 */
    .streamlit-expanderContent .stButton > button {
        margin-left: 0;
        padding-left: 0.75rem;
        font-size: 0.875rem;
    }
    
    /* 메뉴 버튼 스타일 */
    .stButton > button {
        width: 100%;
        border-radius: 0.25rem;
        border: none;
        padding: 0.5rem 0.75rem;
        text-align: left;
        font-weight: 400;
        font-size: 0.875rem;
        transition: all 0.2s ease;
        background-color: transparent;
        color: #262730;
        margin-bottom: 0.125rem;
        justify-content: flex-start;
    }
    
    .stButton > button:hover {
        background-color: rgba(0, 0, 0, 0.05);
    }
    
    /* 선택된 메뉴 버튼 (primary) */
    .stButton > button[kind="primary"] {
        background-color: rgba(0, 0, 0, 0.08);
        font-weight: 500;
    }
    
    /* Home 버튼 - 항상 색상 없음 */
    button[key="menu_home"] {
        background-color: transparent !important;
    }
    
    button[key="menu_home"]:hover {
        background-color: rgba(0, 0, 0, 0.05) !important;
    }
    
    /* 데이터프레임 스타일 */
    .dataframe {
        font-size: 0.875rem;
    }
    
    /* 헤더 스타일 */
    h1 {
        font-size: 1.75rem;
        font-weight: 700;
        color: #262730;
        margin-bottom: 1rem;
        border-bottom: 2px solid #e0e0e0;
        padding-bottom: 0.5rem;
    }
    
    h3 {
        font-size: 1.125rem;
        font-weight: 600;
        color: #262730;
        margin-top: 1.5rem;
        margin-bottom: 0.75rem;
    }
    
    /* 구분선 숨기기 */
    hr {
        display: none;
    }
    
    /* 모든 불필요한 텍스트 숨기기 */
    [class*="keyboard"],
    [class*="arrow"],
    [data-testid*="key"] {
        font-size: 0 !important;
        visibility: hidden !important;
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)

# 사이드바 네비게이션
st.sidebar.markdown("""
<div style='font-size: 1.5rem; font-weight: 700; color: #262730; margin-bottom: 1.5rem;'>
EMS QUANT AI
</div>
""", unsafe_allow_html=True)

# 세션 상태 초기화
if 'selected_page' not in st.session_state:
    st.session_state.selected_page = "🏠 Home"

# 메인 메뉴 섹션
st.sidebar.markdown("### 메인 메뉴")
if st.sidebar.button("🏠 Home", use_container_width=True, key="menu_home", type="secondary"):
    st.session_state.selected_page = "🏠 Home"
    st.rerun()

# 한국장 섹션 (드롭다운 - 항상 펼쳐진 상태)
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

# 미국장 섹션 (드롭다운 - 항상 펼쳐진 상태)
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
    # 타이틀과 수정 정보를 같은 줄에 표시
    col_title, col_info = st.columns([3, 2])
    
    with col_title:
        st.title("EMS OVERVIEW")
    
    with col_info:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        st.markdown(f"""
        <div style='text-align: right; padding-top: 1.5rem; color: #666; font-size: 0.875rem;'>
            <div>최종 수정시간: {current_time}</div>
            <div style='margin-top: 0.25rem;'>test3</div>
        </div>
        """, unsafe_allow_html=True)
    
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
    # 메인 헤더 (밑줄 포함)
    st.markdown("""
    <h1 style='font-size: 1.75rem; font-weight: 700; color: #262730; margin-bottom: 1rem; border-bottom: 2px solid #e0e0e0; padding-bottom: 0.5rem;'>
    📋 일일 섹터 및 종목 분석 리포트
    </h1>
    """, unsafe_allow_html=True)
    
    # 소제목
    st.markdown("### 🎯 오늘의 스크리닝 요약")
    
    # 샘플 데이터 생성 (실제 데이터로 교체 필요)
    sample_data = pd.DataFrame({
        "종목명": ["삼성전자", "SK하이닉스", "LG에너지솔루션", "NAVER", "카카오", "현대차", "포스코", "셀트리온"],
        "현재가": [75000, 150000, 450000, 180000, 55000, 220000, 380000, 180000],
        "등락률": [2.5, -1.2, 3.8, 0.5, -2.1, 1.8, 2.3, -0.8],
        "거래량": [12500000, 3500000, 850000, 2100000, 5800000, 1200000, 450000, 3200000],
        "국면": ["저점 이후 반등", "저점 매수 영역", "저점 이후 반등", "저점 매수 영역", 
                "저점 이후 반등", "저점 매수 영역", "저점 이후 반등", "저점 매수 영역"]
    })
    
    # 데이터프레임 스타일링 함수
    def style_dataframe(df):
        """국면 열에 따라 배경색 적용"""
        def highlight_phase(val):
            if val == "저점 이후 반등":
                return 'background-color: #ffebee'  # 연한 빨간색
            elif val == "저점 매수 영역":
                return 'background-color: #fff3e0'  # 연한 주황색
            return ''
        
        styled = df.style.applymap(highlight_phase, subset=['국면'])
        styled = styled.set_table_styles([
            {'selector': 'th', 'props': [('font-size', '0.875rem'), ('font-weight', '600'), ('padding', '0.5rem'), ('text-align', 'left')]},
            {'selector': 'td', 'props': [('font-size', '0.875rem'), ('padding', '0.5rem')]},
            {'selector': 'table', 'props': [('width', '100%'), ('border-collapse', 'collapse')]},
            {'selector': 'tbody tr', 'props': [('border-bottom', '1px solid #e0e0e0')]}
        ])
        return styled
    
    # 스타일링된 데이터프레임 표시
    styled_df = style_dataframe(sample_data)
    st.markdown(styled_df.to_html(escape=False, index=False), unsafe_allow_html=True)
    
    # 추가 정보
    st.markdown("<br>", unsafe_allow_html=True)
    st.info("💡 위 데이터는 샘플 데이터입니다. 실제 데이터 연동 후 업데이트됩니다.")

# 한국장 - EMS스코어
elif menu == "💯 EMS스코어":
    st.title("💯 EMS스코어")
    st.info("EMS스코어 기능 개발 중입니다.")

# 한국장 - 섹터 모니터링
elif menu == "📊 섹터 모니터링":
    st.title("📊 섹터 모니터링")
    
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
    st.info("미국장 EMS스코어 기능 개발 중입니다.")

# 미국장 - 섹터 모니터링
elif menu == "📊 섹터 모니터링 (US)":
    st.title("📊 섹터 모니터링 (미국장)")
    
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

# 푸터
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray; padding: 2rem 0;'>
        <p>© 2024 EMS QUANT AI. All rights reserved.</p>
    </div>
    """,
    unsafe_allow_html=True
)
