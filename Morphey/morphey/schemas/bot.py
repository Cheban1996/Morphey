from marshmallow import Schema, fields


class SchemaBot(Schema):
    id = fields.String(load_only=True)
    name = fields.String(required=True)
    symbol = fields.String(required=True)
    take_profit = fields.String(required=True)
