# Method 1: Using adb reverse (recommended)
# https://reactnative.dev/docs/running-on-device#method-1-using-adb-reverse-recommended-1

adb -s <device name> reverse tcp:8081 tcp:8081


# To find the device name, run the following adb command:
adb devices