# -*- coding: utf-8 -*-
"""
Harshita's Birthday Countdown + Secret Code Unlock + Surprise Page
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

# --- Paths (adjust to your local setup) ---
IMAGE_PATH = "MANCHURIAN.jpg"
PHOTO_DIR = PHOTO_DIR = "."
photos = sorted([f for f in os.listdir(PHOTO_DIR) if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))])

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
start_date = datetime(2025, 1, 1)
now = datetime.now()
countdown = birthday - now
total_duration = birthday - start_date

# --- Helper Functions ---

def show_landing_page():
    st.markdown("<h1 style='text-align: center; color: #D6336C;'>🎉 Harshita's 21st Birthday 🎉</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #F25F5C;'>Countdown to Her Special Day</h3>", unsafe_allow_html=True)

    # Progress bar
    progress = (now - start_date).total_seconds() / total_duration.total_seconds()
    progress = min(max(progress, 0), 1)
    st.markdown("### ⏳ Time Until December 21, 2025")
    st.progress(progress)
    st.markdown(f"**{progress*100:.2f}%** of the journey to Harshita’s birthday completed! 🎈")

    # Countdown
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
            st.balloons()
        else:
            st.error("❌ That's not the right code. Try again?")

    # Show image
    if os.path.exists(IMAGE_PATH):
        image = Image.open(IMAGE_PATH)
        st.markdown("---")
        st.image(image, caption="Your Favourite 😉", use_column_width=True)
    else:
        st.warning("Couldn't find MANCHURIAN.jpg at the specified path.")

def show_surprise_page():
    st.markdown("<h1 style='text-align: center; color: #D6336C;'>🎉 Happy 21st Birthday, My Love! 🎉</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #F25F5C;'>Here’s your special surprise 💖</h3>", unsafe_allow_html=True)
    st.markdown("---")

    love_letter = """
    Dear Harshita,

    On this beautiful day, your 21st birthday, I want you to know just how much you mean to me...
    """
    st.markdown("<h3 style='color: #6A0572;'>A Love Letter Just For You</h3>", unsafe_allow_html=True)
    st.write(love_letter)

    st.markdown("---")

    # Photo slideshow
    photos = []
    if os.path.exists(PHOTO_DIR):
        photos = sorted([f for f in os.listdir(PHOTO_DIR) if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))])

    if photos:
        total_photos = len(photos)
        song_length_seconds = 231
        photo_display_time = song_length_seconds / total_photos

        # Audio control
        if not st.session_state.audio_playing:
            if st.button("▶️ Play Song"):
                st.session_state.audio_playing = True
                st.session_state.start_time = datetime.now()
                try:
                    with open(SONG_PATH, "rb") as f:
                        st.session_state.audio_bytes = f.read()
                except Exception as e:
                    st.warning(f"Unable to load audio: {e}")
        else:
            if st.session_state.audio_bytes:
                elapsed = (datetime.now() - st.session_state.start_time).total_seconds()
                st.audio(st.session_state.audio_bytes, format="audio/mp3", start_time=elapsed)

        # Current photo
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

    st.markdown("---")

    quotes = [
        "Distance means so little when someone means so much.",
        "Love knows no distance; it hath no continent; its eyes are for the stars. – Gilbert Parker",
        "You are my heart, my life, my one and only thought. – Arthur Conan Doyle",
        "In true love, the smallest distance is too great, and the greatest distance can be bridged. – Hans Nouwens",
        "I carry your heart with me (I carry it in my heart). – E.E. Cummings"
    ]
    quote = random.choice(quotes)
    st.markdown(f"<h4 style='color: #6A0572;'>Daily Love Quote:</h4>", unsafe_allow_html=True)
    st.markdown(f"<em>“{quote}”</em>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: #999;'>Made with ❤️ just for you.</p>", unsafe_allow_html=True)

# --- Main ---
if st.session_state.unlocked:
    show_surprise_page()
else:
    show_landing_page()



