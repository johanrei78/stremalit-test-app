import streamlit as st
import pandas as pd
import matplotlib
matplotlib.use("Agg")  # trygg backend på Streamlit Cloud
import matplotlib.pyplot as plt
from PIL import Image

st.title("📊 Resultater fra simulering")

# Sjekk at nødvendige session_state-variabler finnes
if "mor_img" not in st.session_state or \
   "far_img" not in st.session_state or \
   "resultater" not in st.session_state:
    
    st.warning("Du må starte simulering fra Startside først!")
    st.stop()  # stopper rendering her

# Tilbakeknapp
if st.button("🔙 Tilbake til start"):
    st.switch_page("Home.py")

# To kolonner: bilder og diagram
col1, col2 = st.columns([1, 2], vertical_alignment="center")

with col1:
    st.image(st.session_state.mor_img, caption="Mor", width=150)
    st.image(st.session_state.far_img, caption="Far", width=150)

with col2:
    plt.rcParams.update({
        "axes.titlesize": 9,
        "axes.labelsize": 8,
        "xtick.labelsize": 7,
        "ytick.labelsize": 7
    })
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.bar(st.session_state.resultater.keys(),
           st.session_state.resultater.values(),
           color=["red", "white", "red", "white"], edgecolor="black")
    ax.set_ylabel("Antall avkom")
    ax.set_title("Fenotypefordeling")
    st.pyplot(fig)

# Tabell under
df = pd.DataFrame({
    "Fenotype": list(st.session_state.resultater.keys()),
    "Antall": list(st.session_state.resultater.values())
})
st.subheader("Resultattabell")
st.table(df)
