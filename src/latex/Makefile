BASH = /usr/bin/env bash
PROJ = dokumentace

all:
	latex $(PROJ).tex
	latex $(PROJ).tex
	dvips -t a4 $(PROJ).dvi
	ps2pdf -sPAPERSIZE=a4 $(PROJ).ps

clean:
	rm -f $(PROJ).{aux,dvi,log,pdf,ps,out} xvalac12-fit.zip
