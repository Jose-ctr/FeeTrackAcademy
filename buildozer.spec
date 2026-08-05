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

# Pin python3.10. p4a stable breaks on 3.11
requirements = python3==3.10.13,kivy==2.3.0,cython==0.29.33

orientation = portrait
fullscreen = 0

# ANDROID CONFIG - THIS IS THE KEY
android.api = 33
android.minapi = 21
android.archs = arm64-v8a
android.ndk = 25b
android.accept_sdk = True
android.permissions = INTERNET
