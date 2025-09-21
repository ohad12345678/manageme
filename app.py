# app.py — manageme: שלד ראשי + עיצוב קליל (RiseUp-ish)
from __future__ import annotations
import streamlit as st

st.set_page_config(page_title="manageme – ניהול כספי בית", page_icon="🟡", layout="centered")

# ===== RTL + עיצוב גלובלי קליל =====
st.markdown("""
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
body{
  background:
    linear-gradient(180deg, rgba(255,216,77,.25) 0%, rgba(255,216,77,0) 180px),
    #fff;
}

/* Hero עדין — טקסט שחור, היילייט צהוב */
.hero{
  border-radius:18px;
  padding:18px 16px 8px 16px;
  margin:4px 0 10px 0;
}
.hero .title{
  font-weight:800; font-size:26px; line-height:1.15; color:var(--ink);
  display:inline-block; position:relative; padding:0 6px;
}
.hero .title:after{
  content:""; position:absolute; left:0; right:0; bottom:-2px; height:10px;
  background:var(--yellow-100); z-index:-1; border-radius:8px;
}
.hero .kicker{ color:var(--muted); margin-top:6px; }

/* כרטיסים מאוד קלים */
.card{
  background:#fff; border:1px solid var(--line); border-radius:16px;
  padding:14px; box-shadow:0 2px 8px rgba(0,0,0,.06); margin-bottom:12px;
}

/* כפתור ראשי — צהוב עם טקסט שחור */
.btn-primary > button{
  width:100%; border-radius:999px; padding:12px 16px;
  background:var(--yellow) !important; color:#111 !important; border:1px solid #00000010 !important;
  font-weight:800 !important;
}
.btn-primary > button:hover{ filter:brightness(1.02); }

/* Radio כפתורי-פיל קלילים */
.stRadio label{
  display:block !important; border:1px solid var(--line); border-radius:999px !important;
  padding:10px 14px !important; margin:6px 0; font-weight:700 !important; color:var(--ink);
  background:#fff;
}
.stRadio [role="radio"][aria-checked="true"] + d
