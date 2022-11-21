.PHONY: nb
nb:	## Launch Jupyter Notebook for design notes
	cd book && \
		jupyter notebook

.PHONY: book
book: ## Create book and copy httml pages to docs folder
	jb build book
	cp -r book/_build/html/* docs


