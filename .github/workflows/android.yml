name: Build FeeTrack APK

on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-22.04
    timeout-minutes: 120

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Java 17
        uses: actions/setup-java@v5
        with:
          distribution: temurin
          java-version: '17'

      - name: Set up Python 3.11
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install system packages
        run: |
          sudo apt-get update
          sudo apt-get install -y \
            git zip unzip wget curl \
            autoconf automake libtool pkg-config \
            zlib1g-dev libncurses6 libncurses-dev libtinfo6 \
            cmake libffi-dev libssl-dev build-essential

      - name: Install Android SDK command-line tools
        run: |
          export ANDROID_HOME=$HOME/android-sdk
          mkdir -p $ANDROID_HOME/cmdline-tools
          cd $HOME

          wget -q https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip -O tools.zip

          unzip -q tools.zip -d temp-tools

          mkdir -p $ANDROID_HOME/cmdline-tools/latest

          mv temp-tools/cmdline-tools/* $ANDROID_HOME/cmdline-tools/latest/

          echo "$ANDROID_HOME/cmdline-tools/latest/bin" >> $GITHUB_PATH
          echo "$ANDROID_HOME/platform-tools" >> $GITHUB_PATH
          echo "ANDROID_HOME=$ANDROID_HOME" >> $GITHUB_ENV
          echo "ANDROID_SDK_ROOT=$ANDROID_HOME" >> $GITHUB_ENV

      - name: Install Android SDK packages
        run: |
          export ANDROID_HOME=$HOME/android-sdk
          export PATH=$ANDROID_HOME/cmdline-tools/latest/bin:$ANDROID_HOME/platform-tools:$PATH

          echo "SDKMANAGER PATH:"
          which sdkmanager

          sdkmanager --version

          yes | sdkmanager --sdk_root=$ANDROID_HOME --licenses

          sdkmanager --sdk_root=$ANDROID_HOME \
            "platform-tools" \
            "platforms;android-33" \
            "build-tools;34.0.0" \
            "ndk;28.0.13004108"

          echo "ANDROIDSDK=$ANDROID_HOME" >> $GITHUB_ENV
          echo "ANDROIDNDK=$ANDROID_HOME/ndk/28.0.13004108" >> $GITHUB_ENV

      - name: Install Buildozer
        run: |
          python -m pip install --upgrade pip
          pip install buildozer==1.5.0 cython==0.29.36

      - name: Clean caches
        run: |
          rm -rf .buildozer
          rm -rf ~/.buildozer
          rm -rf ~/.gradle
          rm -rf ~/.android

      - name: Build APK
        env:
          ANDROIDSDK: ${{ env.ANDROIDSDK }}
          ANDROIDNDK: ${{ env.ANDROIDNDK }}
        run: |
          buildozer -v android debug --storage-dir=.buildozer

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: FeeTrack-APK
          path: bin/*.apk
