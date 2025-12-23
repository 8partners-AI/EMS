import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import os
import sys

# 페이지 설정
st.set_page_config(
    page_title="회사 대시보드",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 사이드바 네비게이션
st.sidebar.title("📊 회사 대시보드")
st.sidebar.markdown("---")

# 페이지 선택
page = st.sidebar.selectbox(
    "페이지 선택",
    ["🏠 홈", "📈 데이터 분석", "📋 보고서", "⚙️ 설정"]
)

# 홈 페이지
if page == "🏠 홈":
    st.title("🏠 회사 대시보드 홈")
    st.markdown("---")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("총 사용자", "1,234", "↑ 12%")
    
    with col2:
        st.metric("활성 세션", "567", "↑ 5%")
    
    with col3:
        st.metric("데이터 처리량", "89.2GB", "↑ 8%")
    
    with col4:
        st.metric("시스템 상태", "정상", "✓")
    
    st.markdown("---")
    
    # 최근 활동
    st.subheader("📊 최근 활동")
    
    # 샘플 데이터
    activity_data = pd.DataFrame({
        "시간": pd.date_range(start="2024-01-01", periods=10, freq="D"),
        "활동": ["데이터 분석", "보고서 생성", "시스템 업데이트", "데이터 백업", 
                "사용자 로그인", "데이터 분석", "보고서 생성", "시스템 점검", 
                "데이터 분석", "보고서 생성"],
        "상태": ["완료", "완료", "완료", "완료", "완료", 
                "진행중", "완료", "완료", "완료", "완료"]
    })
    
    st.dataframe(activity_data, use_container_width=True, hide_index=True)

# 데이터 분석 페이지
elif page == "📈 데이터 분석":
    st.title("📈 데이터 분석")
    st.markdown("---")
    
    # 파일 업로드
    uploaded_file = st.file_uploader(
        "데이터 파일 업로드 (CSV, Excel)",
        type=['csv', 'xlsx', 'xls']
    )
    
    if uploaded_file is not None:
        try:
            # 파일 확장자에 따라 읽기
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            
            st.success(f"✅ 파일이 성공적으로 로드되었습니다! ({len(df)} 행)")
            
            # 데이터 미리보기
            st.subheader("📋 데이터 미리보기")
            st.dataframe(df.head(20), use_container_width=True)
            
            # 데이터 통계
            st.subheader("📊 데이터 통계")
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**기본 정보**")
                st.write(f"- 총 행 수: {len(df):,}")
                st.write(f"- 총 열 수: {len(df.columns)}")
                st.write(f"- 결측치: {df.isnull().sum().sum():,}")
            
            with col2:
                st.write("**데이터 타입**")
                dtype_df = pd.DataFrame({
                    "컬럼명": df.dtypes.index,
                    "데이터 타입": df.dtypes.values
                })
                st.dataframe(dtype_df, use_container_width=True, hide_index=True)
            
            # 수치형 데이터 통계
            numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
            if numeric_cols:
                st.subheader("📈 수치형 데이터 통계")
                st.dataframe(df[numeric_cols].describe(), use_container_width=True)
                
                # 차트 선택
                chart_type = st.selectbox(
                    "차트 유형 선택",
                    ["선 그래프", "막대 그래프", "히스토그램", "산점도"]
                )
                
                if chart_type == "선 그래프":
                    selected_col = st.selectbox("컬럼 선택", numeric_cols)
                    st.line_chart(df[selected_col])
                
                elif chart_type == "막대 그래프":
                    selected_col = st.selectbox("컬럼 선택", numeric_cols)
                    st.bar_chart(df[selected_col])
                
                elif chart_type == "히스토그램":
                    selected_col = st.selectbox("컬럼 선택", numeric_cols)
                    st.hist_chart(df[selected_col])
                
                elif chart_type == "산점도":
                    x_col = st.selectbox("X축 컬럼", numeric_cols)
                    y_col = st.selectbox("Y축 컬럼", numeric_cols)
                    if x_col != y_col:
                        st.scatter_chart(df[[x_col, y_col]])
        
        except Exception as e:
            st.error(f"❌ 파일 로드 중 오류가 발생했습니다: {str(e)}")
    else:
        st.info("👆 위에서 데이터 파일을 업로드해주세요.")

# 보고서 페이지
elif page == "📋 보고서":
    st.title("📋 보고서")
    st.markdown("---")
    
    # 보고서 생성 섹션
    st.subheader("📄 보고서 생성")
    
    report_type = st.selectbox(
        "보고서 유형 선택",
        ["일일 보고서", "주간 보고서", "월간 보고서", "사용자 정의 보고서"]
    )
    
    date_range = st.date_input(
        "기간 선택",
        value=(datetime.now().date(), datetime.now().date()),
        max_value=datetime.now().date()
    )
    
    if st.button("📊 보고서 생성"):
        with st.spinner("보고서를 생성하는 중..."):
            # 여기에 실제 보고서 생성 로직 추가
            st.success("✅ 보고서가 성공적으로 생성되었습니다!")
            
            # 샘플 보고서 데이터
            sample_report = pd.DataFrame({
                "항목": ["매출", "비용", "순이익", "고객 수", "주문 수"],
                "값": [1000000, 500000, 500000, 1500, 3200],
                "변화율": ["+10%", "-5%", "+15%", "+8%", "+12%"]
            })
            
            st.dataframe(sample_report, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # 저장된 보고서 목록
    st.subheader("📁 저장된 보고서")
    
    # 샘플 보고서 목록
    reports = [
        {"이름": "2024년 1월 보고서", "생성일": "2024-01-31", "유형": "월간 보고서"},
        {"이름": "2024년 2월 보고서", "생성일": "2024-02-29", "유형": "월간 보고서"},
        {"이름": "2024년 3월 보고서", "생성일": "2024-03-31", "유형": "월간 보고서"},
    ]
    
    reports_df = pd.DataFrame(reports)
    st.dataframe(reports_df, use_container_width=True, hide_index=True)

# 설정 페이지
elif page == "⚙️ 설정":
    st.title("⚙️ 설정")
    st.markdown("---")
    
    # 사용자 설정
    st.subheader("👤 사용자 설정")
    
    username = st.text_input("사용자 이름", value="관리자")
    email = st.text_input("이메일", value="admin@company.com")
    language = st.selectbox("언어", ["한국어", "English", "日本語"])
    
    if st.button("💾 설정 저장"):
        st.success("✅ 설정이 저장되었습니다!")
    
    st.markdown("---")
    
    # 시스템 설정
    st.subheader("🔧 시스템 설정")
    
    auto_refresh = st.checkbox("자동 새로고침", value=False)
    if auto_refresh:
        refresh_interval = st.slider("새로고침 간격 (초)", 10, 300, 60)
    
    theme = st.selectbox("테마", ["라이트", "다크", "시스템 기본값"])
    
    st.markdown("---")
    
    # 정보
    st.subheader("ℹ️ 시스템 정보")
    st.write(f"- Streamlit 버전: {st.__version__}")
    st.write(f"- Python 버전: {sys.version}")
    st.write(f"- 현재 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# 푸터
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray;'>
        <p>© 2024 회사 대시보드. All rights reserved.</p>
    </div>
    """,
    unsafe_allow_html=True
)
