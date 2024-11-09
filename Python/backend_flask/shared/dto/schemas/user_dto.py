user_dto = {
    "type": "object",
    "properties": {
        "email": {"type": "string", "format": "email"},
        "first_name": {"type": "string"},
        "last_name": {"type": "string"},
        "role": {"type": "string", "enum": ["admin", "reader"]},
    },
    "required": ["email", "first_name", "last_name", "role"],
    "additionalProperties": False
}
