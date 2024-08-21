PREFIX=$(CURDIR)/debian/

install: python3-cyberfusion-external-providers-ip-ranges

python3-cyberfusion-external-providers-ip-ranges: PKGNAME	:= python3-cyberfusion-external-providers-ip-ranges
python3-cyberfusion-external-providers-ip-ranges: PKGPREFIX	:= $(PREFIX)/$(PKGNAME)
python3-cyberfusion-external-providers-ip-ranges: SDIR		:= python

python3-cyberfusion-external-providers-ip-ranges:
	rm -rf $(CURDIR)/build
	python3 setup.py install --force --root=$(PKGPREFIX) --no-compile -O0 --install-layout=deb

clean:
	rm -rf $(PREFIX)/python3-cyberfusion-external-providers-ip-ranges/
	rm -rf $(PREFIX)/*debhelper*
	rm -rf $(PREFIX)/*substvars
	rm -rf $(PREFIX)/files
	rm -rf $(CURDIR)/build
	rm -rf $(CURDIR)/src/*.egg-info
