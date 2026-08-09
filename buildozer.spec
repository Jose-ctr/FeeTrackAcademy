[app]
title = FeeTrack Academy
package.name = feetrack
package.domain = com.josephmbui

source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,ttf,xml

version = 1.0.0
version.code = 1

# Python 3.11 + Kivy 2.3.0 (stable Android combo)
requirements = python3==3.11.8,kivy==2.3.0

orientation = portrait
fullscreen = 0

author = Joseph Mbui
author.email = mbuijoseph51@gmail.com

# Android 11+
android.api = 33
android.minapi = 30
android.arch = arm64-v8a
android.permissions = INTERNET

[buildozer]
log_level = 2
