# Package

django (code) + tests (tox + unittest + coverage + flakes) + docker (build/fig scripts)


# Testing

	$ tox


# Clean after succesful tests

	$ ./py_cleanup.sh


# Build image container (as root)

	# fig build


# Start container (as root)

	# fig up


# Look into container (as root)

	# docker ps
	# docker exec -i -t <container_ID> /bin/bash

