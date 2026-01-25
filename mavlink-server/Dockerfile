FROM alpine
WORKDIR /mavlink/

ARG TARGET_ARCH=x86_64-unknown-linux-musl

RUN wget -O mavlink-server "https://github.com/bluerobotics/mavlink-server/releases/latest/download/mavlink-server-x86_64-unknown-linux-musl" \
    && chmod +x /mavlink/mavlink-server

ENTRYPOINT ["/mavlink/mavlink-server"]
