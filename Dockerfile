ARG BASE_IMG='ubuntu:20.04'

FROM ${BASE_IMG}
SHELL ["/bin/bash", "-ci"]

# Timezone Configuration
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /workspace/ros_ws

RUN apt update && apt install -y \
    git vim curl nano tmux curl wget lsb-release \
    net-tools build-essential gcc g++ \
    cmake clang make \
    python3 python3-dev python3-pip python3-distutils libpython3-dev \
    gnupg2 ca-certificates software-properties-common \
    libboost-dev libeigen3-dev

# ROS1 Install
ENV ROS1_DISTRO=noetic
RUN echo "deb http://packages.ros.org/ros/ubuntu focal main" | tee /etc/apt/sources.list.d/ros-focal.list && \
    apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654 && \
    curl -sSL 'http://keyserver.ubuntu.com/pks/lookup?op=get&search=0xC1CF6E31E6BADE8868B172B4F42ED6FBAB17C654' | apt-key add - && \
    apt update && apt install -y ros-$ROS1_DISTRO-ros-base && \
    echo "source /opt/ros/$ROS1_DISTRO/setup.bash">> ~/.bashrc && \
    echo "source /workspace/ros_ws/devel/setup.bash">> ~/.bashrc && \
    apt update && apt install -y python3-rosdep python3-rosinstall python3-rosinstall-generator \
        python3-wstool python3-catkin-tools python-lxml&& \
    rosdep init && rosdep update && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /utils -p
WORKDIR /utils

# Octomap installation
RUN cd /utils && git clone https://github.com/OctoMap/octomap.git --branch v1.8.1 &&\
    cd octomap && mkdir build && cd build && cmake .. && make install && \
    apt update && \
    apt install -y ros-noetic-octomap ros-noetic-octomap-msgs ros-noetic-octomap-ros \
        ros-noetic-octomap-server

RUN pip3 install VL53L1X
RUN pip3 install RPi.GPIO
WORKDIR /workspace/ros_ws

