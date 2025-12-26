import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import os
import sys

# 1. 페이지 설정 (최상단 필수)
st.set_page_config(
    page_title="EMS QUANT AI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. HTTP → HTTPS 리다이렉트
st.markdown("""
<script>
(function() {
    if (window.location.protocol === 'http:') {
        var httpsUrl = window.location.href.replace('http://', 'https://');
        if (window.location.hostname === '8partners.co.kr' || 
            window.location.hostname.includes('8partners.co.kr')) {
            window.location.replace(httpsUrl);
        }
    }
})();
</script>
""", unsafe_allow_html=True)

# 3. [핵심] CSS 스타일링: Ongkoo-ai 스타일 완벽 재현
st.markdown("""
<style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css');
    
    /* 전체 폰트 적용 */
    html, body, [class*="css"] {
        font-family: 'Pretendard', 'Noto Sans KR', sans-serif;
    }

    /* ----------------------------------------------------------------------
       [사이드바 디자인 혁신] 
       1. 드롭다운(Expander)의 박스 테두리 제거
       2. 버튼의 박스 형태 제거 및 왼쪽 정렬 (텍스트 메뉴화)
       ---------------------------------------------------------------------- */
    
    /* 사이드바 배경색: 아주 연한 톤 */
    [data-testid="stSidebar"] {
        background-color: #F8F9FA;
    }

    /* [드롭다운(Expander) 스타일] - 박스 테두리 제거가 핵심 */
    [data-testid="stSidebar"] [data-testid="stExpander"] {
        border: none !important;
        box-shadow: none !important;
        background-color: transparent !important;
        margin-bottom: 0rem !important; /* 간격 축소 */
    }
    
    [data-testid="stSidebar"] [data-testid="stExpander"] > details {
        border: none !important;
    }

    /* 드롭다운 헤더(제목) 스타일 */
    [data-testid="stSidebar"] .streamlit-expanderHeader {
        font-size: 0.9rem;
        font-weight: 600;
        color: #555;
        background-color: transparent !important;
        padding: 0.5rem 0 0.5rem 0.5rem; /* 여백 조정 */
    }
    
    /* 드롭다운 헤더 마우스 오버 시 */
    [data-testid="stSidebar"] .streamlit-expanderHeader:hover {
        color: #000;
    }

    /* [버튼 스타일] - 텍스트 링크처럼 만들기 */
    [data-testid="stSidebar"] .stButton > button {
        width: 100%;
        border: none !important;
        background-color: transparent !important;
        color: #4B5563 !important; /* 짙은 회색 */
        text-align: left !important; /* [중요] 왼쪽 정렬 */
        display: flex !important;
        justify-content: flex-start !important;
        padding: 0.4rem 0.5rem 0.4rem 1.5rem !important; /* 들여쓰기로 계층 구조 표현 */
        font-size: 0.9rem !important;
        font-weight: 400 !important;
        box-shadow: none !important;
        margin-top: -0.5rem !important; /* 버튼 간격 좁히기 */
    }

    /* 버튼 마우스 오버 (Hover) */
    [data-testid="stSidebar"] .stButton > button:hover {
        background-color: rgba(0,0,0,0.03) !important; /* 아주 연한 회색 */
        color: #000 !important;
        font-weight: 500 !important;
    }

    /* [선택된 메뉴 스타일] - type="primary" 인 경우 */
    [data-testid="stSidebar"] .stButton > button[kind="primary"] {
        background-color: #EFF6FF !important; /* 연한 하늘색 배경 */
        color: #1E3A8A !important; /* 진한 파란색 글씨 */
        font-weight: 700 !important;
        border-left: 3px solid #1E3A8A !important; /* 왼쪽에 포인트 컬러바 */
        padding-left: 1.3rem !important; /* 테두리 두께만큼 보정 */
    }
    
    /* Home 버튼 별도 스타일 (들여쓰기 없앰) */
    [data-key="menu_home"] > button {
        padding-left: 0.5rem !important;
        margin-top: 0 !important;
    }

    /* 상단 헤더 숨김 (깔끔하게) */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

</style>
""", unsafe_allow_html=True)

# --- 사이드바 헤더 ---
st.sidebar.markdown("""
<div style='font-size: 1.4rem; font-weight: 800; color: #1E3A8A; margin-bottom: 2rem; padding-left: 0.5rem; letter-spacing: -0.5px;'>
EMS QUANT AI
</div>
""", unsafe_allow_html=True)

# 세션 상태 초기화
if 'selected_page' not in st.session_state:
    st.session_state.selected_page = "🏠 Home"

# --- 메뉴 구성 로직 ---

# 1. 메인 메뉴 (Home)
st.sidebar.markdown("<div style='font-size:0.75rem; font-weight:600; color:#999; margin-bottom:0.5rem; padding-left:0.5rem;'>메인 메뉴</div>", unsafe_allow_html=True)
if st.sidebar.button("🏠 Home", key="menu_home", use_container_width=True,
                     type="primary" if st.session_state.selected_page == "🏠 Home" else "secondary"):
    st.session_state.selected_page = "🏠 Home"
    st.rerun()

st.sidebar.markdown("<div style='margin-top:1.5rem;'></div>", unsafe_allow_html=True)

# 2. 한국장 (Expander)
# 박스 테두리를 없앴으므로, 텍스트가 자연스럽게 그룹화된 것처럼 보입니다.
with st.sidebar.expander("🇰🇷 한국장", expanded=True):
    kr_menu = {
        "📄 일일 리포트": "📄 일일 리포트",
        "💯 EMS스코어": "💯 EMS스코어",
        "📊 섹터 모니터링": "📊 섹터 모니터링",
        "📈 섹터별 수익률": "📈 섹터별 수익률",
        "🔍 종목 스크리닝": "🔍 종목 스크리닝"
    }
    
    for label, page_name in kr_menu.items():
        btn_type = "primary" if st.session_state.selected_page == page_name else "secondary"
        if st.button(label, key=f"kr_{label}", use_container_width=True, type=btn_type):
            st.session_state.selected_page = page_name
            st.rerun()

st.sidebar.markdown("<div style='margin-top:0.5rem;'></div>", unsafe_allow_html=True)

# 3. 미국장 (Expander)
with st.sidebar.expander("🇺🇸 미국장", expanded=True):
    us_menu = {
        "💯 EMS스코어 (US)": "💯 EMS스코어 (US)",
        "📊 섹터 모니터링 (US)": "📊 섹터 모니터링 (US)",
        "📈 섹터별 수익률 (US)": "📈 섹터별 수익률 (US)",
        "🔍 종목 스크리닝 (US)": "🔍 종목 스크리닝 (US)"
    }
    
    for label, page_name in us_menu.items():
        btn_type = "primary" if st.session_state.selected_page == page_name else "secondary"
        if st.button(label, key=f"us_{label}", use_container_width=True, type=btn_type):
            st.session_state.selected_page = page_name
            st.rerun()


# --- 메인 컨텐츠 영역 ---
menu = st.session_state.selected_page

# 1. Home 페이지
if menu == "🏠 Home":
    col_title, col_info = st.columns([3, 2])
    with col_title:
        st.title("EMS OVERVIEW")
    with col_info:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        st.markdown(f"""
        <div style='text-align: right; padding-top: 1.5rem; color: #666; font-size: 0.8rem;'>
            <div>최종 업데이트: {current_time}</div>
            <div style='margin-top: 0.25rem; font-family: monospace; color: #999;'> test7ㄸㄸㄸㄴㄹㄴ89</div>
        </div>
        """, unsafe_allow_html=True)
    
    # 지표 카드
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("한국장 종목 수", "2,847", "↑ 12")
    col2.metric("미국장 종목 수", "5,234", "↑ 45")
    col3.metric("오늘 거래량", "1.2조원", "↑ 5.3%")
    col4.metric("시스템 상태", "정상", "✓")
    
    st.subheader("🚀 빠른 접근")
    c1, c2, c3 = st.columns(3)
    # 빠른 접근 버튼은 여전히 박스 형태가 직관적이므로 유지 (원하시면 이것도 변경 가능)
    if c1.button("📄 일일 리포트 바로가기", use_container_width=True):
        st.session_state.selected_page = "📄 일일 리포트"
        st.rerun()
    if c2.button("📊 섹터 모니터링 확인", use_container_width=True):
        st.session_state.selected_page = "📊 섹터 모니터링"
        st.rerun()
    if c3.button("🔍 종목 검색", use_container_width=True):
        st.session_state.selected_page = "🔍 종목 스크리닝"
        st.rerun()
        
    st.subheader("📊 최근 활동")
    activity_data = pd.DataFrame({
        "시간": pd.date_range(start=datetime.now().date(), periods=5, freq="-1D"),
        "활동": ["한국장 데이터 업데이트", "미국장 분석 완료", "보고서 생성", "시스템 점검", "데이터 백업"],
        "상태": ["완료", "완료", "완료", "완료", "완료"]
    })
    st.dataframe(activity_data, use_container_width=True, hide_index=True)

# 2. 한국장 - 일일 리포트
elif menu == "📄 일일 리포트":
    st.markdown("## 📋 한국 섹터 및 종목 분석 리포트")
    st.markdown(f"<div style='color:#666; font-size:0.8rem; margin-bottom:1rem;'>마지막 리포트 생성 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div>", unsafe_allow_html=True)
    
    st.markdown("### 🎯 오늘의 스크리닝 요약")
    
    sample_data = pd.DataFrame({
        "종목명": ["삼성전자", "SK하이닉스", "LG에너지솔루션", "NAVER", "카카오", "현대차"],
        "현재가": [75000, 150000, 450000, 180000, 55000, 220000],
        "등락률": [0.025, -0.012, 0.038, 0.005, -0.021, 0.018],
        "국면": ["저점 이후 반등", "저점 매수 영역", "저점 이후 반등", "저점 매수 영역", "고점 이후 하락", "상승 추세"],
        "RS점수": [85, 92, 78, 65, 45, 88]
    })

    st.dataframe(
        sample_data,
        column_config={
            "종목명": st.column_config.TextColumn("종목명", width="medium"),
            "현재가": st.column_config.NumberColumn("현재가", format="%d원"),
            "등락률": st.column_config.NumberColumn(
                "등락률", format="%.2f%%", help="전일 대비 등락률"
            ),
            "국면": st.column_config.TextColumn("시장 국면", width="medium"),
            "RS점수": st.column_config.ProgressColumn(
                "RS 강도", format="%d", min_value=0, max_value=100
            ),
        },
        use_container_width=True,
        hide_index=True
    )
    st.info("💡 **Tip**: '저점 이후 반등' 국면은 추세 전환의 신호일 수 있습니다.")

# 3. 나머지 페이지들 (Placeholder)
elif menu == "💯 EMS스코어":
    st.title("💯 EMS스코어")
    st.info("EMS스코어 기능 개발 중입니다.")
elif menu == "📊 섹터 모니터링":
    st.title("📊 섹터 모니터링")
    st.write("섹터별 데이터를 준비 중입니다.")
elif menu == "📈 섹터별 수익률":
    st.title("📈 섹터별 수익률")
    st.write("수익률 차트를 준비 중입니다.")
elif menu == "🔍 종목 스크리닝":
    st.title("🔍 종목 스크리닝")
    st.write("검색 기능을 준비 중입니다.")

# 미국장 페이지들
elif menu == "💯 EMS스코어 (US)":
    st.title("💯 EMS스코어 (미국장)")
    st.info("미국장 데이터 연동 중입니다.")
elif menu == "📊 섹터 모니터링 (US)":
    st.title("📊 섹터 모니터링 (미국장)")
    st.write("미국 섹터 데이터 준비 중입니다.")
elif menu == "📈 섹터별 수익률 (US)":
    st.title("📈 섹터별 수익률 (미국장)")
    st.write("미국 수익률 차트 준비 중입니다.")
elif menu == "🔍 종목 스크리닝 (US)":
    st.title("🔍 종목 스크리닝 (미국장)")
    st.write("미국 종목 검색 준비 중입니다.")

# 푸터
st.markdown("---")
current_year = datetime.now().year
st.markdown(f"<div style='text-align: center; color: #888; font-size: 0.8rem;'>© {current_year} EMS QUANT AI. All rights reserved.</div>", unsafe_allow_html=True)

