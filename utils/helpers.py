import requests
import allure
import json

class APISession(requests.Session):
    def request(self, method, url, **kwargs):
        response = super().request(method, url, **kwargs)

        try:
            body = json.dumps(response.json(), indent=2)
        except Exception:
            body = response.text

        allure.attach(
            body,
            name=f"{method} {url}",
            attachment_type=allure.attachment_type.JSON
        )

        return response


URLS ={

    "base_url": "https://petstore.swagger.io/v2"
}

