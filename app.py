from sanic import Sanic
from sanic.response import json

app = Sanic(__name__)

# Voeg een route toe voor /favicon.ico
@app.route('/favicon.ico')
async def favicon(request):
    return json({"message": "favicon not needed"}, status=204)  # Geeft een 204-status zonder inhoud

# Andere routes van je server
@app.route('/webhook', methods=['POST'])
async def webhook(request):
    # Je webhook-code hier
    return json({"status": "ok"})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1000)
