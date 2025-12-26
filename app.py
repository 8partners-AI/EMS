import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# [버전 관리] Ver: 7 (Hidden Navigation + Custom Sidebar)
VER = 7

# 1. 페이지 설정
st.set_page_config(
    page_title="EMS QUANT AI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. HTTP → HTTPS 리다이렉트 및 기본 스타일링
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
    
    /* 상단 헤더 숨김 (햄버거 메뉴는 유지됨) */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* 사이드바 스타일 깔끔하게 */
    [data-testid="stSidebar"] {
        background-color: #FAFAFA;
    }
    
    /* 드롭다운(Expander) 테두리 제거 - 깔끔한 텍스트 그룹처럼 보이게 */
    [data-testid="stSidebar"] [data-testid="stExpander"] {
        border: none !important;
        box-shadow: none !important;
        background-color: transparent !important;
    }
    
    /* Page Link 스타일 미세 조정 (기본적으로 깔끔하지만 간격 조정) */
    [data-testid="stSidebar"] [data-testid="stPageLink-NavLink"] {
        font-size: 0.9rem;
        padding-top: 0.3rem;
        padding-bottom: 0.3rem;
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# [1] 페이지 함수 정의 (내용은 그대로)
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
# [2] 페이지 객체 생성 (st.Page)
# -----------------------------------------------------------------------------
# 여기서 각 페이지의 '주소(URL)'와 '제목'을 정의합니다.

pg_home = st.Page(page_home, title="Home", icon="🏠", url_path="home")

# 한국장
pg_kr_1 = st.Page(page_kr_report, title="일일 리포트", icon="📄", url_path="kr_report")
pg_kr_2 = st.Page(page_kr_score, title="EMS스코어", icon="💯", url_path="kr_score")
pg_kr_3 = st.Page(page_kr_sector, title="섹터 모니터링", icon="📊", url_path="kr_sector")
pg_kr_4 = st.Page(page_kr_yield, title="섹터별 수익률", icon="📈", url_path="kr_yield")
pg_kr_5 = st.Page(page_kr_screening, title="종목 스크리닝", icon="🔍", url_path="kr_screening")

# 미국장
pg_us_1 = st.Page(page_us_score, title="EMS스코어 (US)", icon="💯", url_path="us_score")
pg_us_2 = st.Page(page_us_sector, title="섹터 모니터링 (US)", icon="📊", url_path="us_sector")
pg_us_3 = st.Page(page_us_yield, title="섹터별 수익률 (US)", icon="📈", url_path="us_yield")
pg_us_4 = st.Page(page_us_screening, title="종목 스크리닝 (US)", icon="🔍", url_path="us_screening")


# -----------------------------------------------------------------------------
# [3] 네비게이션 설정 (★핵심: position="hidden")
# -----------------------------------------------------------------------------
# 화면에 자동으로 그리지 말고(hidden), 기능만 활성화합니다.
pg = st.navigation(
    [pg_home, pg_kr_1, pg_kr_2, pg_kr_3, pg_kr_4, pg_kr_5, pg_us_1, pg_us_2, pg_us_3, pg_us_4],
    position="hidden" 
)


# -----------------------------------------------------------------------------
# [4] 사이드바 '수동' 조립 (여기가 진짜 화면을 만드는 곳)
# -----------------------------------------------------------------------------
# 여기서 st.page_link를 쓰면 '버튼'이 아니라 '깔끔한 텍스트 링크'가 됩니다.

with st.sidebar:
    # 1. 타이틀
    st.markdown("""
    <div style='font-size: 1.5rem; font-weight: 800; color: #1E3A8A; margin-bottom: 1rem; padding-left: 0.2rem; letter-spacing: -0.5px;'>
    EMS QUANT AI
    </div>
    """, unsafe_allow_html=True)
    
    # 2. 메인 메뉴
    st.markdown("<div style='font-size:0.75rem; font-weight:600; color:#999; margin-bottom:0.5rem; padding-left:0.5rem;'>메인 메뉴</div>", unsafe_allow_html=True)
    st.page_link(pg_home, label="Home", icon="🏠")
    
    st.markdown("<div style='margin-top:1rem;'></div>", unsafe_allow_html=True)

    # 3. 한국장 (드롭다운 + 깔끔한 링크)
    # expander를 썼으니 접었다 폈다 가능!
    with st.expander("🇰🇷 한국장", expanded=True):
        st.page_link(pg_kr_1, label="일일 리포트", icon="📄")
        st.page_link(pg_kr_2, label="EMS스코어", icon="💯")
        st.page_link(pg_kr_3, label="섹터 모니터링", icon="📊")
        st.page_link(pg_kr_4, label="섹터별 수익률", icon="📈")
        st.page_link(pg_kr_5, label="종목 스크리닝", icon="🔍")

    # 4. 미국장 (드롭다운 + 깔끔한 링크)
    with st.expander("🇺🇸 미국장", expanded=True):
        st.page_link(pg_us_1, label="EMS스코어 (US)", icon="💯")
        st.page_link(pg_us_2, label="섹터 모니터링 (US)", icon="📊")
        st.page_link(pg_us_3, label="섹터별 수익률 (US)", icon="📈")
        st.page_link(pg_us_4, label="종목 스크리닝 (US)", icon="🔍")


# -----------------------------------------------------------------------------
# [5] 앱 실행
# -----------------------------------------------------------------------------
pg.run()
