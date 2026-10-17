import streamlit as st
import random
from datetime import datetime
import pandas as pd

st.set_page_config(page_title='AquaGuard AI', page_icon='💧', layout='wide')

if 'level' not in st.session_state: st.session_state.level = 55
if 'pump_on' not in st.session_state: st.session_state.pump_on = False
if 'auto_mode' not in st.session_state: st.session_state.auto_mode = True
if 'capacity' not in st.session_state: st.session_state.capacity = 1000
if 'history' not in st.session_state: st.session_state.history = [{'time': datetime.now().strftime('%H:%M:%S'), 'level': st.session_state.level}]
if 'log' not in st.session_state: st.session_state.log = ['AquaGuard AI started. Monitoring simulated tank.']
if 'last_decision' not in st.session_state: st.session_state.last_decision = 'Waiting for first decision.'

LOW = 20
HIGH = 90

def log(message):
    st.session_state.log.insert(0, f"{datetime.now().strftime('%H:%M:%S')} — {message}")
    st.session_state.log = st.session_state.log[:30]

def record():
    st.session_state.history.append({'time': datetime.now().strftime('%H:%M:%S'), 'level': st.session_state.level})
    st.session_state.history = st.session_state.history[-30:]

def decide():
    if not st.session_state.auto_mode:
        st.session_state.last_decision = 'Automatic agent is paused. Manual control is active.'
        return
    if st.session_state.level <= LOW and not st.session_state.pump_on:
        st.session_state.pump_on = True
        st.session_state.last_decision = f'Water level is low ({st.session_state.level}%). Pump switched ON.'
        log(st.session_state.last_decision)
    elif st.session_state.level >= HIGH and st.session_state.pump_on:
        st.session_state.pump_on = False
        st.session_state.last_decision = f'Tank is nearly full ({st.session_state.level}%). Pump switched OFF to prevent overflow.'
        log(st.session_state.last_decision)
    elif st.session_state.pump_on and st.session_state.level < HIGH:
        st.session_state.last_decision = 'Pump remains ON because the tank has not reached the high threshold.'
    else:
        st.session_state.last_decision = 'Water level is in the safe range. No pump change needed.'

st.markdown('''<style>
.main {background: linear-gradient(180deg,#f3fbff 0%,#ffffff 55%)}
.block-container {padding-top: 1.5rem; max-width: 1250px}
.hero {background:linear-gradient(120deg,#063b67,#087eaa);padding:24px 28px;border-radius:18px;color:white;margin-bottom:18px}
.hero h1 {color:white;margin:0;font-size:2.25rem}.hero p {margin:6px 0 0;color:#dff6ff}
</style>''', unsafe_allow_html=True)
st.markdown('<div class="hero"><h1>💧 AquaGuard AI</h1><p>Smart Water Tank Monitoring • Single-Agent Simulation • Automatic Pump Control</p></div>', unsafe_allow_html=True)
st.info('Simulation only: this project does not connect to a physical water tank, sensor, or pump.', icon='ℹ️')

with st.sidebar:
    st.header('⚙️ Settings')
    st.session_state.capacity = st.number_input('Tank capacity (litres)', min_value=100, max_value=20000, value=int(st.session_state.capacity), step=100)
    st.write('Decision thresholds')
    st.metric('Low-level threshold', f'{LOW}%')
    st.metric('High-level threshold', f'{HIGH}%')
    st.divider()
    st.write('**Agent mode**')
    auto_choice = st.toggle('Automatic agent enabled', value=st.session_state.auto_mode)
    if auto_choice != st.session_state.auto_mode:
        st.session_state.auto_mode = auto_choice
        log('Automatic mode ' + ('enabled.' if auto_choice else 'paused; manual control enabled.'))
    st.caption('When automatic mode is enabled, the agent makes decisions from the simulated water level.')

# Agent decision based on the current state
decide()
level = int(st.session_state.level)
litres = int(st.session_state.capacity * level / 100)
status = 'PUMP ON' if st.session_state.pump_on else 'PUMP OFF'
status_color = '🟢' if st.session_state.pump_on else '⚪'

m1, m2, m3, m4 = st.columns(4)
m1.metric('Water level', f'{level}%')
m2.metric('Water in tank', f'{litres:,} L', f'of {st.session_state.capacity:,} L')
m3.metric('Pump status', status_color + ' ' + status)
m4.metric('Agent mode', 'AUTO' if st.session_state.auto_mode else 'MANUAL')

