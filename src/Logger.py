import logging
import datetime


class Logger:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)

    def generate_payload(self, level, function_name, body):
        return {
            "timestamp": str(datetime.datetime.now()),
            "level": level,
            "function_name": function_name,
            "body": body
        }

    def info(self, function_name, body):
        logging.info(self.generate_payload("INFO", function_name, body))

    def warning(self, function_name, body):
        logging.warning(self.generate_payload("WARNING", function_name, body))

    def error(self, function_name, body):
        logging.error(self.generate_payload("ERROR", function_name, body))
