DESTDIR = $(HOME)
SHELL = /bin/bash
INSFLAGS = -m 0755

APP=giit-calc
SRC=../src/$(APP).py

.PHONY: all clean install

all: dist/$(APP)/$(APP)

dist/$(APP)/$(APP): $(SRC)
	pyi-makespec $^
	pyinstaller $(APP).spec

clean:
	rm -rf ./build
	rm -rf ./dist
	rm -f $(APP).spec

install: dist/$(APP)/$(APP)
	mkdir -p $(DESTDIR)/opt
	cd dist; find $(APP) -type f -exec install -D $(INSFLAGS) "{}" "$(DESTDIR)/opt/{}" \;
