# streamlit_page: name="Startside", icon="🏠"

import os
import streamlit as st
from PIL import Image
from genetikk import generer_mor, generer_far, simuler_avkom

# --- Initialiser session_state variabler ---
if "mor_img" not in st.session_state:
    st.session_state.mor_img = None
if "far_img" not in st.session_state:
    st.session_state.far_img = None
if "resultater" not in st.session_state:
    st.session_state.resultater = {}

# Filsti
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BILDEMAPPE = os.path.join(BASE_DIR, "bilder")

st.title("🐝 Bananflue-simulator")

# Mor og far i kolonner
col1, col2 = st.columns(2)
with col1:
    mor_fenotype = st.radio("Velg fenotype for mor", ["røde øyne", "hvite øyne"], horizontal=True)
    mor_bilde = "bananflue_rod.png" if mor_fenotype == "røde øyne" else "bananflue_hvit.png"
    mor_img = Image.open(os.path.join(BILDEMAPPE, mor_bilde))
    st.image(mor_img, caption=f"{mor_fenotype.capitalize()} hunn", width=200)

with col2:
    far_fenotype = st.radio("Velg fenotype for far", ["røde øyne", "hvite øyne"], horizontal=True)
    far_bilde = "bananflue_rod.png" if far_fenotype == "røde øyne" else "bananflue_hvit.png"
    far_img = Image.open(os.path.join(BILDEMAPPE, far_bilde))
    st.image(far_img, caption=f"{far_fenotype.capitalize()} hann", width=200)

# Antall avkom
st.markdown("---")
st.subheader("Avkom")
antall = st.selectbox("Velg antall avkom", [10, 100, 1000])

# Start knapp
if st.button("🚀 Start simulering", use_container_width=True):
    mor = generer_mor(mor_fenotype)
    far = generer_far(far_fenotype)
    st.session_state.resultater = simuler_avkom(mor, far, antall)
    st.session_state.mor_img = mor_img
    st.session_state.far_img = far_img
    st.switch_page("pages/Resultater.py")

# Stil på knappen
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        height: 3em;
        border-radius: 10px;
    }
    div.stButton > button:first-child:hover {
        background-color: #45a049;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)
