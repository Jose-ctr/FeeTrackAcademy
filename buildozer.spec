[app]
title = FeeTrack
package.name = feetrackacademy
package.domain = com.josephmbui
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,db
version = 1.0.1
requirements = python3,kivy==2.3.0,pillow,reportlab,requests,filetype,certifi
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 0

[android]
android.api = 33
android.minapi = 21
android.ndk = 23c
android.ndk_path = /home/runner/Android/Sdk/ndk/23.1.7779620
android.arch = arm64-v8a
android.accept_sdk_license = True
android.sdk_tools = cmdline-tools
android.build_tools = 33.0.2
android.sdk_path = /home/runner/Android/Sdk
