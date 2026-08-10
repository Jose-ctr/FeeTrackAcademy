name: Build Android APK

on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-22.04
    timeout-minutes: 120

    steps:
      # Checkout repository
      - name: Checkout
        uses: actions/checkout@v4

      # Python
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      # Java 17
      - name: Set up Java
        uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: '17'

      # Install Linux packages required by Buildozer
      - name: Install system packages
        run: |
          sudo apt-get update
          sudo apt-get install -y \
            git \
            zip \
            unzip \
            wget \
            openjdk-17-jdk \
            python3-pip \
            autoconf \
            libtool \
            pkg-config \
            zlib1g-dev \
            libncurses6 \
            libncurses-dev \
            libtinfo6

      # Verify Git
      - name: Verify Git
        run:
