.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of"

	@echo "  copy_env        Copies the 'env.example.ini' file to 'env.ini'."
	@echo "  link_hooks      Installs all git hooks stored in 'bin/hooks'."
	@echo "  lint            Lint all project files."
	@echo "  test            Runs unit tests and coverage."

.PHONY: copy_env
copy_env:
	@cp env.example.ini env.ini

.PHONY: link_hooks
link_hooks:
	@bin/link_hooks

.PHONY: lint
lint:
	@bin/lint

.PHONY: test
test:
	@bin/test
