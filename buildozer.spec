[app]
title = FeeTrack
package.name = feetrack
package.domain = com.josephmbui # <- your domain format
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,pillow
orientation = portrait
android.api = 31
android.minapi = 21
android.arch = arm64-v8a

# Author info - shows in Play Store / APK details
author = Joseph Mbui
author.email = mbuijoseph51@gmail.com

android.sdk_path = /opt/android-sdk
android.ndk_path = /opt/android-ndk
log_level = 2

[buildozer]
log_level = 2
warn_on_root = 0
