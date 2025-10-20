import streamlit as st

# MBTI별 진로 데이터
MBTI_CAREERS = {
    "ISTJ": [
        {
            "job": "공무원/행정직",
            "majors": "행정학, 법학, 경영학",
            "personality": "체계적이고 책임감 있는 사람에게 잘 맞아요. 꼼꼼하고 규칙을 잘 따르는 편이면 최고!",
            "emoji": "🏛️"
        },
        {
            "job": "회계/세무",
            "majors": "회계학, 경영학, 세무학",
            "personality": "숫자와 규칙을 좋아하고 정확한 작업을 선호하는 사람에게 추천해요.",
            "emoji": "📊"
        }
    ],
    "ISFJ": [
        {
            "job": "간호사/보건의료",
            "majors": "간호학, 보건학, 의료경영학",
            "personality": "남을 돌보고 배려하는 마음이 큰 사람에게 잘 맞아요. 안정감을 주는 성격이면 좋아요.",
            "emoji": "🩺"
        },
        {
            "job": "사회복지사",
            "majors": "사회복지학, 상담심리학",
            "personality": "사람을 돕는 데 보람을 느끼고 꾸준히 일할 수 있는 분께 추천합니다.",
            "emoji": "🤝"
        }
    ],
    "INFJ": [
        {
            "job": "상담심리사/임상심리",
            "majors": "심리학, 상담심리학",
            "personality": "사람의 마음을 잘 이해하고 깊이 있는 대화를 즐기는 분에게 좋아요.",
            "emoji": "🧠"
        },
        {
            "job": "작가/콘텐츠 크리에이터",
            "majors": "문예창작, 커뮤니케이션, 미디어학",
            "personality": "창의적이고 메시지를 전하는 걸 좋아하는 분께 잘 맞아요.",
            "emoji": "✍️"
        }
    ],
    "INTJ": [
        {
            "job": "연구원/데이터 과학자",
            "majors": "컴퓨터공학, 통계학, 수학",
            "personality": "전략적이고 문제 해결을 즐기는 사람에게 딱이에요. 혼자 깊게 몰입하는 걸 좋아하면 굿!",
            "emoji": "🔬"
        },
        {
            "job": "소프트웨어 엔지니어",
            "majors": "소프트웨어공학, 컴퓨터공학",
            "personality": "논리적 사고와 계획을 잘 세우는 분에게 추천해요.",
            "emoji": "💻"
        }
    ],
    "ISTP": [
        {
            "job": "기술/정비사",
            "majors": "기계공학, 전자공학, 산업시스템공학",
            "personality": "실용적이고 손재주 좋은 분에게 잘 맞아요. 직접 만지고 고치는 걸 좋아하면 굿.",
            "emoji": "🔧"
        },
        {
            "job": "파일럿/운송 관련",
            "majors": "항공운항학, 교통공학",
            "personality": "위기 대응 능력이 좋고 순간 판단을 잘하는 사람에게 추천합니다.",
            "emoji": "✈️"
        }
    ],
    "ISFP": [
        {
            "job": "디자이너/시각예술",
            "majors": "시각디자인, 예술학, 패션디자인",
            "personality": "감각적이고 표현을 좋아하는 분에게 어울려요. 자유로운 분위기에서 빛나요.",
            "emoji": "🎨"
        },
        {
            "job": "수의사/동물 관련",
            "majors": "수의학, 동물자원학",
            "personality": "동물을 사랑하고 섬세한 돌봄을 즐기는 분께 추천해요.",
            "emoji": "🐾"
        }
    ],
    "INFP": [
        {
            "job": "문예창작가/번역가",
            "majors": "문예창작, 영어영문학, 국어국문학",
            "personality": "내면이 풍부하고 창작을 통해 자기표현을 좋아하는 분에게 좋아요.",
            "emoji": "📚"
        },
        {
            "job": "인권/NGO 활동가",
            "majors": "국제관계, 사회복지, 국제개발",
            "personality": "가치 중심적이고 공감 능력이 뛰어난 분에게 추천합니다.",
            "emoji": "🌍"
        }
    ],
    "INTP": [
        {
            "job": "연구개발(R&D)/학자",
            "majors": "물리학, 수학, 컴퓨터공학",
            "personality": "호기심 많고 이론을 탐구하는 걸 좋아하는 분에게 잘 맞아요.",
            "emoji": "📐"
        },
        {
            "job": "시스템 아키텍트/소프트웨어 설계",
            "majors": "컴퓨터공학, 소프트웨어공학",
            "personality": "복잡한 시스템을 설계하는 일에 흥미가 있는 분께 추천해요.",
            "emoji": "🧩"
        }
    ],
    "ESTP": [
        {
            "job": "영업/마케팅",
            "majors": "경영학, 광고홍보학",
            "personality": "사교적이고 빠른 상황 판단을 잘하는 분에게 잘 맞아요.",
            "emoji": "🚀"
        },
        {
            "job": "이벤트 기획/현장 운영",
            "majors": "경영학, 관광학, 문화콘텐츠학",
            "personality": "즉흥적이고 사람을 모으는 걸 즐기는 분께 추천해요.",
            "emoji": "🎪"
        }
    ],
    "ESFP": [
        {
            "job": "연예/퍼포먼스",
            "majors": "공연예술학, 방송연예",
            "personality": "무대체질이고 사람들 앞에서 빛나는 걸 좋아하는 분에게 최고예요.",
            "emoji": "🎤"
        },
        {
            "job": "관광/서비스업",
            "majors": "관광경영, 호텔경영",
            "personality": "밝고 친근한 성격으로 사람을 대하는 일을 즐기는 분께 추천해요.",
            "emoji": "🏖️"
        }
    ],
    "ENFP": [
        {
            "job": "창업가/스타트업",
            "majors": "경영학, 창업학, 컴퓨터공학",
            "personality": "아이디어가 풍부하고 사람을 이끄는 걸 즐기는 분에게 좋아요.",
            "emoji": "💡"
        },
        {
            "job": "홍보/콘텐츠 제작",
            "majors": "미디어학, 광고홍보",
            "personality": "표현력 좋고 소통을 즐기는 분께 추천합니다.",
            "emoji": "📣"
        }
    ],
    "ENTP": [
        {
            "job": "제품기획/컨설턴트",
            "majors": "경영학, 산업공학, 경제학",
            "personality": "문제 해결과 토론을 즐기며 새로운 기회를 찾는 분에게 잘 맞아요.",
            "emoji": "🧠"
        },
        {
            "job": "변호사/논리적 직업",
            "majors": "법학, 정치외교학",
            "personality": "논리적이고 설득력 있는 의사소통을 즐기는 분께 추천합니다.",
            "emoji": "⚖️"
        }
    ],
    "ESTJ": [
        {
            "job": "관리자/사업 운영",
            "majors": "경영학, 회계학",
            "personality": "리더십 있고 조직을 이끄는 걸 좋아하는 분에게 추천해요.",
            "emoji": "🏢"
        },
        {
            "job": "금융/은행",
            "majors": "금융학, 경제학",
            "personality": "안정적이고 실무 중심적인 일을 선호하는 분께 잘 맞아요.",
            "emoji": "💼"
        }
    ],
    "ESFJ": [
        {
            "job": "교사/교육 관련",
            "majors": "교육학, 유아교육",
            "personality": "다른 사람을 돌보고 협력하는 걸 좋아하는 분에게 좋아요.",
            "emoji": "🍎"
        },
        {
            "job": "인사/조직관리",
            "majors": "경영학, 인적자원관리",
            "personality": "사람을 챙기고 분위기를 잘 관리하는 분께 추천합니다.",
            "emoji": "🧑‍🤝‍🧑"
        }
    ],
    "ENFJ": [
        {
            "job": "HR/리더십 코치",
            "majors": "경영학, 심리학",
            "personality": "사람을 이끌고 잠재력을 끌어내는 걸 즐기는 분에게 잘 맞아요.",
            "emoji": "🌟"
        },
        {
            "job": "PR/공공외교",
            "majors": "국제관계, 커뮤니케이션",
            "personality": "사교적이고 비전을 제시하는 걸 좋아하는 분께 추천합니다.",
            "emoji": "🗣️"
        }
    ],
    "ENTJ": [
        {
            "job": "경영진/전략기획",
            "majors": "경영학, 산업공학",
            "personality": "목표지향적이고 전략을 세우는 걸 좋아하는 리더형에게 적합해요.",
            "emoji": "🚩"
        },
        {
            "job": "투자/컨설팅",
            "majors": "금융학, 경제학",
            "personality": "결단력 있고 큰 그림을 보는 걸 좋아하는 분께 추천합니다.",
            "emoji": "📈"
        }
    ]
}


