AQUAGUARD AI — INTERACTIVE WATER TANK AGENT
===========================================

WHAT IS INCLUDED?
- app.py: Interactive Streamlit dashboard and rule-based agent
- requirements.txt: Python libraries needed
- run_windows.bat: Windows double-click launcher

EASY START (WINDOWS)
1. Extract the ZIP file to a normal folder such as Desktop\AquaGuard_AI_Interactive.
2. Install Python 3.10 or newer from https://www.python.org/downloads/ if it is not installed.
   During installation, tick "Add Python to PATH".
3. Make sure the laptop has an internet connection for the first-time library installation.
4. Double-click run_windows.bat.
5. Wait while the libraries install. A browser tab should open with the dashboard.
6. If the browser does not open automatically, look in the terminal for a local address such as:
   http://localhost:8501

HOW TO TEST THE AGENT
- Click "Test low level": level becomes 10%, and the automatic agent should turn the pump ON.
- Click "Test full tank": level becomes 95%, and the agent should turn the pump OFF.
- Use "Add water" and "Use water" to change the simulated level.
- Turn off Automatic agent enabled in the sidebar to reveal manual pump controls.
- Explore Level history, Activity log, and Project information tabs.

TROUBLESHOOTING
- If Windows says Python was not found, install Python and enable Add Python to PATH.
- If installation fails, check internet access and try launching run_windows.bat again.
- If the browser does not open, manually visit http://localhost:8501 while the terminal is running.
- To stop the app, focus the terminal and press Ctrl+C.

IMPORTANT
This is an educational simulation. It does not connect to a real tank, sensor, relay, or pump.
The agent is rule-based and does not use a trained machine-learning model.
