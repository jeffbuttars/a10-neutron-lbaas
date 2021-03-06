PKG_NAME := a10-neutron-lbaas
PKG_NAME_U := a10_neutron_lbaas
PKG_VER := $(shell python -c "from __future__ import print_function; import $(PKG_NAME_U); print($(PKG_NAME_U).__version__)")

.PHONY: test cheese clean

.DEFAULT:
dist: clean
	python ./setup.py sdist

test:
	tox

cheese: clean test dist
	python ./setup.py sdist upload

clean:
	rm -fr dist
	rm -fr *.egg-info

uninstall:
	-yes y | pip uninstall --exists-action=w $(PKG_NAME)

# install: clean test dist
install: clean dist
	pip install --pre --exists-action=w ./

dinstall: uninstall install

