from flask import Flask, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import logging
import logging_loki
# from opentelemetry import trace
# from opentelemetry.sdk.trace import TracerProvider
# from opentelemetry.sdk.trace.export import BatchSpanProcessor
# from opentelemetry.exporter.jaeger.thrift import JaegerExporter
# from opentelemetry.instrumentation.flask import FlaskInstrumentor

handler = logging_loki.LokiHandler(
    url="http://observability-loki:3100/loki/api/v1/push", 
    tags={"application": "crud-app"},
    # auth=("username", "password"),
    version="1",
)

logger = logging.getLogger("central-logger")
logger.addHandler(handler)

# In-memory data storage
data = {}

app = Flask(__name__)

# Set up OpenTelemetry tracing
# trace.set_tracer_provider(TracerProvider())
# jaeger_exporter = JaegerExporter(
#     agent_host_name='localhost',  # Your Jaeger agent's host
#     agent_port=6831,  # The port your Jaeger agent is listening on
# )
# span_processor = BatchSpanProcessor(jaeger_exporter)
# trace.get_tracer_provider().add_span_processor(span_processor)

# FlaskInstrumentor().instrument_app(app) # excluded_urls="client/.*/info,healthcheck"

metrics = PrometheusMetrics(app)

# # static information as metric
# metrics.info('app_info', 'Application info', version='1.0.3')

@app.route('/items', methods=['POST'])
def create_item():
    item_id = len(data) + 1
    item = request.json
    data[item_id] = item
    logger.info('{"request": "post"}')
    return jsonify({'id': item_id, 'item': item}), 201

@app.route('/items', methods=['GET'])
def get_items():
    logger.info('{"request": "get-items"}')
    return jsonify(data), 200

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = data.get(item_id)
    logger.info('{"request": "get-one-item"}')
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    return jsonify({'id': item_id, 'item': item}), 200

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    logger.info('{"request": "put-item"}')
    if item_id not in data:
        return jsonify({'error': 'Item not found'}), 404
    data[item_id] = request.json
    return jsonify({'id': item_id, 'item': data[item_id]}), 200

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    logger.info('{"request": "delete-item"}')
    if item_id not in data:
        return jsonify({'error': 'Item not found'}), 404
    del data[item_id]
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)