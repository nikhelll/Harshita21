# -*- coding: utf-8 -*-
"""
Harshita's Birthday Surprise Page with Menu + Auto Slideshow + Cake Surprise
"""

import streamlit as st
from datetime import datetime
from PIL import Image
import os
import time
from streamlit_autorefresh import st_autorefresh

# --- Paths ---
IMAGE_PATH = "MANCHURIAN.jpg"
PHOTO_DIR = "."  # all photos in repo root

SLIDESHOW_SONG_PATH = "yt1z.net - Gryffin - Nobody Compares To You (Official Music Video) ft. Katie Pearlman (320 KBps).mp3"
CAKE_SONG_PATH = "HAPPY Birthday Song, Happy Birthday to You.mp3"
CAKE_IMAGE_PATH = "HARSHICAKE.png"

CORRECT_CODE = "8891"
SLIDESHOW_SONG_LENGTH_SECONDS = 231

# --- Initialize session state ---
if "unlocked" not in st.session_state:
    st.session_state.unlocked = False
if "slideshow_audio_bytes" not in st.session_state:
    st.session_state.slideshow_audio_bytes = None

# --- Page Setup ---
st.set_page_config(page_title="Harshita's 21st Birthday!", page_icon="🎂", layout="centered")
st.markdown("<h1 style='text-align:center;'>🎉 Harshita's 21st Birthday 🎉</h1>", unsafe_allow_html=True)

# --- Secret Code Page ---
def show_secret_code():
    st.markdown("<h3 style='text-align:center;'>Enter the Secret Code to Unlock a Surprise 🔐</h3>", unsafe_allow_html=True)
    code_input = st.text_input("Secret Code", type="password", max_chars=4, key="code_input")
    if st.button("Unlock"):
        if code_input == CORRECT_CODE:
            st.session_state.unlocked = True
            st.success("Unlocked! 💖")
        else:
            st.error("Wrong code. Try again!")

    # Show cover image while locked
    if os.path.exists(IMAGE_PATH):
        img = Image.open(IMAGE_PATH)
        st.image(img, use_column_width=True)

