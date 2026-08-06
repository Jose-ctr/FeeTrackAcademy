[app]
title = FeeTrack
package.name = feetrackacademy
package.domain = com.josephmbui
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,db
version = 1.0.1
requirements = python3,kivy==2.3.0,pillow,reportlab,sqlite3,requests,filetype,certifi
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 0

[android]
android.api = 31
android.minapi = 21
android.ndk = 25b
android.arch = arm64-v8a
android.accept_sdk_license = True
android.sdk_tools = cmdline-tools
android.sdk_path =
android.ndk_path =
