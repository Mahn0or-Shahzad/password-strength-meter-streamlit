import streamlit as st

import re

def check_password_strength(password):

    score = 0
    suggestions = []

    if not len(password) >= 8:
        suggestions.append("🔢 Increase the lenght of your password to atleast 8 characters.")
    else:
        score += 1
    if not re.search(r"[A_Z]",password) and not re.search(r"[a_z]",password) :
        suggestions.append("🔡 Add both uppercase and lowercase letters.")
    else:
        score += 1
    if not re.search(r"\d",password):
        suggestions.append("🔢 Include at least one digits(0_9).")
    else:
        score += 1
    if not re.search(r"[!,@,#,$,%,^,&,*]",password):
        suggestions.append("🔐 Include at least one special character .")
    else:
        score += 1
    

    if score == 3:
        strength = "🟠 Moderate Password." 
        feedback = "🛡️ Consider adding more securirty feartures."
    elif score == 4:
        strength = "🟢 Strong Password."
        feedback = "✅ Your password is strong."
    else:
        strength = "🔴 Weak password"
        feedback = "⚠️ Your password is weak."
    
    
    return strength,feedback,suggestions

 
st.title("🔑 Password_Strength_Meter!")
password = st.text_input("🔒 **Enter Your Password**:",type = "password")

if st.button("🔎 check password strength"):
    if password.strip():
        strength , feedback , suggestions = check_password_strength(password)
    else:
        strength = "None"
        feedback = "None"
        suggestions = []
        st.warning("⚠️ Please enter the password first!")

    st.markdown(f"🔒 **Strength** : {strength}")

    if suggestions:
            st.markdown(f"🛠️ **Suggestion** : {'  '. join (suggestions)}")
    
    st.markdown(f"💡 **Feedback** : {feedback}")