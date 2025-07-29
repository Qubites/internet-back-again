import time
import socket
import platform
import subprocess
import webbrowser
import json
import os

SETTINGS_PATH = os.path.expanduser("~/.internet_back_settings.json")

def load_settings():
    if os.path.exists(SETTINGS_PATH):
        with open(SETTINGS_PATH, 'r') as f:
            return json.load(f)
    return {"action": "https://www.google.com"}

def is_connected(host="8.8.8.8", port=53, timeout=2):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error:
        return False

def notify(title, message):
    system = platform.system()
    if system == "Darwin":
        subprocess.call([osascript, "-e", f'display notification "{message}" with title "{title}""])

def play_sound():
    system = platform.system()
    if system == "Darwin":
        subprocess.call(["afplay", "/System/Library/Sounds/Glass.aiff"])

def on_restore(action):
    notify("Internet Connected", "Your connection has been restored.")
    play_sound()
    if action.startswith("http"):
        webbrowser.open(action)
    else:
        subprocess.Popen(["open", action])

def monitor_connection():
    was_connected = True
    print("🌐 Monitoring internet connection. Press Ctrl+C to stop.")
    settings = load_settings()
    while True:
        connected = is_connected()
        if connected and not was_connected:
            on_restore(settings.get("action"))
        was_connected = connected
        time.sleep(3)

if __name__ == "__main__":
    monitor_connection()