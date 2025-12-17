# -*- coding: utf-8 -*-
"""
Harshita's Birthday Surprise Page with Cake
"""

import streamlit as st
from datetime import datetime
import random
import os
from PIL import Image, ImageDraw

# --- Page Setup ---
st.set_page_config(
    page_title="Harshita's 21st Birthday!",
    page_icon="🎂",
    layout="centered"
)

# --- Paths (adjust to repo setup) ---
IMAGE_PATH = "MANCHURIAN.jpg"
PHOTO_DIR = "."  # All photos are in the repo root
SONG_PATH = "yt1z.net - Gryffin - Nobody Compares To You (Official Music Video) ft. Katie Pearlman (320 KBps).mp3"

# --- Constants ---
CORRECT_CODE = "2103"

# --- Initialize session state ---
if "unlocked" not in st.session_state:
    st.session_state.unlocked = False

if "audio_playing" not in st.session_state:
    st.session_state.audio_playing = False
    st.session_state.start_time = None
    st.session_state.audio_bytes = None

if "photo_index" not in st.session_state:
    st.session_state.photo_index = 0

# --- Dates ---
birthday = datetime(2025, 12, 21, 0, 0, 0)
now = datetime.now()
countdown = birthday - now

# --- Helper Functions ---

def show_landing_page():
    st.markdown("<h1 style='text-align: center; color: #D6336C;'>🎉 Harshita's 21st Birthday 🎉</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #F25F5C;'>Countdown to Your Special Day</h3>", unsafe_allow_html=True)

    if countdown.total_seconds() > 0:
        days = countdown.days
        hours = countdown.seconds // 3600
        minutes = (countdown.seconds % 3600) // 60
        st.markdown(
            f"<h2 style='text-align: center; color: #FF6F91;'>"
            f"{days} day{'s' if days != 1 else ''}, {hours} hour{'s' if hours != 1 else ''}, and {minutes} minute{'s' if minutes != 1 else ''} left!"
            f"</h2>", unsafe_allow_html=True)
    else:
        st.markdown("<h2 style='text-align: center; color: #FF6F91;'>🎂 Today is your day! Happy 21st Birthday! 🎂</h2>", unsafe_allow_html=True)
        st.balloons()

    st.markdown("---")
    st.markdown("<h3 style='text-align: center;'>🔐 Enter the Secret Code to Unlock a Surprise</h3>", unsafe_allow_html=True)

    code_input = st.text_input("🔢 Enter 4-digit Secret Code", type="password", max_chars=4)

    if code_input:
        if code_input == CORRECT_CODE:
            st.success("🔓 Unlocked! You're amazing for figuring it out. 💖")
            st.session_state.unlocked = True
        else:
            st.error("❌ That's not the right code. Try again?")

    # Show image
    if os.path.exists(IMAGE_PATH):
        image = Image.open(IMAGE_PATH)
        st.markdown("---")
        st.image(image, caption="Your Favourite 😉", use_column_width=True)
    else:
        st.warning("Couldn't find MANCHURIAN.jpg in the repo.")

# --- Menu ---
def show_menu():
    menu_html = """
    <div style='background-color:#ADD8E6; padding:15px; border-radius:10px; text-align:center; font-family:"Comic Sans MS", cursive;'>
        <h3>💌 Choose Your Surprise 💌</h3>
    </div>
    """
    st.markdown(menu_html, unsafe_allow_html=True)
    
    choice = st.radio(
        "",
        ("Love Letter", "Photo Slideshow + Song", "See Cake")
    )
    return choice

