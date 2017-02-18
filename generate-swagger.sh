#!/bin/bash
swagger-codegen generate -i swagger.yaml -l html2 -o docs/swagger -v
swagger-codegen generate -i swagger.yaml -l python -o swagger -v