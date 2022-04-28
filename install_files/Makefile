DESTDIR = $(HOME)
SHELL = /bin/bash
INSFLAGS = -m 0755

SRC=../src/giit-calc.py
APP=${giit-calc}

.PHONY: all clean install

all: dist/$(APP)/$(APP)

dist/$(APP)/$(APP): $(SRC)
	pyi-makespec $^
	pyinstaller $^


install: dist/$(APP)/$(APP)
	mkdir -p $(DESTDIR)/opt
	cd dist; find $(APP) -type f -exec install -D $(INSFLAGS) "{}" "$(DESTDIR)/opt/{}" \;

clean:
	rm -rf ./build
	rm -rf ./dist
	rm -f giit-calc.spec