PY=python
PELICAN=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(HOME)/Dropbox/bhrutledge.com/content
OUTPUTDIR=$(HOME)/Sites/bhrutledge
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHDIR=$(HOME)/tmp/bhrutledge
PUBLISHCONF=$(BASEDIR)/publishconf.py

SSH_HOST=debugged.org
SSH_PORT=22
SSH_USER=rutt
SSH_TARGET_DIR=/home/rutt/webapps/pelican

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


html: clean $(OUTPUTDIR)/index.html

$(OUTPUTDIR)/%.html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || find $(OUTPUTDIR) -mindepth 1 -delete

regenerate: clean
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

publish:
	$(PELICAN) $(INPUTDIR) -o $(PUBLISHDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

upload: publish
	rsync -e "ssh -p $(SSH_PORT)" -P -rvzp --delete $(PUBLISHDIR)/ $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR) --cvs-exclude

.PHONY: html help clean regenerate publish upload
