NAME=xvalac12
DESTDIR=install/giit-calc-$(VERSION)
INSFLAGS=

VERSION=1.0
LICENSE=gpl3
EMAIL=xvalac12@stud.fit.vutbr.cz


SRC_FILES= src/gui.py src/functions.py src/calc.py
ICON=src/icon/icon.xpm

.PHONY: all pack profile doc install clean

all:


pack: doc install repo
	zip ../$(NAME).zip $^ || echo "Packing failed"


profile:
	./profiling/profile.sh > ./profiling/prof_out || echo "Profiling failed"

test:
	python3 ./src/tests.py

repo:
	(git clone . $@ || (rm -rf $@  && git clone . $@)) || echo "Couldn't make folder repo"

doc:

release:
	install $(INSFLAGS) install_files/debian/* install/giit-calc-$(VERSION)/debian
	install $(INSFLAGS) install_files/giit-calc-$(VERSION)/install/giit-calc install/giit-calc-$(VERSION)/usr/bin
# install $(INSFLAGS) install_files/giit-calc-$(VERSION)/install/giit-calc.desktop install/gitt-calc-$(VERSION)/usr/share/applications

	cd $(DESTDIR) && dpkg-buildpackage -rfakeroot


install: calc-$(VERSION) calc-$(VERSION).tar.gz
	cd $(DESTDIR) && dh_make -e $(EMAIL) -n  -c $(LICENSE) -f ../$<.tar.gz


calc-$(VERSION): $(SRC_FILES) 
	mkdir -p $(DESTDIR)/usr/bin
	mkdir -p $(DESTDIR)/usr/share/pixmaps
	mkdir -p $(DESTDIR)/usr/opt/giit-calc
	mkdir -p $(DESTDIR)/usr/share/applications

	install $(INSFLAGS) $(word 1, $^) $(DESTDIR)/usr/opt/giit-calc
	install $(INSFLAGS) $(word 2, $^) $(DESTDIR)/usr/opt/giit-calc
	install $(INSFLAGS) $(word 3, $^) $(DESTDIR)/usr/opt/giit-calc

	install $(INSFLAGS) $(ICON) $(DESTDIR)/usr/share/pixmaps/

calc-$(VERSION).tar.gz:
	tar -czvf $(DESTDIR).tar.gz $(DESTDIR)


clean:
	rm -rf __pycache__