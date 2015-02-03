SERVER_URL = https://blogs-dev.allizom.org

# Hackety-hack around OSX system python bustage.
# The need for this should go away with a future osx/xcode update.
ARCHFLAGS = -Wno-error=unused-command-line-argument-hard-error-in-future
INSTALL = ARCHFLAGS=$(ARCHFLAGS) ./bin/pip install

.PHONY: build small medium

# Build virtualenv, to ensure we have all the dependencies.
build:
	virtualenv -p /usr/bin/python .
	$(INSTALL) -r requirements.txt
	rm -rf ./local  # ubuntu, why you create this useless folder?

# Clean all the things installed by `make build`.
clean:
	rm -rf ./include ./bin ./lib ./lib64 *.pyc

# Run a single test from the local machine, for sanity-checking.
small:
	./bin/loads-runner --config=./config/small.ini --server-url=$(SERVER_URL) test_wp.TestWP.test_root_blog

# Run a medium-sized test of 20 concurrent users.
medium:
	./bin/loads-runner --config=./config/medium.ini --server-url=$(SERVER_URL) test_wp.TestWP.test_root_blog

# Run a much bigger test, by submitting to broker in AWS.
large:
	./bin/loads-runner --config=./config/large.ini --user-id=$(USER) --server-url=$(SERVER_URL) test_wp.TestWP.test_root_blog

# Purge any currently-running loadtest runs.
purge:
	./bin/loads-runner --config=./config/large.ini --purge-broker
