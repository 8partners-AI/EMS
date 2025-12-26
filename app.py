import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# [버전 관리] Ver: 23 (섹션 타이틀 강제 색상 변경 및 노출)
VER = 23

# 1. 페이지 설정
st.set_page_config(
    page_title="EMS QUANT AI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CSS 스타일링 (섹션 타이틀 '한국장/미국장'이 안 보이는 문제 해결)
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
<style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css');
    
    html, body, [class*="css"] {
        font-family: 'Pretendard', 'Noto Sans KR', sans-serif;
    }

    /* 상단 헤더, 푸터 숨김 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* ----------------------------------------------------------------------
       [1] 타이틀 및 구분선
       ---------------------------------------------------------------------- */
    [data-testid="stSidebarNav"] {
        padding-top: 1rem; 
    }
    
    [data-testid="stSidebarNav"]::before {
        content: "EMS QUANT AI";
        display: block;
        font-size: 1.6rem;
        font-weight: 800;
        color: #1E3A8A; 
        letter-spacing: -0.5px;
        margin-left: 20px;
        margin-right: 20px;
        margin-top: 10px;
        padding-bottom: 20px;
        border-bottom: 1px solid #e0e0e0;
        margin-bottom: 25px;
    }

    /* ----------------------------------------------------------------------
       [2] 메뉴 링크 디자인 (텍스트 스타일)
       ---------------------------------------------------------------------- */
    [data-testid="stSidebarNav"] a span {
        font-size: 0.95rem;
        font-weight: 500;
        color: #555;
    }
    
    [data-testid="stSidebarNav"] a[aria-current="page"] {
        background-color: transparent !important;
    }
    [data-testid="stSidebarNav"] a[aria-current="page"] span {
        color: #1E3A8A !important;
        font-weight: 800 !important;
    }
    [data-testid="stSidebarNav"] a:hover {
        background-color: rgba(0,0,0,0.03) !important;
    }

    /* ----------------------------------------------------------------------
       [3] ★ 섹션 타이틀(한국장, 미국장) 강제 노출 (핵심 수정) ★
       ---------------------------------------------------------------------- */
    /* 섹션 구분자(Separator) 안의 텍스트를 타격합니다 */
    div[data-testid="stSidebarNav"] span {
        /* 기본적으로 모든 span을 건드리되, 링크(a) 안의 span은 제외해야 함을 유의 */
        /* 하지만 Streamlit 구조상 섹션 헤더는 a 태그 밖에 존재함 */
    }

    /* 섹션 헤더(Main, 한국장, 미국장) 스타일링 */
    /* Streamlit 버전에 따라 구조가 다르므로 강력한 선택자 사용 */
    li[role="presentation"] {
        margin-top: 20px !important;
        margin-bottom: 10px !important;
    }
    
    /* 섹션 텍스트 강제 색상 변경 */
    li[role="presentation"] span,
    span[data-testid="stSidebarNavSeparator"] {
        display: block !important;       /* 무조건 보이기 */
        visibility: visible !important;  /* 무조건 보이기 */
        color: #1E3A8A !important;       /* 진한 남색으로 변경 (눈에 띄게) */
        font-size: 0.85rem !important;
        font-weight: 700 !important;
        text-transform: uppercase;
        padding-left: 20px !important;   /* 타이틀 라인 맞춤 */
        opacity: 1 !important;
    }

</style>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# [페이지 내용 정의]
# -----------------------------------------------------------------------------

def page_home():
    col_title, col_info = st.columns([3, 2])
    with col_title:
        st.title("EMS OVERVIEW")
    with col_info:
        kst_time = datetime.utcnow() + timedelta(hours=9)
        current_time_str = kst_time.strftime('%Y-%m-%d %H:%M:%S')
        st.markdown(f"""
        <div style='text-align: right; padding-top: 1.5rem; color: #666; font-size: 0.8rem;'>
            <div>최종 업데이트: {current_time_str}</div>
            <div style='margin-top: 0.25rem; font-family: monospace; color: #999;'>ver: {VER}</div>
        </div>
        """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("한국장 종목 수", "2,847", "↑ 12")
    col2.metric("미국장 종목 수", "5,234", "↑ 45")
    col3.metric("오늘 거래량", "1.2조원", "↑ 5.3%")
    col4.metric("시스템 상태", "정상", "✓")
    
    st.subheader("🚀 빠른 접근")
    c1, c2, c3 = st.columns(3)
    if c1.button("📄 일일 리포트 바로가기", use_container_width=True):
        st.switch_page(pg_kr_1)
    if c2.button("📊 섹터 모니터링 확인", use_container_width=True):
        st.switch_page(pg_kr_3)
    if c3.button("🔍 종목 검색", use_container_width=True):
        st.switch_page(pg_kr_5)
        
    st.subheader("📊 최근 활동")
    activity_data = pd.DataFrame({
        "시간": pd.date_range(start=datetime.now().date(), periods=5, freq="-1D"),
        "활동": ["한국장 데이터 업데이트", "미국장 분석 완료", "보고서 생성", "시스템 점검", "데이터 백업"],
        "상태": ["완료", "완료", "완료", "완료", "완료"]
    })
    st.dataframe(activity_data, use_container_width=True, hide_index=True)

def page_kr_report():
    kst_time = datetime.utcnow() + timedelta(hours=9)
    st.markdown("## 📋 한국 섹터 및 종목 분석 리포트")
    st.markdown(f"<div style='color:#666; font-size:0.8rem; margin-bottom:1rem;'>마지막 리포트 생성 시간: {kst_time.strftime('%Y-%m-%d %H:%M:%S')}</div>", unsafe_allow_html=True)
    st.markdown("### 🎯 오늘의 스크리닝 요약")
    sample_data = pd.DataFrame({
        "종목명": ["삼성전자", "SK하이닉스", "LG에너지솔루션", "NAVER", "카카오", "현대차"],
        "현재가": [75000, 150000, 450000, 180000, 55000, 220000],
        "등락률": [0.025, -0.012, 0.038, 0.005, -0.021, 0.018],
        "국면": ["저점 이후 반등", "저점 매수 영역", "저점 이후 반등", "저점 매수 영역", "고점 이후 하락", "상승 추세"],
        "RS점수": [85, 92, 78, 65, 45, 88]
    })
    st.dataframe(sample_data, use_container_width=True, hide_index=True)

def page_kr_score(): st.title("💯 EMS스코어"); st.info("기능 개발 중입니다.")
def page_kr_sector(): st.title("📊 섹터 모니터링"); st.write("준비 중입니다.")
def page_kr_yield(): st.title("📈 섹터별 수익률"); st.write("준비 중입니다.")
def page_kr_screening(): st.title("🔍 종목 스크리닝"); st.write("준비 중입니다.")

def page_us_score(): st.title("💯 EMS스코어 (US)"); st.info("기능 개발 중입니다.")
def page_us_sector(): st.title("📊 섹터 모니터링 (US)"); st.write("준비 중입니다.")
def page_us_yield(): st.title("📈 섹터별 수익률 (US)"); st.write("준비 중입니다.")
def page_us_screening(): st.title("🔍 종목 스크리닝 (US)"); st.write("준비 중입니다.")


# -----------------------------------------------------------------------------
# [st.navigation 설정]
# -----------------------------------------------------------------------------

pg_home = st.Page(page_home, title="Home", icon="🏠", default=True)

pg_kr_1 = st.Page(page_kr_report, title="일일 리포트", icon="📄")
pg_kr_2 = st.Page(page_kr_score, title="EMS스코어", icon="💯")
pg_kr_3 = st.Page(page_kr_sector, title="섹터 모니터링", icon="📊")
pg_kr_4 = st.Page(page_kr_yield, title="섹터별 수익률", icon="📈")
pg_kr_5 = st.Page(page_kr_screening, title="종목 스크리닝", icon="🔍")

pg_us_1 = st.Page(page_us_score, title="EMS스코어 (US)", icon="💯")
pg_us_2 = st.Page(page_us_sector, title="섹터 모니터링 (US)", icon="📊")
pg_us_3 = st.Page(page_us_yield, title="섹터별 수익률 (US)", icon="📈")
pg_us_4 = st.Page(page_us_screening, title="종목 스크리닝 (US)", icon="🔍")

# [딕셔너리 구조] -> 이것이 '한국장', '미국장'이라는 섹션 헤더를 만듭니다.
pg = st.navigation({
    "Main": [pg_home],
    "한국장": [pg_kr_1, pg_kr_2, pg_kr_3, pg_kr_4, pg_kr_5],
    "미국장": [pg_us_1, pg_us_2, pg_us_3, pg_us_4]
})

pg.run()

# 푸터
st.sidebar.markdown("---")
current_year = datetime.now().year
st.sidebar.markdown(f"<div style='text-align: center; color: #888; font-size: 0.8rem;'>© {current_year} EMS QUANT AI. All rights reserved.</div>", unsafe_allow_html=True)
