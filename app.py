import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# [버전 관리] Ver: 37 (Event-Elo 순정 구조 + Ver 10 타이틀 결합)
VER = 37

# 1. 페이지 설정
st.set_page_config(
    page_title="EMS QUANT AI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CSS 스타일링
# [핵심] 버튼, 화살표, 폰트 관련 CSS는 싹 다 지웠습니다. (순정 유지)
# 오직 'EMS QUANT AI' 타이틀을 넣는 코드만 Ver 10 방식으로 넣었습니다.
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
       [타이틀 삽입 - Ver 10 방식 복구]
       position: absolute (공중부양) -> X (메뉴 겹침 원인)
       display: block (벽돌쌓기) -> O (메뉴를 자연스럽게 아래로 밀어냄)
       ---------------------------------------------------------------------- */
    [data-testid="stSidebarNav"]::before {
        content: "EMS QUANT AI";
        display: block;  /* 블록 요소로 만들어서 메뉴를 아래로 밀어냅니다 */
        
        font-size: 1.6rem;
        font-weight: 800;
        color: #1E3A8A; /* 진한 남색 */
        letter-spacing: -0.5px;
        
        /* 위치 및 간격 조정 */
        margin-left: 20px;
        margin-top: 20px;
        margin-bottom: 20px;
        padding-bottom: 10px;
        border-bottom: 1px solid #e0e0e0;
    }

    /* [약속] 네비게이션 버튼, 화살표, 드롭다운 관련 CSS는 0줄입니다. */

</style>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# [페이지 함수 정의]
# -----------------------------------------------------------------------------

def page_home():
    st.title("EMS OVERVIEW")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("한국장 종목 수", "2,847", "↑ 12")
    col2.metric("미국장 종목 수", "5,234", "↑ 45")
    col3.metric("오늘 거래량", "1.2조원", "↑ 5.3%")
    col4.metric("시스템 상태", "정상", "✓")
    
    st.subheader("🚀 빠른 접근")
    c1, c2, c3 = st.columns(3)
    if c1.button("📄 일일 리포트 바로가기", use_container_width=True):
        st.switch_page(kr_1)
    if c2.button("📊 섹터 모니터링 확인", use_container_width=True):
        st.switch_page(kr_3)
    if c3.button("🔍 종목 검색", use_container_width=True):
        st.switch_page(kr_5)

def page_kr_report(): st.title("📋 일일 리포트"); st.write("한국장 분석 리포트입니다.")
def page_kr_score(): st.title("💯 EMS스코어"); st.info("준비 중")
def page_kr_sector(): st.title("📊 섹터 모니터링"); st.write("준비 중")
def page_kr_yield(): st.title("📈 섹터별 수익률"); st.write("준비 중")
def page_kr_screening(): st.title("🔍 종목 스크리닝"); st.write("준비 중")

def page_us_score(): st.title("💯 EMS스코어 (US)"); st.info("준비 중")
def page_us_sector(): st.title("📊 섹터 모니터링 (US)"); st.write("준비 중")
def page_us_yield(): st.title("📈 섹터별 수익률 (US)"); st.write("준비 중")
def page_us_screening(): st.title("🔍 종목 스크리닝 (US)"); st.write("준비 중")


# -----------------------------------------------------------------------------
# [네비게이션 설정] - GitHub 'event-elo' 방식 (Native Dictionary)
# -----------------------------------------------------------------------------

# 1. 페이지 객체 생성
home_page = st.Page(page_home, title="Home", icon="🏠", default=True)

# 한국장
kr_1 = st.Page(page_kr_report, title="일일 리포트", icon="📄")
kr_2 = st.Page(page_kr_score, title="EMS스코어", icon="💯")
kr_3 = st.Page(page_kr_sector, title="섹터 모니터링", icon="📊")
kr_4 = st.Page(page_kr_yield, title="섹터별 수익률", icon="📈")
kr_5 = st.Page(page_kr_screening, title="종목 스크리닝", icon="🔍")

# 미국장
us_1 = st.Page(page_us_score, title="EMS스코어 (US)", icon="💯")
us_2 = st.Page(page_us_sector, title="섹터 모니터링 (US)", icon="📊")
us_3 = st.Page(page_us_yield, title="섹터별 수익률 (US)", icon="📈")
us_4 = st.Page(page_us_screening, title="종목 스크리닝 (US)", icon="🔍")

# 2. 딕셔너리로 그룹화 (드롭다운 자동 생성)
pages = {
    "Main": [home_page],
    "한국장": [kr_1, kr_2, kr_3, kr_4, kr_5],
    "미국장": [us_1, us_2, us_3, us_4]
}

# 3. 실행
pg = st.navigation(pages)
pg.run()

# [하단 푸터]
with st.sidebar:
    st.markdown("<div style='margin-top: 3rem;'></div>", unsafe_allow_html=True)
    current_year = datetime.now().year
    st.markdown(f"<div style='text-align: center; color: #888; font-size: 0.8rem;'>© {current_year} EMS QUANT AI. All rights reserved.</div>", unsafe_allow_html=True)
