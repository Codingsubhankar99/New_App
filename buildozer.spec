[app]
title = Subhanr Calculator
package.name = subhanrcalcu
package.domain = org.subhankar.calcu
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = kivy, cython
orientation = portrait
fullscreen = 0
osx.kivy_version = 2.1.0

[buildozer]
log_level = 2
warn_on_root = 1
android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a
android.build_tools = 36.0.0
p4a.branch = master

[android]
# No permissions here since you don't want INTERNET

[log]
log_level = 2
