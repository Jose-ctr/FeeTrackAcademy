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

# FIX 1: Use python3.10. p4a stable breaks on 3.11.15
requirements = python3==3.10.13,kivy==2.3.0,cython==0.29.33

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21

# FIX 2: Only build 64-bit. 32-bit armeabi-v7a fails with new NDK
android.archs = arm64-v8a

# FIX 3: Use NDK 25b. 28c is too new and breaks p4a
android.ndk = 25b

android.permissions = INTERNET
android.accept_sdk = True
