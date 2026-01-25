FROM alpine
WORKDIR /mavlink/

ARG TARGET_ARCH=x86_64-unknown-linux-musl

RUN wget -O mavlink2rest "https://github.com/mavlink/mavlink2rest/releases/latest/download/mavlink2rest-x86_64-unknown-linux-musl" \
    && chmod +x /mavlink/mavlink2rest

ENTRYPOINT ["/mavlink/mavlink2rest"]
