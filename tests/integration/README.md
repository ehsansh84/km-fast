### Run test in debug mode:
```commandline
DEBUG=http,http:capture,http:response npx artillery run tests/integration/sample.yaml
```

Quiet mode:
```
npx artillery run --quiet tests/integration/sample.yaml
```

### To check project using lint:
```commandline
ruff check .
```
