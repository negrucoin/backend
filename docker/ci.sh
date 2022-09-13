echo "-> Analyzing code with pylint"
pylint /negrucoin/ --load-plugins pylint_django
echo "-> Running tests"
pytest /negrucoin/