[app]

title = FeeTrack Academy
package.name = feetrackacademy
package.domain = com.josephmbui

author = Joseph Mbui
author_email = mbuijoseph51@gmail.com

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf
source.exclude_dirs = .git,.github,.buildozer,bin,pycache

version = 1.0.1

FINAL stable versions

requirements = python3==3.11.15,kivy==2.3.0,cython==0.29.33

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21
android.archs = arm64-v8a
android.permissions = INTERNET

android.accept_sdk_license = True
android.enable_androidx = True
android.private_storage = True

log_level = 2
warn_on_root = 1

android.entrypoint = org.kivy.android.PythonActivity
