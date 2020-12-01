import os

from notebook.notebookapp import NotebookWebApplication

default_whitelist = [
    "PWD",
    "KERNEL_USERNAME",
    "KERNEL_HUB_USERNAME",
    "HOME",
    "LANG",
    "SHLVL",
    "KERNEL_LANGUAGE",
    "TERM",
    "CLICOLOR",
    "PAGER",
    "NO_PROXY",
    "HTTP_PROXY",
    "HTTPS_PROXY",
]


def load_jupyter_server_extension(_nb_server_app: NotebookWebApplication) -> None:
    whitelist_str = os.environ.get("JUPYTER_WHITELIST_ENV", None)
    if whitelist_str is not None:
        whitelist = [s.strip().upper() for s in whitelist_str.split(",")]
    else:
        whitelist = default_whitelist

    for name in os.environ:
        if name.upper() not in whitelist:
            del os.environ[name]
