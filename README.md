# WAQI Prometheus Exporter

A simple exporter that can requests waqi.info and exposes the data as prometheus metrics.


## Usage

```bash
make docker

Replace on docker-compose.yml with your CITIES (CITY1,CITY2,ect) & AQICN_TOKEN

docker-compose up -d
```