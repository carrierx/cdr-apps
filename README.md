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

Replace line 3 in either `after_selected_fields.py` or `after_all_fields.py` with your own CarrierX API access token:

```python
headers = {'Authorization': 'Bearer 12345678-abcd-1234-abcd-1234567890ab'}
```

Update the date that will be used to poll the calls (line 6):

```python
date = '2020-03-15'
```

## Run Application

Now run one of the applications (e.g., `after_selected_fields.py`):

```shell
python3 ./after_selected_fields.py
```

Refer to our [Call Detail Record Application](https://www.carrierx.com/documentation/quick-start/cdr-before-after) quick start for the detailed description of the application and its work.