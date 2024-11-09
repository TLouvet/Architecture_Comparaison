author_dto = {
    "type": "object",
    "properties": {
        "first_name": {"type": "string", "maxLength": 100},
        "last_name": {"type": "string", "maxLength": 100},
        "birth_date": {"type": "string", "format": "date"},
        "death_date": {"type": "string", "format": "date"},
        "nationality": {"type": "string", "maxLength": 100},
        "biography": {"type": "string", "maxLength": 2000},
        "books": {
            "type": "array",
            "items": {"type": "integer"},
            "uniqueItems": True
        }
    },
    "required": ["first_name", "last_name", "birth_date", "nationality"],
    "additionalProperties": False
}