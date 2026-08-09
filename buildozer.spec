[app]

title = FeeTrack Academy
package.name = feetrackacademy
package.domain = com.josephmbui

source.dir = .

source.include_exts = py,png,jpg,jpeg,kv,atlas,db,ttf,xml

version = 1.0.1

requirements = python3,kivy==2.3.0

orientation = portrait

fullscreen = 0

author = Joseph Mbui
author.email = mbuijoseph51@gmail.com


[android]

android.api = 33
android.minapi = 30
android.archs = arm64-v8a

android.permissions = INTERNET

android.accept_sdk_license = True

android.build_tools_version = 34.0.0


[buildozer]

log_level = 2
warn_on_root = 0
