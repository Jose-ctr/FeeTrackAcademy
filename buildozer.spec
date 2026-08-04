[app]

# App information
title = FeeTrack Academy
package.name = feetrack_academy
package.domain = com.josephmbui

# Author
author = Joseph Mbui
author_email = mbuijoseph51@gmail.com

# Source files
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf

# Version
version = 1.0.1

# Requirements
requirements = python3,kivy==2.3.0

# Orientation
orientation = portrait

# Window mode (0 = normal window, 1 = fullscreen)
fullscreen = 0

# Android settings
android.api = 33
android.minapi = 21
android.archs = arm64-v8a
android.permissions = INTERNET

# Buildozer settings
log_level = 2
warn_on_root = 1

# Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# Presplash / icon (optional)
# presplash.filename = assets/presplash.png
# icon.filename = assets/icon.png

# Do not copy build folders into APK
source.exclude_dirs = .git,.github,.buildozer,bin,__pycache__

# Keep the APK smaller
android.add_aars =
android.gradle_dependencies =

# Storage behavior
android.private_storage = True

# Enable AndroidX
android.enable_androidx = True

# End of file
