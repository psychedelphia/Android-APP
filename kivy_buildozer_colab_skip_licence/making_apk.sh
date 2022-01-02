#!/bin/bash 

# Upgrade Pip(pip with python3)
# builozer(build with 3.7, 3.8)
python3 -m pip install --upgrade pip

# Install Cython(latest version recommended)
pip install --upgrade Cython==0.29.26 virtualenv 

# Export PATH(buildozer webpage says)
export PATH=$PATH:~/.local/bin/ 

# Ubuntu repositories(E: Unable to locate package)
# sudo add-apt-repository universe

# Upgrade apt-get
sudo apt-get update

# Google Colab max: 16
# Install necessary system packages - 1
# required or not
sudo apt-get install -y \
python3-pip \
python3 \
python3-dev \
python3-distutils

# Install necessary system packages - 2
# required or not
sudo apt-get install -y \
libsdl2-dev \
libsdl2-image-dev \
libsdl2-mixer-dev \
libsdl2-ttf-dev \
libportmidi-dev \
libswscale-dev \
libavformat-dev \
libavcodec-dev \
libtool \
lld

# Install necessary system packages - 3
# required or not
sudo apt-get install -y \
libbz2-dev \
libssl-dev \
libgdbm-dev \
libgdbm-compat-dev \
liblzma-dev \
libffi-dev \
libtinfo5 \
libncurses5-dev \
libncursesw5-dev \
libgstreamer1.0

# Install necessary system packages - 4
# required or not
sudo apt-get install -y \
build-essential \
git \
ffmpeg \
zlib1g-dev \
autoconf \
automake \
openssl \
sqlite3 bzip2 \
zip \
unzip \
pkg-config \
cmake \
gstreamer1.0-plugins-base \
gstreamer1.0-plugins-good

# Install necessary system packages - 5
# required or not
sudo apt-get install \
openjdk-11-jdk

# Install Buildozer
pip install --upgrade buildozer

# Buildozer Init
printf 'y' | buildozer init

# Buildozer debug mode
printf 'y' | buildozer -v android debug
