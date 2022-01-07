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

# Install expect
# (first :[y/n]?, second: [y/n]?) -> full: Are you sure you want to continue [y/n]?
apt-get install expect

# apt-get: Colab max: 16 installation at once
# Install necessary system packages - 1
# required or not
sudo apt-get install -y \
python3 \
python3-pip \
python3-dev \
python3-distutils

# Install necessary system packages - 2
# required or not
sudo apt-get install -y \
libtool \
libsdl2-dev \
libavcodec-dev \
libswscale-dev \
libavformat-dev \
libsdl2-ttf-dev \
libportmidi-dev \
libsdl2-image-dev \
libsdl2-mixer-dev \
libgdbm-compat-dev

# Install necessary system packages - 3
# required or not
sudo apt-get install -y \
libtinfo5 \
libbz2-dev \
libssl-dev \
libffi-dev \
libgdbm-dev \
liblzma-dev \
libgstreamer1.0 \
libncurses5-dev \
libncursesw5-dev \
gstreamer1.0-plugins-base \
gstreamer1.0-plugins-good \
gcc \
lld \
cmake

# Install necessary system packages - 4
# required or not
sudo apt-get install -y \
git \
zip \
ant \
patch \
unzip \
bzip2 \
ccache \
ffmpeg \
openssl \
sqlite3 \
autoconf \
automake \
zlib1g-dev \
pkg-config \
build-essential

# Install necessary system packages - 5
# required or not : check jdk-version with linux-version
sudo apt-get install \
openjdk-11-jdk

# Install Buildozer(stable version)
pip install --upgrade buildozer

# Buildozer Init(making buildozer.spec)
expect <(cat << EOF
spawn buildozer init
expect "[y/n]?"
send "y\r"
interact
EOF
)

# Buildozer debug mode(adb logcat)
expect <(cat << EOF
spawn buildozer -v android debug deploy run logcat
expect "[y/n]?"
send "y\r"
interact
EOF
)

