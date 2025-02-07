import streamlit as st
import time

# Set page title and background color
st.set_page_config(page_title="Happy Rose Day, Muskan!", page_icon="🌹")

st.markdown(
    """
    <style>
        body {
            background-color: #fff0f5;
            text-align: center;
        }
        .title {
            font-size: 55px;
            font-weight: bold;
            color: #ff1493;
            text-shadow: 2px 2px 5px #ff69b4;
        }
        .heart {
            font-size: 35px;
            color: #ff4500;
            animation: pulse 1.5s infinite;
        }
        .message {
            font-size: 24px;
            color: #8b0000;
            font-style: italic;
        }
        .rose {
            font-size: 45px;
            animation: fadeIn 2s infinite alternate;
        }
        @keyframes fadeIn {
            from { opacity: 0.4; }
            to { opacity: 1; }
        }
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.2); }
            100% { transform: scale(1); }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display title and roses
st.markdown('<p class="title">💖 Happy Rose Day, Muskan! 💖</p>', unsafe_allow_html=True)

# Animated roses
roses = "🌹 " * 10
for _ in range(5):
    st.markdown(f'<p class="rose">{roses}</p>', unsafe_allow_html=True)
    time.sleep(0.5)

# Sweet message with animation
st.markdown(
    """
    <p class="heart">💖 My Dearest Muskan 💖</p>
    <p class="message">Just like this beautiful rose, you bring so much joy, love, and happiness into my life. 
    Wishing you a day filled with smiles, laughter, and endless love! You are my sunshine and my favorite person. 
    Happy Rose Day, my love! 🌹💕</p>
    """,
    unsafe_allow_html=True,
)

# More animated hearts
for _ in range(3):
    st.markdown('<p class="heart">❤️ 💖 💕 💞 💓</p>', unsafe_allow_html=True)
    time.sleep(0.7)

# Button to spread love
if st.button("Send Love 💝"):
    st.balloons()
    st.success("Muskan, you are truly special! 💕")

