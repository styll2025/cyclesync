import streamlit as st
import datetime
import calendar

# Load logic from the full phase data
phase_data = [
    {
        "phase": "Menstruation",
        "days": list(range(1, 6)),
        "color": "#FFCCCC",
        "hormonal_landscape": "Low estrogen and progesterone",
        "behavior_insights": "Lower energy, increased introspection, reduced cognitive flexibility",
        "professional_strategies": [
            "Prioritize low-stimulation, solo tasks like admin work, planning, or deep focus writing",
            "Reflect on recent achievements and set intentions for the cycle ahead",
            "Be gentle with energy output; consider blocking calendar time for rest or reduced workload",
            "Use journaling or voice memos to track pain, fatigue, or mood patterns"
        ]
    },
    {
        "phase": "Follicular",
        "days": list(range(6, 14)),
        "color": "#CCE5FF",
        "hormonal_landscape": "Rising estrogen, low progesterone",
        "behavior_insights": "Increased dopamine activity, improved motivation, verbal fluency, and creativity",
        "professional_strategies": [
            "Schedule brainstorming sessions, innovation meetings, and ambitious planning",
            "Tackle complex problem-solving and new project launches",
            "Take initiative on proposals, applications, and public speaking",
            "Learn new skills or tools; cognitive flexibility is high"
        ]
    },
    {
        "phase": "Ovulation",
        "days": list(range(14, 17)),
        "color": "#CCFFCC",
        "hormonal_landscape": "Peak estrogen, LH surge, slight progesterone increase",
        "behavior_insights": "High verbal ability, social acuity, and confidence",
        "professional_strategies": [
            "Lead presentations, pitch ideas, network actively",
            "Organize team-building or client engagement activities",
            "Practice negotiation or interview skills—your communication is sharp",
            "Delegate or collaborate on shared goals; this is a peak energy window"
        ]
    },
    {
        "phase": "Luteal",
        "days": list(range(17, 29)),
        "color": "#E5CCFF",
        "hormonal_landscape": "High progesterone, moderate estrogen",
        "behavior_insights": "Increased attention to detail, sensitivity, and emotional depth. PMS symptoms may arise",
        "professional_strategies": [
            "Shift focus to execution, editing, and quality control",
            "Review contracts, budgets, and project deliverables",
            "Build in flexibility and buffer time as physical symptoms may increase",
            "Practice self-compassion; reduce meetings or confrontation-heavy tasks in late luteal days"
        ]
    }
]

# App UI
st.title("🌸 CycleSync Pro")
st.markdown("Track your menstrual cycle and get tailored career guidance across the entire cycle.")

# Input cycle start date and length
start_date = st.date_input("Select the first day of your current cycle:", datetime.date.today())
cycle_length = st.slider("Cycle Length (days)", 24, 35, 28)

# Generate calendar view with clickable days
st.subheader("🗓️ Cycle Calendar")
selected_day = st.number_input("Click a day to explore (1 to cycle length):", min_value=1, max_value=cycle_length, value=1)

# Calculate selected day details
def get_phase_for_day(day):
    for phase in phase_data:
        if day in phase["days"]:
            return phase
    return None

phase = get_phase_for_day(selected_day)

# Display selected day info
st.markdown(f"### Day {selected_day}: {phase['phase']}")
st.markdown(f"**Hormonal Landscape:** {phase['hormonal_landscape']}")
st.markdown(f"**Behavioural Insights:** {phase['behavior_insights']}")

st.markdown("**Recommended Professional Strategies:**")
for strategy in phase["professional_strategies"]:
    st.markdown(f"- {strategy}")

# Optional: add journaling/energy log
st.markdown("---")
st.subheader("📝 Energy Log")
st.text_area("How are you feeling today? Any symptoms or wins to note?", key="energy_log")
