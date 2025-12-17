import streamlit as st
from datetime import datetime
import random
import os
from PIL import Image
from streamlit_autorefresh import st_autorefresh
import re

# --- Page Setup ---
st.set_page_config(
    page_title="Happy 21st Birthday, My Love!",
    page_icon="🎂",
    layout="centered"
)

# --- Auto-refresh every 1 second ---
st_autorefresh(interval=1000, limit=None, key="refresh")

# --- Countdown Section ---
birthday = datetime(2025, 12, 21, 0, 0, 0)
now = datetime.now()
countdown = birthday - now

st.markdown("<h1 style='text-align: center; color: #D6336C;'>🎉 Happy 21st Birthday! 🎉</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #F25F5C;'>Countdown to Your Special Day</h3>", unsafe_allow_html=True)

if countdown.total_seconds() > 0:
    days = countdown.days
    hours = countdown.seconds // 3600
    minutes = (countdown.seconds % 3600) // 60
    day_label = "day" if days == 1 else "days"
    hour_label = "hour" if hours == 1 else "hours"
    minute_label = "minute" if minutes == 1 else "minutes"
    st.markdown(
        f"<h2 style='text-align: center; color: #FF6F91;'>"
        f"{days} {day_label}, {hours} {hour_label}, and {minutes} {minute_label} left!"
        f"</h2>", unsafe_allow_html=True
    )
else:
    st.markdown("<h2 style='text-align: center; color: #FF6F91;'>🎂 Today is your day! Happy 21st Birthday! 🎂</h2>", unsafe_allow_html=True)

# --- Love Letter ---
st.markdown("<h3 style='color: #6A0572;'>A Love Letter Just For You</h3>", unsafe_allow_html=True)
love_letter = """
Dear Harshita,

On this beautiful day, your 21st birthday, I want you to know just how much you mean to me. 
I think of you every single day—your smile, your voice, your kindness—how lucky I am to have you in my life, even across the miles...

[Add full love letter here]
"""
st.write(love_letter)
st.markdown("---")

# --- Natural sort function for proper photo ordering ---
def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

# --- Photo Slideshow ---
song_path = "Song/song.mp3"

# Get all image files in repo root and sort naturally
photos = sorted(
    [f for f in os.listdir() if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))],
    key=natural_sort_key
)
total_photos = len(photos)

# Song duration in seconds (update to match your song)
song_length_seconds = 231
photo_display_time = song_length_seconds / total_photos if total_photos > 0 else 1

# --- Audio Handling ---
if "audio_playing" not in st.session_state:
    st.session_state.audio_playing = False
    st.session_state.start_time = None

if not st.session_state.audio_playing:
    if st.button("▶️ Play Song"):
        st.session_state.audio_playing = True
        st.session_state.start_time = datetime.now()
        try:
            with open(song_path, "rb") as f:
                st.session_state.audio_bytes = f.read()
        except Exception as e:
            st.warning(f"Unable to load audio: {e}")
else:
    if "audio_bytes" in st.session_state and st.session_state.start_time:
        elapsed = (datetime.now() - st.session_state.start_time).total_seconds()
        st.audio(st.session_state.audio_bytes, format="audio/mp3", start_time=elapsed)

# --- Slideshow Timing ---
if st.session_state.audio_playing and st.session_state.start_time:
    elapsed = (datetime.now() - st.session_state.start_time).total_seconds()
else:
    elapsed = 0

if total_photos > 0:
    current_index = int(elapsed // photo_display_time) % total_photos
    image_path = photos[current_index]
    img = Image.open(image_path)
    st.image(img, use_column_width=True)
    st.markdown(f"<p style='text-align: center; color: gray;'>Photo {current_index + 1} of {total_photos}</p>", unsafe_allow_html=True)
else:
    st.warning("No images found in the repository.")

st.markdown("---")

# --- Daily Romantic Quote ---
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
