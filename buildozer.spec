[app]
title = FeeTrack Academy
package.name = feetrack
package.domain = com.josephmbui

source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,ttf,xml

version = 1.0.0
version.code = 1

# Stable Android build combo
requirements = python3==3.11.9,kivy==2.3.0,openssl

orientation = portrait
fullscreen = 0

author = Joseph Mbui
author.email = mbuijoseph51@gmail.com

# Android
android.api = 33
android.minapi = 24
android.archs = arm64-v8a
android.ndk = 28c
android.build_tools_version = 34.0.0
android.permissions = INTERNET

# python-for-android
p4a.branch = develop

[buildozer]
log_level = 2
