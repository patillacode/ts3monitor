## ts3monitor


### What?

A simple flask app that monitors a TeamSpeak 3 server.
It will return status 200 if the server is up and running, otherwise it will return status 503 if offline and 500 if the server is not reachable/there is an error.

### Why?

I needed a simple way to monitor the status of a TeamSpeak 3 server, so I created this small app.
The main use case is to use it as a health check for my server's [homepage](https://gethomepage.dev/latest/).

### System Requirements

Before using ts3monitor, ensure you have the following installed:

- Python >= `3.10`
- pip >= `21.2.4`
- Docker >= `20.10.8` (optional)

### Installation

Clone the repository:
```bash
git clone https://github.com/dvitto/ts3monitor.git
cd ts3monitor
```

Install the dependencies and the package:
```bash
make install

# or manually:

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Usage

#### Local/Development
```bash
make serve

# or

python main.py
```

#### Docker
```bash
docker-compose up -d --build
```

### Configuration

The configuration is done via environment variables, check the `.env` file for the available options.

### License

ts3monitor is released under MIT License. See [LICENSE](LICENSE) for details.

