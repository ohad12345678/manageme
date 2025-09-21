# pages/01_⬇️_הזנת_הוצאות.py — דף הזנת הוצאות
from __future__ import annotations
from datetime import date
import streamlit as st
from components.ui import show_big_toast
from services.storage import init_db, insert_transaction, list_accounts, add_account

init_db()

st.markdown("### ⬇️ הזנת הוצאה")

with st.form("expense_form", clear_on_submit=False):
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        trx_date = st.date_input("תאריך", value=date.today())
    with col2:
        amount = st.number_input("סכום (₪)", min_value=0.0, step=1.0, format="%.2f")
    with col3:
        currency = st.selectbox("מטבע", options=["₪", "$", "€"], index=0)

    # קטגוריות בסיס (אפשר להשלים/לשנות בהמשך)
    CATEGORIES = {
        "סופרמרקט": ["מזון", "ניקיון", "טואלטיקה"],
        "מסעדות": ["טייקאווי", "מסעדה", "קפה"],
        "דיור": ["שכירות/משכנתא", "ועד בית", "ארנונה"],
        "תחבורה": ["דלק", "תחבורה ציבורית", "חניה"],
        "בריאות": ["תרופות", "ביטוח בריאות", "רופא"],
        "תקשורת": ["סלולר", "אינטרנט", "טלוויזיה"],
        "בידור": ["מנויים", "טיולים", "קולנוע"],
        "חינוך": ["גן/בית ספר", "חוגים", "ספרים"],
        "אחר": ["אחר"],
    }

    col4, col5 = st.columns([1, 1])
    with col4:
        cat = st.selectbox("קטגוריה", options=["— בחר —"] + list(CATEGORIES.keys()), index=0)
    with col5:
        subcats = CATEGORIES.get(cat, [])
        subcat = st.selectbox("תת־קטגוריה", options=(["— בחר —"] + subcats) if subcats else ["— בחר —"], index=0)

    # חשבון + הוספת חשבון חדש
    accs = list_accounts()
    acc_choice = st.selectbox("חשבון", options=["— בחר —"] + accs + ["הוספת חשבון חדש…"], index=0)
    new_acc = ""
    if acc_choice == "הוספת חשבון חדש…":
        new_acc = st.text_input("שם חשבון חדש")
        # טריק קטן למובייל – פוקוס
        st.markdown("""
        <script>
          setTimeout(function(){
            try{
              const inputs = window.document.querySelectorAll('input[type="text"]');
              if(inputs.length){ const i = inputs[inputs.length-1]; i.focus(); i.click(); }
            }catch(e){}
          }, 120);
        </script>
        """, unsafe_allow_html=True)

    col6, col7 = st.columns([1, 1])
    with col6:
        payment_method = st.selectbox("אמצעי תשלום", ["מזומן", "אשראי", "העברה", "צ׳ק", "אחר"], index=1)
    with col7:
        counterparty = st.text_input("ספק / לצד נגדי (למשל: שופרסל, סלקום)")

    notes = st.text_area("הערות (לא חובה)")
    tags = st.text_input("תגיות (מופרדות בפסיק), למשל: 'חגים, מבצע'")

    col8, col9 = st.columns([1, 1])
    with col8:
        keep_open = st.checkbox("להשאיר את הטופס פתוח לעוד הוצאות", value=True)
    with col9:
        submit = st.form_submit_button("שמור הוצאה", use_container_width=True)

if submit:
    # ולידציה פשוטה
    errors = []
    if amount <= 0:
        errors.append("נא להזין סכום חיובי.")
    if cat == "— בחר —":
        errors.append("נא לבחור קטגוריה.")
    if acc_choice == "— בחר —":
        errors.append("נא לבחור חשבון (או להוסיף חדש).")

    # יצירת חשבון חדש אם צריך
    account_final = acc_choice
    if acc_choice == "הוספת חשבון חדש…":
        if not new_acc.strip():
            errors.append("נא להזין שם חשבון חדש.")
        else:
            add_account(new_acc.strip())
            account_final = new_acc.strip()

    if errors:
        for e in errors:
            st.error(e)
    else:
        data = {
            "date": str(trx_date),
            "amount": float(amount),
            "currency": currency,
            "category": cat,
            "subcategory": (None if subcat == "— בחר —" else subcat),
            "account": account_final,
            "payment_method": payment_method,
            "counterparty": counterparty.strip(),
            "notes": notes.strip(),
            "tags": tags.strip(),
            "source": "manual",
        }
        ok, msg = insert_transaction(data)
        if ok:
            show_big_toast("נשמר בהצלחה ✅")
            if not keep_open:
                st.experimental_rerun()
        else:
            st.error(f"שגיאה בשמירה: {msg}")
