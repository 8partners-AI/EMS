import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# [버전 관리] Ver: 8 (기능은 Ver 7 + 디자인은 Ver 5)
VER = 8

# 1. 페이지 설정
st.set_page_config(
    page_title="EMS QUANT AI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. HTTP → HTTPS 리다이렉트 및 CSS 스타일링
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
    
    /* 사이드바 배경 */
    [data-testid="stSidebar"] {
        background-color: #FAFAFA;
    }

    /* ----------------------------------------------------------------------
       [핵심] st.page_link 디자인 뜯어고치기 (Ongkoo 스타일)
       기본적인 버튼 모양(회색 박스)을 제거하고 텍스트처럼 만듭니다.
       ---------------------------------------------------------------------- */
    
    /* 1. 기본 링크 스타일: 투명 배경, 테두리 제거 */
    [data-testid="stPageLink-NavLink"] {
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
        color: #555 !important;
        text-align: left !important;
        font-size: 0.95rem !important;
        font-weight: 400 !important;
        padding: 0.3rem 0.5rem !important;
        margin: 0 !important;
        border-radius: 4px !important;
    }

    /* 2. 마우스 올렸을 때 (Hover) */
    [data-testid="stPageLink-NavLink"]:hover {
        background-color: rgba(0,0,0,0.03) !important;
        color: #000 !important;
        font-weight: 600 !important;
    }

    /* 3. [중요] 현재 보고 있는 페이지 (Active) 스타일 */
    /* aria-current="page" 속성을 감지하여 스타일 적용 */
    [data-testid="stPageLink-NavLink"][aria-current="page"] {
        background-color: transparent !important; /* 배경 투명 (요청사항) */
        color: #1E3A8A !important; /* 진한 남색 글씨 */
        font-weight: 800 !important;
        border-left: 3px solid #1E3A8A !important; /* 왼쪽에 파란 줄 */
        padding-left: calc(0.5rem - 3px) !important; /* 줄 두께만큼 보정 */
    }

    /* 4. 드롭다운(Expander) 테두리 제거 */
    [data-testid="stSidebar"] [data-testid="stExpander"] {
        border: none !important;
        box-shadow: none !important;
        background-color: transparent !important;
    }
    
    /* 드롭다운 헤더 */
    [data-testid="stSidebar"] .streamlit-expanderHeader {
        font-size: 0.9rem;
        font-weight: 600;
        color: #666;
        padding-left: 0.5rem;
        background-color: transparent !important;
    }
    
</style>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# [1] 페이지 함수 (컨텐츠) - 이전과 동일
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
    # switch_page를 사용하여 부드럽게 이동
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
# [2] 페이지 정의 (URL 및 제목)
# -----------------------------------------------------------------------------
pg_home = st.Page(page_home, title="Home", icon="🏠", url_path="home")

pg_kr_1 = st.Page(page_kr_report, title="일일 리포트", icon="📄", url_path="kr_report")
pg_kr_2 = st.Page(page_kr_score, title="EMS스코어", icon="💯", url_path="kr_score")
pg_kr_3 = st.Page(page_kr_sector, title="섹터 모니터링", icon="📊", url_path="kr_sector")
pg_kr_4 = st.Page(page_kr_yield, title="섹터별 수익률", icon="📈", url_path="kr_yield")
pg_kr_5 = st.Page(page_kr_screening, title="종목 스크리닝", icon="🔍", url_path="kr_screening")

pg_us_1 = st.Page(page_us_score, title="EMS스코어 (US)", icon="💯", url_path="us_score")
pg_us_2 = st.Page(page_us_sector, title="섹터 모니터링 (US)", icon="📊", url_path="us_sector")
pg_us_3 = st.Page(page_us_yield, title="섹터별 수익률 (US)", icon="📈", url_path="us_yield")
pg_us_4 = st.Page(page_us_screening, title="종목 스크리닝 (US)", icon="🔍", url_path="us_screening")

# -----------------------------------------------------------------------------
# [3] 네비게이션 숨김 처리 (기능만 활성화)
# -----------------------------------------------------------------------------
pg = st.navigation(
    [pg_home, pg_kr_1, pg_kr_2, pg_kr_3, pg_kr_4, pg_kr_5, pg_us_1, pg_us_2, pg_us_3, pg_us_4],
    position="hidden"
)

# -----------------------------------------------------------------------------
# [4] 커스텀 사이드바 구성 (Page Link + CSS 해킹 조합)
# -----------------------------------------------------------------------------
with st.sidebar:
    # 1. 타이틀
    st.markdown("""
    <div style='font-size: 1.5rem; font-weight: 800; color: #1E3A8A; margin-bottom: 1rem; padding-left: 0.2rem; letter-spacing: -0.5px;'>
    EMS QUANT AI
    </div>
    """, unsafe_allow_html=True)
    
    # 2. 메인 메뉴
    st.markdown("<div style='font-size:0.75rem; font-weight:600; color:#999; margin-bottom:0.5rem; padding-left:0.5rem;'>메인 메뉴</div>", unsafe_allow_html=True)
    
    # st.page_link는 기능적으로 완벽하며, 위의 CSS로 디자인을 덮어씌웠습니다.
    st.page_link(pg_home, label="Home", icon="🏠")
    
    st.markdown("<div style='margin-top:1rem;'></div>", unsafe_allow_html=True)

    # 3. 한국장 (드롭다운)
    with st.expander("🇰🇷 한국장", expanded=True):
        st.page_link(pg_kr_1, label="일일 리포트", icon="📄")
        st.page_link(pg_kr_2, label="EMS스코어", icon="💯")
        st.page_link(pg_kr_3, label="섹터 모니터링", icon="📊")
        st.page_link(pg_kr_4, label="섹터별 수익률", icon="📈")
        st.page_link(pg_kr_5, label="종목 스크리닝", icon="🔍")

    # 4. 미국장 (드롭다운)
    with st.expander("🇺🇸 미국장", expanded=True):
        st.page_link(pg_us_1, label="EMS스코어 (US)", icon="💯")
        st.page_link(pg_us_2, label="섹터 모니터링 (US)", icon="📊")
        st.page_link(pg_us_3, label="섹터별 수익률 (US)", icon="📈")
        st.page_link(pg_us_4, label="종목 스크리닝 (US)", icon="🔍")

# -----------------------------------------------------------------------------
# [5] 앱 실행
# -----------------------------------------------------------------------------
pg.run()
