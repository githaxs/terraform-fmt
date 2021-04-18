test:
	@GITHUB_TOKEN=$(shell git config --get githaxs.token) python3 -m pytest src/test_task.py
