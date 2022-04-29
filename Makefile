NAME=xbezak02_xbukas00_xstola03_xvalac12
APP=giit-calc

DESTDIR=giit-calc/$(APP)-$(VERSION)
INSFLAGS= -m 0755

INSTALL_FILES=install_files
VERSION=1.0
LICENSE=gpl3
EMAIL=xvalac12@stud.fit.vutbr.cz
ICON=src/icon/giit-calc.xpm

SRC_FILES= src/giit-calc.py src/functions.py src/calc.py


BASH = /bin/env bash
PROJ = dokumentace


.PHONY: all pack profile doc install clean release test rm_app

all: install doc


pack: doc repo
	mkdir doc
	cp -r src/html doc/html

	mkdir install
	cp -r install_files install
	cp Makefile install

	mkdir $(NAME)
	mv doc repo install $(NAME) 
	zip -r ../$(NAME).zip $(NAME) || echo "Packing failed"
	rm -rf $(NAME)


profile:
	./profiling/profile.sh > ./profiling/prof_out || echo "Profiling failed"

test:
	python3 ./src/tests.py

repo:
	(git clone . $@ || (rm -rf $@  && git clone . $@)) || echo "Couldn't make folder repo"

doc:
	cd src && doxygen Doxyfile

	latex ./src/latex/$(PROJ).tex

	dvips -t a4 $(PROJ).dvi
	ps2pdf -sPAPERSIZE-a4 $(PROJ).ps


##############################################

release:
	cp $(INSTALL_FILES)/debian/* $(APP)-$(VERSION)/debian
	cd $(APP)-$(VERSION) && dpkg-buildpackage -rfakeroot -uc -b

install: $(APP)-$(VERSION) $(APP)-$(VERSION).tar.gz
	cd $< && dh_make -e $(EMAIL) -n -s -c  $(LICENSE) -p "$<" -f ../$<.tar.gz

$(APP)-$(VERSION): $(SRC_FILES)
	mkdir -p $@/install
	cp $^ $@
	cp $(INSTALL_FILES)/Makefile $@
	cp $(INSTALL_FILES)/setup.py $@
	cp -r $(INSTALL_FILES)/app/* $@/install
	cp $(SRC_FILES) $@/install

%.tar.gz: %
	tar -czvf $@ $<

clean:
	rm -rf __pycache__
	rm -rf $(PROJ).{aux,dvi,log,pdf,ps,out} html xvalac12-fit.zip

rm_app:
	rm -rf $(APP)-$(VERSION)
	rm $(APP)-$(VERSION).tar.gz || rm $(APP)-$(VERSION).tgz 
