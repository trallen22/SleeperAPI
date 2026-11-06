import logging

# Create or get the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Log everything (DEBUG level or higher)

# Prevent multiple handlers if the logger is configured multiple times
if not logger.handlers:
    # Create a file handler to log to a file
    file_handler = logging.FileHandler('shared_log_file.log')
    file_handler.setLevel(logging.DEBUG)

    # Define log format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Add file handler to logger
    logger.addHandler(file_handler)

# debug_handler_ref = None

# def setup_logger():
#     handler = logging.StreamHandler() # Send logs to the console
#     handler.setLevel(logging.NOTSET) # Set the handler level; NOTSET logs everything
#     debugHandler = logging.FileHandler("debug_file.log")
#     global debug_handler_ref
#     debug_handler_ref = debugHandler
#     debugHandler.setLevel(0)
#     debugFormatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#     debugFormatter.default_msec_format = None
#     debugFormatter.default_time_format = '%Y-%m-%d %H:%M:%S'
#     debugHandler.setFormatter(debugFormatter)
#     rootLogger = logging.getLogger()
#     rootLogger.setLevel(logging.DEBUG)
#     rootLogger.addHandler(handler) # Attach the handler to the logger
#     # rootLogger.addHandler(debugHandler)

# def add_debug_handler():
#     if (debug_handler_ref) and (debug_handler_ref not in logging.getLogger().handlers):
#         logging.getLogger().addHandler(debug_handler_ref)

# def remove_debug_handler():
#     if (debug_handler_ref) and (debug_handler_ref in logging.getLogger().handlers):
#         logging.getLogger().removeHandler(debug_handler_ref)

# ######################
# # Main Execution
# ######################
# # set up the logger for all files
# setup_logger()
# myLogger = logging.getLogger(__name__)