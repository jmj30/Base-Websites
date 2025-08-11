{ pkgs, lib, config, ... }:
{ 
  env.LD_LIBARY_PATH = "${pkgs.stdenv.cc.cc.lib}/lib";

  languages.python = {
    enable = true;
    package = pkgs.python313;
    uv.enable = true;
    venv = {
      enable = true;
      requirements = ''
        python-dotenv
        uvicorn
        quart
      '';
    };
  };
}