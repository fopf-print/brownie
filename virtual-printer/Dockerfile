FROM debian:bookworm

EXPOSE 631

RUN apt-get update \
    && apt-get install -y \
    cups \
    cups-pdf \
    hplip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* && \
    useradd -m fopf -G lpadmin && \
    echo fopf:fopf | chpasswd

RUN sed -i 's/Listen localhost:631/Listen 0.0.0.0:631/' /etc/cups/cupsd.conf && \
    sed -i 's/Browsing Off/Browsing On/' /etc/cups/cupsd.conf && \
    sed -i 's/<Location \/>/<Location \/>\n  Allow All/' /etc/cups/cupsd.conf && \
    sed -i 's/<Location \/admin>/<Location \/admin>\n  Allow All\n  Require user @SYSTEM/' /etc/cups/cupsd.conf && \
    sed -i 's/<Location \/admin\/conf>/<Location \/admin\/conf>\n  Allow All/' /etc/cups/cupsd.conf && \
    echo "ServerAlias *" >> /etc/cups/cupsd.conf && \
    echo "DefaultEncryption Never" >> /etc/cups/cupsd.conf

RUN service cups start && \
    lpadmin \
        -p virtual-hp-laserjet_m14-m17 \
        -E -m 'hplip:0/ppd/hplip/HP/hp-laserjet_m14-m17.ppd' \
        -D 'Virtual printer to do tests' \
        -L 'right in your computer' \
        -v 'cups-pdf:/' && \
    sleep 120
    # я не придумал ничего лучше, чем sleep: https://stackoverflow.com/a/49510750

CMD ["/usr/sbin/cupsd", "-f"]
