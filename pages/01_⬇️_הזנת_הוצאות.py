# pages/01_⬇️_הזנת_הוצאות.py — הזנת הוצאות (UI קליל וצבעוני)
from __future__ import annotations
from datetime import date
import streamlit as st
from components.ui import show_big_toast
from services.storage import init_db, insert_transaction, list_accounts, add_account

init_db()
st.markdown("### ⬇️ הזנת הוצאה")

with st.form("expense_form", clear_on_submit=False):
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("**סכום ההוצאה**")
    amount = st.number_input(" ", min_value=0.0, step=1.0, format="%.2f")
    st.markdown('</div>', unsafe_allow_html=True)

    colA, colB, colC = st.columns([1,1,1])
    with colA:
        trx_date = st.date_input("תאריך", value=date.today())
    with colB:
        currency = st.selectbox("מטבע", ["₪", "$", "€"], index=0)
    with colC:
        payment_method = st.selectbox("אמצעי תשלום", ["אשראי", "מזומן", "העברה", "צ׳ק", "אחר"], index=0)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("**קטגוריה**")
    CATEGORIES = ["סופרמרקט","מסעדות","דיור","תחבורה","בריאות","תקשורת","בידור","חינוך","אחר"]
    cat = st.radio("קטגוריה", options=CATEGORIES, index=0, label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

    SUBS = {
        "סופרמרקט":["מזון","ניקיון","טואלטיקה"],
        "מסעדות":["טייקאווי","מסעדה","קפה"],
        "דיור":["שכירות/משכנתא","ועד בית","ארנונה"],
        "תחבורה":["דלק","תחבורה ציבורית","חניה"],
        "בריאות":["תרופות","ביטוח בריאות","רופא"],
        "תקשורת":["סלולר","אינטרנט","טלוויזיה"],
        "בידור":["מנויים","טיולים","קולנוע"],
        "חינוך":["גן/בית ספר","חוגים","ספרים"],
        "אחר":["אחר"]
    }
    subcat = st.selectbox("תת־קטגוריה", SUBS.get(cat, ["אחר"]))

    accs = list_accounts()
    acc_choice = st.selectbox("חשבון", ["— בחר —"] + accs + ["הוספת חשבון חדש…"], index=1 if accs else 0)
    new_acc = ""
    if acc_choice == "הוספת חשבון חדש…":
        new_acc = st.text_input("שם חשבון חדש")
        # פוקוס להזנה ידנית במובייל
        st.markdown("""
        <script>
          setTimeout(function(){
            try{
              const inputs = window.document.querySelectorAll('input[type="text"]');
              if(inputs.length){ const i = inputs[inputs.length-1]; i.focus(); i.click(); }
            }catch(e){}
          }, 100);
        </script>
        """, unsafe_allow_html=True)

    counterparty = st.text_input("ספק / בית עסק")
    notes = st.text_area("הערות (לא חובה)")
    tags = st.text_input("תגיות (פסיקים)")

    st.markdown('<div class="btn-primary">', unsafe_allow_html=True)
    submit = st.form_submit_button("שמור הוצאה")
    st.markdown('</div>', unsafe_allow_html=True)

# שמירה
if submit:
    errs = []
    if amount <= 0: errs.append("נא להזין סכום חיובי.")
    if acc_choice == "— בחר —": errs.append("נא לבחור חשבון (או להוסיף חדש).")

    final_acc = acc_choice
    if acc_choice == "הוספת חשבון חדש…":
        if not new_acc.strip():
            errs.append("נא להזין שם לחשבון החדש.")
        else:
            add_account(new_acc.strip()); final_acc = new_acc.strip()

    if errs:
        for e in errs: st.error(e)
    else:
        ok, msg = insert_transaction({
            "date": str(trx_date),
            "amount": float(amount),
            "currency": currency,
            "category": cat,
            "subcategory": subcat,
            "account": final_acc,
            "payment_method": payment_method,
            "counterparty": counterparty.strip(),
            "notes": notes.strip(),
            "tags": tags.strip(),
            "source": "manual",
        })
        if ok:
            show_big_toast("נשמר! ✨")
            st.experimental_rerun()
        else:
            st.error(f"שגיאה בשמירה: {msg}")
