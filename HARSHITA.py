# -*- coding: utf-8 -*-
"""
Harshita's Birthday Surprise Page with Menu + Auto Slideshow
"""

import streamlit as st
from datetime import datetime
import os
from PIL import Image
import time
import plotly.graph_objects as go
import numpy as np

# For auto-refresh
try:
    from streamlit_autorefresh import st_autorefresh
except:
    st.warning("Install streamlit_autorefresh: pip install streamlit-autorefresh")

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
SONG_LENGTH_SECONDS = 231  # adjust for your song

# --- Initialize session state ---
if "unlocked" not in st.session_state:
    st.session_state.unlocked = False
if "audio_bytes" not in st.session_state:
    st.session_state.audio_bytes = None
if "slideshow_start_time" not in st.session_state:
    st.session_state.slideshow_start_time = None

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
    choice = st.radio("", ("Love Letter", "Photo Slideshow + Song", "View Cake"))
    return choice


# --- Love Letter ---
def show_love_letter():
    love_letter = """
On this day, 21 years ago, the most precious girl was born. Fast forward to today, Happy Birthday my beautiful girlfriend. You're 21 now, and trust me, 21 never looked better. Every time I see you, I am reminded of how extraordinary you are — not just in your beauty, which leaves me breathless, but in your spirit, your laugh, your kindness, and the way your heart shines in every little thing you do.

These past eight months together have been the most magical months of my life. Every moment spent with you feels like a treasure — from our long conversations, to the little jokes that only we understand, to the quiet moments where nothing needs to be said because just being near you is enough. Your laughter lights up my world, your smile warms my soul, and your eyes, my love, they hold a universe I could get lost in forever.

You are stunning, not only in the way you look — though I could write a thousand words just on that — but in the way you carry yourself, in the way you treat others, and in the immense heart you show to everyone lucky enough to know you. Your beauty is complemented by your humor; your jokes, your witty remarks, the way you can make even the dullest moment feel alive — it’s one of the countless reasons I adore you. You have this magical combination of intelligence and kindness that makes people gravitate toward you, and I am the luckiest person alive to be the one who gets to call you mine.

I know you sometimes doubt yourself, especially when it comes to your dream of going to law school. I see that self-doubt creeping in at times, and I want to tell you right now: you are more than ready. You are brilliant, passionate, determined, and compassionate — all the qualities of someone who will not only succeed but thrive in law school and beyond. I believe in you completely. Even on days when you may feel unsure, when you question your path, remember this: I see your potential, I see your drive, and I see the incredible impact you are destined to make on the world. You are capable of anything you set your mind to, and I will be by your side every step of the way, cheering you on louder than anyone else could.

You are thoughtful, generous, and caring, always looking out for the people around you. I have seen it in the way you treat your friends and family, in the way you listen so attentively, and in the small acts of kindness that you do without anyone noticing. Your heart is one of your most beautiful qualities, and it makes me fall in love with you more deeply every day. I admire your courage, your intelligence, your curiosity, and the way you never stop striving to be your best self. You inspire me constantly to grow, to love, and to live fully.

Being with you has taught me what it means to truly love someone. I have learned patience, empathy, and joy in ways I never imagined possible. I love the way we talk about everything and nothing, how we dream together, how we support each other, and how we can simply enjoy each other’s presence without any words at all. You have become my confidant, my partner, my love, and my best friend. Your love fills me up in ways I cannot even describe, and I hope you feel the same depth of love from me.

On your 21st birthday, I want to celebrate not just the incredible person you are but also the journey you’ve been on — the challenges you’ve overcome, the dreams you’ve chased, the growth you’ve embraced, and the countless moments that have made you the extraordinary woman you are today. I want you to feel proud of yourself because I am endlessly proud of you. You have accomplished so much already, and yet I know this is only the beginning. Your future is luminous, full of potential, adventures, and victories — and I cannot wait to witness every moment.

I love everything about you — your laughter, your tears, your quirks, your intelligence, your compassion, your strength. I love the way you light up a room just by being in it. I love the way you care deeply about your dreams and about the people around you. I love your ambition, your resilience, your ability to see the good in people, and your desire to make the world a better place. I love you for the person you are, for the person you are becoming, and for the love you give so freely.

So today, I want to remind you of all the ways you are extraordinary. You are beautiful beyond words, intelligent beyond measure, and your heart is one of the most precious things I have ever known. Never doubt yourself, my love, because you are stronger, smarter, and more capable than you realize. Your dreams, including your path to law school, are within reach, and I have absolute faith that you will achieve everything you desire. And through it all, I will be here, supporting you, loving you, and celebrating every victory along the way.

Happy 21st birthday, my love. May this year bring you happiness, adventure, growth, love, and fulfillment. May you always remember that you are cherished, adored, and admired beyond measure. You are my heart, my joy, my inspiration, and my forever. I cannot wait to continue building memories with you, laughing with you, dreaming with you, and loving you with all that I am.

Forever and always,  
Nikhil
"""

    st.markdown("<h3 style='color:#6A0572;'>A Love Letter Just For You</h3>", unsafe_allow_html=True)
    st.write(love_letter)

