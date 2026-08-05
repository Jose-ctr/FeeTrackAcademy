[app]

title = FeeTrack Academy
package.name = feetrackacademy
package.domain = com.josephmbui

author = Joseph Mbui
author_email = mbuijoseph51@gmail.com

source.dir =.
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf
source.exclude_dirs =.git,.github,.buildozer,bin,__pycache__

version = 1.0.2

# THE FIX: Pin python3 only. Let buildozer pick hostpython3 automatically
requirements = python3==3.11.15,kivy==2.3.0,cython==0.29.33

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21
android.archs = arm64-v8a,armeabi-v7a
android.ndk = 21e

android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-sdk/ndk/21.3.6528147

android.permissions = INTERNET
android.accept_sdk_license = True
android.enable_androidx = True
android.private_storage = True

log_level = 2
warn_on_root = 1

android.entrypoint = org.kivy.android.PythonActivity