left, right = st.columns([1, 1.2], gap='large')
with left:
    st.subheader('🛢️ Simulated water tank')
    st.progress(level / 100, text=f'{level}% full')
    st.markdown(f"<div style='height:260px;max-width:250px;margin:10px auto;border:5px solid #246b8e;border-radius:22px 22px 35px 35px;position:relative;overflow:hidden;background:#edf8ff;box-shadow:0 4px 14px #0001'><div style='position:absolute;bottom:0;left:0;width:100%;height:{level}%;background:linear-gradient(0deg,#087db5,#49c6f0);transition:height .3s'></div><div style='position:absolute;top:12px;left:0;width:100%;text-align:center;color:#06405c;font-size:22px;font-weight:700'>{level}%</div></div>", unsafe_allow_html=True)
    st.caption('Blue fill represents the simulated amount of water.')
with right:
    st.subheader('🧠 Agent decision')
    st.write(st.session_state.last_decision)
    if st.session_state.pump_on:
        st.success('Pump is ON — simulated water is being added when you use the action below.')
    else:
        st.warning('Pump is OFF — the agent is waiting for the low-level condition or manual input.')
    st.markdown('**How the agent decides**')
    st.write('1. Read the current water level.  2. If level is 20% or below, turn pump ON.  3. If level is 90% or above, turn pump OFF.  4. Otherwise, keep the current pump state.')

st.divider()
st.subheader('🎛️ Interactive controls')
c1, c2 = st.columns([1, 1])
with c1:
    new_level = st.slider('Set simulated water level', 0, 100, int(st.session_state.level), 1, disabled=False)
    if st.button('Apply water level', use_container_width=True):
        st.session_state.level = new_level
        record()
        decide()
        log(f'Simulated water level set to {new_level}%.')
        st.rerun()
with c2:
    a, b = st.columns(2)
    if a.button('➕ Add water (+10%)', use_container_width=True):
        st.session_state.level = min(100, st.session_state.level + 10)
        record(); decide(); log('Added simulated water (+10%).'); st.rerun()
    if b.button('➖ Use water (-10%)', use_container_width=True):
        st.session_state.level = max(0, st.session_state.level - 10)
        record(); decide(); log('Used simulated water (-10%).'); st.rerun()
    a, b = st.columns(2)
    if a.button('🧪 Test low level', use_container_width=True):
        st.session_state.level = 10; record(); decide(); log('Low-level test executed.'); st.rerun()
    if b.button('🧪 Test full tank', use_container_width=True):
        st.session_state.level = 95; record(); decide(); log('High-level/overflow prevention test executed.'); st.rerun()
    if not st.session_state.auto_mode:
        a, b = st.columns(2)
        if a.button('Manual pump ON', use_container_width=True):
            st.session_state.pump_on = True; st.session_state.last_decision = 'Pump manually switched ON.'; log(st.session_state.last_decision); st.rerun()
        if b.button('Manual pump OFF', use_container_width=True):
            st.session_state.pump_on = False; st.session_state.last_decision = 'Pump manually switched OFF.'; log(st.session_state.last_decision); st.rerun()

st.divider()
tab1, tab2, tab3 = st.tabs(['📈 Level history', '📋 Activity log', 'ℹ️ Project information'])
with tab1:
    df = pd.DataFrame(st.session_state.history)
    st.line_chart(df.set_index('time')['level'], y_label='Water level (%)')
    st.caption('History is held in memory during this app session and resets when the app restarts.')
with tab2:
    if st.button('Clear activity log'):
        st.session_state.log = ['Activity log cleared.']
        st.rerun()
    for item in st.session_state.log:
        st.write('• ' + item)
with tab3:
    st.markdown('''**Project title:** AquaGuard AI — Intelligent Water Tank Monitoring Agent

**Agent type:** Rule-based model-based reflex agent (educational simulation).

**Inputs:** Simulated water level and automatic/manual mode.

**Actions:** Turn simulated pump ON/OFF and show alerts/status.

**Performance goals:** Avoid low-water situations, prevent overflow, and make understandable decisions.

**Technology:** Python + Streamlit.

**Limitations:** This prototype uses simulated values only. Real hardware would require a level sensor, relay/driver, suitable pump, electrical safety measures, and testing. Do not connect a real pump directly to a computer.''')

st.caption('AquaGuard AI • Final-year project prototype • Rule-based simulation')
