FROM ubuntu:24.04

ARG DEBIAN_FRONTEND=noninteractive

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt update -y && \
    apt install -y --no-install-recommends \
        libgstreamer1.0-0 \
        libgstreamer-plugins-base1.0-0 \
        libgstreamer-plugins-bad1.0-0 \
        libgstrtspserver-1.0-0 \
        gstreamer1.0-x \
        gstreamer1.0-nice \
        gstreamer1.0-libav \
        gstreamer1.0-plugins-ugly \
        wget \
        ca-certificates \
        htop \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /mavlink
# Download the latest release binary from GitHub
RUN wget -O mavlink-camera-manager "https://github.com/mavlink/mavlink-camera-manager/releases/download/t3.22.3/mavlink-camera-manager-linux-desktop" \
    && chmod +x /mavlink/mavlink-camera-manager \
    && mkdir -p /mavlink/config

ENTRYPOINT ["/mavlink/mavlink-camera-manager", "--mavlink=tcpout:0.0.0.0:5777", "--settings-file", "/mavlink/config/settings.json", "--verbose"]

