# -*- coding: utf-8 -*-
"""
Harshita's Birthday Surprise Page with Menu + Auto Slideshow + Cake Surprise
"""

import streamlit as st
from datetime import datetime
from PIL import Image
import os
import time

# --- Paths ---
IMAGE_PATH = "MANCHURIAN.jpg"
PHOTO_DIR = "."  # all photos in repo root

SLIDESHOW_SONG_PATH = "yt1z.net - Gryffin - Nobody Compares To You (Official Music Video) ft. Katie Pearlman.mp3"
CAKE_SONG_PATH = "HAPPY Birthday Song, Happy Birthday to You.mp3"
CAKE_IMAGE_PATH = "HARSHICAKE.png"  # static cake image

CORRECT_CODE = "8891"
SLIDESHOW_SONG_LENGTH_SECONDS = 231  # adjust for your song

# --- Initialize session state ---
if "unlocked" not in st.session_state:
    st.session_state.unlocked = False
if "slideshow_audio_bytes" not in st.session_state:
    st.session_state.slideshow_audio_bytes = None
if "slideshow_start_time" not in st.session_state:
    st.session_state.slideshow_start_time = None

# --- Countdown ---
birthday = datetime(2025, 12, 21)
now = datetime.now()
countdown = birthday - now

# --- Landing Page / Secret Code Input ---
st.set_page_config(
    page_title="Harshita's 21st Birthday!",
    page_icon="🎂",
    layout="centered"
)

st.markdown("<h1 style='text-align:center;'>🎉 Harshita's 21st Birthday 🎉</h1>", unsafe_allow_html=True)

if not st.session_state.unlocked:
    st.markdown("<h3 style='text-align:center;'>Enter the Secret Code to Unlock a Surprise 🔐</h3>", unsafe_allow_html=True)
    code_input = st.text_input("Secret Code", type="password", max_chars=4)
    
    if code_input == CORRECT_CODE:
        st.session_state.unlocked = True
        st.success("Unlocked! 💖")
    elif code_input:
        st.error("Wrong code. Try again!")

    if os.path.exists(IMAGE_PATH):
        img = Image.open(IMAGE_PATH)
        st.image(img, use_column_width=True)
else:
    # --- Main Menu ---
    st.markdown("<h3 style='text-align:center;'>Choose Your Surprise 💌</h3>", unsafe_allow_html=True)
    choice = st.radio("", ["Love Letter", "Photo Slideshow + Song", "Cake Surprise"])

    # --- Love Letter ---
    if choice == "Love Letter":
        st.markdown("<h3 style='color:#6A0572;'>A Love Letter Just For You</h3>", unsafe_allow_html=True)
        st.write("""
        Dear Harshita,

        Happy 21st Birthday! 🎉💖
        
        You are an incredible person, and I hope this special day fills your heart with joy and love. 
        Remember, this is just the beginning of a wonderful journey ahead. 

        Love always,  
        [Your Name]
        """)

    # --- Photo Slideshow + Song ---
    elif choice == "Photo Slideshow + Song":
        photos = sorted([f for f in os.listdir(PHOTO_DIR) if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))])
        if not photos:
            st.info("No photos found for the slideshow.")
        else:
            total_photos = len(photos)
            photo_display_time = SLIDESHOW_SONG_LENGTH_SECONDS / total_photos

            if st.session_state.slideshow_start_time is None:
                st.session_state.slideshow_start_time = time.time()

            elapsed = time.time() - st.session_state.slideshow_start_time
            photo_index = int(elapsed // photo_display_time) % total_photos
            image_path = os.path.join(PHOTO_DIR, photos[photo_index])
            img = Image.open(image_path)
            
            # Display photo and audio
            st.image(img, use_column_width=True)
            st.markdown(f"<p style='text-align:center; color:gray;'>Photo {photo_index + 1} of {total_photos}</p>", unsafe_allow_html=True)

            if os.path.exists(SLIDESHOW_SONG_PATH):
                if st.session_state.slideshow_audio_bytes is None:
                    with open(SLIDESHOW_SONG_PATH, "rb") as f:
                        st.session_state.slideshow_audio_bytes = f.read()
                st.audio(st.session_state.slideshow_audio_bytes, format="audio/mp3", start_time=elapsed)
            else:
                st.warning("Slideshow song not found!")

    # --- Cake Surprise ---
    elif choice == "Cake Surprise":
        st.markdown("<h1 style='text-align:center; color:red;'>HAPPY 21ST BIRTHDAY MY LOVE ❤️</h1>", unsafe_allow_html=True)
        
        # Display static cake image
        if os.path.exists(CAKE_IMAGE_PATH):
            st.image(CAKE_IMAGE_PATH, use_column_width=True)
        else:
            st.warning("Cake image not found! Make sure HARSHICAKE.png is in the repo.")

        # Play birthday song
        if os.path.exists(CAKE_SONG_PATH):
            st.audio(CAKE_SONG_PATH, format="audio/mp3", start_time=0)
        else:
            st.warning("Birthday song not found!")
