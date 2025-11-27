from pywinauto import keyboard
from pywinauto import Application
from pywinauto import Desktop
import time

# ---------------------
# Launch HP Smart App
# ---------------------
keyboard.send_keys("{VK_LWIN}")
keyboard.send_keys("HP Smart")
keyboard.send_keys("{ENTER}")
time.sleep(15)

# Connect to main HP Smart window
# app = Application(backend="uia").connect(title_re="HP Smart")
app = Desktop(backend="uia").windows(title_re="HP Smart")[0].wrapper_object()
main = app.window(title_re="HP Smart")
main.wait("visible", timeout=40)
main.set_focus()

# ========================================================
# CLICK "App Settings"  (Correct)
# ========================================================
app_settings = main.child_window(
    title="App Settings",
    control_type="ListItem"
)

app_settings.wait("ready", timeout=30)
app_settings.click_input()
time.sleep(3)

# ========================================================
# CLICK "Privacy Settings"
# (Click the TEXT child)
# ========================================================
privacy_text = main.child_window(
    title="Privacy Settings",
    control_type="Text"
)

privacy_text.wait("ready", timeout=30)
privacy_text.click_input()
time.sleep(3)

# ========================================================
# Title Verification
# ========================================================
privacy_title = main.child_window(
    title="Privacy Settings",
    control_type="Text"
)
privacy_title.wait("ready", timeout=30) 
current_title = privacy_title.window_text()
expected_title = "Privacy Settings" 
if current_title == expected_title:
    print("Privacy Settings title verified:", current_title)
else:
    print("Title verification failed. Expected:", expected_title, "Got:", current_title)

# ========================================================
# HP Smart terms of use link verification
# ========================================================  
terms_link = main.child_window(
    title="HP Smart Terms of Use",
    control_type="Hyperlink",
    class_name="Hyperlink"
)

terms_link.wait("visible", timeout=30)

if terms_link.exists() and terms_link.is_visible():
    print("HP Smart Terms of Use link is present and visible.")
else:
    print("Verification failed: Link not visible.")

terms_link.click_input()
time.sleep(3)

Switch to newly opened window
desktop = Application(backend="uia").connect(title_re=".*HP Smart Terms of Use.*")
terms_window = desktop.window(title_re=".*HP Smart Terms of Use.*")     
terms_window.wait("visible", timeout=30)
terms_window.set_focus()    
print("Switched to Terms of Use window.")

time.sleep(3)
