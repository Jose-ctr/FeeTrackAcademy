[app]
title = FeeTrack Academy
package.name = feetrack
package.domain = com.josephmbui
source.dir = FeeTrackAcademy
source.include_exts = py,kv,png,jpg,jpeg,ttf,xml
version = 1.0.0
version.code = 1

requirements = python3,kivy

orientation = portrait
fullscreen = 0

author = Joseph Mbui
author.email = mbuijoseph51@gmail.com

# ANDROID SETTINGS
android.api = 31
android.minapi = 21
android.ndk = 25c
android.accept_sdk_license = True
android.archs = arm64-v8a
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.logcat_filters = *:S python:D

[buildozer]
log_level = 2
warn_on_root = 1
