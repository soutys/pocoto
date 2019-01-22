# Package

django (code) + tests (tox + unittest + coverage + flakes) + docker (build/fig scripts)


# Testing

	$ tox


# Clean after succesful tests

	$ ./py_cleanup.sh


# Build and start container

	$ docker-compose up --build


# Test

	$ curl -v 'http://127.0.0.1:8080/?a=0,0&b=1,1'


# Look into container (as root)

	# docker ps
	# docker exec -i -t pocoto /bin/bash
