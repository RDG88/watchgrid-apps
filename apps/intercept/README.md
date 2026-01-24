# iNTERCEPT - WatchGrid App

This is a WatchGrid-compatible deployment of [iNTERCEPT](https://github.com/smittix/intercept), a signal intelligence platform for software-defined radio.

## Features

- Pager Decoding (POCSAG/FLEX)
- 433MHz Sensors (Weather stations, TPMS, IoT devices)
- Aircraft Tracking (ADS-B)
- Vessel Tracking (AIS)
- ACARS Messaging
- Listening Post (Frequency scanner)
- Satellite Tracking
- WiFi Scanning
- Bluetooth Scanning
- Spy Stations Database

## Hardware Requirements

- RTL-SDR or HackRF USB device
- WiFi adapter with monitor mode support (for WiFi scanning)
- Optional: GPS device for location tracking

## Deployment

This app is designed to be deployed through the WatchGrid platform. The GitHub Actions workflow automatically builds and pushes the Docker image to GitHub Container Registry.

### Configuration

Available configuration options:
- `SDR_DEVICE`: SDR device type (rtlsdr, hackrf, or auto)
- `ADMIN_USERNAME`: Web interface admin username
- `ADMIN_PASSWORD`: Web interface admin password
- `GPS_ENABLED`: Enable GPS support
- `GPSD_HOST`: GPS daemon host

## Building Locally

```bash
docker build -t intercept:local .
```

## License

Based on [smittix/intercept](https://github.com/smittix/intercept) - MIT License
# iNTERCEPT is building...
