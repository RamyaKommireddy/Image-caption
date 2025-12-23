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

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #667eea, #764ba2);
}
.stApp {
    background-image: linear-gradient(135deg, #667eea, #764ba2);
}
.title {
    font-size: 42px;
    font-weight: bold;
    color: #ffffff;
    text-align: center;
}
.subtitle {
    font-size: 18px;
    color: #f1f1f1;
    text-align: center;
    margin-bottom: 30px;
}
.caption-box {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 15px;
    color: #333;
    font-size: 20px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ------------------ TITLE ------------------
st.markdown('<div class="title">🖼️ AI Image Caption Generator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Upload an image and let AI describe it beautifully ✨</div>', unsafe_allow_html=True)

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
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("✨ Generate Caption"):
        with st.spinner("AI is thinking... 🤖"):
            inputs = processor(image, return_tensors="pt")
            output = model.generate(**inputs)
            caption = processor.decode(output[0], skip_special_tokens=True)

        st.markdown(
            f'<div class="caption-box">📸 <b>{caption}</b></div>',
            unsafe_allow_html=True
        )

# ------------------ FOOTER ------------------
st.markdown("<br><center style='color:white;'>Made with ❤️ using Streamlit & AI</center>", unsafe_allow_html=True)
