# app.py — manageme: שלד ראשי + עיצוב RiseUp-style
from __future__ import annotations
import streamlit as st

st.set_page_config(page_title="manageme – ניהול כספי בית", page_icon="🟡", layout="wide")

# ===== RTL + עיצוב גלובלי =====
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Rubik:wght@300;400;700;900&display=swap');

/* צבעים */
:root{
  --yellow:#FFD12A;          /* צהוב חם ל-CTAs ודגשים */
  --purple:#5B6EF5;          /* סגול Hero */
  --ink:#0f172a;             /* טקסט */
  --muted:#6b7280;           /* משני */
  --surface:#ffffff;         /* לבן */
  --line:#E7EBF0;            /* גבולות עדינים */
}

/* RTL וטיפוגרפיה */
html, body, .main, .block-container{direction:rtl;}
.main .block-container{font-family:"Rubik",-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;}

/* רקע כללי נקי + מסגרת שחורה */
body{ background:var(--surface); border:4px solid #000; border-radius:16px; margin:10px; }

/* Hero סגול עליון */
.hero{
  background:var(--purple);
  color:#fff;
  border-radius:24px;
  padding:22px 18px;
  margin:6px 0 18px 0;
  box-shadow:0 8px 24px rgba(0,0,0,.10);
}
.hero .title{ font-weight:900; font-size:30px; line-height:1.15; margin:0; }
.hero .kicker{ opacity:.9; margin-top:6px; font-weight:700; }

/* כרטיסים */
.card{
  background:#fff; border:1px solid var(--line); border-radius:18px;
  padding:16px; box-shadow:0 8px 24px rgba(0,0,0,.06); margin-bottom:14px;
}

/* כפתור ראשי שחור בסגנון RiseUp */
.btn-primary > button{
  width:100%; border-radius:999px; padding:14px 16px;
  background:#111 !important; color:#fff !important; border:0 !important; font-weight:900 !important;
}
.btn-primary > button:hover{ filter:brightness(1.05); }

/* כפתורי פיל (לרדיואים/בחירות) */
.stRadio label{
  display:block !important; border:2px solid var(--line); border-radius:999px !important;
  padding:12px 14px !important; margin:8px 0; font-weight:800 !important;
  box-shadow:0 4px 14px rgba(0,0,0,.04);
}
.stRadio [role="radio"][aria-checked="true"] + div > label{
  border-color:var(--purple) !important; background:#f4f5ff !important; color:#111 !important;
}

/* קלט סכום — גדול ומודגש */
.amount input{
  font-size:28px !important; font-weight:900 !important; text-align:center !important; height:56px !important;
}

/* Selectים ושדות */
.stSelectbox div[data-baseweb="select"],
.stTextInput input, .stTextArea textarea{
  border-radius:14px !important; border:1px solid var(--line) !important; background:#fff !important; color:var(--ink) !important;
}
.stSelectbox div[data-baseweb="select"]:focus-within,
.stTextInput input:focus, .stTextArea textarea:focus{
  box-shadow:0 0 0 3px rgba(91,110,245,.25) !important; border-color:var(--purple) !important;
}

/* הסתרת “Press Enter to apply” */
div[data-testid="stWidgetInstructions"]{display:none !important;}
</style>
""", unsafe_allow_html=True)

# Hero קבוע בראש כל דף
st.markdown("""
<div class="hero">
  <p class="title">manageme — שליטה פשוטה בכסף של הבית</p>
  <div class="kicker">נתחיל בהזנת הוצאה, ונוסיף סריקת חשבוניות בהמשך</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.write("השתמש/י בתפריט הצד כדי לעבור ל־**הזנת הוצאות**. העיצוב מותאם למובייל: כפתורי פיל, כותרות גדולות ורכיבים נוחים.")
st.markdown('</div>', unsafe_allow_html=True)
