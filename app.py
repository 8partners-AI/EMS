import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# [버전 관리] Ver: 21 (섹션 헤더 '한국장/미국장' 강제 노출 복구)
VER = 21

# 1. 페이지 설정
st.set_page_config(
    page_title="EMS QUANT AI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CSS 스타일링
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
       [2] 메뉴 텍스트 및 기본 디자인
       ---------------------------------------------------------------------- */
    [data-testid="stSidebarNav"] span {
        font-size: 0.95rem;
        font-weight: 500;
        color: #555;
        padding-left: 5px;
    }
    
    [data-testid="stSidebarNav"] a[aria-current="page"] {
        background-color: transparent !important;
        color: #1E3A8A !important;
    }
    
    [data-testid="stSidebarNav"] a[aria-current="page"] span {
        color: #1E3A8A !important;
        font-weight: 800 !important;
    }

    [data-testid="stSidebarNav"] a:hover {
        background-color: rgba(0,0,0,0.03) !important;
    }

    /* ----------------------------------------------------------------------
       [3] ★ 섹션 헤더(한국장, 미국장) 강제 노출 및 화살표 디자인 ★
       여기가 핵심입니다. details > summary를 확실하게 꾸밉니다.
       ---------------------------------------------------------------------- */
       
    /* 1. 그룹 헤더 컨테이너 */
    [data-testid="stSidebarNav"] details {
        margin-bottom: 10px !important; /* 섹션 간 간격 */
    }

    /* 2. 요약(헤더) 부분 디자인 */
    [data-testid="stSidebarNav"] details > summary {
        display: flex !important;
        align-items: center !important;
        padding-left: 10px !important;  
        padding-top: 5px !important;
        padding-bottom: 5px !important;
        cursor: pointer;
        list-style: none !important; /* 기본 삼각형 제거 */
    }

    /* 3. 화살표 아이콘(SVG) - Ver 20의 성공 코드 */
    [data-testid="stSidebarNav"] details > summary svg {
        transform: scale(1.2) translateY(1px) !important;
        margin-right: 0.5rem !important;
        color: #555 !important; /* 색상 진하게 */
        stroke-width: 2px !important;
        vertical-align: middle !important;
        display: inline-block !important; /* 숨김 방지 */
        visibility: visible !important;   /* 숨김 방지 */
    }

    /* 4. [핵심 수정] 텍스트(한국장, 미국장) - 숨김 방지 및 스타일링 */
    [data-testid="stSidebarNav"] details > summary span {
        font-size: 0.85rem !important;
        font-weight: 700 !important; /* 굵게 */
        color: #444 !important;      /* 진한 회색 */
        text-transform: uppercase !important;
        display: inline-block !important; /* 숨김 방지 */
        visibility: visible !important;   /* 숨김 방지 */
        opacity: 1 !important;            /* 투명도 제거 */
    }

    /* 5. 구분선(Separator) 숨김 처리 */
    /* 혹시 이것 때문에 텍스트가 같이 사라졌을 수 있으니, 선택자를 아주 구체적으로 잡습니다 */
    div[data-testid="stSidebarNavSeparator"] {
        display: none !important;
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
