#!/usr/bin/env python3

from botocore import credentials
import botocore.session
import os
import json
import sys

cli_cache = os.path.join(os.path.expanduser("~"), ".aws/cli/cache")
params = {}


def print_credentials(credentials):
    credentials_for_proc = {
        "Version": 1,
        "AccessKeyId": credentials.access_key,
        "SecretAccessKey": credentials.secret_key,
        "SessionToken": credentials.token,
        "Expiration": credentials._expiry_time.isoformat()
    }
    print(json.dumps(credentials_for_proc))


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Usage: aws_auth_helper.py role_profile')
        exit(1)
    else:
        profile = sys.argv[1]

    if profile:
        params["profile"] = profile

    session = botocore.session.Session(**params)
    session.get_component("credential_provider").get_provider(
        "assume-role").cache = credentials.JSONFileCache(cli_cache)

    credentials = session.get_credentials()

    if credentials.access_key and not credentials._is_expired():
        print_credentials(credentials)
