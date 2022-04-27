NAME=xvalac00
DESTDIR=calc-1.0
INSFLAGS=

all:


pack: doc install repo
	zip ../$(NAME).zip $^ || echo "Packing failed"
 
