[app]
title = FeeTrack Academy
package.name = feetrackacademy
package.domain = com.josephmbui

author = Joseph Mbui
author_email = mbui.joseph51@gmail.com

source.dir =.
source.include_exts = py,png,jpg,jpeg,kv,atlas,db

version = 1.0.1

requirements = python3==3.11.8,kivy==2.3.0,reportlab

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 30
android.archs = arm64-v8a
android.ndk = 25b
android.permissions = INTERNET

# MUHIMU: Eleza buildozer wapi SDK na NDK ziko ili isidownload yake mwenyewe
android.sdk_path = %(home)s/android-sdk
android.ndk_path = %(home)s/android-sdk/ndk/25.2.9519653

android.allow_backup = False
android.enable_androidx = True

log_level = 2
