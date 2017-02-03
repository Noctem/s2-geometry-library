#!/bin/sh -x
# Continuous integration script for Travis

# Add flags for openssl and Python on osx
if [ "${TRAVIS_OS_NAME}" == "osx" ]; then
	export OPENSSL_ROOT_DIR="/usr/local/opt/openssl"
	export PATH="/usr/bin:${PATH}"
fi

# Build the library and install it.
echo "## Building and installing libs2 and the Python bindings ..."
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=../install ../geometry
make -j4
make install

# Build and run the C++ tests
echo "## Building and running the C++ tests..."
make check

cd ..
export PYTHONPATH=$PWD/install/python2.7/site-packages:${PYTHONPATH}
# Run the Python tests
echo "## Running the Python tests..."
python -v -c 'import s2'
python geometry/python/test.py
