# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 14:20:25 2025

@author: johvik
"""

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.title("📊 Resultater fra simulering")

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
           color=["red", "white", "red", "white"],edgecolor="black")
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