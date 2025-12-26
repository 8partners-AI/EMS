import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# 1. 페이지 설정 (반드시 가장 먼저 와야 함 - 에러 해결 핵심)
st.set_page_config(
    page_title="EMS QUANT AI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. HTTP → HTTPS 자동 리다이렉트 (설정 직후 배치)
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

# 3. CSS 스타일링 (메뉴바 사라짐 해결)
st.markdown("""
<style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css');
    
    /* 전체 폰트 적용 */
    html, body, [class*="css"] {
        font-family: 'Pretendard', 'Noto Sans KR', sans-serif !important;
    }
    
    /* [수정됨] 헤더를 숨기지 않음 (햄버거 메뉴 살리기) */
    /* header {visibility: hidden;}  <-- 이 줄이 문제였습니다 */
    
    #MainMenu {visibility: hidden;} /* 우측 상단 점 3개 메뉴는 숨김 (선택사항) */
    footer {visibility: hidden;}    /* 하단 Made with Streamlit 숨김 */
    
    /* 사이드바 스타일 */
    [data-testid="stSidebar"] {
        background-color: #f8f9fa;
    }
    
    /* Expander 스타일 깔끔하게 */
    .streamlit-expanderHeader {
        font-weight: 600 !important;
        background-color: transparent !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 사이드바 구성 ---
st.sidebar.markdown("""
<div style='font-size: 1.5rem; font-weight: 700; color: #1E3A8A; margin-bottom: 1.5rem; padding-left: 0.5rem;'>
EMS QUANT AI
</div>
""", unsafe_allow_html=True)

# 세션 상태 초기화
if 'selected_page' not in st.session_state:
    st.session_state.selected_page = "🏠 Home"

# 메인 메뉴 버튼
if st.sidebar.button("🏠 Home", use_container_width=True, type="secondary"):
    st.session_state.selected_page = "🏠 Home"
    st.rerun()

# 한국장 메뉴
with st.sidebar.expander("🇰🇷 한국장", expanded=True):
    kr_items = ["📄 일일 리포트", "💯 EMS스코어", "📊 섹터 모니터링", "📈 섹터별 수익률", "🔍 종목 스크리닝"]
    for item in kr_items:
        if st.button(item, use_container_width=True, key=f"kr_{item}", 
                     type="primary" if st.session_state.selected_page == item else "secondary"):
            st.session_state.selected_page = item
            st.rerun()

# 미국장 메뉴
with st.sidebar.expander("🇺🇸 미국장", expanded=True):
    us_items = ["💯 EMS스코어 (US)", "📊 섹터 모니터링 (US)", "📈 섹터별 수익률 (US)", "🔍 종목 스크리닝 (US)"]
    for item in us_items:
        if st.button(item, use_container_width=True, key=f"us_{item}",
                     type="primary" if st.session_state.selected_page == item else "secondary"):
            st.session_state.selected_page = item
            st.rerun()

# --- 메인 컨텐츠 로직 ---
menu = st.session_state.selected_page

# 1. Home 페이지
if menu == "🏠 Home":
    st.title("EMS OVERVIEW")
    st.markdown(f"<div style='text-align: right; color: gray;'>최종 업데이트: {datetime.now().strftime('%Y-%m-%d %H:%M')}</div>", unsafe_allow_html=True)
    st.markdown("---")

    # 지표 카드
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("한국장 종목", "2,847", "↑ 12")
    col2.metric("미국장 종목", "5,234", "↑ 45")
    col3.metric("거래 대금", "1.2조", "↑ 5.3%")
    col4.metric("시스템", "정상", "OK")

    st.subheader("🚀 빠른 접근")
    c1, c2, c3 = st.columns(3)
    if c1.button("📄 오늘의 리포트 보러가기", use_container_width=True):
        st.session_state.selected_page = "📄 일일 리포트"
        st.rerun()
    if c2.button("📊 섹터 동향 확인", use_container_width=True):
        st.session_state.selected_page = "📊 섹터 모니터링"
        st.rerun()
    if c3.button("🔍 종목 찾기", use_container_width=True):
        st.session_state.selected_page = "🔍 종목 스크리닝"
        st.rerun()

# 2. 일일 리포트 (핵심 기능 리팩토링)
elif menu == "📄 일일 리포트":
    st.title("📋 일일 섹터 및 종목 분석 리포트")
    st.markdown("---")
    
    st.markdown("### 🎯 오늘의 스크리닝 요약")
    
    # 샘플 데이터 생성
    data = {
        "종목명": ["삼성전자", "SK하이닉스", "LG에너지솔루션", "에코프로", "현대차", "카카오"],
        "현재가": [75000, 150000, 450000, 650000, 220000, 55000],
        "등락률": [0.025, -0.012, 0.038, 0.154, 0.018, -0.021], # 퍼센트 계산을 위해 소수로 변경
        "거래량": [12500000, 3500000, 850000, 2100000, 1200000, 5800000],
        "국면": ["저점 이후 반등", "저점 매수 영역", "저점 이후 반등", "상승 추세", "저점 매수 영역", "고점 이후 하락"],
        "RS점수": [85, 92, 78, 96, 88, 45] # 점수 추가
    }
    df = pd.DataFrame(data)

    # [중요] 최신 Streamlit 기능을 사용한 표 꾸미기 (HTML 인젝션보다 훨씬 안정적이고 예쁨)
    st.dataframe(
        df,
        column_config={
            "종목명": st.column_config.TextColumn("종목명", width="medium"),
            "현재가": st.column_config.NumberColumn("현재가", format="%d원"),
            "등락률": st.column_config.NumberColumn(
                "등락률",
                format="%.2f%%", # 퍼센트 포맷
                help="전일 대비 등락률입니다."
            ),
            "거래량": st.column_config.NumberColumn("거래량", format="%d주"),
            "국면": st.column_config.TextColumn("시장 국면", width="medium"),
            "RS점수": st.column_config.ProgressColumn(
                "RS 강도",
                format="%d",
                min_value=0,
                max_value=100,
            ),
        },
        use_container_width=True,
        hide_index=True
    )
    
    # 국면별 색상 가이드 (범례)
    st.info("💡 **국면 가이드**: '저점 이후 반등'은 추세 전환 초기, '저점 매수 영역'은 분할 매수 유효 구간을 의미합니다.")

# 3. 섹터 모니터링
elif menu == "📊 섹터 모니터링":
    st.title("📊 섹터 모니터링")
    
    # 샘플 데이터
    sector_df = pd.DataFrame({
        "업종": ["반도체", "2차전지", "IT서비스", "자동차", "바이오"],
        "수익률": [5.2, 3.8, 2.1, 2.8, -1.2],
        "종목수": [45, 32, 28, 25, 52]
    })
    
    c1, c2 = st.columns([1, 2])
    with c1:
        st.dataframe(sector_df, hide_index=True, use_container_width=True)
    with c2:
        st.bar_chart(sector_df.set_index("업종")["수익률"])

# 4. 나머지 페이지들 (Placeholder)
else:
    st.title(f"{menu}")
    st.warning(f"🚧 '{menu}' 페이지는 현재 개발 중입니다.")
    st.write("데이터 연동 작업이 진행 중입니다.")
