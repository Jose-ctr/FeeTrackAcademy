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
android.ndk = 28b
android.permissions = INTERNET

# THESE 2 ARE MANDATORY FOR CI
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-sdk/ndk/28.0.13025108

android.allow_backup = False
android.enable_androidx = True

log_level = 2
