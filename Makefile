NAME=xvalac00
DESTDIR=calc-$(VERSION)
INSFLAGS=

VERSION=1.0
LICENSE=gpl3
EMAIL=xvalac00@fit.vutbr.cz


SRC_FILES= src/gui.py src/functions.py
ICON=calc_icon.xpm

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



install: calc-$(VERSION) calc-$(VERSION).tar.gz
	cd $(DESTDIR) && dh_make -e $(EMAIL) -n  -c $(LICENSE) -f ../$<.tar.gz
	cd $(DESTDIR) && dpkg-buildpackage -rfakeroot

#TODO add an icon
# $(ICON)
# 	install $(INSFLAGS) $(word 3, $^) $(DESTDIR)/usr/share/pixmaps/
calc-$(VERSION): $(SRC_FILES) 
	mkdir -p $(DESTDIR)/usr/bin

	install $(INSFLAGS) $(word 1, $^) $(DESTDIR)/usr/bin
	install $(INSFLAGS) $(word 2, $^) $(DESTDIR)/usr/bin

calc-$(VERSION).tar.gz:
	tar -czvf $(DESTDIR).tar.gz $(DESTDIR)


clean:
	rm -rf __pycache__