# -*- coding: utf-8 -*-
"""
Harshita's Birthday Surprise Page with Menu + Slideshow
"""

import streamlit as st
from datetime import datetime
import random
import os
from PIL import Image

# --- Page Setup ---
st.set_page_config(
    page_title="Harshita's 21st Birthday!",
    page_icon="🎂",
    layout="centered"
)

# --- Paths ---
IMAGE_PATH = "MANCHURIAN.jpg"
PHOTO_DIR = "."  # all photos in repo root
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

# --- Landing Page ---
def show_landing_page():
    st.markdown("<h1 style='text-align: center; color: #D6336C;'>🎉 Harshita's 21st Birthday 🎉</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #F25F5C;'>Countdown to Your Special Day</h3>", unsafe_allow_html=True)

    if countdown.total_seconds() > 0:
        days = countdown.days
        hours = countdown.seconds // 3600
        minutes = (countdown.seconds % 3600) // 60
        st.markdown(f"<h2 style='text-align: center; color: #FF6F91;'>{days} day{'s' if days != 1 else ''}, {hours} hour{'s' if hours != 1 else ''}, and {minutes} minute{'s' if minutes != 1 else ''} left!</h2>", unsafe_allow_html=True)
    else:
        st.markdown("<h2 style='text-align: center; color: #FF6F91;'>🎂 Today is your day! Happy 21st Birthday! 🎂</h2>", unsafe_allow_html=True)
        st.balloons()

    st.markdown("---")
    st.markdown("<h3 style='text-align: center;'>🔐 Enter the Secret Code to Unlock a Surprise</h3>", unsafe_allow_html=True)

    code_input = st.text_input("🔢 Enter 4-digit Secret Code", type="password", max_chars=4)

    if code_input:
        if code_input == CORRECT_CODE:
            st.session_state.unlocked = True
            st.success("🔓 Unlocked! You're amazing for figuring it out. 💖")
            st.balloons()
            st.rerun()  # <-- new way to force page rerun in modern Streamlit
        else:
            st.error("❌ That's not the right code. Try again?")

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
    choice = st.radio("", ("Love Letter", "Photo Slideshow + Song"))
    return choice

# --- Love Letter ---
def show_love_letter():
    love_letter = """
Dear Harshita,

On this beautiful day, your 21st birthday, I want to pause and tell you how deeply you mean to me...
(Include full heartfelt letter as before)
"""
    st.markdown("<h3 style='color:#6A0572;'>A Love Letter Just For You</h3>", unsafe_allow_html=True)
    st.write(love_letter)

# --- Slideshow + Song ---
def show_slideshow():
    photos = sorted([f for f in os.listdir(PHOTO_DIR) if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))])
    if not photos:
        st.info("No photos found for the slideshow.")
        return

    total_photos = len(photos)
    song_length_seconds = 231
    photo_display_time = song_length_seconds / total_photos

    # Audio
    if not st.session_state.audio_playing:
        st.session_state.audio_playing = True
        st.session_state.start_time = datetime.now()
        with open(SONG_PATH, "rb") as f:
            st.session_state.audio_bytes = f.read()

    elapsed = (datetime.now() - st.session_state.start_time).total_seconds()
    st.audio(st.session_state.audio_bytes, format="audio/mp3", start_time=elapsed)

    # Photo index based on elapsed
    st.session_state.photo_index = int(elapsed // photo_display_time) % total_photos
    image_path = os.path.join(PHOTO_DIR, photos[st.session_state.photo_index])
    img = Image.open(image_path)
    st.image(img, use_column_width=True)
    st.markdown(f"<p style='text-align: center; color: gray;'>Photo {st.session_state.photo_index + 1} of {total_photos}</p>", unsafe_allow_html=True)

# --- Main ---
if st.session_state.unlocked:
    choice = show_menu()
    if choice == "Love Letter":
        show_love_letter()
    elif choice == "Photo Slideshow + Song":
        show_slideshow()
else:
    show_landing_page()

