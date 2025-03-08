import streamlit as st
import datetime
import random
import json

# Load daily challenges
challenges = [
    "Embrace a mistake you made today and write what you learned from it.",
    "Seek constructive feedback from someone and apply it.",
    "Try something new today that pushes you out of your comfort zone.",
    "Set a small learning goal and accomplish it today.",
    "Reframe a failure as a learning experience.",
    "Celebrate someone else's success and learn from their journey.",
    "Write down three things you are grateful for in your learning process."
]

# Function to get today's challenge
def get_today_challenge():
    random.seed(datetime.date.today().toordinal())  # Ensures a fixed challenge per day
    return random.choice(challenges)

# Function to load user progress
def load_progress():
    try:
        with open("progress.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save user progress
def save_progress(progress):
    with open("progress.json", "w") as file:
        json.dump(progress, file)

# App UI
st.set_page_config(page_title="Growth Mindset Challenge", layout="centered")
st.title("🚀 Growth Mindset Challenge")
st.write("Embrace challenges, learn from failures, and grow every day!")

# User Profile
st.sidebar.title("👤 Your Profile")
name = st.sidebar.text_input("Name", "Muhammad Hamza")
age = st.sidebar.number_input("Age", 18, 100, 18)
profession = st.sidebar.text_input("Profession", "BSCS Student")
skills = st.sidebar.text_area("Skills", "Python, AI, Machine Learning")

# Daily Check-in
st.sidebar.title("📅 Daily Check-in")
day_rating = st.sidebar.slider("How was your day?", 1, 10, 5)
energy_level = st.sidebar.slider("Energy Level", 1, 10, 5)
routine_summary = st.sidebar.text_area("Daily Routine Summary", "")

# Namaz Tracking
st.sidebar.title("🕌 Namaz Tracking")
fajr = st.sidebar.checkbox("Fajr")
dhuhr = st.sidebar.checkbox("Dhuhr")
asr = st.sidebar.checkbox("Asr")
maghrib = st.sidebar.checkbox("Maghrib")
isha = st.sidebar.checkbox("Isha")

# Display today's challenge
today_challenge = get_today_challenge()
st.subheader("📌 Today's Challenge:")
st.info(today_challenge)

# User response input
st.subheader("📝 Reflect on Today's Challenge")
user_response = st.text_area("How did you approach today's challenge? What did you learn?")

# Save progress
progress = load_progress()
date_str = str(datetime.date.today())
if st.button("Submit Reflection"):
    if user_response.strip():
        progress[date_str] = {
            "challenge": today_challenge,
            "response": user_response,
            "day_rating": day_rating,
            "energy_level": energy_level,
            "routine_summary": routine_summary,
            "namaz": {
                "Fajr": fajr,
                "Dhuhr": dhuhr,
                "Asr": asr,
                "Maghrib": maghrib,
                "Isha": isha
            }
        }
        save_progress(progress)
        st.success("✅ Your response has been saved! Keep growing!")
    else:
        st.warning("⚠️ Please enter your reflection before submitting.")

# Show past reflections
st.subheader("📅 Your Growth Journey")
if progress:
    for date, details in sorted(progress.items(), reverse=True):
        with st.expander(f"📖 {date}"):
            st.write(f"**Challenge:** {details['challenge']}")
            st.write(f"**Reflection:** {details['response']}")
            st.write(f"**Day Rating:** {details['day_rating']}/10")
            st.write(f"**Energy Level:** {details['energy_level']}/10")
            st.write(f"**Daily Routine Summary:** {details['routine_summary']}")
            st.write("**Namaz Performance:**")
            st.write(f"✔️ Fajr: {'Yes' if details['namaz']['Fajr'] else 'No'}")
            st.write(f"✔️ Dhuhr: {'Yes' if details['namaz']['Dhuhr'] else 'No'}")
            st.write(f"✔️ Asr: {'Yes' if details['namaz']['Asr'] else 'No'}")
            st.write(f"✔️ Maghrib: {'Yes' if details['namaz']['Maghrib'] else 'No'}")
            st.write(f"✔️ Isha: {'Yes' if details['namaz']['Isha'] else 'No'}")
else:
    st.write("No reflections yet. Start your journey today!")
