.PHONY: format
format:
	black python_tips_and_tricks/

.PHONY: lint
lint:
	pylint python_tips_and_tricks/
