[app]
title = FeeTrack Academy
package.name = feetrackacademy
package.domain = com.josephmbui

author = Joseph Mbui
author_email = mbui.joseph51@gmail.com

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,db

version = 1.0.1

# NOTE: ReportLab often fails to build on android (no p4a recipe). 
# Remove it from requirements unless you have a recipe or a pure-Python alternative.
requirements = python3==3.11,kivy==2.3.0

orientation = portrait
fullscreen = 0

android.api = 33
# Lowering minapi to 21 improves device coverage; if you need 30, keep your value.
android.minapi = 21
# include both common ABIs for broader device support
android.archs = armeabi-v7a,arm64-v8a
# leave ndk setting if you have a matching ndk installed; mismatch causes build errors
android.ndk = 28b
android.permissions = INTERNET

# REQUIRED FOR CI - ADD THESE (only needed for CI runners)
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-sdk/ndk/28.0.13025108

android.allow_backup = False
android.enable_androidx = True

log_level = 2
