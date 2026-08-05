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

IMPORTANT: stable versions for Android build

requirements = python3==3.11.15,kivy==2.3.0,cython==0.29.33

App orientation

orientation = portrait

Window mode

fullscreen = 0

Android configuration

android.api = 33
android.minapi = 21
android.archs = arm64-v8a
android.permissions = INTERNET

Accept SDK licenses

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

Optional icon / splash

icon.filename = assets/icon.png

presplash.filename = assets/presplash.png

Keep APK smaller

android.add_aars =
android.gradle_dependencies =

End of file
