import uvicorn
import asyncio
from Utils import Toml, TomlHelper, TomlException

TOML = './config.toml'
ENV = './.env'

Defaults = {"ip": "127.0.0.1", "port": 8092, "reverse_proxy": False, "forwarded_allow_ips": [], "debug": False}
Logging_defaults = {"enabled": False}

# Try to load ip address from toml file 
IP = Toml().loadDefaults(TOML, TomlHelper("Webserver", "ip"), Defaults)
# Try to load port from toml file
PORT = Toml().loadDefaults(TOML, TomlHelper("Webserver", "port"), Defaults)
# Reverse proxy support
PROXY = Toml().loadDefaults(TOML, TomlHelper("Webserver", "reverse_proxy"), Defaults)
# Forwarded allow ips
FAI = Toml().loadDefaults(TOML, TomlHelper("Webserver", "forwarded_allow_ips"), Defaults)
# Debug mode
DEBUG = Toml().loadDefaults(TOML, TomlHelper("Webserver", "debug"), Defaults)
# Logging
LOGENABLED = Toml().loadDefaults(TOML, TomlHelper("Webserver.logging", "enabled"), Logging_defaults)
if LOGENABLED: LOGFILE = Toml().loadTomlData(TOML, TomlHelper("Webserver.logging", "file"))
else: LOGFILE = None


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