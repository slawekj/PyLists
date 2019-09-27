#!/bin/bash

find ./students -name '*.py' -exec sh -c "echo '{}' \$(python '{}' | python tester.py)" \;
