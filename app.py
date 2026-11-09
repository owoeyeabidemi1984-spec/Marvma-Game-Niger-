import streamlit as st
import random

st.set_page_config(page_title="Naija Word Scramble", page_icon="🇳🇬")

WORDS = [
    ("LAGOS", "Biggest city in Nigeria"),
    ("JOLLOF", "Famous Nigerian rice dish"),
    ("SUYA", "Spicy grilled meat on a stick"),
    ("DANFO", "Yellow bus in Lagos"),
    ("AMALA", "Yam flour swallow"),
    ("MOIMOI", "Steamed bean cake"),
    ("NOLLYWOOD", "Nigerian film industry"),
    ("AFROBEATS", "Music genre from Nigeria"),
    ("OWAMBE", "Big Nigerian party"),
    ("ASOEBI", "Matching clothes for party"),
    ("EBA", "Made from garri"),
    ("PEPPER", "What makes soup hot"),
    ("ZOBO", "Hibiscus drink"),
    ("AKARA", "Bean fritters for breakfast"),
    ("BANGA", "Palm nut soup"),
]

def scramble(word):
    letters = list(word)
    random.shuffle(letters)
    scrambled = "".join(letters)
    if scrambled == word:
        return scramble(word)
    return scrambled

if "index" not in st.session_state:
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.scrambled = scramble(WORDS[0][0])
    st.session_state.feedback = ""
    st.session_state.finished = False
    st.session_state.answered = False

st.title("🇳🇬 Naija Word Scramble")
st.write("Unscramble the Naija word! 15 words. How many can you get?")

if not st.session_state.finished:
    word, hint = WORDS[st.session_state.index]
    
    st.markdown(f"### Word {st.session_state.index + 1} / 15")
    st.markdown(f"## 🔀 {st.session_state.scrambled}")
    st.info(f"💡 Hint: {hint}")
    st.write(f"Score: **{st.session_state.score}**")

    guess = st.text_input("Your answer:", key=f"guess_{st.session_state.index}").upper().strip()

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Check ✅", use_container_width=True):
            if guess == word:
                st.session_state.score += 1
                st.session_state.feedback = f"Correct! 🎉 It was {word}"
            else:
                st.session_state.feedback = f"Wrong 😅 It was {word}. Your answer: {guess if guess else 'empty'}"
            st.session_state.answered = True
    
    if st.session_state.feedback:
        if "Correct" in st.session_state.feedback:
            st.success(st.session_state.feedback)
        else:
            st.error(st.session_state.feedback)

    if st.session_state.answered:
        if st.button("Next Word ➡️", use_container_width=True):
            st.session_state.index += 1
            st.session_state.feedback = ""
            st.session_state.answered = False
            if st.session_state.index >= len(WORDS):
                st.session_state.finished = True
            else:
                st.session_state.scrambled = scramble(WORDS[st.session_state.index][0])
            st.rerun()

else:
    score = st.session_state.score
    st.balloons()
    st.markdown(f"## Game Over! 🎮")
    st.markdown(f"## Your Score: {score} / 15")
    
    if score == 15:
        st.success("🏆 LAGOS CHAMPION! Perfect score! You sabi everything!")
    elif score >= 11:
        st.success("🔥 NAIJA STAR! You really know your culture!")
    elif score >= 7:
        st.warning("👍 GOOD TRY! You know Lagos well!")
    else:
        st.info("😅 OMO, TRY AGAIN! You go still learn small!")

    if st.button("Play Again 🔄", use_container_width=True):
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.scrambled = scramble(WORDS[0][0])
        st.session_state.feedback = ""
        st.session_state.finished = False
        st.session_state.answered = False
        st.rerun()

st.markdown("---")
st.write("Share with your friends - who can get 15/15? 🇳🇬")
