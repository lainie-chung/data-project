import streamlit as st
import random

# MBTI별 진로 및 과목 데이터
MBTI_DATA = {
    "ISTJ": {
        "careers": [
            {"job": "공무원/행정직", "majors": "행정학, 법학, 경영학", "personality": "체계적이고 책임감 있는 사람에게 잘 맞아요. 꼼꼼하고 규칙을 잘 따르는 편이면 최고!", "emoji": "🏛️"},
            {"job": "회계/세무", "majors": "회계학, 경영학, 세무학", "personality": "숫자와 규칙을 좋아하고 정확한 작업을 선호하는 사람에게 추천해요.", "emoji": "📊"}
        ],
        "good_subjects": ["수학", "사회"],
        "weak_subjects": ["미술", "음악"],
        "tips": "공부 계획표를 만들어 꾸준히 실천해봐요. 계획적인 공부가 최고의 무기예요! 🗓️"
    },
    "ISFJ": {
        "careers": [
            {"job": "간호사/보건의료", "majors": "간호학, 보건학, 의료경영학", "personality": "남을 돌보고 배려하는 마음이 큰 사람에게 잘 맞아요.", "emoji": "🩺"},
            {"job": "사회복지사", "majors": "사회복지학, 상담심리학", "personality": "사람을 돕는 데 보람을 느끼는 분께 추천합니다.", "emoji": "🤝"}
        ],
        "good_subjects": ["도덕", "사회"],
        "weak_subjects": ["체육", "수학"],
        "tips": "도움을 주는 일에서 힘을 얻는 타입! 친구랑 함께 공부하면 집중이 잘 될 거예요 💬"
    },
    "INFJ": {
        "careers": [
            {"job": "상담심리사/임상심리", "majors": "심리학, 상담심리학", "personality": "사람의 마음을 잘 이해하는 분에게 좋아요.", "emoji": "🧠"},
            {"job": "작가/콘텐츠 크리에이터", "majors": "문예창작, 커뮤니케이션", "personality": "창의적이고 메시지를 전하는 걸 좋아하는 분께 잘 맞아요.", "emoji": "✍️"}
        ],
        "good_subjects": ["국어", "도덕"],
        "weak_subjects": ["수학", "체육"],
        "tips": "조용한 공간에서 집중 공부하기가 좋아요. 감정이입이 강하니 휴식도 잊지 말아요 🌿"
    },
    "INTJ": {
        "careers": [
            {"job": "연구원/데이터 과학자", "majors": "컴퓨터공학, 통계학", "personality": "전략적이고 문제 해결을 즐기는 사람에게 딱이에요.", "emoji": "🔬"},
            {"job": "소프트웨어 엔지니어", "majors": "소프트웨어공학, 컴퓨터공학", "personality": "논리적 사고를 잘하는 분에게 추천해요.", "emoji": "💻"}
        ],
        "good_subjects": ["수학", "과학"],
        "weak_subjects": ["미술", "음악"],
        "tips": "목표를 세우면 끝까지 밀어붙이는 타입! 복습 루틴을 만들면 완벽해요 🔁"
    },
    "ISTP": {
        "careers": [
            {"job": "기계공학자/자동차 정비", "majors": "기계공학, 자동차공학", "personality": "손으로 직접 무언가 만드는 걸 좋아한다면 최고예요!", "emoji": "🔧"},
            {"job": "파일럿/항공 관련", "majors": "항공운항학, 항공기계학", "personality": "침착하고 판단력 있는 사람에게 어울려요.", "emoji": "✈️"}
        ],
        "good_subjects": ["과학", "기술가정"],
        "weak_subjects": ["국어", "도덕"],
        "tips": "실습 위주의 공부나 프로젝트가 잘 맞아요. 직접 해보면서 배우면 기억에 쏙쏙! 🧩"
    },
    "ISFP": {
        "careers": [
            {"job": "디자이너/시각예술", "majors": "시각디자인, 예술학", "personality": "감각적이고 표현을 좋아하는 분에게 어울려요.", "emoji": "🎨"},
            {"job": "수의사/동물 관련", "majors": "수의학, 동물자원학", "personality": "동물을 사랑하는 분께 추천해요.", "emoji": "🐾"}
        ],
        "good_subjects": ["미술", "음악"],
        "weak_subjects": ["수학", "사회"],
        "tips": "감성적인 음악 들으면서 공부하면 집중력 업! 🎧"
    },
    "INFP": {
        "careers": [
            {"job": "작가/시인", "majors": "문예창작, 국어국문학", "personality": "상상력과 감성이 풍부한 사람에게 좋아요.", "emoji": "📖"},
            {"job": "심리상담사", "majors": "심리학, 사회복지학", "personality": "다른 사람의 마음을 이해하려는 따뜻한 성격이에요.", "emoji": "💬"}
        ],
        "good_subjects": ["국어", "음악"],
        "weak_subjects": ["수학", "기술가정"],
        "tips": "글쓰기나 그림으로 감정을 표현하면 공부 스트레스도 줄어요 ✨"
    },
    "INTP": {
        "careers": [
            {"job": "프로그래머/개발자", "majors": "컴퓨터공학, 데이터과학", "personality": "논리적이고 문제 해결을 즐기는 분에게 좋아요.", "emoji": "💻"},
            {"job": "연구원", "majors": "물리학, 수학", "personality": "새로운 개념을 탐구하는 데 흥미가 큰 사람에게 어울려요.", "emoji": "🔍"}
        ],
        "good_subjects": ["과학", "수학"],
        "weak_subjects": ["미술", "체육"],
        "tips": "혼자 탐구하는 시간을 충분히 주세요. 집중력이 폭발할 거예요 💡"
    },
    "ESTP": {
        "careers": [
            {"job": "스포츠 코치/트레이너", "majors": "체육학, 스포츠과학", "personality": "에너지 넘치고 활동적인 분에게 잘 맞아요!", "emoji": "🏋️‍♂️"},
            {"job": "영업/마케팅", "majors": "경영학, 광고홍보", "personality": "사람을 설득하고 관계를 맺는 걸 잘해요.", "emoji": "💬"}
        ],
        "good_subjects": ["체육", "사회"],
        "weak_subjects": ["과학", "국어"],
        "tips": "움직이면서 공부하거나 짧게 끊어서 하면 집중이 오래가요 ⚡"
    },
    "ESFP": {
        "careers": [
            {"job": "연예인/MC", "majors": "공연예술, 방송연예", "personality": "사람들 앞에서 빛나는 타입이에요!", "emoji": "🎤"},
            {"job": "이벤트 기획자", "majors": "경영학, 광고홍보", "personality": "창의력과 유머감각이 넘치는 사람에게 추천!", "emoji": "🎉"}
        ],
        "good_subjects": ["음악", "미술"],
        "weak_subjects": ["수학", "과학"],
        "tips": "밝은 에너지로 공부 친구들을 모아 함께 하면 더 즐거워요 ☀️"
    },
    "ENFP": {
        "careers": [
            {"job": "창업가/스타트업", "majors": "경영학, 창업학", "personality": "아이디어가 풍부한 분에게 좋아요.", "emoji": "💡"},
            {"job": "홍보/콘텐츠 제작", "majors": "미디어학, 광고홍보", "personality": "표현력 좋고 소통을 즐기는 분께 추천합니다.", "emoji": "📣"}
        ],
        "good_subjects": ["국어", "미술"],
        "weak_subjects": ["수학", "과학"],
        "tips": "새로운 아이디어를 기록해두세요! 영감은 공부에도 큰 도움이 돼요 🌈"
    },
    "ENTP": {
        "careers": [
            {"job": "기획자/전략가", "majors": "경영학, 광고홍보", "personality": "토론과 아이디어 싸움 좋아하는 분에게 찰떡!", "emoji": "🧠"},
            {"job": "유튜버/콘텐츠 크리에이터", "majors": "미디어커뮤니케이션, 디자인", "personality": "새로운 걸 시도하는 용감한 사람!", "emoji": "🎬"}
        ],
        "good_subjects": ["국어", "사회"],
        "weak_subjects": ["과학", "기술가정"],
        "tips": "토론식 공부로 지루함을 없애보세요! 친구랑 이야기하며 배우기 👍"
    },
    "ESTJ": {
        "careers": [
            {"job": "경영자/리더", "majors": "경영학, 경제학", "personality": "리더십 있고 계획적인 성격이에요.", "emoji": "👔"},
            {"job": "군인/경찰", "majors": "행정학, 법학", "personality": "책임감 강하고 현실적인 분께 어울려요.", "emoji": "🛡️"}
        ],
        "good_subjects": ["사회", "수학"],
        "weak_subjects": ["음악", "미술"],
        "tips": "목표 설정이 중요해요! 공부 스케줄을 정확히 지키면 성취감이 커질 거예요 🗂️"
    },
    "ESFJ": {
        "careers": [
            {"job": "교사/강사", "majors": "교육학, 심리학", "personality": "사람들과 소통하고 돕는 걸 좋아해요.", "emoji": "🍎"},
            {"job": "간호사/서비스직", "majors": "간호학, 보건학", "personality": "친절하고 따뜻한 마음을 가진 분에게 딱!", "emoji": "💖"}
        ],
        "good_subjects": ["도덕", "국어"],
        "weak_subjects": ["과학", "기술가정"],
        "tips": "함께 공부할 친구를 찾아보세요! 서로 도와가며 배우면 더 즐겁답니다 🤗"
    },
    "ENFJ": {
        "careers": [
            {"job": "상담사/교사", "majors": "심리학, 교육학", "personality": "다른 사람의 성장을 돕는 걸 좋아해요.", "emoji": "🎓"},
            {"job": "홍보/기획", "majors": "미디어학, 경영학", "personality": "사람과 소통하는 능력이 탁월해요!", "emoji": "📢"}
        ],
        "good_subjects": ["국어", "도덕"],
        "weak_subjects": ["과학", "수학"],
        "tips": "친구의 고민을 들어주며 공부도 함께 하면 효과 만점! 💬"
    },
    "ENTJ": {
        "careers": [
            {"job": "CEO/리더", "majors": "경영학, 경제학", "personality": "목표를 향해 달리는 추진력 1등!", "emoji": "🚀"},
            {"job": "전략컨설턴트", "majors": "경제학, 산업공학", "personality": "계획적이고 문제 해결 중심적인 분에게 잘 맞아요.", "emoji": "📈"}
        ],
        "good_subjects": ["수학", "사회"],
        "weak_subjects": ["음악", "체육"],
        "tips": "리더십을 발휘할 프로젝트형 공부에 강점이 있어요 💪"
    }
}


