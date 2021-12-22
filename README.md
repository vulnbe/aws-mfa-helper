# AWS auth helper for MFA support in terraform

# AWS config example

    [profile user]
    region = eu-central-1

    [profile privileged]
    source_profile = user
    mfa_serial = arn:aws:iam::xxx:mfa/user
    role_arn = arn:aws:iam::xxx:role/PrivilegedRole

    [profile privileged_terraform]
    credential_process = aws_auth_helper.py privileged
