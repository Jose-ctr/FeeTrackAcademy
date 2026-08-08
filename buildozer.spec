[app]
title = FeeTrack
package.name = feetrackacademy
package.domain = com.josephmbui
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db
version = 1.0.1
requirements = python3,kivy==2.3.0,reportlab
author = Joseph
author.email = mbuijoseph51@gmail.com
osx.python_version = 3
osx.kivy_version = 2.3.0

android.api = 33
android.minapi = 24
android.ndk = 28c
android.archs = arm64-v8a
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.accept_sdk_license = True
android.logcat_filters = *:S python:D

[buildozer]
log_level = 2
warn_on_root = 0
