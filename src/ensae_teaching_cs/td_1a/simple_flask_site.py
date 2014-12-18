# -*- coding: utf-8 -*-
"""
@file
@brief Defines a simple web site in Flask which allows unit testing
"""


from flask import Flask, Response, request
from .flask_helper import Text2Response, Exception2Response

app = Flask(__name__)

def shutdown_server():
    """
    to shutdown the service
    """
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown/', methods=['POST'])
def shutdown():
    """
    shuts down the service
    """
    shutdown_server()
    return Text2Response('Server shutting down...')

@app.route('/help/<path:command>')
def help_command(command):
    """
    return a very basic help message on command command

    @param      command     command
    @return                 help
    """
    try:
        if command is None or command == "exception":
            raise Exception("no help for command: {0}".format(command))
        return Text2Response("help for command: {0}".format(command))
    except Exception as e :
        return Exception2Response(e)

@app.route('/')
def main_page():
    """
    defines the main page
    """
    message = """Simple Flask Site
                            /                   help on command
                            /help/<command>     help on command command
                            /upload/            upload a file (use post)
                            /shutdown/          shutdown the server (for unit test)
            """.replace("                            ","")
    return Text2Response(message)



if __name__ == "__main__":
    app.run(host="localhost", port=8019)