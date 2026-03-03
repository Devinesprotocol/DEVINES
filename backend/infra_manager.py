import os
import time

def get_environment_info():
    return {
        "environment": os.getenv("RENDER", "local"),
        "timestamp": int(time.time())
    }


def is_production():
    return os.getenv("RENDER") is not None


def get_version():
    return os.getenv("RENDER_GIT_COMMIT", "dev")
