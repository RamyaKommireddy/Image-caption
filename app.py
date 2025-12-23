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
.heart:nth-chi
