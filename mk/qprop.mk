QPROPURL = https://web.mit.edu/drela/Public/web/qprop/
QPROPTAR = qprop1.22.tar.gz

FC = gfortran

FDIR = master/Qprop/src
FSRCS = $(FDIR)/qprop.f \
		$(FDIR)/gvcalc.f \
		$(FDIR)/cdfun.f \
		$(FDIR)/tqcalc.f \
		$(FDIR)/motor.f \
		$(FDIR)/spline.f \
		$(FDIR)/io.f \
		$(FDIR)/qcget.f
FOBJS = $(FSRCS:.f=.o)

# qprop test code ------------------------------------
TSRCS = $(FDIR)/test1.f
TOBJS = $(TSRCS:.f=.o)


# fetch copy of master QProp codes from MIT ==========
.PHONY: fetch
fetch: master/$(QPROPTAR)	## download master qprop from MIT

master/$(QPROPTAR):
	curl $(QPROPURL)/$(QPROPTAR) -o $@
	echo "installed Qprop"

.PHONY:	unpack
unpack:	 master/$(QPROPTAR)		## unpack qprop
	cd master && \
		tar zxvf $(QPROPTAR)

# compile qprop --------------------------------------
qprop:	$(FOBJS)	## compile qprop program
	$(FC) -o $@ $^
	mv qprop .venv/bin

%.o:    %.f
	$(FC) -fdollar-ok -c $< -o $@

test1:	 $(FDIR)/test1.o $(FDIR)/gvcalc.o
	$(FC) -o $@ $^ 
