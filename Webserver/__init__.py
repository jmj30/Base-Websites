from quart import Quart, render_template, request
from Utils.WS import loadKey
from main import ENV, LOGENABLED, LOGFILE

app = Quart(__name__)
app.secret_key = loadKey(ENV)


@app.get('/')
async def Home():
    return await render_template('Home_Page.html')