[app]

title = Lucky Gems
package.name = luckygems
package.domain = org.luckygems

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 35
android.minapi = 23
android.archs = arm64-v8a

android.accept_sdk_license = True

[buildozer]

log_level = 2
warn_on_root = 1

