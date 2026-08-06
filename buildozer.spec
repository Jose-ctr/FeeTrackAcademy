name: Build FeeTrack Kivy APK
on: workflow_dispatch
jobs:
  build:
    runs-on: ubuntu-latest
    env:
      ANDROID_SDK_ROOT: ${{ github.workspace }}/android-sdk
      ANDROIDNDK: ${{ github.workspace }}/android-sdk/ndk/21.4.7075529
      ANDROID_NDK_HOME: ${{ github.workspace }}/android-sdk/ndk/21.4.7075529
      ANDROID_NDK_ROOT: ${{ github.workspace }}/android-sdk/ndk/21.4.7075529
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with: {java-version: '17', distribution: 'temurin'}
      - uses: actions/setup-python@v5
        with: {python-version: '3.10.9'}
      - name: Install Buildozer + Cython
        run: |
          python -m pip install --upgrade pip
          python -m pip install buildozer cython==0.29.33
      - name: Install Android SDK + Dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y ant wget unzip zip lib32z1 lib32stdc++6 libffi-dev
          mkdir -p "$ANDROID_SDK_ROOT/cmdline-tools"
          cd /tmp && wget -q "https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip"
          unzip -q commandlinetools-linux-11076708_latest.zip -d cmdline-tools-temp
          mkdir -p "$ANDROID_SDK_ROOT/cmdline-tools/latest"
          mv cmdline
