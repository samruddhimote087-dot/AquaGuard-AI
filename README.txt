SMART WATER TANK MONITORING AGENT
=================================

WHAT THIS PROJECT DOES
This is a beginner-friendly, interactive demonstration of a SINGLE intelligent agent.
It observes tank water level, decides whether to turn a simulated pump ON/OFF, and explains
its decision on the screen.

IMPORTANT SAFETY NOTE
This is a SOFTWARE SIMULATION ONLY. It does not connect to a real pump, relay, electrical
wiring, or physical sensor. Do not connect this demo directly to real equipment.

HOW TO RUN ON WINDOWS
1. Extract the ZIP file to a folder.
2. Install Python 3.10 or newer from https://www.python.org/downloads/
   During setup, enable "Add Python to PATH".
3. Double-click run_windows.bat.
4. Wait while Streamlit installs and starts.
5. A browser tab should open. If not, copy the Local URL from the terminal
   (usually http://localhost:8501) into your browser.
6. Move the "Simulated water level" slider to test the agent.

HOW TO TEST
- Set level to 15%: agent should turn the pump ON (low water).
- Set level to 50%: agent keeps the previous pump state (safe band).
- Set level to 95%: agent should turn the pump OFF (high water).
- Switch to Manual mode to test the manual pump toggle.
- Change thresholds in the sidebar to test different settings.

AGENT WORKING IN SIMPLE WORDS
1. Observe: read water level.
2. Decide: compare the level with low and high thresholds.
3. Act: switch the simulated pump ON or OFF.
4. Explain: display the reason for the decision.

AGENT TYPE
A single rule-based, model-based/reflex-style agent. One controller makes decisions;
it does not require multiple agents.

FILES
app.py            - interactive UI and agent decision logic
requirements.txt  - Python package needed
run_windows.bat   - launcher for Windows
README.txt        - setup and testing guide

TROUBLESHOOTING
- If Python was not found, install Python and tick "Add Python to PATH".
- If installation fails, check internet access and try again.
- Alternatively, open Command Prompt in this folder and run:
    py -m pip install -r requirements.txt
    py -m streamlit run app.py

HARDWARE VERSION
A real implementation needs a suitable water-level sensor, a properly rated relay/contactor,
electrical isolation, waterproof enclosure, and hardware-specific code. Have a qualified
supervisor/electrician review the design. This ZIP is simulation-only.