# --- Main Menu ---
def show_main_menu():
    st.markdown("<h3 style='text-align:center;'>Choose Your Surprise 💌</h3>", unsafe_allow_html=True)
    choice = st.radio("", ["Love Letter", "Photo Slideshow + Song", "Cake Surprise"])

    # --- Love Letter ---
    if choice == "Love Letter":
        st.markdown("<h3 style='color:#6A0572;'>A Love Letter Just For You</h3>", unsafe_allow_html=True)
        st.write("""
On this day, 21 years ago, the most precious girl was born. Fast forward to today, Happy Birthday my beautiful girlfriend. You're 21 now, and trust me, 21 never looked better. Every time I see you, I am reminded of how extraordinary you are — not just in your beauty, which leaves me breathless, but in your spirit, your laugh, your kindness, and the way your heart shines in every little thing you do. These past eight months together have been the most magical months of my life. Every moment spent with you feels like a treasure — from our long conversations, to the little jokes that only we understand, to the quiet moments where nothing needs to be said because just being near you is enough. Your laughter lights up my world, your smile warms my soul, and your eyes, my love, they hold a universe I could get lost in forever. You are stunning, not only in the way you look — though I could write a thousand words just on that — but in the way you carry yourself, in the way you treat others, and in the immense heart you show to everyone lucky enough to know you. Your beauty is complemented by your humor; your jokes, your witty remarks, the way you can make even the dullest moment feel alive — it’s one of the countless reasons I adore you. You have this magical combination of intelligence and kindness that makes people gravitate toward you, and I am the luckiest person alive to be the one who gets to call you mine. I know you sometimes doubt yourself, especially when it comes to your dream of going to law school. I see that self-doubt creeping in at times, and I want to tell you right now: you are more than ready. You are brilliant, passionate, determined, and compassionate — all the qualities of someone who will not only succeed but thrive in law school and beyond. I believe in you completely. Even on days when you may feel unsure, when you question your path, remember this: I see your potential, I see your drive, and I see the incredible impact you are destined to make on the world. You are capable of anything you set your mind to, and I will be by your side every step of the way, cheering you on louder than anyone else could. You are thoughtful, generous, and caring, always looking out for the people around you. I have seen it in the way you treat your friends and family, in the way you listen so attentively, and in the small acts of kindness that you do without anyone noticing. Your heart is one of your most beautiful qualities, and it makes me fall in love with you more deeply every day. I admire your courage, your intelligence, your curiosity, and the way you never stop striving to be your best self. You inspire me constantly to grow, to love, and to live fully. Being with you has taught me what it means to truly love someone. I have learned patience, empathy, and joy in ways I never imagined possible. I love the way we talk about everything and nothing, how we dream together, how we support each other, and how we can simply enjoy each other’s presence without any words at all. You have become my confidant, my partner, my love, and my best friend. Your love fills me up in ways I cannot even describe, and I hope you feel the same depth of love from me. On your 21st birthday, I want to celebrate not just the incredible person you are but also the journey you’ve been on — the challenges you’ve overcome, the dreams you’ve chased, the growth you’ve embraced, and the countless moments that have made you the extraordinary woman you are today. I want you to feel proud of yourself because I am endlessly proud of you. You have accomplished so much already, and yet I know this is only the beginning. Your future is luminous, full of potential, adventures, and victories — and I cannot wait to witness every moment. I love everything about you — your laughter, your tears, your quirks, your intelligence, your compassion, your strength. I love the way you light up a room just by being in it. I love the way you care deeply about your dreams and about the people around you. I love your ambition, your resilience, your ability to see the good in people, and your desire to make the world a better place. I love you for the person you are, for the person you are becoming, and for the love you give so freely. So today, I want to remind you of all the ways you are extraordinary. You are beautiful beyond words, intelligent beyond measure, and your heart is one of the most precious things I have ever known. Never doubt yourself, my love, because you are stronger, smarter, and more capable than you realize. Your dreams, including your path to law school, are within reach, and I have absolute faith that you will achieve everything you desire. And through it all, I will be here, supporting you, loving you, and celebrating every victory along the way. Happy 21st birthday, my love. May this year bring you happiness, adventure, growth, love, and fulfillment. May you always remember that you are cherished, adored, and admired beyond measure. You are my heart, my joy, my inspiration, and my forever. I cannot wait to continue building memories with you, laughing with you, dreaming with you, and loving you with all that I am. Forever and always, Nikhil
        """)

    # --- Photo Slideshow + Song ---
    elif choice == "Photo Slideshow + Song":
        photos = sorted([
            f for f in os.listdir(PHOTO_DIR)
            if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))
            and f not in {os.path.basename(CAKE_IMAGE_PATH), os.path.basename(IMAGE_PATH)}
        ])

        if not photos:
            st.info("No photos found for the slideshow.")
            return

        total_photos = len(photos)
        photo_display_time = SLIDESHOW_SONG_LENGTH_SECONDS / total_photos

        # auto-refresh every 1 second
        count = st_autorefresh(interval=1000, limit=None, key="slideshow_refresh")
        photo_index = count % total_photos
        image_path = os.path.join(PHOTO_DIR, photos[photo_index])
        img = Image.open(image_path)
        st.image(img, use_column_width=True)
        st.markdown(f"<p style='text-align:center; color:gray;'>Photo {photo_index + 1} of {total_photos}</p>", unsafe_allow_html=True)

        # Play slideshow song
        if os.path.exists(SLIDESHOW_SONG_PATH):
            if st.session_state.slideshow_audio_bytes is None:
                with open(SLIDESHOW_SONG_PATH, "rb") as f:
                    st.session_state.slideshow_audio_bytes = f.read()
            st.audio(st.session_state.slideshow_audio_bytes, format="audio/mp3")
        else:
            st.warning("Slideshow song not found! Make sure the file is in the repo.")

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
            st.warning("Birthday song not found! Make sure the file is in the repo.")

# --- Main Logic ---
if not st.session_state.unlocked:
    show_secret_code()
else:
    show_main_menu()
