# INIT APP
npx react-native init [appName]

# init template --- typescript
npx react-native init MyApp --template react-native-template-typescript


# RUN DEVICE
npx react-native run-android

#  You can also use the React Native CLI to generate and run a Release build 
npx react-native run-android --variant=release

# List of Devices
adb devices

# Connecting to the development server

# Method 1: Using adb reverse (recommended)#
adb -s <device name> reverse tcp:8081 tcp:8081
adb devices

# ======================== < DEBUG > ======================== #

# RUN ANDROID DEBUG MODE
adb shell input keyevent 82

# Note: on Android, if the times between the debugger and device have drifted; 
# things such as animation, event behavior, etc., might not work properly or the results 
# may not be accurate. Please correct this by running  on your debugger machine. 
# Root access is required for the use in real device:

adb shell "date `date +%m%d%H%M%Y.%S%3N`"

# LOGS
npx react-native log-ios
npx react-native log-android