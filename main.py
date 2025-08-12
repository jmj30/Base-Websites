import uvicorn
import asyncio
from Utils import Load_defaults, TomlException, Load_data

TOML = './Config.toml'
ENV = './.env'

Defaults = {"ip": "127.0.0.1", "port": 8092, "reverse_proxy": False, "forwarded_allow_ips": [], "debug": False}
Logging_defaults = {"enabled": False}

# Try to load ip address from toml file 
IP = Load_defaults(TOML, ["Webserver", "ip"], Defaults)
# Try to load port from toml file
PORT = Load_defaults(TOML, ["Webserver", "port"], Defaults)
# Reverse proxy support
PROXY = Load_defaults(TOML, ["Webserver", "reverse_proxy"], Defaults)
# Forwarded allow ips
FAI = Load_defaults(TOML, ["Webserver", "forwarded_allow_ips"], Defaults)
# Debug mode
DEBUG = Load_defaults(TOML, ["Webserver", "debug"], Defaults)
# Logging
LOGENABLED = Load_defaults(TOML, ["Webserver.logging", "enabled"], Logging_defaults)
if LOGENABLED: LOGFILE = Load_data(TOML, ["Webserver.logging", "file"])

async def Start_Webserver():
    """Starts the webserver"""
    if PROXY:
        if FAI == []: raise TomlException('"forwarded_allow_ips" Required')
        config = uvicorn.Config("Webserver:app", IP, PORT, proxy_headers=True, forwarded_allow_ips=FAI, reload=DEBUG)
    else: config = uvicorn.Config("Webserver:app", IP, PORT, reload=DEBUG)
    server = uvicorn.Server(config)
    if LOGENABLED: print(f"Log file enabled: {LOGFILE}")
    await server.serve()

if __name__ == "__main__":
    try: asyncio.run(Start_Webserver())
    except KeyboardInterrupt: pass