# --- Love Letter ---
def show_love_letter():
    love_letter = """
    Dear Harshita,

On this beautiful day, your 21st birthday, I want to pause for a moment and tell you just how much you mean to me. Words often feel inadequate when I try to express my feelings for you, but I’m going to try anyway because you deserve to hear them.

From the moment we started this journey together eight months ago, my life has been brighter, fuller, and more meaningful. Every laugh we’ve shared, every conversation, every quiet moment, every silly joke—we’ve built a world together in such a short time, and it feels like I’ve known you forever. You’ve shown me what it means to care deeply, to love fearlessly, and to be patient, understanding, and kind, not only to me but to everyone around you.

Today, as you celebrate your 21st birthday, I want you to know how proud I am of you. I see all the effort you put into your dreams, all the moments you doubt yourself, and all the times you push through challenges even when it’s hard. I know you sometimes worry about whether you’ll get into law school or whether you’re ready for the next step in your journey—but let me tell you this: you are more than ready. You have the brilliance, the determination, the courage, and the heart of someone who is destined to make a difference. I have never doubted for a single second that you will achieve everything you set your mind to, and I will be by your side cheering you on every step of the way.

These past eight months have been a journey of joy and love for me. I’ve fallen in love with every part of you—the way you laugh, the way your eyes light up when you’re excited, the way your heart is so big and so full of care for others. You have a strength and a beauty that leave me in awe every day.

Happy 21st birthday, my love. I can’t wait to see the amazing things this year brings for you, for us, and for the life you’re building. Thank you for letting me be a part of your life, for trusting me, for loving me, and for being you—so perfectly, wonderfully, you.

Forever and always,
Nikhil (Your Man)!
    """
    st.markdown("<h3 style='color:#6A0572;'>A Love Letter Just For You</h3>", unsafe_allow_html=True)
    st.write(love_letter)

# --- Slideshow ---
def show_slideshow():
    photos = sorted([f for f in os.listdir(PHOTO_DIR) if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))])

    if photos:
        total_photos = len(photos)
        song_length_seconds = 231  # adjust if needed
        photo_display_time = song_length_seconds / total_photos

        if not st.session_state.audio_playing:
            if st.button("▶️ Play Song"):
                st.session_state.audio_playing = True
                st.session_state.start_time = datetime.now()
                with open(SONG_PATH, "rb") as f:
                    st.session_state.audio_bytes = f.read()

        if st.session_state.audio_playing and st.session_state.start_time:
            elapsed = (datetime.now() - st.session_state.start_time).total_seconds()
        else:
            elapsed = 0

        st.session_state.photo_index = int(elapsed // photo_display_time) % total_photos
        image_path = os.path.join(PHOTO_DIR, photos[st.session_state.photo_index])
        img = Image.open(image_path)
        st.image(img, use_column_width=True)
        st.markdown(f"<p style='text-align: center; color: gray;'>Photo {st.session_state.photo_index + 1} of {total_photos}</p>", unsafe_allow_html=True)
    else:
        st.info("No photos found for the slideshow.")

# --- Cake (Pillow) ---
def show_cake():
    width, height = 400, 400
    cake_img = Image.new("RGB", (width, height), "#ADD8E6")
    draw = ImageDraw.Draw(cake_img)

    # Draw three chocolate layers with simple 3D effect
    layers = [
        {"color": "#3E1F0D", "height": 50},  # dark chocolate
        {"color": "#5C3317", "height": 50},  # milk chocolate
        {"color": "#8B4513", "height": 50}   # light chocolate
    ]

    y = 300
    for layer in layers:
        draw.rectangle([100, y-layer["height"], 300, y], fill=layer["color"], outline="black")
        # 3D effect: lighter top
        draw.rectangle([100, y-layer["height"], 300, y-layer["height"]+5], fill="#C08050")
        y -= layer["height"]

    # Icing
    draw.rectangle([100, y-10, 300, y], fill="#fff5ee")
    y -= 10

    # Cherries
    draw.ellipse([140, y-20, 160, y], fill="red")
    draw.ellipse([180, y-20, 200, y], fill="red")
    draw.ellipse([220, y-20, 240, y], fill="red")

    st.image(cake_img, caption="🎂 Triple Chocolate Cake for You!", use_column_width=True)

# --- Main ---
if st.session_state.unlocked:
    choice = show_menu()
    if choice == "Love Letter":
        show_love_letter()
    elif choice == "Photo Slideshow + Song":
        show_slideshow()
    elif choice == "See Cake":
        show_cake()
else:
    show_landing_page()
