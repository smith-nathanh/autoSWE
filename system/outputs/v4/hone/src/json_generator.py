import json

class JSONGenerator:
    def convert_to_json(self, data, schema=None):
        if schema:
            return [self._apply_schema(row, schema) for row in data]
        else:
            return [dict(zip(data[0], row)) for row in data[1:]]

    def _apply_schema(self, row, schema):
        json_object = {}
        for key, value in schema.items():
            if isinstance(value, dict):
                json_object[key] = self._apply_schema(row, value)
            else:
                json_object[key] = row[value]
        return json_object

    def output_json(self, data, filepath):
        with open(filepath, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4, sort_keys=True)
