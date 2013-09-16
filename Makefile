PY=python
PELICAN=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(HOME)/Dropbox/bhrutledge.com/content
LOCALCONF=$(BASEDIR)/pelicanconf.py
LOCALDIR=$(HOME)/Sites/bhrutledge
PUBLISHCONF=$(BASEDIR)/publishconf.py
PUBLISHDIR=/home/rutt/webapps/pelican
TMPDIR=$(HOME)/tmp/bhrutledge

SSH_HOST=debugged.org
SSH_PORT=22
SSH_USER=rutt

help:
	@echo 'Makefile for a pelican Web site                                        '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make html                        (re)generate the web site          '
	@echo '   make clean                       remove the generated files         '
	@echo '   make regenerate                  regenerate files upon modification '
	@echo '   make publish                     generate using production settings '
	@echo '   make upload                      upload the web site via rsync+ssh  '
	@echo '                                                                       '

clean:
	[ ! -d $(LOCALDIR) ] || find $(LOCALDIR) -mindepth 1 -delete

html: clean
	$(PELICAN) $(INPUTDIR) -o $(LOCALDIR) -s $(LOCALCONF) $(PELICANOPTS)

regenerate: clean
	$(PELICAN) -r $(INPUTDIR) -o $(LOCALDIR) -s $(LOCALCONF) $(PELICANOPTS)

publish:
	[ ! -d $(PUBLISHDIR) ] || find $(PUBLISHDIR) -mindepth 1 -delete
	$(PELICAN) $(INPUTDIR) -o $(PUBLISHDIR) -s $(PUBLISHCONF) $(PELICANOPTS)
	chmod -R a+rX $(PUBLISHDIR)

upload:
	[ ! -d $(TMPDIR) ] || find $(TMPDIR) -mindepth 1 -delete
	$(PELICAN) $(INPUTDIR) -o $(TMPDIR) -s $(PUBLISHCONF) $(PELICANOPTS)
	rsync -e "ssh -p $(SSH_PORT)" -P -rvzp --delete $(TMPDIR)/ $(SSH_USER)@$(SSH_HOST):$(PUBLISHDIR) --cvs-exclude

.PHONY: help clean html regenerate publish upload
