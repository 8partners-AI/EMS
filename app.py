import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# [버전 관리] Ver: 36 (GitHub 'event-elo' 방식 적용 + 타이틀 상단 고정)
VER = 36

# 1. 페이지 설정
st.set_page_config(
    page_title="EMS QUANT AI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CSS 스타일링 (네비게이션 간섭 0%)
st.markdown("""
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
       [타이틀 상단 고정 전략]
       네비게이션(메뉴) 자체를 건드리는 CSS는 싹 다 뺐습니다. (순정 유지)
       대신 메뉴 전체를 아래로 80px 밀어버리고(margin-top),
       그 빈 공간에 타이틀을 '살포시' 얹었습니다.
       ---------------------------------------------------------------------- */
    
    /* 1. 네비게이션 메뉴를 아래로 80px 내리기 */
    [data-testid="stSidebarNav"] {
        margin-top: 80px !important;
    }

    /* 2. 빈 공간에 EMS QUANT AI 타이틀 넣기 */
    [data-testid="stSidebar"]::before {
        content: "EMS QUANT AI";
        position: absolute;
        top: 30px;
        left: 20px;
        width: calc(100% - 40px);
        
        font-size: 1.6rem;
        font-weight: 800;
        color: #1E3A8A; /* 진한 남색 */
        letter-spacing: -0.5px;
        
        padding-bottom: 20px;
        border-bottom: 1px solid #e0e0e0;
        z-index: 999;
    }

    /* [확인] 
       버튼 투명화, 화살표 수정 등 메뉴 스타일을 건드리는 CSS는 
       단 한 줄도 넣지 않았습니다. 이제 GitHub 예제처럼 완벽하게 작동할 겁니다.
    */
    
</style>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# [페이지 함수 정의]
# -----------------------------------------------------------------------------

def page_home():
    st.title("EMS OVERVIEW")
    st.write("메인 대시보드 화면입니다.")
    # (내용 생략 - 기존과 동일하게 사용하시면 됩니다)

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
# [네비게이션 설정] - GitHub 'event-elo' 방식 (딕셔너리 구조)
# -----------------------------------------------------------------------------

# 1. 페이지 객체 생성 (st.Page)
# 각 페이지를 연결하고 아이콘과 제목을 설정합니다.
home_page = st.Page(page_home, title="Home", icon="🏠", default=True)

# 한국장 페이지들
kr_1 = st.Page(page_kr_report, title="일일 리포트", icon="📄")
kr_2 = st.Page(page_kr_score, title="EMS스코어", icon="💯")
kr_3 = st.Page(page_kr_sector, title="섹터 모니터링", icon="📊")
kr_4 = st.Page(page_kr_yield, title="섹터별 수익률", icon="📈")
kr_5 = st.Page(page_kr_screening, title="종목 스크리닝", icon="🔍")

# 미국장 페이지들
us_1 = st.Page(page_us_score, title="EMS스코어 (US)", icon="💯")
us_2 = st.Page(page_us_sector, title="섹터 모니터링 (US)", icon="📊")
us_3 = st.Page(page_us_yield, title="섹터별 수익률 (US)", icon="📈")
us_4 = st.Page(page_us_screening, title="종목 스크리닝 (US)", icon="🔍")


# 2. 네비게이션 구조 정의 (딕셔너리 사용)
# [핵심] 이 딕셔너리 구조가 드롭다운 메뉴를 자동으로 만듭니다.
# "Main", "한국장", "미국장"이 각각의 섹션 헤더가 됩니다.
pages = {
    "Main": [home_page],
    "한국장": [kr_1, kr_2, kr_3, kr_4, kr_5],
    "미국장": [us_1, us_2, us_3, us_4]
}

# 3. 네비게이션 실행
pg = st.navigation(pages)
pg.run()

# -----------------------------------------------------------------------------
# [푸터]
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("<div style='margin-top: 3rem;'></div>", unsafe_allow_html=True)
    current_year = datetime.now().year
    st.markdown(f"<div style='text-align: center; color: #888; font-size: 0.8rem;'>© {current_year} EMS QUANT AI. All rights reserved.</div>", unsafe_allow_html=True)
