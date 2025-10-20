# 00지도.py
import streamlit as st
from streamlit_folium import st_folium
import folium
from folium.plugins import MarkerCluster

st.set_page_config(page_title="Seoul Top 10 (Foreigners)", layout="wide")

st.title("🇰🇷 서울 외국인 인기 관광지 Top 10 (Folium)")
st.markdown("지도에서 명소를 클릭하면 간단한 설명과 위치를 볼 수 있어요. 오른쪽 사이드바에서 표시 항목을 필터링할 수 있습니다.")

# Top 10 attractions list (name, lat, lon, short description)
ATTRACTIONS = [
    {
        "name": "Gyeongbokgung Palace (경복궁)",
        "lat": 37.580467,
        "lon": 126.976944,
        "desc": "조선의 대표 궁궐 — 근정전, 경회루 등 역사 명소."
    },
    {
        "name": "Changdeokgung Palace (창덕궁)",
        "lat": 37.579617,
        "lon": 126.991049,
        "desc": "유네스코 세계유산, 후원이 유명한 궁궐."
    },
    {
        "name": "N Seoul Tower (남산타워)",
        "lat": 37.551170,
        "lon": 126.988228,
        "desc": "서울 전경 감상 명소 — 야경과 전망대로 유명."
    },
    {
        "name": "Myeongdong (명동)",
        "lat": 37.560190,
        "lon": 126.986387,
        "desc": "쇼핑·스트리트푸드 허브 — 뷰티/패션 인기 스팟."
    },
    {
        "name": "Bukchon Hanok Village (북촌한옥마을)",
        "lat": 37.582178,
        "lon": 126.983256,
        "desc": "전통 한옥들이 밀집한 포토 스팟 — 산책하기 좋아요."
    },
    {
        "name": "Insadong (인사동)",
        "lat": 37.574411,
        "lon": 126.985045,
        "desc": "전통 공예품과 찻집이 많은 문화거리."
    },
    {
        "name": "Hongdae / Hongik University Area (홍대)",
        "lat": 37.555280,
        "lon": 126.923330,
        "desc": "젊음의 거리 — 스트리트 퍼포먼스, 카페, 클럽."
    },
    {
        "name": "Gangnam (강남)",
        "lat": 37.517235,
        "lon": 127.047325,
        "desc": "쇼핑·식사·한류 문화의 현대적 중심지."
    },
    {
        "name": "Dongdaemun Design Plaza (DDP, 동대문디자인플라자)",
        "lat": 37.566295,
        "lon": 127.009401,
        "desc": "독특한 건축과 야간 마켓 — 디자인 랜드마크."
    },
    {
        "name": "Hangang / Yeouido Hangang Park (한강·여의도)",
        "lat": 37.526040,
        "lon": 126.934994,
        "desc": "한강공원 — 여유로운 산책과 야경, 피크닉 명소."
    },
]

# Sidebar controls
st.sidebar.header("지도 옵션")
show_cluster = st.sidebar.checkbox("마커 클러스터 사용", value=True)
default_zoom = st.sidebar.slider("초기 확대(줌레벨)", min_value=11, max_value=16, value=12)
center_choice = st.sidebar.selectbox("지도 중심 위치", ["Seoul Center", "All Attractions", "Specific Attraction"])
if center_choice == "Seoul Center":
    center = (37.5665, 126.9780)  # 서울 중심(광화문/시청 근처)
elif center_choice == "All Attractions":
    lats = [a["lat"] for a in ATTRACTIONS]
    lons = [a["lon"] for a in ATTRACTIONS]
    center = (sum(lats)/len(lats), sum(lons)/len(lons))
else:
    names = [a["name"] for a in ATTRACTIONS]
    sel = st.sidebar.selectbox("명소 선택", names)
    sel_at = next(a for a in ATTRACTIONS if a["name"] == sel)
    center = (sel_at["lat"], sel_at["lon"])

# Map creation
m = folium.Map(location=center, zoom_start=default_zoom)

if show_cluster:
    marker_cluster = MarkerCluster().add_to(m)

for a in ATTRACTIONS:
    popup_html = f"<b>{a['name']}</b><br/>{a['desc']}<br/><a target='_blank' href='https://www.google.com/maps/search/?api=1&query={a['lat']},{a['lon']}'>길찾기 (Google Maps)</a>"
    marker = folium.Marker(
        location=(a["lat"], a["lon"]),
        popup=folium.Popup(popup_html, max_width=300),
        tooltip=a["name"]
    )
    if show_cluster:
        marker.add_to(marker_cluster)
    else:
        marker.add_to(m)

# Add a minimap (optional)
try:
    from folium.plugins import MiniMap
    minimap = MiniMap()
    m.add_child(minimap)
except Exception:
    pass

st.markdown("### 지도")
st_folium(m, width="100%", height=700)

st.markdown("---")
st.markdown("**데이터/출처(예시)**: VisitSeoul, TripAdvisor, Klook 등 관광 가이드/포털을 참고하여 Top10을 선정했습니다. (구체적 좌표는 공개 좌표/지도 데이터를 기반으로 합니다.)")
