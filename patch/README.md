# Owasp ZAP with support for authentication

## How to build
```bash
patch -p1 < patch/Dockerfile.patch
docker build -t my-zap .
```

## Example
```bash
docker run --rm -v $(pwd)/patch:/zap/wrk/:rw -t myzap zap-baseline.py -I -j \
  -c zap.conf \
  -t https://demo.website.net \
  -t "https://demo.website.net/cb/pulse/viewers/brandPulse/brandPulseViewer.html?id=462d341a-d797-4b13-bea7-3dcd86d83618" \
  -r testreport.html \
   --hook=/zap/auth_hook.py \
  -z "auth.loginurl='https://demo.website.net/cb/nb/login.html' \
      auth.username='admin' \
      auth.password='sandbox' \
      auth.username_field='j_username' \
      auth.password_field='j_password' \
      auth.exclude='.*logout.*' \
      auth.include='https://demo.website.net/cb/nb/.*'"
```

## Extra authentication parameters
```
auth.auto                 Automatically try to find the login fields (username, password, submit). Default True.
auth.loginurl             The URL to the login page. Required.
auth.username             A valid username. Required.
auth.password             A valid password. Required.
auth.username_field       The HTML name or id attribute of the username field.
auth.password_field       The HTML name or id attribute of the password field.
auth.submit_field         The HTML name or id attribute of the submit field.
auth.first_submit_field   The HTML name or id attribute of the first submit field (in case of username -> next page -> password -> submit).
auth.exclude              Comma separated list of excluded URL's (regex). Default: (logout|uitloggen|afmelden|signout)
auth.include              Comma separated list of included URL's (regex). Default: only the target URL and everything below it.
```

# Reference
[ICTU zap-baseline](https://github.com/ICTU/zap-baseline)
