import streamlit as st
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="AI Image Caption Generator",
    page_icon="🖼️",
    layout="centered"
)

# ------------------ CUSTOM CSS (PINK HEARTS THEME) ------------------
st.markdown("""
<style>

/* MAIN BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #ffd1dc, #ffc0cb, #ffb6c1);
    overflow: hidden;
    font-family: 'Segoe UI', sans-serif;
}

/* HEART SHAPE */
.heart {
    position: fixed;
    width: 20px;
    height: 20px;
    background: #ff69b4;
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
    background: #ff69b4;
    border-radius: 50%;
    position: absolute;
}

.heart:before {
    top: -10px;
    left: 0;
}

.heart:after {
    left: -10px;
    top: 0;
}

/* HEART FLOAT ANIMATION */
@keyframes float {
    0% {
        transform: translateY(100vh) rotate(45deg);
        opacity: 0;
    }
    50% {
        opacity: 0.8;
    }
    100% {
        transform: translateY(-10vh) rotate(45deg);
        opacity: 0;
    }
}

/* HEART POSITIONS */
.heart:nth-child(1) { left: 10%; animation-duration: 6s; }
.heart:nth-child(2) { left: 30%; animation-duration: 8s; }
.heart:nth-child(3) { left: 50%; animation-duration: 7s; }
.heart:nth-child(4) { left: 70%; animation-duration: 9s; }
.heart:nth-child(5) { left: 90%; animation-duration: 6s; }

/* TITLE */
.title {
    font-size: 48px;
    font-weight: 900;
    text-align: center;
    color: #ad1457;
    text-shadow: 0 0 12px #ff80ab;
}

/* SUBTITLE */
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #6a1b9a;
    margin-bottom: 30px;
}

/* FILE UPLOADER */
[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.75);
    border-radius: 20px;
    border: 2px dashed #f06292;
    padding: 20px;
}

/* BUTTON */
.stButton button {
    background: linear-gradient(135deg, #ff80ab, #ff4081);
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 40px;
    padding: 14px 40px;
    border: none;
    box-shadow: 0 0 20px rgba(255, 64, 129, 0.6);
    transition: all 0.3s ease;
}

.stButton button:hover {
    transform: scale(1.1);
    box-shadow: 0 0 35px rgba(255, 64, 129, 0.9);
}

/* IMAGE */
img {
    border-radius: 20px;
    box-shadow: 0 0 25px rgba(255,105,180,0.6);
}

/* CAPTION BOX */
.caption-box {
    margin-top: 25px;
    padding: 25px;
    border-radius: 25px;
    font-size: 22px;
    font-weight: bold;
    text-align: center;
    background: rgba(255,255,255,0.85);
    color: #880e4f;
    border: 2px solid #f48fb1;
}

/* FOOTER */
.footer {
    text-align: center;
    color: #880e4f;
    margin-top: 40px;
}

</style>

<!-- FLOATING HEARTS -->
<div class="heart"></div>
<div class="heart"></div>
<div class="heart"></div>
<div class="heart"></div>
<div class="heart"></div>
""", unsafe_allow_html=True)

# ------------------ TITLE ------------------
st.markdown('<div class="title">🖼️ AI Image Caption Generator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Upload an image and let AI describe it with love 💕</div>', unsafe_allow_html=True)

# ------------------ LOAD MODEL ------------------
@st.cache_resource
def load_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

processor, model = load_model()

# ------------------ IMAGE UPLOAD ------------------
uploaded_file = st.file_uploader("📤 Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="✨ Uploaded Image ✨", use_container_width=True)

    if st.button("✨ Generate Caption"):
        with st.spinner("AI is creating magic... 🤖✨"):
            inputs = processor(image, return_tensors="pt")
            output = model.generate(**inputs)
            caption = processor.decode(output[0], skip_special_tokens=True)

        st.markdown(
            f'<div class="caption-box">📸 {caption}</div>',
            unsafe_allow_html=True
        )

# ------------------ FOOTER ------------------
st.markdown('<div class="footer">Made with ❤️ using Streamlit & AI</div>', unsafe_allow_html=True)
