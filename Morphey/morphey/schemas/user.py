from marshmallow import (Schema, fields, post_load, validate)


class SchemaUser(Schema):
    id = fields.String(load_only=True)
    first_name = fields.String(required=True, validate=validate.Length(min=2))
    last_name = fields.String(required=True, validate=validate.Length(min=2))
    full_name = fields.String(load_only=True)
    email = fields.Email(load_only=True)
    # password = fields.String(required=True, load_only=True, validate=validate.Length(min=8))
