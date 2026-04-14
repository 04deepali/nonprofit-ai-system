import streamlit as st

# Page config
st.set_page_config(
    page_title="NGO AI Suite",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("🤖 NGO AI Suite")
st.success("AI-powered system for Non-Profit organizations")
st.write("Triage incoming emails and train your staff — all in one place.")

# Create tabs
tab1, tab2 = st.tabs(["🔀 Triage Agent", "📚 Tutor Bot"])

# ==============================
# TAB 1 — Triage Agent
# ==============================
with tab1:
    st.header("Support Triage Agent")

    user_input = st.text_area(
        "Enter email / request",
        placeholder="Example: I want to donate ₹500",
        height=150
    )

    if st.button("Analyze"):
        if user_input:
            st.success("✅ Analysis Complete")

            # Demo output
            st.write("### 🎯 Intent:")
            st.info("Donation Inquiry")

            st.write("### 🚦 Urgency:")
            st.warning("Medium")

            st.write("### ✉️ Suggested Response:")
            st.write("Thank you for your interest in donating. Please visit our website to proceed.")
        else:
            st.error("Please enter some text")

# ==============================
# TAB 2 — Tutor Bot
# ==============================
with tab2:
    st.header("Quiz / Tutor Bot")

    st.write("Generate simple quiz from text")

    text = st.text_area("Enter content for quiz")

    if st.button("Generate Quiz"):
        if text:
            st.success("Quiz Generated")

            st.write("### Question 1")
            st.write("What is the intent of the message?")

            option = st.radio(
                "Choose answer",
                ["Donation", "Complaint", "Emergency"]
            )

            if st.button("Submit Answer"):
                st.success("Answer Submitted")
        else:
            st.error("Enter some text first")
            # test
