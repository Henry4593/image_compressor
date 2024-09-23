import logging

def init_logging(app):
    logging.basicConfig(
        level=app.config.get("LOG_LEVEL", logging.DEBUG),
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler()
        ]
    )
    app.logger.setLevel(app.config.get("LOG_LEVEL", logging.DEBUG))

    




