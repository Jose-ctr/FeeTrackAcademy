[app]
title = FeeTrack
package.name = feetrack
package.domain = com.josephmbui
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3==3.10.9,hostpython3==3.10.9,kivy==2.1.0,pillow,sdl2,reportlab
orientation = portrait

android.api = 31
android.minapi = 21
android.ndk = 21.4.7075529
android.ndk_path =./android-sdk/ndk/21.4.7075529 # <-- ADD THIS LINE
android.archs = arm64-v8a
android.accept_sdk_license = True
android.gradle_dependencies = 

author = Joseph Mbui
author.email = mbuijoseph51@gmail.com

log_level = 2

[buildozer]
log_level = 2
warn_on_root = 0
