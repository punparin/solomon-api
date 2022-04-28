import json
from flask import Flask, request, Response
from BigWebPriceFinder import BigWebPriceFinder
from YuyuteiPriceFinder import YuyuteiPriceFinder


app = Flask(__name__)
bigWebPriceFinder = BigWebPriceFinder()
yuyuteiPriceFinder = YuyuteiPriceFinder()

@app.route('/api/cards', methods=['GET'])
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
                    status=400,
                    mimetype="application/json"
                    )
        
    json_result = result.toJSON()
    response = Response(response=json_result,
                    status=200,
                    mimetype="application/json"
                    )

    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0")
