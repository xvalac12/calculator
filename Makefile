NAME=xvalac00
DESTDIR=calc-1.0
INSFLAGS=

all:


pack: doc install repo
	zip ../$(NAME).zip $^ || echo "Packing failed"


profile:
	./profiling/profile.sh > ./profiling/prof_out || echo "Profiling failed"

test:
	python3 ./src/tests.py

doc:

install:
	echo "Install target"
	mkdir -p $(DESTDIR)/usr/bin
	install $(INSFLAGS) src/gui.py $(DESTDIR)/usr/bin
	install $(INSFLAGS) src/functions.py $(DESTDIR)/usr/bin

repo:
	(git clone . $@ || (rm -rf $@  && git clone . $@)) || echo "Couldn't make folder repo"

clean:
	rm -rf __pycache__