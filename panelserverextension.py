from subprocess import Popen

def load_jupyter_server_extension(nbapp):
    """serve the notebook with bokeh server"""
    Popen(["panel", "serve", "myvigicrues_binder.ipynb", "--allow-websocket-origin=*"])