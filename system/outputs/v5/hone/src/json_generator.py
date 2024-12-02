import json

class JSONGenerator:
    def convert_to_json(self, data, schema=None):
        if schema:
            return self._apply_schema(data, schema)
        return self._auto_generate_schema(data)

    def _apply_schema(self, data, schema):
        json_data = []
        for row in data:
            json_object = {}
            for key, value in schema.items():
                if isinstance(value, dict):
                    json_object[key] = {sub_key: row[sub_value] for sub_key, sub_value in value.items()}
                else:
                    json_object[key] = row[value]
            json_data.append(json_object)
        return json_data

    def _auto_generate_schema(self, data):
        return [dict(zip(data[0], row)) for row in data[1:]]

    def output_json(self, data, filepath):
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, sort_keys=True)