# --- Slideshow + Song ---
def show_slideshow():
    # Auto-refresh every 1 second
    st_autorefresh(interval=1000, key="slideshow_refresh")

    # Load photos
    photos = sorted([f for f in os.listdir(PHOTO_DIR) if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))])
    if not photos:
        st.info("No photos found for the slideshow.")
        return

    total_photos = len(photos)
    photo_display_time = SONG_LENGTH_SECONDS / total_photos

    # Load audio once
    if st.session_state.audio_bytes is None:
        if os.path.exists(SONG_PATH):
            with open(SONG_PATH, "rb") as f:
                st.session_state.audio_bytes = f.read()
        else:
            st.warning("Song file not found!")
            return

    # Set slideshow start time once
    if st.session_state.slideshow_start_time is None:
        st.session_state.slideshow_start_time = time.time()

    elapsed = time.time() - st.session_state.slideshow_start_time
    photo_index = int(elapsed // photo_display_time) % total_photos
    image_path = os.path.join(PHOTO_DIR, photos[photo_index])
    img = Image.open(image_path)

    st.audio(st.session_state.audio_bytes, format="audio/mp3", start_time=elapsed)
    st.image(img, use_column_width=True)
    st.markdown(f"<p style='text-align:center; color:gray;'>Photo {photo_index + 1} of {total_photos}</p>", unsafe_allow_html=True)

def show_cake():
    st.markdown("<h3 style='text-align:center; color:#D2691E;'>🎂 Your 3D Chocolate Cake! 🎂</h3>", unsafe_allow_html=True)

    # Cake parameters
    cake_radius = 1
    cake_height = 1
    layers = 3
    layer_height = cake_height / layers

    fig = go.Figure()
    theta = np.linspace(0, 2*np.pi, 50)
    x = cake_radius * np.cos(theta)
    y = cake_radius * np.sin(theta)

    # Cake layers
    for i in range(layers):
        z = np.full_like(theta, i * layer_height)
        fig.add_trace(go.Scatter3d(
            x=x, y=y, z=z,
            mode='lines',
            line=dict(color='saddlebrown', width=10),
            showlegend=False
        ))
        fig.add_trace(go.Scatter3d(
            x=x, y=y, z=z + layer_height,
            mode='lines',
            line=dict(color='peru', width=10),
            showlegend=False
        ))

    # Top surface
    fig.add_trace(go.Mesh3d(
        x=np.append(x, 0), y=np.append(y, 0), z=np.append(np.full_like(x, cake_height), cake_height),
        color='saddlebrown', opacity=0.9
    ))

    # Function to add candle
    def add_candle(x_pos, y_pos, candle_height=0.2, candle_radius=0.03):
        phi = np.linspace(0, 2*np.pi, 20)
        x_c = x_pos + candle_radius * np.cos(phi)
        y_c = y_pos + candle_radius * np.sin(phi)
        z_c = np.zeros_like(phi)
        fig.add_trace(go.Mesh3d(
            x=np.concatenate([x_c, [x_pos]]),
            y=np.concatenate([y_c, [y_pos]]),
            z=np.concatenate([z_c + cake_height, np.full(1, cake_height + candle_height)]),
            color='white',
            opacity=1.0
        ))
        # Flame as small marker
        flame_height = candle_height * 0.3
        fig.add_trace(go.Scatter3d(
            x=[x_pos],
            y=[y_pos],
            z=[cake_height + candle_height + flame_height],
            mode='markers',
            marker=dict(size=5, color='orange'),
            showlegend=False
        ))

    # Candles for "21"
    add_candle(-0.3, 0.2)  # '2'
    add_candle(-0.1, 0.2)  # '2'
    add_candle(0.25, 0.2)  # '1'

    fig.update_layout(scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        aspectratio=dict(x=1, y=1, z=0.6)
    ))

    st.plotly_chart(fig)


# --- Main ---
if st.session_state.unlocked:
    choice = show_menu()
    if choice == "Love Letter":
        show_love_letter()
    elif choice == "Photo Slideshow + Song":
        show_slideshow()
    elif choice == "View Cake":
        show_cake()
else:
    show_landing_page()


