[app]
title = FeeTrack
package.name = feetrackacademy
package.domain = com.josephmbui

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db

version = 1.0.1
orientation = portrait

author = Joseph
author.email = mbuijoseph51@gmail.com

requirements = python3==3.11.8,kivy==2.3.0

osx.python_version = 3
osx.kivy_version = 2.3.0

android.api = 33
android.minapi = 24
android.ndk = 28c
android.archs = arm64-v8a
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.accept_sdk_license = True
android.logcat_filters = *:S python:D

p4a.url = https://github.com/kivy/python-for-android.git
p4a.branch = 2024.01.21-release

[buildozer]
log_level = 2
warn_on_root = 0
