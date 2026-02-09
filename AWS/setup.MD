AWS -- Setup
============

Simple setup of AWS for developer -- personal use which still sticks to best practices in order to provide 
access to AWS console (person), CLI's, local terminal and applications (i.e Web app or a CI/CD tool).


* **Root User:** **Admin** and account creation, as small operations as possible account-level stuff (billing, MFA, closing account, rare “break-glass” actions)
* **IAM Identity Center (SSO):** Person's access to AWS console (human) + CLI locally
* **IAM Role** Assume Role
* **IAM Role attached to the compute**: Application code (i.e Python Web app accessing S3)

* **IAM User**: managed individually per account with long-lived credentials, are generally discouraged for human access due to security risks and scalability challenges.

### Steps

When enabling Identity Center, choose the region carefully (Identity Center lives in one region per instance)

1. Enable root MFA
2. Create (or enable) AWS Organizations (still just you + one account)
3. Enable IAM Identity Center as an Organization instance
4. Create a user for yourself in Identity Center, assign a permission set (Admin for labs, or a tighter one)

then:

```bash
aws configure sso
aws sso login
```

5. 🚨🚨🚨 Create a Billing Alert (to avoid forget something and pay!!!) 🚨🚨🚨

