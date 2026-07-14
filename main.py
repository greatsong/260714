import streamlit as st

st.set_page_config(page_title="MBTI 직업 & 포켓몬 추천", page_icon="✨", layout="centered")

# MBTI: (직업, 포켓몬 이름, 포켓몬 도감번호, 추천 이유)
mbti_data = {
    "INTJ": ("전략기획가", "폴리곤", 137, "논리적이고 체계적인 사고로 목표를 설계하는 모습이 닮았어요."),
    "INTP": ("연구원 · 과학자", "삐삐", 39, "호기심 많고 탐구를 즐기는 성향이 잘 어울려요."),
    "ENTJ": ("경영자 · CEO", "리자몽", 6, "강한 추진력과 카리스마 넘치는 리더십이 특징이에요."),
    "ENTP": ("창업가 · 발명가", "조로아크", 571, "틀을 깨는 발상과 순발력이 돋보이는 조합이에요."),
    "INFJ": ("상담가 · 심리학자", "가디안", 282, "타인의 마음을 깊이 이해하는 공감 능력이 닮았어요."),
    "INFP": ("작가 · 예술가", "이브이", 133, "무한한 가능성과 섬세한 감수성을 지녔어요."),
    "ENFJ": ("교사 · 코치", "루카리오", 448, "타인의 성장을 이끄는 리더십과 따뜻함이 있어요."),
    "ENFP": ("마케터 · 이벤트 기획자", "피카츄", 25, "밝은 에너지로 주변 사람을 사로잡는 매력이 닮았어요."),
    "ISTJ": ("회계사 · 공무원", "메타그로스", 376, "신중하고 체계적이며 규칙을 철저히 지키는 성향이에요."),
    "ISFJ": ("간호사 · 사회복지사", "럭키", 113, "헌신적으로 주변을 돌보는 따뜻함이 특징이에요."),
    "ESTJ": ("프로젝트 매니저", "괴력몬", 68, "강한 실행력으로 일을 밀어붙이는 힘이 닮았어요."),
    "ESFJ": ("HR 담당자 · 코디네이터", "픽시", 36, "사교적이고 사람들을 잘 챙기는 성격이에요."),
    "ISTP": ("엔지니어 · 정비사", "쇠집게", 212, "실용적이고 손재주가 뛰어난 문제 해결사예요."),
    "ISFP": ("디자이너 · 사진작가", "님피아", 700, "감성적이고 아름다움을 추구하는 예술가 기질이에요."),
    "ESTP": ("영업직 · 프로 운동선수", "번치코", 257, "순발력과 에너지가 넘치는 행동파예요."),
    "ESFP": ("배우 · 엔터테이너", "푸린", 39, "무대를 즐기고 사람들 앞에서 빛나는 성격이에요."),
}

st.title("✨ MBTI로 알아보는 나의 직업 & 포켓몬")
st.write("당신의 MBTI를 선택하면 어울리는 직업과 포켓몬을 추천해드려요!")

mbti = st.selectbox("MBTI를 선택하세요", list(mbti_data.keys()))

if mbti:
    job, pokemon_name, pokemon_id, reason = mbti_data[mbti]
    image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{pokemon_id}.png"

    st.subheader(f"🧭 {mbti} 유형에게 어울리는 직업")
    st.success(f"**{job}**")

    st.subheader(f"🎮 당신을 닮은 포켓몬은?")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(image_url, caption=pokemon_name, width=180)
    with col2:
        st.markdown(f"### {pokemon_name}")
        st.write(reason)
