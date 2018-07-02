"""Original case templates with independently supplied expected results."""
import copy
import re

TEMPLATES = [('allow the same employee ID under different tenant keys', {'employees': [{'tenant': 'a{n}', 'id': 1}, {'tenant': 'b{n}', 'id': 1}], 'references': [{'tenant': 'a{n}', 'employee_id': 1}]}, {'valid': True, 'missing': []}), ('report a reference absent from the selected tenant', {'employees': [{'tenant': 'a{n}', 'id': 1}], 'references': [{'tenant': 'b{n}', 'employee_id': 1}]}, {'valid': False, 'missing': [{'tenant': 'b{n}', 'employee_id': 1}]}), ('accept empty key and reference sets', {'employees': [], 'references': []}, {'valid': True, 'missing': []}), ('reject duplicate composite employee keys', {'employees': [{'tenant': 'a{n}', 'id': 1}, {'tenant': 'a{n}', 'id': 1}], 'references': []}, None), ('reject boolean employee IDs', {'employees': [{'tenant': 'a{n}', 'id': True}], 'references': []}, None)]


def make_case(index):
    description, source, expected = copy.deepcopy(TEMPLATES[index % len(TEMPLATES)])
    def fill(value):
        if isinstance(value, str):
            if re.fullmatch(r"@i[+]\d+", value):
                return index + int(value[3:])
            return value.replace("{n}", str(index))
        if isinstance(value, list):
            return [fill(item) for item in value]
        if isinstance(value, dict):
            return {fill(key): fill(item) for key, item in value.items()}
        return value
    case = {"id": "keys-{:04d}".format(index), "description": description, "input": fill(source)}
    case.update({"expected_error": True} if expected is None else {"expected": fill(expected)})
    return case
