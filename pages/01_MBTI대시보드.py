import streamlit as st
import pandas as pd
import plotly.express as px

# 앱 제목
st.set_page_config(page_title="🌏 국가별 MBTI 유형 분포", layout="wide")
st.title("🌏 국가별 MBTI 유형 분포 대시보드")
st.markdown("**국가를 선택하면 해당 나라의 16가지 MBTI 유형 비율을 시각화해줍니다.**")

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

# 국가 선택
country = st.selectbox("🔽 국가를 선택하세요", df["Country"].unique())

# 선택한 국가 데이터 추출
country_data = df[df["Country"] == country].drop(columns=["Country"]).T
country_data.columns = ["비율"]
country_data = country_data.reset_index().rename(columns={"index": "MBTI"})
country_data = country_data.sort_values(by="비율", ascending=False)

# 색상 설정 (1등은 빨간색, 나머지는 그라데이션)
colors = ["#ff4d4d" if i == 0 else px.colors.sequential.Reds[2 + i % 7] for i in range(len(country_data))]

# Plotly 막대 그래프
fig = px.bar(
    country_data,
    x="MBTI",
    y="비율",
    text=country_data["비율"].apply(lambda x: f"{x*100:.1f}%"),
    color="비율",
    color_continuous_scale="Reds",
)

# 1등 막대 강조 (빨간색으로)
fig.update_traces(
    marker=dict(color=colors),
    textposition="outside"
)

fig.update_layout(
    title=f"🇺🇳 {country}의 MBTI 유형별 비율",
    xaxis_title="MBTI 유형",
    yaxis_title="비율",
    template="plotly_white",
    height=600,
    coloraxis_showscale=False,
    margin=dict(l=40, r=40, t=60, b=40)
)

st.plotly_chart(fig, use_container_width=True)

# 부가 설명
st.markdown(
    f"""
    **{country}**의 MBTI 유형 분포를 살펴보면,  
    🔺 가장 높은 유형은 **{country_data.iloc[0]['MBTI']} ({country_data.iloc[0]['비율']*100:.1f}%)** 입니다.
    """
)
