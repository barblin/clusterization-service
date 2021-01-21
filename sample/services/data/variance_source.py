import os

from sample.config.config import variances_location


def store(variance_data):
    if not os.path.exists(variances_location()):
        os.mkdir(variances_location())

    content = variance_data.jsonify()
    __write_overwrite(variance_data.identity, str(content))


def load(identity):
    return str(__read(identity))


def delete_repo():
    if os.path.isdir(variances_location()):
        for f in os.listdir(variances_location()):
            os.remove(os.path.join(variances_location(), f))


def __write_overwrite(filename, content):
    file = open(variances_location() + filename, "w")
    file.write(content)
    file.close()


def __read(filename):
    try:
        file = open(variances_location() + filename, "r")
        return file.read()
    except FileNotFoundError:
        return ""
