# app.py — manageme: שלד ראשי + עיצוב קליל וצבעוני
from __future__ import annotations
import streamlit as st

st.set_page_config(page_title="manageme – ניהול כספי בית", page_icon="🟡", layout="centered")

# ===== RTL + עיצוב גלובלי קליל =====
st.markdown('''
<style>
/* טיפוגרפיה עברית קלה */
@import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;600;700&display=swap');

:root{
  --bg:#ffffff;
  --ink:#111827;           /* טקסט ראשי */
  --muted:#6B7280;         /* טקסט משני */
  --line:#E7EBF0;          /* קווי מתאר עדינים */

  --primary:#6E8BFF;       /* סגול-כחלחל עדין */
  --primary-100:#EEF2FF;   /* רקע פסטלי לסגול */
  --accent:#FFE279;        /* צהוב רך להדגשות */
  --accent-100:#FFF9DB;    /* צהוב בהיר */
}

/* RTL + רוחב ממורכז */
html, body, .main, .block-container{direction:rtl;}
.main .block-container{
  font-family:"Heebo",-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;
  max-width: 720px;
  padding-top: .4rem;
  color: var(--ink);
  background: var(--bg);
}

/* רקע עדין עם גרדיאנט פסטלי בראש הדף */
body{
  background:
    radial-gradient(1200px 300px at 50% 0%, var(--primary-100) 0%, rgba(238,242,255,0) 70%) ,
    var(--bg);
}

/* טייטלים כלליים — פחות כבדים */
h1,h2,h3{ font-weight:700; letter-spacing:-.2px; color:var(--ink); }
h1{ font-size: clamp(22px, 4.5vw, 34px); }
h2{ font-size: clamp(18px, 3.4vw, 26px); }
h3{ font-size: clamp(16px, 3vw, 22px); }

/* HERO קליל צבעוני */
.hero{
  border-radius:16px;
  padding:18px 16px 12px;
  margin:6px 0 12px;
  background: linear-gradient(135deg, var(--primary-100), var(--accent-100));
  border: 1px solid var(--line);
}
.hero .title{
  font-weight:700; color:var(--ink);
  display:inline-block; position:relative; padding:0 .35rem;
  font-size: clamp(20px, 4.2vw, 30px);
}
.hero .title:after{
  content:""; position:absolute; left:0; right:0; bottom:-3px; height:8px;
  background: var(--accent-100); z-index:-1; border-radius:6px;
}
.hero .kicker{ color:var(--muted); margin-top:6px; font-weight:500; }

/* כרטיסים קלילים */
.card{
  background:#fff; border:1px solid var(--line); border-radius:14px;
  padding:14px; box-shadow:0 2px 10px rgba(0,0,0,.04); margin-bottom:12px;
}

/* שדות וקומפוננטים — קווים דקים ופוקוס עדין */
.stSelectbox div[data-baseweb="select"],
.stTextInput input, .stTextArea textarea{
  border-radius:12px !important; border:1px solid var(--line) !important;
  background:#fff !important; color:var(--ink) !important;
}
.stSelectbox div[data-baseweb="select"]:focus-within,
.stTextInput input:focus, .stTextArea textarea:focus{
  box-shadow:0 0 0 3px rgba(110,139,255,.20) !important; border-color:var(--primary) !important;
}

/* קלט סכום — גדול אך לא “צועק” */
input[type="number"]{
  font-size:22px !important; font-weight:700 !important; text-align:center !important; height:50px !important;
}

/* רדיו בצורת פיל — קליל */
.stRadio label{
  display:block !important; border:1px solid var(--line); border-radius:999px !important;
  padding:10px 14px !important; margin:6px 0; font-weight:600 !important; color:var(--ink);
  background:#fff;
}
.stRadio [role="radio"][aria-checked="true"] + div > label{
  border-color:var(--primary) !important; background:var(--primary-100) !important; color:#0f172a !important;
}

/* כפתור ראשי — צהוב רך עם טקסט שחור */
.btn-primary > button{
  width:100%; border-radius:999px; padding:12px 16px;
  background:var(--accent) !important; color:#111 !important; border:1px solid #00000010 !important;
  font-weight:700 !important;
}
.btn-primary > button:hover{ filter:brightness(1.03); }

/* טוסט ירוק עדין */
.big-toast{
  position:fixed; left:50%; bottom:18px; transform:translateX(-50%);
  background:#fff; border:2px solid #22c55e; border-radius:14px;
  padding:10px 14px; font-weight:700; font-size:16px; color:#14532d;
  box-shadow:0 8px 28px rgba(0,0,0,.10); z-index:9999; display:flex; align-items:center; gap:10px;
}
.big-toast .close{ border:0; background:transparent; cursor:pointer; color:#14532d; font-weight:900; }

/* הסתרת “Press Enter to apply” */
div[data-testid="stWidgetInstructions"]{display:none !important;}
</style>
''', unsafe_allow_html=True)

# HERO
st.markdown('''
<div class="hero">
  <div class="title">manageme — בוא/י ננהל את הכסף בפשטות</div>
  <div class="kicker">עיצוב פסטלי קליל, מותאם מובייל. התחלה בהזנת הוצאות, ובהמשך סריקת חשבוניות וניתוח חכם.</div>
</div>
''', unsafe_allow_html=True)

st.markdown('''
<div class="card">
  השתמש/י בתפריט הצד כדי לעבור ל־<b>הזנת הוצאות</b>.  
  נשמור את הלוגיקה כמו שהיא — רק הלוק־אנד־פיל הותאם לצבעים ולטיפוגרפיה קלילה.
</div>
''', unsafe_allow_html=True)
