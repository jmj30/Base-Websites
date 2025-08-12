from quart import Quart, render_template, request
from Utils import Load_SC
from main import ENV, LOGENABLED, LOGFILE

app = Quart(__name__, static_folder="./Static", template_folder="./Templates")
app.secret_key = Load_SC(ENV)


if LOGENABLED:
    import logging
    logging.basicConfig(filename=LOGFILE, format='%(asctime)s: %(message)s', level=logging.INFO)
    logger = logging.getLogger("file logger")

@app.get('/')
async def Home():
    ip = request.remote_addr
    if LOGFILE: logger.info(f'"{request.url_rule}" | {ip}')
    return await render_template('Home.html')