from quart import Quart
from Utils import Load_env
from main import ENV

app = Quart(__name__, static_folder="./Static", template_folder="./Templates")

Load_env(ENV, "render")

