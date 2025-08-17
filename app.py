import streamlit as st
import random
import time

st.set_page_config(page_title="I'm Sorry ❤️", page_icon="💔", layout="centered")

# Title
st.markdown("<h1 style='text-align: center; color: pink;'>💌 I'm Sorry My Love 💌</h1>", unsafe_allow_html=True)

# Intro message
st.markdown("""
### 🌹 Hey Babe,
I know I mess up sometimes and hurt you 😔.  
But I love you more than words can ever say. 💖  
This little app is just my way of saying:  
**I'm really sorry, and I’ll do better.** 🥺
""")

st.write("---")

# 🎮 Love Meter
st.markdown("### ❤️ How much do I love you?")
love = st.slider("Slide to find out!", 0, 100, 50)

if love < 30:
    st.warning("😢 Not enough... Let me try harder!")
elif love < 70:
    st.info("😊 Getting closer... but my love is way more!")
else:
    st.success("💖 Infinity & beyond!! You’re my everything 💍")
    st.balloons()

st.write("---")

# 💌 Reveal Love Letter
if st.button("📜 Open my love letter"):
    with st.spinner("Opening love letter... 💌"):
        time.sleep(2)
    st.success("Here it is, just for you 💖")
    st.markdown("""
    ### My Dearest Love,  
    I'm sorry for being a bad boyfriend sometimes.  
    But I promise:  
    - To always listen 👂  
    - To always care 🤗  
    - To always love you ❤️  

    Forever yours,  
    **Your (sometimes silly) Boyfriend** 💕
    """)

    st.image("https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif", use_column_width=True)

st.write("---")

# 🎮 Mini Game: Collect Hearts
st.markdown("### 🎮 A Game for You: Collect My Love ❤️")

if "hearts" not in st.session_state:
    st.session_state.hearts = 0

if st.button("💖 Collect a Heart"):
    st.session_state.hearts += 1
    st.success(f"You collected {st.session_state.hearts} hearts! 💕")

    if st.session_state.hearts >= 10:
        st.balloons()
        st.markdown("### 🎉 You unlocked **My Forever Love** 💍💖")

st.write("---")

# Final forgiveness buttons
st.markdown("### So... will you forgive me, babe? 🥺")

col1, col2 = st.columns(2)

with col1:
    if st.button("💖 Yes, of course! 💖"):
        st.success("Yay!! You're the best ❤️")
        st.image("https://media.giphy.com/media/26ufdipQqU2lhNA4g/giphy.gif", use_column_width=True)

with col2:
    if st.button("😤 Not yet"):
        st.error("Oh nooo! I'll keep trying until you forgive me 💔")
        st.image("https://media.giphy.com/media/3o7TKtnuHOHHUjR38Y/giphy.gif", use_column_width=True)

st.write("---")

# Footer
st.markdown(
    """
    <div style="text-align: center; font-size: 20px; color: hotpink;">
    🌸 This whole app is just for YOU, my love 🌸  
    💖 Forgive me? 💖
    </div>
    """,
    unsafe_allow_html=True
)
