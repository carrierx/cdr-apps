# Call Detail Record Applications

This repository contains the applications which you can use to get detailed information about the calls.

Currently, the following Python apps are present:

- Get detailed information about the calls using the `after` query parameter
  - [selected Call Detail Record object fields](after_selected_fields.py)
  - [all Call Detail Record object fields](after_all_fields.py)

## System Requirements

- Python 3

## Checkout Source

```bash
git clone git@gitlab.int:carrierx/cdr-apps.git
cd cdr-apps
```

## Change Configuration

Copy the `configuration.py.template` file to `configuration.py` and replace the following variables:

1. Enter your credentials used to make requests to CarrierX API. To create a token, see the [Security Token](https://www.carrierx.com/documentation/quick-start/token) quick start guide.

    ```python
    CARRIERX_API_TOKEN = ''
    ```

2. If you use some specific base API URL, change it here

    ```python
    BASE_CARRIERX_API_URL = 'https://api.carrierx.com'
    ```

3. Set the date that will be used to poll the calls

    ```python
    DATE = ''
    ```

The date is set in the `YYYY-MM-DD` format, e.g., `DATE = '2020-03-15'`.

## Run Application

Now run one of the applications (e.g., `after_selected_fields.py`):

```shell
python3 ./after_selected_fields.py
```

Refer to our [Call Detail Record Application](https://www.carrierx.com/documentation/quick-start/cdr-before-after) quick start for the detailed description of the application and its work.