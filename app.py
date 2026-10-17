import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Smart Water Tank Agent", page_icon="💧", layout="wide")

def water_tank_agent(level, mode, pump_manual, low_threshold, high_threshold, pump_on_previous):
    """Single rule-based agent: observes level, decides, and acts on a simulated pump."""
    if mode == "Manual":
        return pump_manual, "Manual mode is selected. The agent is not changing the pump.", "Manual control"
    if level <= low_threshold:
        return True, f"Water level is low ({level}%). I am turning the pump ON to refill the tank.", "Refill tank"
    if level >= high_threshold:
        return False, f"Water level is high ({level}%). I am turning the pump OFF to prevent overflow.", "Prevent overflow"
    return pump_on_previous, f"Water level is between {low_threshold}% and {high_threshold}%. I am keeping the previous pump state.", "Maintain safe range"

if "pump_on" not in st.session_state:
    st.session_state.pump_on = False
if "events" not in st.session_state:
    st.session_state.events = ["Agent started. Demo is running in simulation mode."]

st.title("💧 Smart Water Tank Monitoring Agent")
st.caption("A single intelligent agent observes water level, decides what to do, and controls a simulated pump.")
st.warning("Simulation only: this project does not connect to real pumps, sensors, or electrical equipment.")

with st.sidebar:
    st.header("⚙️ Agent Settings")
    mode = st.radio("Control mode", ["Automatic Agent", "Manual"], index=0)
    low_threshold = st.slider("Low-level threshold (%)", 5, 45, 25)
    high_threshold = st.slider("High-level threshold (%)", 55, 100, 85)
    st.divider()
    manual_pump = st.toggle("Pump ON (manual mode)", value=st.session_state.pump_on, disabled=(mode != "Manual"))
    st.caption("Manual control works only in Manual mode.")

left, right = st.columns([1.1, 1])
with left:
    st.subheader("Tank status")
    level = st.slider("Simulated water level (%)", 0, 100, 45, key="tank_level")
    st.markdown("### Water tank")
    tank_height = 220
    filled = int(tank_height * level / 100)
    st.markdown(f"""
    <div style="width:180px;height:{tank_height}px;border:4px solid #8aa4b8;border-radius:16px;
    overflow:hidden;display:flex;flex-direction:column-reverse;background:#f4f8fb;margin:10px auto;">
      <div style="height:{filled}px;background:linear-gradient(0deg,#087cf0,#35c6f4);"></div>
    </div>
    <div style="text-align:center;font-size:28px;font-weight:700;">{level}%</div>
    """, unsafe_allow_html=True)
    if level <= low_threshold:
        st.error("LOW WATER LEVEL")
    elif level >= high_threshold:
        st.error("HIGH WATER LEVEL — overflow risk")
    else:
        st.success("WATER LEVEL IN SAFE RANGE")

with right:
    st.subheader("Agent decision")
    effective_mode = "Manual" if mode == "Manual" else "Automatic"
    new_pump, reason, action = water_tank_agent(
        level, effective_mode, manual_pump, low_threshold, high_threshold, st.session_state.pump_on
    )
    if new_pump != st.session_state.pump_on:
        state_text = "ON" if new_pump else "OFF"
        st.session_state.events.insert(0, f"{datetime.now().strftime('%H:%M:%S')} — Pump turned {state_text}.")
        st.session_state.pump_on = new_pump
    st.metric("Pump status", "ON 🟢" if st.session_state.pump_on else "OFF ⚪")
    st.info(f"**What the agent decided:** {action}\n\n{reason}")
    if mode == "Automatic Agent":
        st.write("**Agent cycle:** Observe level → Check thresholds → Decide → Act → Explain")
    else:
        st.write("**Agent cycle:** Manual setting is applied; automatic decisions are paused.")

st.divider()
st.subheader("🧠 How the single agent works")
c1, c2, c3, c4 = st.columns(4)
c1.markdown("**1. Observe**\n\nReads the current tank level.")
c2.markdown("**2. Decide**\n\nCompares level with low/high thresholds.")
c3.markdown("**3. Act**\n\nTurns the simulated pump ON or OFF.")
c4.markdown("**4. Explain**\n\nShows why it selected the action.")

st.subheader("📋 Agent activity log")
if st.button("Clear activity log"):
    st.session_state.events = ["Activity log cleared."]
for event in st.session_state.events[:10]:
    st.write("• " + event)

st.caption("Try 15% to see the pump turn ON, then 95% to see it turn OFF.")
