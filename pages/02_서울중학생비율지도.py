import streamlit as st
import folium
from streamlit_folium import st_folium
import plotly.graph_objects as go
import pandas as pd

# -------------------------------
# 서울시 자치구별 중학생 수 (가상 데이터)
# -------------------------------
data = {
    "지역": ["강남구", "송파구", "강서구", "노원구", "관악구", "은평구", "강동구", "성북구", "도봉구", "구로구"],
    "위도": [37.5172, 37.5145, 37.5509, 37.6543, 37.4784, 37.6176, 37.5301, 37.5894, 37.6688, 37.4954],
    "경도": [127.0473, 127.1066, 126.8495, 127.0568, 126.9516, 126.9227, 127.1238, 127.0182, 127.0463, 126.8877],
    "남학생": [5200, 4900, 4700, 4600, 4400, 4200, 4100, 4000, 3800, 3700],
    "여학생": [5000, 4800, 4600, 4500, 4300, 4100, 4000, 3900, 3700, 3600]
}

df = pd.DataFrame(data)
df["총합"] = df["남학생"] + df["여학생"]

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="서울 중학생 분포", layout="wide")
st.title("📊 서울시 중학생 분포 및 남녀 비율 지도")

# -------------------------------
# 지도 생성 (Folium)
# -------------------------------
m = folium.Map(location=[37.55, 126.98], zoom_start=11)

for _, row in df.iterrows():
    popup_text = (
        f"<b>{row['지역']}</b><br>"
        f"총 중학생 수: {row['총합']:,}명<br>"
        f"남학생: {row['남학생']:,}명<br>"
        f"여학생: {row['여학생']:,}명"
    )
    folium.CircleMarker(
        location=[row["위도"], row["경도"]],
        radius=10,
        color="blue",
        fill=True,
        fill_opacity=0.6,
        popup=popup_text,
    ).add_to(m)

st.subheader("🗺️ 서울시 중학생 Top10 지도")
st_folium(m, width=700, height=500)

# -------------------------------
# 지역 선택 및 Plotly 시각화
# -------------------------------
st.subheader("📈 지역별 남녀 비율 보기")

selected_region = st.selectbox("지역을 선택하세요:", df["지역"])

region_data = df[df["지역"] == selected_region].iloc[0]

fig = go.Figure(
    data=[
        go.Pie(
            labels=["남학생", "여학생"],
            values=[region_data["남학생"], region_data["여학생"]],
            marker=dict(colors=["#3A7BD5", "#FF8FAB"]),  # 파랑/핑크
            hole=0.3,
        )
    ]
)

fig.update_layout(
    title=f"{selected_region} 남녀 중학생 비율",
    title_x=0.5,
    font=dict(size=14),
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------------
# 전체 요약 테이블
# -------------------------------
st.subheader("📋 서울시 중학생 수 요약 (Top10)")
st.dataframe(df[["지역", "남학생", "여학생", "총합"]].set_index("지역"))
