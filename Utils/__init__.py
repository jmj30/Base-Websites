# Path
from pathlib import Path

# Toml Stuff
from tomllib import load

# Env Stuff
from dotenv import load_dotenv
from os import environ

# Toml
class TomlException(Exception):
    """For raising a toml exception

    Args:
        Exception (str): Message to send
    """
    def __init__(self, message):
        super().__init__(message)

def Load_toml(path:Path | str):
    """Loads a toml file

    Args:
        path (Path): Path object or string

    Raises:
        FileNotFoundError: When the file can't be found

    Returns:
        dict: The toml file as a dict
    """
    if type(path) is str: path = Path(path)
    if path.is_file(): return load(path.open("rb"))
    raise FileNotFoundError(f'"{path}" Is Not a File')

def Load_data(path:Path, data:list) -> any:
    """loads data from a toml file

    Args:
        path (Path | str): Path object or string
        data (str): String of the valve to get

    Raises:
        TomlException: When toml file is missing data

    Returns:
        any: any type of object
    """
    Lt = Load_toml(path)[data[0]]
    try: return Lt[data[1]]
    except KeyError: raise TomlException(f'Toml Missing "{data}"')


# Env
class EnvException(Exception):
    """For raising a env exception

    Args:
        Exception (str): Message to send
    """
    def __init__(self, message):
        super().__init__(message)

def Load_env(path:Path | str, data:str):
    if type(path) is str: path = Path(path)
    e = load_dotenv(path)
    if path.is_file():
        try: return environ[data]
        except KeyError: raise EnvException(f'Env Missing "{data}"')
    else: raise FileNotFoundError(f'"{path}" Is Not a File')

def Load_SC(path:Path):
    try: Load_env(path, "SECRET_KEY")
    except EnvException or FileNotFoundError:
        try: open(path, 'x').close()
        except FileExistsError: pass
        with open(path, 'rt+') as l:
            if l.read().strip() == "":
                import secrets
                l.write(f'SECRET_KEY="{secrets.token_urlsafe(16)}"')
        exit()