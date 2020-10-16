# SMS

# Build and generate a new version
``` shell
python3 setup.py sdist bdist_wheel

twine upload --repository-url http://10.131.3.7:8081/repository/pypi-hosted/ dist/sms-0.0.1-py3-none-any.whl
```