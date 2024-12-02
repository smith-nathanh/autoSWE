import json

class JSONGenerator:
    def convert_to_json(self, data, schema=None):
        if schema:
            return [self._apply_schema(row, schema) for row in data]
        else:
            return [dict(zip(self.column_names, row)) for row in data]

    def _apply_schema(self, row, schema):
        json_object = {}
        for key, value in schema.items():
            if isinstance(value, dict):
                json_object[key] = self._apply_schema(row, value)
            else:
                json_object[key] = row[self.column_names.index(value)]
        return json_object

    def output_json(self, data, filepath):
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4, sort_keys=True)