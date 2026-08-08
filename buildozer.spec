[app]
title = FeeTrack
package.name = feetrackacademy
package.domain = com.josephmbui
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,db
version = 1.0.1
requirements = python3,kivy==2.3.0,sqlite3,reportlab
author = Joseph
author.email = mbuijoseph51@gmail.com

[buildozer]
log_level = 2
warn_on_root = 0

[android]
android.api = 33
android.sdk = 33
android.minapi = 24
android.ndk = 28c
android.sdk_path = /home/runner/work/FeeTrackAcademy/FeeTrackAcademy/android-sdk
android.ndk_path = /home/runner/work/FeeTrackAcademy/FeeTrackAcademy/android-ndk-r28c
android.arch = arm64-v8a
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.accept_sdk_license = True
android.build_tools_version = 33.0.2
android.skip_update = True
android.gradle_version = 8.2.0

# Use P4A master branch - THIS IS THE FIX
p4a.branch = master
p4a.source_dir =
