[app]

title = FeeTrack Academy
package.name = feetrackacademy
package.domain = com.josephmbui

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db

version = 1.0.1

requirements = python3,kivy==2.3.0

orientation = portrait

author = Joseph Mbui
author.email = mbuijoseph51@gmail.com

[android]

android.api = 33
android.minapi = 24
android.archs = arm64-v8a

android.permissions = INTERNET

android.accept_sdk_license = True

p4a.url = https://github.com/kivy/python-for-android.git
p4a.branch = master

[buildozer]

log_level = 2
warn_on_root = 0
