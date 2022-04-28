NAME=xvalac12
APP=giit-calc

DESTDIR=install/$(APP)-$(VERSION)
INSFLAGS= -m 0755
INSTALL_FILES=install_files
VERSION=1.0
LICENSE=gpl3
EMAIL=xvalac12@stud.fit.vutbr.cz


SRC_FILES= src/giit-calc.py src/functions.py src/calc.py
ICON=src/icon/giit-calc.xpm

.PHONY: all pack profile doc install clean release

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


##############################################

release:
	install $(INSFLAGS) install_files/debian/* install/giit-calc-$(VERSION)/debian

	cd $(DESTDIR) && dpkg-buildpackage -rfakeroot


install: calc-$(VERSION) calc-$(VERSION).tar.gz
	cd $(DESTDIR) && dh_make -e $(EMAIL) -n  -c $(LICENSE) -f ../$<.tar.gz


calc-$(VERSION): $(SRC_FILES) 
	mkdir -p $(DESTDIR)/usr/bin
	mkdir -p $(DESTDIR)/usr/share/pixmaps
	mkdir -p $(DESTDIR)/usr/share/applications

	install $(INSFLAGS) $(INSTALL_FILES)/$(APP)-$(VERSION)/giit-calc $(DESTDIR)/usr/bin
	install $(INSFLAGS) $(ICON) $(DESTDIR)/usr/share/pixmaps/
	install $(INSFLAGS) $(INSTALL_FILES)/$(APP)-$(VERSION)/giit-calc.desktop $(DESTDIR)/usr/share/applications

calc-$(VERSION).tar.gz:
	tar -czvf $(DESTDIR).tar.gz $(DESTDIR)


clean:
	rm -rf install
	rm -rf __pycache__