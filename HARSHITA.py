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

SLIDESHOW_SONG_PATH = "slideshow.mp3"       # make sure this file exists
CAKE_SONG_PATH = "birthday.mp3"             # make sure this file exists
CAKE_IMAGE_PATH = "HARSHICAKE.png"          # static cake image

CORRECT_CODE = "8891"
SLIDESHOW_SONG_LENGTH_SECONDS = 231  # adjust for your song duration

# --- Initialize session state ---
if "unlocked" not in st.session_state:
    st.session_state.unlocked = False
if "slideshow_audio_bytes" not in st.session_state:
    st.session_state.slideshow_audio_bytes = None
if "slideshow_start_time" not in st.session_state:
    st.session_state.slideshow_start_time = None

# --- Page Setup ---
st.set_page_config(
    page_title="Harshita's 21st Birthday!",
    page_icon="🎂",
    layout="centered"
)

st.markdown("<h1 style='text-align:center;'>🎉 Harshita's 21st Birthday 🎉</h1>", unsafe_allow_html=True)

# --- Secret Code Page ---
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

# --- Main Menu ---
else:
    st.markdown("<h3 style='text-align:center;'>Choose Your Surprise 💌</h3>", unsafe_allow_html=True)
    choice = st.radio("", ["Love Letter", "Photo Slideshow + Song", "Cake Surprise"])

    # --- Love Letter ---
    if choice == "Love Letter":
        st.markdown("<h3 style='color:#6A0572;'>A Love Letter Just For You</h3>", unsafe_allow_html=True)
        st.write("Your full love letter here...")

    # --- Photo Slideshow + Song ---
    elif choice == "Photo Slideshow + Song":
        photos = sorted(
            [f for f in os.listdir(PHOTO_DIR)
             if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))
             and f not in [os.path.basename(CAKE_IMAGE_PATH), os.path.basename(IMAGE_PATH)]]
        )

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
            
            st.image(img, use_column_width=True)
            st.markdown(f"<p style='text-align:center; color:gray;'>Photo {photo_index + 1} of {total_photos}</p>", unsafe_allow_html=True)

            # Load slideshow song
            if os.path.exists(SLIDESHOW_SONG_PATH):
                if st.session_state.slideshow_audio_bytes is None:
                    with open(SLIDESHOW_SONG_PATH, "rb") as f:
                        st.session_state.slideshow_audio_bytes = f.read()
                st.audio(st.session_state.slideshow_audio_bytes, format="audio/mp3", start_time=elapsed)
            else:
                st.warning("Slideshow song not found! Make sure 'slideshow.mp3' is in the repo.")

    # --- Cake Surprise ---
    elif choice == "Cake Surprise":
        st.markdown("<h1 style='text-align:center; color:red;'>HAPPY 21ST BIRTHDAY MY LOVE ❤️</h1>", unsafe_allow_html=True)
        
        if os.path.exists(CAKE_IMAGE_PATH):
            st.image(CAKE_IMAGE_PATH, use_column_width=True)
        else:
            st.warning("Cake image not found! Make sure HARSHICAKE.png is in the repo.")

        if os.path.exists(CAKE_SONG_PATH):
            st.audio(CAKE_SONG_PATH, format="audio/mp3", start_time=0)
        else:
            st.warning("Birthday song not found! Make sure 'birthday.mp3' is in the repo.")
