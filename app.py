import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os
from PIL import Image

# =============================================================================
# [설정 영역]
# =============================================================================
# [버전 관리] v0.2.5 (화살표 자동화 및 메뉴명 영문 변경)
VER = "v0.2.5"

# [로고 크기 조절]
LOGO_WIDTH = 150
# =============================================================================


# 1. 페이지 설정
st.set_page_config(
    page_title="EMS QUANT AI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# [로고 이미지 처리]
# -----------------------------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
# [수정됨] 요청하신 logo2.png로 변경
logo_path = os.path.join(current_dir, "logo2.png") 

if os.path.exists(logo_path):
    try:
        image = Image.open(logo_path)
        aspect_ratio = image.height / image.width
        new_height = int(LOGO_WIDTH * aspect_ratio)
        resized_image = image.resize((LOGO_WIDTH, new_height), Image.Resampling.LANCZOS)
        st.logo(resized_image, icon_image=resized_image)
    except:
        pass


# 2. CSS 스타일링
st.markdown(f"""
<style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css');
    
    html, body, [class*="css"] {{
        font-family: 'Pretendard', 'Noto Sans KR', sans-serif;
    }}

    /* 상단 헤더, 푸터 숨김 */
    header {{visibility: visible !important; background: transparent !important;}}
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    
    /* ----------------------------------------------------------------------
       [1] 메인 타이틀 (EMS QUANT AI)
       ---------------------------------------------------------------------- */
    [data-testid="stSidebarNav"] {{
        padding-top: 0rem; 
    }}
    
    [data-testid="stSidebarNav"]::before {{
        content: "EMS QUANT AI";
        display: block;
        text-align: center; 
        
        font-size: 1.6rem;
        font-weight: 800;
        color: #0B1E31; 
        letter-spacing: -0.5px;
        
        margin-top: 10px; 
        margin-bottom: 35px;
    }}

    /* ----------------------------------------------------------------------
       [2] 메뉴 컨테이너 (ul) + [상단 회색 구분선]
       ---------------------------------------------------------------------- */
    div[data-testid="stSidebarNav"] > ul {{
        /* [수정됨] #g0g0g0(오타) -> #e0e0e0 (유효한 밝은 회색, 아래쪽 선과 통일) */
        border-top: 1px solid #e0e0e0; 
        padding-top: 20px;             
        position: relative;            
    }}

    /* ----------------------------------------------------------------------
       [3] 버전 뱃지 ({VER}) 
       ---------------------------------------------------------------------- */
    div[data-testid="stSidebarNav"] > ul::before {{
        content: "{VER}";
        position: absolute;  
        top: -38px;          /* 줄 바로 위, 타이틀 바로 아래 */
        left: 50%;           
        transform: translateX(-50%); 
        
        background-color: rgba(255, 255, 255, 0.7); 
        color: #46B1E1;                             
        
        padding: 2px 8px;    
        border-radius: 6px;   
        
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: 0.5px;
    }}

</style>
""", unsafe_allow_html=True)


# -----------------------------------------------------------------------------
# [페이지 함수 정의]
# -----------------------------------------------------------------------------

def page_home():
    col_title, col_info = st.columns([3, 2])
    with col_title:
        st.title("OVERVIEW")
    with col_info:
        kst_time = datetime.utcnow() + timedelta(hours=9)
        current_time_str = kst_time.strftime('%Y-%m-%d %H:%M:%S')
        
        st.markdown(f"""
<div style='text-align: right; padding-top: 1.5rem; color: #666; font-size: 0.8rem;'>
    <div>최종 업데이트: {current_time_str}</div>
</div>
""", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    # [수정됨] "↑ 12" -> "12"
    # 문자열에 화살표를 넣지 않아도, 양수면 Streamlit이 자동으로 초록색 화살표를 붙여줍니다.
    col1.metric("국내 증시 종목 수", "2,847", "12") 
    col2.metric("미국 증시 종목 수", "5,234", "45")
    col3.metric("오늘 거래량", "1.2조원", "5.3%")
    
    # "↑✓" 같은 특수기호는 자동생성이 안 되므로, 이런 경우엔 직접 넣는 게 맞습니다.
    # 하지만 보통은 "정상" 상태라면 delta를 안 쓰거나, 그냥 색상만 입히기도 합니다.
    # 여기서는 유지하겠습니다.
    col4.metric("시스템 상태", "정상", "✓") 
    
    st.subheader("🚀 빠른 접근")
    c1, c2, c3 = st.columns(3)
    if c1.button("📄 일일 리포트 바로가기", use_container_width=True):
        st.switch_page(kr_1)
    if c2.button("📊 섹터 모니터링 확인", use_container_width=True):
        st.switch_page(kr_3)
    if c3.button("🔍 종목 검색", use_container_width=True):
        st.switch_page(kr_5)
        
    st.subheader("📊 최근 활동")
    activity_data = pd.DataFrame({
        "시간": pd.date_range(start=datetime.now().date(), periods=5, freq="-1D"),
        "활동": ["국내 증시 데이터 업데이트", "미국 증시 분석 완료", "보고서 생성", "시스템 점검", "데이터 백업"],
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
# [네비게이션 설정]
# -----------------------------------------------------------------------------

# 1. 페이지 객체 생성
home_page = st.Page(page_home, title="Home", icon="🏠", default=True)

# KOR
kr_1 = st.Page(page_kr_report, title="일일 리포트", icon="📄")
kr_2 = st.Page(page_kr_score, title="EMS스코어", icon="💯")
kr_3 = st.Page(page_kr_sector, title="섹터 모니터링", icon="📊")
kr_4 = st.Page(page_kr_yield, title="섹터별 수익률", icon="📈")
kr_5 = st.Page(page_kr_screening, title="종목 스크리닝", icon="🔍")

# US
us_1 = st.Page(page_us_score, title="EMS스코어 (US)", icon="💯")
us_2 = st.Page(page_us_sector, title="섹터 모니터링 (US)", icon="📊")
us_3 = st.Page(page_us_yield, title="섹터별 수익률 (US)", icon="📈")
us_4 = st.Page(page_us_screening, title="종목 스크리닝 (US)", icon="🔍")

# 2. 딕셔너리 구조
pages = {
    "Main": [home_page],
    "KOR": [kr_1, kr_2, kr_3, kr_4, kr_5],
    "US": [us_1, us_2, us_3, us_4]
}

# 3. 실행
pg = st.navigation(pages)
pg.run()

# -----------------------------------------------------------------------------
# [하단 푸터 - 회색 선 통일]
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("""
        <div style="
            margin-top: 3rem; 
            padding-bottom: 1rem;
            border-top: 1px solid #e0e0e0; /* 상단 선과 100% 동일한 코드 */
        "></div>
    """, unsafe_allow_html=True)
    
    current_year = datetime.now().year
    st.markdown(f"<div style='text-align: center; color: #888; font-size: 0.8rem;'>© {current_year} EMS QUANT AI. All rights reserved.</div>", unsafe_allow_html=True)
