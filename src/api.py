import os
import json
from flask import Flask, request, Response
from flask_caching import Cache
from flask_api import status

from BigWebPriceFinder import BigWebPriceFinder
from YuyuteiPriceFinder import YuyuteiPriceFinder


app = Flask(__name__)
app.config.from_object('Config.Config')

cache = Cache(app)

bigWebPriceFinder = BigWebPriceFinder()
yuyuteiPriceFinder = YuyuteiPriceFinder()

@app.route('/api/cards', methods=['GET'])
@cache.cached(timeout=259200, query_string=True)
def cards():
    args = request.args
    name = args.get("name")
    source = args.get("source")

    if source == "bigweb":
        result = bigWebPriceFinder.find_prices(name)
    elif source == "yuyutei":
        result = yuyuteiPriceFinder.find_prices(name)
    else:
        return Response(response=json.dumps({"message": "Invalid request"}),
                    status=status.HTTP_400_BAD_REQUEST,
                    mimetype="application/json"
                    )
        
    json_result = result.toJSON()
    response = Response(response=json_result,
                    status=status.HTTP_200_OK,
                    mimetype="application/json"
                    )

    return response

@app.route('/health', methods=['GET'])
def health():
    return Response(response="OK", status=status.HTTP_200_OK)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
