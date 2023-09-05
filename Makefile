# AudioVis
# Visualize audio with graphs.
# Github: https://www.github.com/lewisevans2007/AudioVis
# Licence: GNU General Public License v3.0
# By: Lewis Evans

python = python3

pip = pip3

all: update_pip install_requirements build

build:
	$(python) setup.py sdist bdist_wheel

update_pip:
	$(pip) install --upgrade pip

install_requirements:
	$(pip) install -r requirements.txt
	$(pip) install --user --upgrade setuptools

clean:
	rm -rf build dist ImgVis.egg-info

.PHONY: all build update_pip install_requirements clean