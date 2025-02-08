import streamlit as st
import time

# Set page title and icon
st.set_page_config(page_title="A Special Proposal for Muskan", page_icon="💖")

# Custom CSS for better visuals
st.markdown(
    """
    <style>
        .title-text {
            font-size: 36px;
            font-weight: bold;
            text-align: center;
            color: #FF4081;
        }
        .message-text {
            font-size: 24px;
            text-align: center;
            font-style: italic;
            color: #ff6699;
        }
        .button-container {
            text-align: center;
        }
        .footer-text {
            font-size: 20px;
            text-align: center;
            font-weight: bold;
            color: #FF4081;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Display a heartfelt message
st.markdown('<p class="title-text">💖 Happy Propose Day, Muskan! 💖</p>', unsafe_allow_html=True)

st.markdown(
    """
    <p class="message-text">Tumhare thhe tumhare hain<br>
    <b>Tumhare hi rahenge hum</b><br>
    Tumhare thhe tumhare hain<br>
    <b>Tumhare hi rahenge hum</b></p>
    """,
    unsafe_allow_html=True
)

st.image("https://source.unsplash.com/800x400/?romantic,proposal", caption="For You, Muskan 💕", use_column_width=True)

# Proposal Button
st.markdown('<div class="button-container">', unsafe_allow_html=True)
if st.button(" Will You Be My Valentine? "):
    st.success("Yes! You just made my world brighter! 💖✨")
    st.balloons()
    time.sleep(1)
    st.snow()
st.markdown('</div>', unsafe_allow_html=True)

# Footer message
st.markdown('<p class="footer-text">💖 Forever Yours 💖</p>', unsafe_allow_html=True)


