[app]
title = Jogo IA Mimi
package.name = jogoiamimi
package.domain = org.mimi
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db,ttf
version = 1.0.0

# BIBLIOTECAS ADICIONADAS: kivymd
requirements = python3,kivy

orientation = portrait
fullscreen = 0

# Arquitetura do celular
android.archs = arm64-v8a

# Atualizações para Android moderno (API 33 / Android 13)
android.api = 33
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 34.0.0
android.accept_sdk_license = True

# Permissões (Internet para os anúncios)
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# Dependências do AdMob
android.gradle_dependencies = com.google.android.gms:play-services-ads:22.6.0
android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-3118010994727094~5382002346

# Aumenta a compatibilidade com bibliotecas modernas
android.enable_androidx = True

# (Opcional) Diminui o tamanho do APK
android.aapt2 = True

[buildozer]
log_level = 2
warn_on_root = 1

# Essas 3 linhas abaixo são CRUCIAIS para o Termux:
android.sdk_path = /data/data/com.termux/files/home/android-sdk
android.ndk_path = /data/data/com.termux/files/home/android-ndk
android.accept_sdk_license = True
