import streamlit as st
import datetime

# Load logic from the full phase data
phase_data = [
    {
        "phase": "Menstruation",
        "days": list(range(1, 6)),
        "color": "#f28b82",
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
        "color": "#aecbfa",
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
        "color": "#ccff90",
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
        "color": "#d7aefb",
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
st.markdown("""
    <style>
        .calendar-box {
            background: #fff;
            border-radius: 12px;
            padding: 1rem;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        }
        .calendar-cell {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 70px;
            width: 70px;
            border-radius: 10px;
            color: #333;
            font-weight: 500;
            margin: 4px;
        }
        .calendar-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🌸 CycleSync Pro")
st.markdown("Track your menstrual cycle and get tailored career guidance across the entire cycle.")

# Input cycle start date and length
start_date = st.date_input("Select the first day of your current cycle:", datetime.date.today())
cycle_length = st.slider("Cycle Length (days)", 24, 35, 28)

st.subheader("🗓️ Cycle Calendar")
selected_day = None

st.markdown("<div class='calendar-box'><div class='calendar-grid'>", unsafe_allow_html=True)

for i in range(cycle_length):
    day_num = i + 1
    phase = next((p for p in phase_data if day_num in p["days"]), None)
    if phase:
        color = phase['color']
        if st.button(f"{day_num}", key=f"btn_{day_num}"):
            selected_day = day_num
        st.markdown(f"<div class='calendar-cell' style='background-color: {color}'>{day_num}<br><small>{phase['phase']}</small></div>", unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)

# Show insights for selected day
if selected_day:
    phase = next((p for p in phase_data if selected_day in p["days"]), None)
    if phase:
        st.markdown(f"### 📅 Day {selected_day} • {phase['phase']}")
        st.info(f"**Hormonal Landscape**\n\n{phase['hormonal_landscape']}")
        st.warning(f"**Behavioral Insights
