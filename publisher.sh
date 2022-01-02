rm -rf dist
rm -rf dats_*
rm -rf build
venv/bin/python -m pip install twine
venv/bin/python -m pip install wheel
venv/bin/python setup.py sdist
venv/bin/python setup.py bdist_wheel --universal
venv/bin/twine upload dist/* --verbose