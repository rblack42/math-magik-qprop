.PHONY: inc-major
inc-major:	## increment major version number
	@bump2version major

.PHONY: inc-minor
inc-minor:	## increment minor version number
	@bump2version minor

.PHONY: inc-patch
inc-patch:	## increment patch version number
	@bump2version patch

.PHONY:	version
version: ## display current version number
	@cat $(PROJECT)/__init__.py
