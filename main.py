import uvicorn
import asyncio
from Utils import Load_data, TomlException

TOML = './Config.toml'
ENV = './.env'

# Try to load ip address from toml file 
try: IP = Load_data(TOML, ["Webserver", "ip"])
except TomlException or FileNotFoundError: IP = "127.0.0.1"
# Try to load port from toml file
try: PORT = Load_data(TOML, ["Webserver", "port"])
except TomlException or FileNotFoundError: PORT = 8092
# Reverse proxy support
try: PROXY = Load_data(TOML, ["Webserver", "reverse_proxy"])
except TomlException or FileNotFoundError: PROXY = False
# Forwarded allow ips
try: FAI = Load_data(TOML, ["Webserver", "forwarded_allow_ips"])
except TomlException or FileNotFoundError: FAI = []
try: DEBUG = Load_data(TOML, ["Webserver", "debug"])
except TomlException or FileNotFoundError: DEBUG = False

async def Start_Webserver():
    """Starts the webserver"""
    if PROXY:
        if FAI == []: raise TomlException('"forwarded_allow_ips" Required')
        config = uvicorn.Config("Webserver:app", IP, PORT, proxy_headers=True, forwarded_allow_ips=FAI, reload=DEBUG)
    else: config = uvicorn.Config("Webserver:app", IP, PORT, reload=DEBUG)
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    try: asyncio.run(Start_Webserver())
    except KeyboardInterrupt: pass