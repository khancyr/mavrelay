from http.server import BaseHTTPRequestHandler, HTTPServer

HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>MavRelay Home</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', Arial, sans-serif;
            background: linear-gradient(120deg, #e0eafc, #cfdef3 100%);
            margin: 0;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .container {
            background: #fff;
            margin-top: 3em;
            padding: 2.5em 2em 2em 2em;
            border-radius: 18px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.18);
            max-width: 480px;
            width: 100%;
            text-align: center;
        }
        .logo {
            max-width: 220px;
            margin-bottom: 1.5em;
        }
        h1 {
            color: #1a2634;
            font-size: 2.2em;
            margin-bottom: 0.5em;
            letter-spacing: 1px;
        }
        ul {
            list-style: none;
            padding: 0;
            margin: 2em 0 1em 0;
        }
        ul li {
            background: #f5f8fa;
            margin: 0.5em 0;
            padding: 1em 1.2em;
            border-radius: 10px;
            font-size: 1.08em;
            box-shadow: 0 2px 8px 0 rgba(31, 38, 135, 0.06);
            transition: background 0.2s;
        }
        ul li:hover {
            background: #eaf3fb;
        }
        a {
            color: #1976d2;
            text-decoration: none;
            font-weight: 500;
            transition: color 0.2s;
        }
        a:hover {
            color: #0d47a1;
            text-decoration: underline;
        }
        .info {
            margin-top: 2.5em;
            color: #555;
            font-size: 0.98em;
        }
        @media (max-width: 600px) {
            .container { padding: 1em; }
            h1 { font-size: 1.3em; }
        }
    </style>
</head>
<body>
    <div class="container">
        <img src="https://www.ardupilot.org/assets/images/ardupilot_logo_2017.png" alt="ArduPilot Logo" class="logo" />
        <h1>MavRelay Home</h1>
        <ul>
            <li><a href="http://localhost:8889/">MediaMTX WebRTC (port 8889)</a></li>
            <li>RTSP feed available at <b>rtsp://localhost:8554/</b> (port 8554)</li>
            <li>Mavlink2Rest WebSocket: <b>ws://localhost:8080/v1/rest/ws</b></li>
            <li>Mavlink2Rest Web UI: <a href="http://localhost:8080/">http://localhost:8080/</a></li>
            <li>Mavlink-Camera-Manager WebRTC: <b>ws://localhost:6021</b></li>
            <li>Mavlink-Camera-Manager Config: <a href="http://localhost:6020/">http://localhost:6020/</a></li>
            <li><a href="http://localhost:8000/">Cockpit (port 8000)</a></li>
        </ul>
        <div class="info">
            <p>All links assume you are accessing from the host machine. Replace <b>localhost</b> with your server IP if needed.</p>
        </div>
    </div>
</body>
</html>
'''


class HomeHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        host = self.headers.get('Host', 'localhost')
        # Extract just the hostname (strip port)
        host_ip = host.split(':')[0]
        # Use the same port as in the Host header for homepage, else default to 8081
        # homepage_port = host.split(':')[1] if ':' in host else '8081'
        # Compose URLs with the detected host
        html = HTML.replace('localhost:8889', f'{host_ip}:8889') \
            .replace('localhost:8554', f'{host_ip}:8554') \
            .replace('localhost:8080', f'{host_ip}:8080') \
            .replace('localhost:6021', f'{host_ip}:6021') \
            .replace('localhost:6020', f'{host_ip}:6020') \
            .replace('localhost:8000', f'{host_ip}:8000')
        html = html.replace('rtsp://localhost:', f'rtsp://{host_ip}:')
        html = html.replace('ws://localhost:', f'ws://{host_ip}:')
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))


def run(server_class=HTTPServer, handler_class=HomeHandler, port=8081):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving homepage on port {port}...")
    httpd.serve_forever()


if __name__ == '__main__':
    run()
