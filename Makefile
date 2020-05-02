.PHONY: gui clean test lint run package

gui:
	pyside2-uic ./projectdiffview/gui.ui -o ./projectdiffview/gui.py

tox:
	tox -p all

lint:
	tox -e flake8,pylint

test:
	tox -e test

clean:
	rm -rf .tox .pytest_cache htmlcov *.egg-info .coverage

package:
	PYTHONOPTIMIZE=1 pyinstaller projectdiffview/__main__.py \
		--clean \
		--nowindowed \
		--noconsole \
		--add-data "tests/data:tests/data" --add-data "README.md:." \
		--noconfirm
