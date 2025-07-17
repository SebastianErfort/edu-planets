test_program:
	./test.sh

test_pytest:
	pytest --cov-report "xml:coverage.xml" --cov=.
