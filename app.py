# app.py — manageme: שלד ראשי + עיצוב קליל (RiseUp-ish)
from __future__ import annotations
import streamlit as st

st.set_page_config(page_title="manageme – ניהול כספי בית", page_icon="🟡", layout="centered")

# ===== RTL + עיצוב גלובלי קליל =====
st.markdown('''
<style>
@import url('https://fonts.googleapis.com/css2?family=Rubik:wght@300;400;600;800&display=swap');

/* צבעים עדינים */
:root{
  --yellow:#FFD84D;        /* צהוב רך */
  --yellow-100:#FFF7CC;    /* צהוב בהיר */
  --purple:#6C63FF;        /* סגול דגש */
  --ink:#111827;           /* טקסט */
  --muted:#6B7280;         /* אפור טקסט */
  --line:#ECEFF3;          /* קווי מתאר עדינים */
  --surface:#ffffff;       /* לבן */
}

/* RTL + טיפוגרפיה + רוחב ממורכז */
html, body, .main, .block-container{direction:rtl;}
.main .block-container{
  font-family:"Rubik",-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;
  max-width: 720px;   /* מובייל+ */
  padding-top: 0.6rem;
}

/* רקע כללי בהיר עם פס צהוב עדין למעלה */
body
