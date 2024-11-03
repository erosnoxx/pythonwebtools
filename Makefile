test:
	pytest -v -p no:warnings

dist:
	python3 setup.py sdist bdist_wheel

upload:
	twine upload dist/*
