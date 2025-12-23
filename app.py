st.markdown("""
<style>

/* MAIN BACKGROUND - PINK HEARTS */
.stApp {
    background: linear-gradient(135deg, #ffd1dc, #ffc0cb, #ffb6c1);
    overflow: hidden;
    font-family: 'Segoe UI', sans-serif;
}

/* HEART ANIMATION */
.heart {
    position: fixed;
    width: 20px;
    height: 20px;
    background: pink;
    transform: rotate(45deg);
    animation: float 8s infinite ease-in;
    opacity: 0.6;
    z-index: 0;
}

.heart:before,
.heart:after {
    content: "";
    width: 20px;
    height: 20px;
    background: pink;
    border-radius: 50%;
    position: absolute;
}

.heart:before {
    top: -10px;
    left: 0;
}

.heart:after {
