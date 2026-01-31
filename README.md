Petstore API Tests  
  
Automated API tests for the Swagger Petstore using **pytest**, **requests**, **jsonschema** and **Allure**.  

Tech stack  

-Python 3.11  
-pytest  
-requests  
-jsonschema  
-allure-pytest  
-Github Actions (CI)  

PROJECT STRUCTURE  

|-----tests/  
| |----pet/  
| | |---test_pet_crud.py  
| | |---test_pet_negative.py  
| | |---test_pet_contract.py  
| | |---test_pet_smoke.py  
| | |---test_pet_edge.py  
| |----conftest.py  
|-----schemas/  
| |----schemas.py  
|-----utils/  
| |----pet_payloads.py  
| |----helpers.py  
| |----__init__.py  
|-----.github/  
| |----workflows/  
| | |---tests.yml  
|-----requirements.txt  
|-----pytest.ini  
|-----README.md  
|-----.gitignore  

How to run tests locally  

Install dependencies:  
pip install -r requirements.txt  

Run all tests:  
pytest -v  

Run selected tests:  
pytest -m smoke  
pytest -m contract  
pytest -m crud  
pytest -m edge  
pytest -m negative  
  
Generate Allure results:  
pytest --alluredir=allure_results  

Open Allure report:  
allure serve allure-results  
Note: allure_results and allure_report are generated locally or in CI and are not commited to the repository.  

Test types  

Smoke - basic API availability  
CRUD - create/read/update/delete flows  
Contract - reponse schema validation  
Negative - invalid input handling  
Edge - edge cases and unexpected behavior  

CI/CD  

Tests are automatically executed on:  
-push to main  
-pull requests  
via Github Actions  
  
Allure results are stored as workflow artifacts  

KNOWN ISSUES  

Some tests are marked as xfail due to known Petstore API bugs:  
-invalid ID handling  
-empty status validation  
-server errors instead of 400 responses  
