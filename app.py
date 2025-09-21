# app.py — manageme: שלד ראשי + עיצוב בסיסי
from __future__ import annotations
import streamlit as st

st.set_page_config(page_title="manageme – ניהול כספי בית", page_icon="🟢", layout="wide")

# ===== RTL + עיצוב כללי =====
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Rubik:wght@300;400;700;900&display=swap');
html, body, .main, .block-container{direction:rtl;}
.main .block-container{font-family:"Rubik",-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;}
body{ border:4px solid #000; border-radius:16px; margin:10px; background:#fff; }
.header{background:#ecfdf5; border:1px solid #d1fae5; border-radius:18px; padding:18px; text-align:center; margin-bottom:14px;}
.header .title{font-weight:900; font-size:28px; margin:0; color:#0f172a;}
.card{background:#fff; border:1px solid #e7ebf0; border-radius:16px; padding:16px; box-shadow:0 4px 18px rgba(10,20,40,.04); margin-bottom:12px;}
.stRadio [data-baseweb="radio"] svg{ color:#000 !important; fill:#000 !important; }
div[data-testid="stWidgetInstructions"]{display:none !important;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="header"><p class="title">manageme — ניהול כלכלי למשק בית</p></div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.write("👋 ברוכים הבאים! השתמש/י בתפריט הצד כדי לעבור ל־**הזנת הוצאות**.")
st.write("בשלב הבא נוסיף: סריקת חשבוניות, דשבורד, ניהול תקציב וניתוחים חכמים.")
st.markdown('</div>', unsafe_allow_html=True)
