#!/bin/bash


Usage()
{
	echo "Usage: /bin/bash $0 --help"
	echo "options:"
	echo "-h, --help    Print this help"
	echo
}

PREFIX=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
INSTALL=true

VENV_DIR="${PREFIX}/venv"
VENV_REQUIREMENTS="${PREFIX}/requirements.txt"
ENV="${PREFIX}/etc/.env"


if $INSTALL; then
	#::::::::::::::::::::::::::::::::::::::::::::::::::::::::
	#                INSTALLATION ONLY
	#::::::::::::::::::::::::::::::::::::::::::::::::::::::::

	echo "Start installation"

	if [ -d "$VENV_DIR" ]; then
		echo "Directory $VENV_DIR already exists"
		Usage
		exit 1
	fi

	echo "Set up the virtual environment"
	mkdir -p ${VENV_DIR}
	python3 -m venv $VENV_DIR

	source $VENV_DIR/bin/activate

	if [ -f "${ENV}" ]; then
		echo "${ENV} exists"
	else
		echo "Create default env file ${ENV}"
		cp ${PREFIX}/etc/.env.tmpl ${ENV}
	fi
fi

echo "Install requirements"
${VENV_DIR}/bin/python3 -m pip install --upgrade pip
${VENV_DIR}/bin/python3 -m pip install -r ${VENV_REQUIREMENTS}