def main():
    st.set_page_config(page_title="MBTI 진로 추천 🎯", layout="centered")

    st.title("🎒 MBTI로 알아보는 너의 진로와 공부 스타일!")
    st.markdown("MBTI를 선택하면 **진로 2가지**, **추천 학과**, **공부 팁**, 그리고 **잘하는 과목 / 어려운 과목**까지 모두 알려줄게 😎")

    mbti = st.selectbox("MBTI 선택하기", list(MBTI_DATA.keys()))

    if st.button("결과 보기 🚀"):
        data = MBTI_DATA[mbti]
        st.subheader(f"{mbti} 유형의 추천 진로 ✨")
        for idx, c in enumerate(data["careers"], start=1):
            st.markdown(f"### {idx}. {c['emoji']} {c['job']}")
            st.write(f"**추천 학과:** {c['majors']}")
            st.write(f"**잘 맞는 성격:** {c['personality']}")
            st.write("---")

        st.subheader("📘 공부 스타일 분석")
        st.write(f"**잘하는 과목:** {', '.join(data['good_subjects'])} ✅")
        st.write(f"**조금 어려운 과목:** {', '.join(data['weak_subjects'])} ⚠️")
        st.info(data['tips'])

        # 랜덤 하루 진로 추천 기능
        random_mbti = random.choice(list(MBTI_DATA.keys()))
        random_career = random.choice(MBTI_DATA[random_mbti]['careers'])
        st.write("---")
        st.subheader("🎲 오늘의 랜덤 진로 추천!")
        st.write(f"오늘은 **{random_mbti}형** 스타일의 **{random_career['emoji']} {random_career['job']}** 어떠세요?")
        st.caption("새로운 진로를 알아보는 것도 좋은 경험이 될 거예요 🌟")

    st.caption("참고: MBTI는 참고용이에요! 진짜 중요한 건, **내가 좋아하는 것**을 찾는 거랍니다 💕")


if __name__ == '__main__':
    main()
