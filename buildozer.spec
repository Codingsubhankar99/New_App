[app]
title = Subhanr Calculator
package.name = subhanrcalcu
package.domain = org.subhankar.calcu
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
icon.filename = icon.png
requirements = python3,kivy,cython
orientation = portrait
fullscreen = 1
osx.kivy_version = 2.1.0

[buildozer]
log_level = 2
warn_on_root = 1
android.api = 34
android.minapi = 24
android.sdk = 34
android.ndk = 26.1.10991
android.ndk_api = 24
android.archs = arm64-v8a, armeabi-v7a
android.build_tools = 34.0.0
p4a.branch = master

[android]

[log]
log_level = 2
