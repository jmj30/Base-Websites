# Base Site

Main repo: [Gitlab](https://gitlab.jmj30yt.xyz/jmj30/)

Made with caffine, love and [Python](https://www.python.org/)

## How to use

Open terminal and run (one of them):

[UV](https://github.com/astral-sh/uv) (Default way):
`uv run main.py`

Python:
`python -m venv .venv`
`python -m pip -r requirements.txt`

[Docker](https://www.docker.com/):
`docker build -t Site .`

Docker compose:
`docker compose up -d && docker compose logs -f`


Nix/Nixos [devenv](https://devenv.sh/):
`devenv shell`
`uv run main.py`