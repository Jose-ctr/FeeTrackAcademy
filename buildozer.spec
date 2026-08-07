[app]
title = FeeTrack
package.name = feetrackacademy
package.domain = com.josephmbui
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,db
version = 1.0.1
requirements = python3,kivy==2.3.0
orientation = portrait
author = Joseph
author.email = mbuijoseph51@gmail.com

[buildozer]
log_level = 2
warn_on_root = 0

[android]
android.api = 33
android.minapi = 30
android.ndk = 28c
android.arch = arm64-v8a
android.accept_sdk_license = True
android.sdk_tools = cmdline-tools
android.build_tools_version = 33.0.2
android.skip_update = True
p4a.branch = stable
p4a.source_dir =
