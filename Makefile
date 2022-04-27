NAME=xvalac00
DESTDIR=calc-1.0
INSFLAGS=

SRC_FILES= src/gui.py src/functions.py
ICON=calc_icon.xpm

all:


pack: doc install repo
	zip ../$(NAME).zip $^ || echo "Packing failed"


profile:
	./profiling/profile.sh > ./profiling/prof_out || echo "Profiling failed"

test:
	python3 ./src/tests.py

doc:

install: $(SRC_FILES) $(ICON)
	echo "Install target"
	mkdir -p $(DESTDIR)/usr/bin

	install $(INSFLAGS) $(word 1, $^) $(DESTDIR)/usr/bin
	install $(INSFLAGS) $(word 2, $^) $(DESTDIR)/usr/bin
	install $(INSFLAGS) $(word 3, $^) $(DESTDIR)/usr/share/pixmaps/

	tar -czvf $(DESTDIR).tar.gz $(DESTDIR)

repo:
	(git clone . $@ || (rm -rf $@  && git clone . $@)) || echo "Couldn't make folder repo"

clean:
	rm -rf __pycache__