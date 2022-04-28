NAME=xvalac12
APP=giit-calc

DESTDIR=giit-calc/$(APP)-$(VERSION)
INSFLAGS= -m 0755

INSTALL_FILES=install_files
VERSION=1.0
LICENSE=gpl3
EMAIL=xvalac12@stud.fit.vutbr.cz
ICON=src/icon/giit-calc.xpm

SRC_FILES= src/giit-calc.py src/functions.py src/calc.py

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
	cp $(INSTALL_FILES)/debian/* $(APP)-$(VERSION)/debian
	cd $(APP)-$(VERSION) && dpkg-buildpackage -rfakeroot -uc -b


install: $(APP)-$(VERSION) $(APP)-$(VERSION).tar.gz
	cd $< && dh_make -e $(EMAIL) -n  -c $(LICENSE) -y -p "$<" -f ../$<.tar.gz
	
$(APP)-$(VERSION): $(SRC_FILES)
	mkdir -p $@/install
	cp $^ $@
	cp $(INSTALL_FILES)/Makefile $@
	cp -r $(INSTALL_FILES)/app/* $@/install


%.tar.gz: %
	tar -czvf $@ $<

clean:
	rm -rf __pycache__
	rm -rf $(APP)-$(VERSION)
	rm $(APP)-$(VERSION).tar.gz || rm $(APP)-$(VERSION).tgz 
