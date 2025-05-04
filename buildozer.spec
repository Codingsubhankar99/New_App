[app]

# App name and metadata
title = SubhanrCalcu
package.name = subhanrcalcu
package.domain = org.subhankar.calculator
source.dir = .
version = 1.0
icon.filename = icon.png

# Main Python file
source.include_exts = py,png,jpg,kv,atlas
main.py = main.py

# Orientation and fullscreen
orientation = portrait
fullscreen = 0

# Supported screens
supported.orientation = portrait

# Permissions (if needed)
#android.permissions = INTERNET

# Requirements
requirements = python3,kivy,cython,setuptools

# Presplash and theme
presplash.filename = 
theme = 

# Logging and errors
log_level = 2
log_enable = 1

# Include *.so libs
android.copy_libs = 1

# Include assets (optional)
# android.add_assets = assets/*

# Include data files (optional)
# include_patterns = assets/*, images/*.png

# Android configurations
[android]
android.api = 31
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a
android.minapi = 21
android.sdk = 24
# android.gradle_dependencies =

# Optional build settings
# android.private_storage = true

# Build type: debug or release
android.release = 0

# Java version and heap
android.java_src = 0
android.add_jars = 
android.add_src = 
android.add_gradle_repos = 
android.add_gradle_dependencies = 
android.gradle_dependencies = 
android.gradle_repositories = 
android.extra_jars = 

# Set Java heap size (increase if needed)
# android.maxheap = 1024m

# Other platforms (you can ignore them)
[buildozer]
warn_on_root = 1
build_dir = .buildozer
bin_dir = bin

[hostpython]

[ios]

[toolchain]

[build]

[dependencies]

[python]
