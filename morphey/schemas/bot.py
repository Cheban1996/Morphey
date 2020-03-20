from marshmallow import (Schema, fields)


class SchemaBot(Schema):
    _id = fields.String(dump_only=True)
    name = fields.String(required=True)
    symbol = fields.String(required=True)
    take_profit = fields.String(required=True)
