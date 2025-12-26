import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# [버전 관리] Ver: 6 (순정 네비게이션 + 타이틀 상단 고정)
VER = 6

# 1. 페이지 설정
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

# 3. [핵심] CSS 스타일링: 순정 네비게이션 사용 + 타이틀 강제 삽입
st.markdown("""
<style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css');
    
    html, body, [class*="css"] {
        font-family: 'Pretendard', 'Noto Sans KR', sans-serif;
    }

    /* 상단 헤더, 푸터, 3점 메뉴 숨김 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* ----------------------------------------------------------------------
       [타이틀 위치 해결 매직] 
       순정 네비게이션(stSidebarNav)의 머리 위에 
       "EMS QUANT AI" 타이틀을 CSS 가상 요소(::before)로 심어버립니다.
       이렇게 하면 로직상 네비게이션이 최상단이어도, 시각적으로는 타이틀이 위에 옵니다.
       ---------------------------------------------------------------------- */
    
    [data-testid="stSidebarNav"]::before {
        content: "EMS QUANT AI";
        display: block;
        font-size: 1.5rem;
        font-weight: 800;
        color: #1E3A8A; /* 진한 남색 */
        margin-bottom: 1.5rem;
        margin-top: 1rem;
        padding-left: 1.2rem; /* 메뉴 텍스트 라인과 맞춤 */
        letter-spacing: -0.5px;
    }

    /* 네비게이션 텍스트 스타일 미세 조정 */
    [data-testid="stSidebarNav"] span {
        font-size: 0.95rem;
        font-weight: 500;
        color: #4B5563;
    }

</style>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# [페이지 함수 정의] - 각 메뉴를 클릭했을 때 보여줄 화면들
# -----------------------------------------------------------------------------

def page_home():
    col_title, col_info = st.columns([3, 2])
    with col_title:
        st.title("EMS OVERVIEW")
    with col_info:
        # 시간: KST 적용
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
    # switch_page 함수는 st.navigation 구조에서 페이지 이동을 담당합니다.
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
    st.dataframe(
        sample_data,
        column_config={
            "종목명": st.column_config.TextColumn("종목명", width="medium"),
            "현재가": st.column_config.NumberColumn("현재가", format="%d원"),
            "등락률": st.column_config.NumberColumn("등락률", format="%.2f%%"),
            "국면": st.column_config.TextColumn("시장 국면", width="medium"),
            "RS점수": st.column_config.ProgressColumn("RS 강도", format="%d", min_value=0, max_value=100),
        },
        use_container_width=True,
        hide_index=True
    )

def page_kr_score():
    st.title("💯 EMS스코어")
    st.info("EMS스코어 기능 개발 중입니다.")

def page_kr_sector():
    st.title("📊 섹터 모니터링")
    st.write("섹터별 데이터를 준비 중입니다.")

def page_kr_yield():
    st.title("📈 섹터별 수익률")
    st.write("수익률 차트를 준비 중입니다.")

def page_kr_screening():
    st.title("🔍 종목 스크리닝")
    st.write("검색 기능을 준비 중입니다.")

def page_us_score():
    st.title("💯 EMS스코어 (US)")
    st.info("미국장 데이터 연동 중입니다.")

def page_us_sector():
    st.title("📊 섹터 모니터링 (US)")
    st.write("미국 섹터 데이터 준비 중입니다.")

def page_us_yield():
    st.title("📈 섹터별 수익률 (US)")
    st.write("미국 수익률 차트 준비 중입니다.")

def page_us_screening():
    st.title("🔍 종목 스크리닝 (US)")
    st.write("미국 종목 검색 준비 중입니다.")


# -----------------------------------------------------------------------------
# [핵심] st.navigation 설정 (질문자님이 원하시던 '유령 메뉴' 활성화)
# -----------------------------------------------------------------------------

# 페이지 정의 (st.Page)
pg_home = st.Page(page_home, title="Home", icon="🏠", default=True)

# 한국장 페이지들
pg_kr_1 = st.Page(page_kr_report, title="일일 리포트", icon="📄")
pg_kr_2 = st.Page(page_kr_score, title="EMS스코어", icon="💯")
pg_kr_3 = st.Page(page_kr_sector, title="섹터 모니터링", icon="📊")
pg_kr_4 = st.Page(page_kr_yield, title="섹터별 수익률", icon="📈")
pg_kr_5 = st.Page(page_kr_screening, title="종목 스크리닝", icon="🔍")

# 미국장 페이지들
pg_us_1 = st.Page(page_us_score, title="EMS스코어 (US)", icon="💯")
pg_us_2 = st.Page(page_us_sector, title="섹터 모니터링 (US)", icon="📊")
pg_us_3 = st.Page(page_us_yield, title="섹터별 수익률 (US)", icon="📈")
pg_us_4 = st.Page(page_us_screening, title="종목 스크리닝 (US)", icon="🔍")

# 네비게이션 그룹핑 (섹션 헤더가 자동으로 드롭다운/구분자 역할을 합니다)
pg = st.navigation({
    "메인 메뉴": [pg_home],
    "한국장": [pg_kr_1, pg_kr_2, pg_kr_3, pg_kr_4, pg_kr_5],
    "미국장": [pg_us_1, pg_us_2, pg_us_3, pg_us_4]
})

# 앱 실행
pg.run()

# 푸터
st.sidebar.markdown("---")
current_year = datetime.now().year
st.sidebar.markdown(f"<div style='text-align: center; color: #888; font-size: 0.8rem;'>© {current_year} EMS QUANT AI. All rights reserved.</div>", unsafe_allow_html=True)