def main():
    st.set_page_config(page_title="MBTI 진로 추천 🎯", layout="centered")

    st.title("🎒 너에게 딱 맞는 MBTI 진로 추천")
    st.markdown("안녕! MBTI 하나 골라줘 — 그 유형에 어울리는 **진로 2개**랑 어떤 학과가 적합한지, 어떤 성격이 잘 맞는지도 알려줄게. 편하게 골라봐~ 😄")

    mbti_list = list(MBTI_CAREERS.keys())
    mbti = st.selectbox("MBTI 선택", options=mbti_list, index=0)

    if st.button("추천 보기 ✨"):
        careers = MBTI_CAREERS.get(mbti, [])
        st.subheader(f"{mbti} 유형을 위한 추천 진로 📌")
        for idx, c in enumerate(careers, start=1):
            st.markdown(f"### {idx}. {c['emoji']} {c['job']}")
            st.write(f"**추천 학과:** {c['majors']}")
            st.write(f"**어떤 성격이 잘 맞을까?** {c['personality']}")
            st.write("---")

        st.success("마음에 드는 진로가 있었어? 더 궁금하면 다른 MBTI도 골라봐~ 👍")

    st.info("📎 사용 설명: 상단에서 MBTI를 골라 '추천 보기' 버튼을 누르면 결과가 나와요. Streamlit 클라우드에 바로 올려서 테스트할 수 있어요.")

    st.caption("참고: MBTI는 성격을 이해하는 하나의 도구에요. 진로 선택은 여러 요소(흥미, 적성, 환경 등)를 함께 고려하는 게 좋아요!")


if __name__ == '__main__':
    main()
