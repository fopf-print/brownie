# brownie

Этот сервис запускается непосредственно на малинке и отвечает за печать.

## Develop

Для удобства разработки и тестирования есть `virtual-printer`. Для компьютера (и программ)
он неотличим от обычного принтера, но после отрправки файла на печать он сохраняется в папке `printer-output`


Как поднять `virtual-printer`
```bash
cd virtual-printer
docker compose build
docker compose up
```

## Если Даня не победил docker

Райт нау (2024-05-20 00:09) пока(?) не получилось заставить работать cups
через docker.

Пока выглядит, что получится запустить через docker, но если вруг нет - 
то нужно поставить poetry локально на малинку (скорее всего уже стоит), а
дальше запустить)
