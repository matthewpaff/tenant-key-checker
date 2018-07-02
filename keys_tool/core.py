"""Original bounded concept exercise with supplied synthetic data only."""


def fields(value, required, optional=()):
    if not isinstance(value, dict) or not set(required) <= value.keys() or not value.keys() <= set(required) | set(optional):
        raise ValueError("Unexpected or missing object fields")


def integer(value, low=0, high=10**12):
    if type(value) is not int or not low <= value <= high:
        raise ValueError("Integer outside the supported range")
    return value


def label(value):
    if not isinstance(value, str) or not value.strip() or len(value) > 80 or any(ord(c) < 32 for c in value):
        raise ValueError("Expected a nonblank label of at most 80 characters")
    return value.strip()


def sequence(value, maximum):
    if not isinstance(value, list) or len(value) > maximum:
        raise ValueError("Expected a bounded list")
    return value

def evaluate(data):
    fields(data, ("employees", "references"))
    keys = set()
    for employee in sequence(data["employees"], 500):
        fields(employee, ("tenant", "id"))
        key = (label(employee["tenant"]), integer(employee["id"], 1))
        if key in keys:
            raise ValueError("Duplicate composite employee key")
        keys.add(key)
    missing = []
    for reference in sequence(data["references"], 500):
        fields(reference, ("tenant", "employee_id"))
        key = (label(reference["tenant"]), integer(reference["employee_id"], 1))
        if key not in keys:
            missing.append({"tenant": key[0], "employee_id": key[1]})
    return {"valid": not missing, "missing": missing}
