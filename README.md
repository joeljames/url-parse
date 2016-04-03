The application is setup to run locally with a docker container.

## Set up Docker Environment (Mac)
1. Install [Dinghy](https://github.com/codekitchen/dinghy)

2. Install [docker toolbox](https://www.docker.com/products/docker-toolbox)

3. Install [Virtual Box](https://www.virtualbox.org/wiki/Downloads)

4. Creat the docker-machine VM

    ``` bash
    $ dinghy create
    ```

5. Start the Docker VM and services

    ``` bash
    $ dinghy up
    ```

## Getting Started

1. Setup environment

    ``` bash
    $ make copy_env
    ```

2. Build the image:

    ``` bash
    $ docker-compose build
    ```

3. Start the server:

    ``` bash
    $ docker-compose up
    ```

4. Check the server is up and running by hitting the url `http://url-parse.docker/`.

## Running Tests

1. Install flake8

    ``` bash
    $ docker-compose run web make test
    ```

## Running Lints

1. Install flake8

    ``` bash
    $ sudo pip3 install flake8
    ```

2. Run Lint

    ``` bash
    $ make lint
    ```
