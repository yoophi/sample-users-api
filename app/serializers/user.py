from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Integer()
    email = fields.Str()
    password = fields.Str()
