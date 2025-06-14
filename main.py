import streamlit as st
from PIL import Image, ImageDraw

st.set_page_config(page_title="Makeup Game for Kids", layout="centered")
st.title("🎨 Game Makeup Dễ Thương Cho Bé 👧")

# --- Chọn màu ---
lip_color = st.color_picker("Chọn màu son môi", "#e91e63")
blush_color = st.color_picker("Chọn màu má hồng", "#f48fb1")
eye_color = st.color_picker("Chọn màu mắt", "#000000")

# --- Tạo ảnh khuôn mặt ---
def draw_face(lip_c, blush_c, eye_c):
    img = Image.new("RGB", (400, 500), "#fce4ec")
    draw = ImageDraw.Draw(img)

    # Khuôn mặt
    draw.ellipse((100, 100, 300, 400), fill="#ffe0b2", outline="black")

    # Mắt
    draw.ellipse((140, 180, 160, 200), fill=eye_c)
    draw.ellipse((240, 180, 260, 200), fill=eye_c)

    # Miệng (son môi)
    draw.ellipse((180, 320, 220, 340), fill=lip_c)

    # Má hồng
    draw.ellipse((120, 250, 150, 270), fill=blush_c)
    draw.ellipse((250, 250, 280, 270), fill=blush_c)

    return img

# --- Vẽ và hiển thị ---
result_img = draw_face(lip_color, blush_color, eye_color)
st.image(result_img, caption="Khuôn mặt đã được trang điểm 🎀", use_column_width=True)

