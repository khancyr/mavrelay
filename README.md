# mavrelay


mavrelay is a deployment script and Docker Compose setup for deploying a MAVLink and video relay server on a cloud server (e.g., DigitalOcean droplet). It integrates:

- **zerotier**: VPN overlay network for secure communication between drone and server
- **mavlink2rest**: Exposes MAVLink telemetry as REST API and WebSocket
- **mediamtx**: Video streaming relay (RTSP/RTMP/HLS)
- **mavlink-camera-manager**: Bridges MAVLink camera protocol, mediamtx, and mavlink2rest
- **cockpit**: Lightweight web-based GCS (Ground Control Station)


This setup is intended to serve as a relay for MAVLink telemetry and video feeds, providing a web interface for remote drone operations. All services communicate over a Zerotier VPN for security and flexibility.

## Web Home Page
The project includes a simple Python web server as a homepage, providing quick links to all major services:

- **Homepage**: [http://localhost:8081](http://localhost:8081) (or your server IP)
   - ArduPilot logo
   - Link to MediaMTX WebRTC (port 8889)
   - RTSP feed info (port 8554)
   - Mavlink2Rest WebSocket and Web UI (port 8080)
   - Mavlink-Camera-Manager WebRTC (port 6021) and config (port 6020)
   - Cockpit (port 8000)

The homepage is built as a Docker service and launched automatically with Docker Compose.


## Features
- Easy deployment with Docker Compose
- Secure VPN networking with Zerotier
- Relays MAVLink telemetry and video streams
- MAVLink camera protocol support for video advertisement
- Web-based GCS interface via Cockpit
- Designed for cloud deployment (e.g., DigitalOcean)


## Architecture

```
         +-------------------+         +-------------------+
         |     Drone         |         |     Server        |
         |-------------------|         |-------------------|
         | Zerotier VPN      | <------> | Zerotier VPN      |
         | MAVLink ->        |         |                   |
         | mavlink2rest      |         | mavlink2rest      |
         | RTSP   ->         |         | mediamtx          |
         +-------------------+         | mavlink-camera-mgr|
                                        | cockpit (web GCS) |
                                        +-------------------+
```


## Repository Structure
```
.
├── docker-compose.yml         # Main Docker Compose file
├── README.md                  # Project documentation
├── homepage/                  # Homepage web server (Python)
│   ├── homepage.py            # Python web server script
│   └── homepage.Dockerfile    # Dockerfile for homepage
├── mediamtx/                  # MediaMTX config
│   └── mediamtx.yml           # Example MediaMTX config
├── mavlink-camera-manager/    # Camera manager config
│   ├── config.yaml            # Example camera manager config
│   └── camera_definition.xml  # Example MAVLink camera definition
├── cockpit-lite/              # Cockpit config
│   └── config.json            # Example Cockpit config
├── .gitignore                 # Git ignore rules
├── .dockerignore              # Docker ignore rules
```


## Quick Start
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/mavrelay.git
   cd mavrelay
   ```
2. Edit the `.env` file:
   - Set your Zerotier network ID in the `ZEROTIER_NETWORK_ID` variable (default is provided).
   - You do not need to edit `docker-compose.yml` for the network ID.
   - Adjust IPs and ports in config files as needed for your setup.
## Environment Variables

The `.env` file in the project root is used to configure the Zerotier network ID (and can be extended for other settings). Example:

```
ZEROTIER_NETWORK_ID=HAHAIAMANETWORKDID
```

Docker Compose will automatically use this value for the zerotier service. To change the network, simply edit the `.env` file and restart the stack.
3. Edit config files in `mediamtx/`, `mavlink-camera-manager/`, and `cockpit-lite/` as needed.
4. Deploy with Docker Compose:
   ```sh
   docker compose up -d
   ```
5. Access the homepage at `http://<server-ip>:8081` for quick links to all services.
6. Access the Cockpit web interface at `http://<server-ip>:8000` (use the Zerotier IP if remote).
## Local Development

To run the homepage server locally (without Docker):

```sh
cd homepage
python3 homepage.py
```
Then open [http://localhost:8081](http://localhost:8081) in your browser.


## Configuration
- **zerotier**: Edit the `docker-compose.yml` to set your Zerotier network ID.
- **mediamtx**: Handles RTSP/RTMP video relay. Configure in `mediamtx/mediamtx.yml` (set drone RTSP source address).
- **mavlink2rest**: Exposes MAVLink telemetry. No config needed by default, but can be customized via environment variables.
- **mavlink-camera-manager**: Bridges MAVLink camera protocol, mediamtx, and mavlink2rest. Configure in `mavlink-camera-manager/config.yaml` and `camera_definition.xml`.
- **cockpit**: Web GCS. Configure endpoints in `cockpit-lite/config.json`.


## License
MIT
