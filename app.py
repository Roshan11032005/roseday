import streamlit as st
import time


st.set_page_config(page_title="Happy Rose Day, Muskan!", page_icon="🌹")
st.markdown(
    """
    <style>
        body {
            background-color: #ffe6f2;
            text-align: center;
        }
        .title {
            font-size: 50px;
            font-weight: bold;
            color: #d63384;
        }
        .heart {
            font-size: 30px;
            color: #ff1493;
        }
        .message {
            font-size: 22px;
            color: #8b0000;
        }
        .rose {
            font-size: 40px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


st.markdown('<p class="title">Happy Rose Day, Muskan! 🌹</p>', unsafe_allow_html=True)


roses = "🌹 " * 10
for _ in range(5):
    st.markdown(f'<p class="rose">{roses}</p>', unsafe_allow_html=True)
    time.sleep(0.5)


st.markdown(
    """
    <p class="heart">💖 My Dearest Muskan 💖</p>
    <p class="message">Just like this beautiful rose, you bring so much joy, love, and happiness into my life. 
    Wishing you a day filled with smiles, laughter, and endless love! You are my sunshine and my favorite person. 
    Happy Rose Day, my love! 🌹💕</p>
    """,
    unsafe_allow_html=True,
)

# Button to spread love
if st.button("Send Love 💝"):
    st.success("Muskan, you are truly special! 💕")
