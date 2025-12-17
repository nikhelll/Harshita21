# -*- coding: utf-8 -*-
"""
Harshita's 21st Birthday Surprise Page
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
PHOTO_DIR = "."  # All photos are in the repo root
SONG_PATH = "yt1z.net - Gryffin - Nobody Compares To You (Official Music Video) ft. Katie Pearlman (320 KBps).mp3"
CAKE_IMAGE_PATH = "triple_chocolate_cake.jpg"  # Use a pre-rendered image of cake

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

    code_input = st.text_input("🔢 Enter 4-digit Secret Code", type="password", max_chars=4, key="code_input")

    if code_input and not st.session_state.get("unlocked", False):
        if code_input == CORRECT_CODE:
            st.success("🔓 Unlocked! You're amazing for figuring it out. 💖")
            st.session_state.unlocked = True
            st.session_state.rerun_trigger = random.random()  # Force rerun
        else:
            st.error("❌ That's not the right code. Try again?")

    # Show main image
    if os.path.exists(IMAGE_PATH):
        image = Image.open(IMAGE_PATH)
        st.markdown("---")
        st.image(image, caption="Your Favourite 😉", use_column_width=True)
    else:
        st.warning("Couldn't find MANCHURIAN.jpg in the repo.")

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

def show_love_letter():
    love_letter = """
Dear Harshita,

On this beautiful day, your 21st birthday, I want to pause for a moment and tell you just how much you mean to me. Words often feel inadequate when I try to express my feelings for you, but I’m going to try anyway because you deserve to hear them.

From the moment we started this journey together eight months ago, my life has been brighter, fuller, and more meaningful. Every laugh we’ve shared, every conversation, every quiet moment, every silly joke—we’ve built a world together in such a short time, and it feels like I’ve known you forever. You’ve shown me what it means to care deeply, to love fearlessly, and to be patient, understanding, and kind, not only to me but to everyone around you.

Today, as you celebrate your 21st birthday, I want you to know how proud I am of you. I see all the effort you put into your dreams, all the moments you doubt yourself, and all the times you push through challenges even when it’s hard. I know you sometimes worry about whether you’ll get into law school or whether you’re ready for the next step in your journey—but let me tell you this: you are more than ready. You have the brilliance, the determination, the courage, and the heart of someone who is destined to make a difference. I have never doubted for a single second that you will achieve everything you set your mind to, and I will be by your side cheering you on every step of the way.

These past eight months have been a journey of joy and love for me. I’ve fallen in love with every part of you—the way you laugh, the way your eyes light up when you’re excited, the way your heart is so big and so full of care for others. You have a strength and a beauty that leave me in awe every day. I never imagined that someone could make me feel this much love, but you’ve done it effortlessly, naturally, and completely.

On this special day, I hope you feel just how cherished you are. I hope you know that every smile, every moment, every heartbeat between us is a gift I treasure endlessly. Today is about celebrating you—not just for the amazing person you are, but for everything you’ve endured, accomplished, and dreamed of. I’m so lucky that I get to be a part of your life while all of that unfolds.

I want you to promise me something: that even on days when you feel small, unsure, or overwhelmed, you’ll remember this moment and the love that surrounds you. You’re never alone. You’re never unloved. You are extraordinary in ways you cannot even imagine. Your potential is limitless, and your heart is more beautiful than words can ever describe.

Happy 21st birthday, my love. I can’t wait to see the amazing things this year brings for you, for us, and for the life you’re building. Thank you for letting me be a part of your life, for trusting me, for loving me, and for being you—so perfectly, wonderfully, you.

I love you more than I could ever put into words. You are my heart, my joy, my everything, and I am so proud of the person you are and the person you are becoming.

Forever and always,
Nikhil (Your Man)!
    """
    st.markdown("<h3 style='color:#6A0572;'>A Love Letter Just For You</h3>", unsafe_allow_html=True)
    st.write(love_letter)

def show_slideshow():
    photos = sorted([f for f in os.listdir(PHOTO_DIR) if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))])

    if photos:
        total_photos = len(photos)
        song_length_seconds = 231  # update if needed
        photo_display_time = song_length_seconds / total_photos

        # Audio control
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
        if st.session_state.audio_bytes:
            st.audio(st.session_state.audio_bytes, format="audio/mp3", start_time=elapsed)
    else:
        st.info("No photos found for the slideshow.")

def show_cake():
    if os.path.exists(CAKE_IMAGE_PATH):
        img = Image.open(CAKE_IMAGE_PATH)
        st.markdown("<h3 style='color:#6A0572;'>🎂 Triple Chocolate Cake Just For You!</h3>", unsafe_allow_html=True)
        st.image(img, use_column_width=True)
    else:
        st.warning("Cake image not found. Make sure triple_chocolate_cake.jpg is in the repo.")

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
