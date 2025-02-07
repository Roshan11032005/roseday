import streamlit as st
import time

# Configure page
st.set_page_config(
    page_title="Muskan's Rose Day",
    page_icon="🌹",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Advanced CSS styling
st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Great+Vibes&display=swap');
        
        body {{
            background: linear-gradient(45deg, #ffb6c1, #ff69b4, #ff1493);
            animation: gradient 15s ease infinite;
            min-height: 100vh;
        }}
        
        @keyframes gradient {{
            0% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
            100% {{ background-position: 0% 50%; }}
        }}
        
        .title {{
            font-family: 'Dancing Script', cursive;
            font-size: 4.5rem;
            color: #fff;
            text-shadow: 0 0 10px #ff69b4;
            animation: titleGlow 2s ease-in-out infinite;
            margin: 2rem 0;
        }}
        
        @keyframes titleGlow {{
            0%, 100% {{ text-shadow: 0 0 10px #ff69b4; }}
            50% {{ text-shadow: 0 0 20px #ff1493, 0 0 30px #ff69b4; }}
        }}
        
        .love-letter {{
            background: rgba(255, 255, 255, 0.9);
            border-radius: 15px;
            padding: 2rem;
            box-shadow: 0 0 20px rgba(255, 105, 180, 0.3);
            transform: rotate(-2deg);
            margin: 2rem 0;
            transition: transform 0.3s ease;
        }}
        
        .love-letter:hover {{
            transform: rotate(1deg) scale(1.02);
        }}
        
        .message {{
            font-family: 'Great Vibes', cursive;
            font-size: 1.8rem;
            color: #8b0000;
            line-height: 1.6;
        }}
        
        .heart-rain::before {{
            content: "❤";
            position: fixed;
            animation: fall linear infinite;
            opacity: 0;
        }}
        
        @keyframes fall {{
            to {{ transform: translateY(100vh) rotate(360deg); }}
        }}
        
        .interactive-rose {{
            font-size: 4rem;
            cursor: pointer;
            transition: all 0.3s ease;
            animation: float 3s ease-in-out infinite;
        }}
        
        @keyframes float {{
            0%, 100% {{ transform: translateY(0); }}
            50% {{ transform: translateY(-20px); }}
        }}
        
        .love-meter {{
            background: rgba(255, 255, 255, 0.9);
            padding: 1.5rem;
            border-radius: 15px;
            margin: 2rem 0;
        }}
        
        #heart-cursor {{
            position: fixed;
            pointer-events: none;
            font-size: 24px;
            z-index: 9999;
        }}
    </style>
""", unsafe_allow_html=True)

# Add custom cursor
st.markdown('<div id="heart-cursor">❤</div>', unsafe_allow_html=True)

# Main content
st.markdown('<h1 class="title">🌹 My Eternal Love for Muskan 🌹</h1>', unsafe_allow_html=True)

# Interactive rose garden
col1, col2, col3 = st.columns(3)
with col2:
    rose = st.empty()
    if rose.button("🌸 Click to Grow Our Love 🌸"):
        for i in range(1, 6):
            rose.markdown(f'<div class="interactive-rose" style="font-size:{4 + i}rem">🌹</div>', 
                        unsafe_allow_html=True)
            time.sleep(0.3)
        st.success("Our love grows stronger every day! 💖")

# Love letter
st.markdown("""
    <div class="love-letter">
        <p class="message">
            My Dearest Muskan,<br><br>
            On this Rose Day, I want to express what you mean to me...<br>
            You're the melody in my heart's song,<br>
            The colors in my world,<br>
            The warmth in every sunrise.<br><br>
            Like a rose that blooms eternally,<br>
            My love for you grows stronger with each petal of time.<br>
            Thank you for being my forever Valentine.<br><br>
            With all my heart,<br>
            Your [Your Name] 💞
        </p>
    </div>
""", unsafe_allow_html=True)

# Love meter
st.markdown("""
    <div class="love-meter">
        <h3 style="color:#ff1493; font-family: 'Dancing Script', cursive;">Our Love Meter 💘</h3>
        <input type="range" min="100" max="100" value="100" style="width:100%">
        <p style="color:#8b0000; font-size:1.2rem;">100% Pure Love - Forever and Always! 💖</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <script>
        function createHearts() {{
            const container = document.querySelector('body');
            for (let i = 0; i < 50; i++) {{
                const heart = document.createElement('div');
                heart.className = 'heart-rain';
                heart.style.left = Math.random() * 100 + 'vw';
                heart.style.animation = `fall ${{Math.random() * 3 + 2}}s linear infinite`;
                heart.style.animationDelay = Math.random() * 2 + 's';
                container.appendChild(heart);
            }}
        }}
        document.addEventListener('DOMContentLoaded', createHearts);
        
        // Custom cursor effect
        document.addEventListener('mousemove', function(e) {{
            const cursor = document.getElementById('heart-cursor');
            cursor.style.left = e.pageX + 'px';
            cursor.style.top = e.pageY + 'px';
        }});
    </script>
""", unsafe_allow_html=True)

