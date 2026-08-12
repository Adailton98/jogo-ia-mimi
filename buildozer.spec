[app]
title = Jogo IA Mimi
package.name = jogoiamimi
package.domain = org.mimi
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db
version = 0.6
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
android.api = 33
android.minapi = 24
android.build_tools_version = 33.0.2
android.ndk = 25b
android.accept_sdk_license = True
android.permissions = INTERNET
android.gradle_dependencies = com.google.android.gms:play-services-ads:22.6.0
# 1. Adicione a biblioteca do Google Play Services Ads
android.gradle_dependencies = com.google.android.gms:play-services-ads:22.6.0

# 2. Adicione a Meta-Data com o seu ID do App (o que tem o til '~')
android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-3118010994727094~5382002346

# 3. Garanta as permissões de rede
android.permissions = INTERNET, ACCESS_NETWORK_STATE
