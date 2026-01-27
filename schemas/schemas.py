
pet_response_schema = {

  "properties": {
    "id": {
      "type": "integer"
    },
    "name": {
      "type": "string"
    },
    "photoUrls": {
      "type": "array",
      "items": {}
    },
    "tags": {
      "type": "array",
      "items": {}
    },
    "status": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "name",
    "photoUrls",
    "tags",
    "status"
  ]
}