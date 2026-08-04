[app]

App information

title = FeeTrack Academy
package.name = feetrackacademy
package.domain = com.josephmbui

Author

author = Joseph Mbui
author_email = mbuijoseph51@gmail.com

Source files

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf

Exclude unnecessary folders

source.exclude_dirs = .git,.github,.buildozer,bin,pycache

Version

version = 1.0.1

Python requirements

requirements = python3,kivy==2.3.0

App orientation

orientation = portrait

Window mode

fullscreen = 0

Android configuration

android.api = 33
android.minapi = 21
android.archs = arm64-v8a
android.permissions = INTERNET

Use installed SDK/NDK from GitHub Actions

android.accept_sdk_license = True

Logging

log_level = 2
warn_on_root = 1

AndroidX support

android.enable_androidx = True

Private storage

android.private_storage = True

Entry point

android.entrypoint = org.kivy.android.PythonActivity

Optional app icon and splash screen

icon.filename = assets/icon.png

presplash.filename = assets/presplash.png

Keep APK smaller

android.add_aars =
android.gradle_dependencies =

End of file
