from lib import aimer
from lib import helpers
from lib import keycodes
from lib.bones import bones
import ctypes

#### CHANGE OPTIONS HERE ####

# Field of View
# Alter this between 0.1 and 3.0 for best results. 0.1 is very narrow, while larger numbers allow
# for more soldiers to be targeted
fov = 0.2

# Distance Limit
# Example, set to 100 to limit locking onto soldiers further than 100 meters away.
distance_limit = 300

# Trigger Button
# Grab your preferred button from lib/keycodes.py
trigger = keycodes.RBUTTON


# Aim Location Options
# Aim Location Switching (default is the first one listed)
# Check available bones in lib/bones.py
aim_locations = [bones['Head'], bones['Spine']]

# Key to switch aim location (set to None to disable)
aim_switch = keycodes.LALT
#aim_switch = RALT

# Normally, you won't need to change this
# This will attempt to gather your primary screen size. If you have issues or use
# a windowed version of BFV, you'll need to set this yourself, which probably comes with its own issues
screensize = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
# or
#screensize = (1280, 960)

#### END OF CHANGE OPTIONS ####



version = "0.5"

if fov < 0.1 or fov > 3.0:  # you can delete this if you know what you're doing
    print("Check your fov setting.")
    exit(1)
if distance_limit is not None and distance_limit <= 0:
    print("Check your distance_limit setting")
    exit(1)

if __name__ == "__main__":
    print("xx4 aim assist Version %s" % version)
    print("Thanks to Tormund and jo2305")
    print("提示", "F2关闭 F1开启 左alt切换瞄准位置 右键自瞄")
    if not helpers.is_admin():
        print("- Error: This must be run with admin privileges")
        print("提示", "必须以管理员权限运行")
        input("Press Enter to continue...")
        exit(1)

    if not helpers.is_python3():
        print("- Error: This script requires Python 3")
        [rint]("提示", "这个脚本需要Python 3")
        raw_input("Press Enter to continue...")
        exit(1)

    arch = helpers.get_python_arch()
    if arch != 64:
        print("- Error: This version of Python is not 64-bit")
        input("Press Enter to continue...")
        exit(1)

    print ("Using screensize: %s x %s" % screensize)
    aimer = aimer.Aimer(screensize, trigger, distance_limit, fov, aim_locations, aim_switch)
    aimer.start()

