#!/usr/bin/env bash

set -euxo pipefail

echo "Running linters and formatters..."

isort democritus_hypothesis/ tests/

black democritus_hypothesis/ tests/

mypy democritus_hypothesis/ tests/

pylint --fail-under 9 democritus_hypothesis/*.py

flake8 democritus_hypothesis/ tests/

bandit -r democritus_hypothesis/

# we run black again at the end to undo any odd changes made by any of the linters above
black democritus_hypothesis/ tests/
