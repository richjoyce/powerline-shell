import os

virtual_env_symbol = u'\ue73c'

def add_virtual_env_segment(powerline):
    env = os.getenv('VIRTUAL_ENV') or os.getenv('CONDA_ENV_PATH') or os.getenv('CONDA_DEFAULT_ENV')
    if env is None:
        return

    env_name = os.path.basename(env)
    bg = Color.VIRTUAL_ENV_BG
    fg = Color.VIRTUAL_ENV_FG
    powerline.append(' {} {} '.format(virtual_env_symbol, env_name), fg, bg)
