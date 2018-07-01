# Create emulator
```
avdmanager create avd -n pwnable-emulator -k "system-images;android-28;default;x86_64"
```

# Run emulator
```
emulator -wipe-data -accel on -no-boot-anim -no-audio -avd pwnable-emulator
```

# Setup emulator
```
adb install <apk>
adb shell echo flag{this_is_the_flag} > /data/local/tmp/challenge5
adb shell su root chown root:<apk user> /data/local/tmp/challenge5
adb shell su root chmod 550 /data/local/tmp/challenge4
```

# Run apk
```
pkg=$(aapt dump badging <apk>|awk -F" " '/package/ {print $2}'|awk -F"'" '/name=/ {print $2}')
act=$(aapt dump badging <apk>|awk -F" " '/launchable-activity/ {print $2}'|awk -F"'" '/name=/ {print $2}')
adb shell am start -n "$pkg/$act"
```
