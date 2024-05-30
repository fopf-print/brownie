# да, на arch-ике ставим debian))
# нужно зафиксировать версии либ,
# а в этом дебиан лучший (оцените шутку)
FROM debian:12.5

RUN \
    apt-get update && \
    apt-get upgdate -y && \
    apt-get install -y cups hplip system-config-printer

# debug tools
RUN \
    apt-get install -y vim tmux

CMD ["/usr/sbin/cupsd", '-f']
