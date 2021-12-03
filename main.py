import sys
from sanic import Sanic, response
import os

app = Sanic(__name__)
here = os.path.dirname(__file__)

app.static("/static", os.path.join(here, "static/"))


@app.route("/")
def default(request):
    return response.redirect(app.url_for("frontend"))


@app.route("/fe/")
def frontend(request):
    return response.file(
        os.path.join(here, "static/frontend/index.html")
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, access_log=False)
