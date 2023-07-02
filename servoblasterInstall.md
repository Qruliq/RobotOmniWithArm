sudo apt-get install python-dev python-setuptools
git clone https://github.com/WiringPi/WiringPi-Python
cd WiringPi-Python
git submodule update --init
python setup.py install
cd ..
