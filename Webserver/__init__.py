from quart import Quart, render_template
from Utils import Load_SC
from main import ENV

app = Quart(__name__, static_folder="./Static", template_folder="./Templates")
app.secret_key = Load_SC(ENV)


@app.get('/')
async def Home():
    return render_template('Home.html')