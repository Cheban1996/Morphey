from marshmallow import (Schema, fields, post_load, validate)


class SchemaUser(Schema):
    _id = fields.String(dump_only=True)
    username = fields.String(
        required=True,
        validate=validate.Length(min=5)
    )
    password = fields.String(
        required=True,
        load_only=True,
        validate=validate.Length(min=8)
    )