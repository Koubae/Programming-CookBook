# Method 1: Using adb reverse (recommended)
# https://reactnative.dev/docs/running-on-device#method-1-using-adb-reverse-recommended-1

adb -s <device name> reverse tcp:8081 tcp:8081


# To find the device name, run the following adb command:
adb devices


# DEVICE NOT AUTHORIZED
# https://stackoverflow.com/questions/23081263/adb-android-device-unauthorized
# 1. Check if authorized:

# <ANDROID_SDK_HOME>\platform-tools>adb devices
# List of devices attached
# 4df798d76f98cf6d        unauthorized

# 2. Revoke USB Debugging on phone

# If the device is shown as unauthorized, go to the developer options on the phone and click "Revoke USB debugging authorization" (tested with JellyBean & Samsung GalaxyIII).

# 3. Restart ADB Server:

# Then restarted adb server

adb kill-server
adb start-server

# 4. Reconnect the device

# The device will ask if you are agree to connect the computer id. You need to confirm it.

# 5. Now Check the device

# It is now authorized!

# adb devices
# <ANDROID_SDK_HOME>\platform-tools>adb devices
# List of devices attached
# 4df798d76f98cf6d        device