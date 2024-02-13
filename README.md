
# Ringba API Client


<div align="center">

[![PyPI - Version](https://img.shields.io/pypi/v/ringba-api-client.svg)](https://pypi.python.org/pypi/ringba-api-client)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ringba-api-client.svg)](https://pypi.python.org/pypi/ringba-api-client)
[![Tests](https://github.com/nat5142/ringba-api-client/workflows/tests/badge.svg)](https://github.com/nat5142/ringba-api-client/actions?workflow=tests)
[![Codecov](https://codecov.io/gh/nat5142/ringba-api-client/branch/main/graph/badge.svg)](https://codecov.io/gh/nat5142/ringba-api-client)
[![Read the Docs](https://readthedocs.org/projects/ringba-api-client/badge/)](https://ringba-api-client.readthedocs.io/)
[![PyPI - License](https://img.shields.io/pypi/l/ringba-api-client.svg)](https://pypi.python.org/pypi/ringba-api-client)

<!-- [![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) -->

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)


</div>


Simple *unofficial* request wrapper to integrate with the Ringba Public API.


* GitHub repo: <https://github.com/nat5142/ringba-api-client.git>
* Documentation: <https://ringba-api-client.readthedocs.io>
* Free software: MIT


## Quickstart

Install:

```shell
pip install ringba-api-client
```

Import:

```python
from ringba_api_client import RingbaApiClient
```

Initialize:

```python
# provide an API key and account ID
ringba = RingbaApiClient(api_key='XXXXXXXXXXXXXXXX', account_id='XXXXXXXXXXXXXXXX')

# change the account ID
ringba.account_id = 'XXXXXXXXXXXXXXXX'
```

Use:

```python
target = ringba.get_targets(target_id='abdc12345')
```


## Environment variables:

- `RINGBA_API_KEY`
- `RINGBA_ACCOUNT_ID`

Both of these are looked up if not provided on object initialization. If API Key is not provided, object initialization fails.


## Extending

Is the library missing a function that you need and you don't want to update the package? Just extend the class:

```python
# utilities/ringba.py
from ringba_api_client import RingbaApiClient as _RingbaApiClient

class RingbaApiClient(_RingbaApiClient):

    def some_new_method(self, *args, **kwargs):
        # do stuff
```

And then import in your project like so:

```python
from utilities.ringba import RingbaApiClient
```


## TODO:

- Add schema validation for create/update bodies


## Credits

This package was created with [Cookiecutter][cookiecutter] and the [fedejaure/cookiecutter-modern-pypackage][cookiecutter-modern-pypackage] project template.

[cookiecutter]: https://github.com/cookiecutter/cookiecutter
[cookiecutter-modern-pypackage]: https://github.com/fedejaure/cookiecutter-modern-pypackage
