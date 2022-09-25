echo "-> Analyzing code with pylint"
pylint /negrucoin/*.py --load-plugins pylint_django
echo "-> Running tests"
pytest