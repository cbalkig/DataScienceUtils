rm -rf dist
rm -rf dats_*
rm -rf build
python setup.py sdist bdist_wheel --universal
venv/bin/twine upload dist/* --verbose