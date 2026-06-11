class YAMLError(Exception):
    pass


def safe_load(text):
    result = {}
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            raise YAMLError(f"Unsupported YAML line: {raw_line}")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value in {"", "null", "Null", "NULL"}:
            result[key] = None
        elif value in {"true", "True", "TRUE"}:
            result[key] = True
        elif value in {"false", "False", "FALSE"}:
            result[key] = False
        else:
            if (
                len(value) >= 2
                and value[0] == value[-1]
                and value[0] in {"'", '"'}
            ):
                value = value[1:-1]
            result[key] = value
    return result
