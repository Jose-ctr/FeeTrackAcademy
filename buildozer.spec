[app]
title = FeeTrack Academy
package.name = feetrackacademy
package.domain = com.josephmbui

author = Joseph Mbui
author_email = mbuijoseph51@gmail.com

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,db

version = 1.0.1

requirements = python3==3.11.8,kivy==2.3.0

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21
android.archs = armeabi-v7a,arm64-v8a
android.ndk = 21b
android.permissions = INTERNET

android.allow_backup = False
android.enable_androidx = True

log_level = 2
