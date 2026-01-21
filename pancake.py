import streamlit as st

st.title("Pancakes Developed")

# CSS for a simple pancake
pancake_css = """
<style>
.parent-container {
        position: relative;
        height: 150px; /* Set height to prevent layout collapse */
    }
.pancake{
    position: absolute;
    left: 50%;
    top: 0px;
    transform: translateX(-50%);
    background-color: #DEB887; /* Golden brown */
    border-radius: 50%;
    width: 200px;
    height: 100px;
    margin: 10px auto;
    z-index: 1000;
    border: 5px outset #8B4513; /* Darker edge */
    box-shadow: 0px 5px 5px rgba(139, 69, 19, 1);
    filter: drop-shadow(0px 5px 5px rgba(139, 69, 19, 1));
}
.butter {
    position: absolute;
    left: 50%;
    transform: translateX(-100%);
    background-color: #FFD700;
    width: 40px;
    height: 30px;
    margin: 30px auto;
    transform: perspective(300px) rotateX(40deg) skewX(-10deg);
    transform-origin: center;
    z-index: 4;
    border-radius: 5px;
    filter: drop-shadow(0px 5px 5px #FFD700);
}
</style>
"""

st.markdown(pancake_css, unsafe_allow_html=True)

# Generate a stack
num_pancakes = st.slider("Stack Size", 1, 1000, 3)
st.markdown('<div class="parent-container">', unsafe_allow_html=True)
st.markdown('<div class="butter"></div>', unsafe_allow_html=True)
for i in range(num_pancakes):
     st.markdown(f'<div class="pancake" style="top: {i * 20}px; z-index: {1000-i};"></div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

#st.markdown("""
#<div class="parent-container">
#    <div class="butter"></div>
#    <div class="pancake-one"></div>
#    <div class="pancake-two"></div>
#    <div class="pancake-three"></div>
#</div>
#""", unsafe_allow_html=True)

