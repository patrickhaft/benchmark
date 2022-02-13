#! /bin/bash

source venv_config.sh

echo "Setting up virtual environment in '$VENV_DIR'"
python3 -m venv "$VENV_DIR" || exit 1

echo "Activating environment"
source "$VENV_DIR/bin/activate" || exit 1

# Update pip3
pip3 install -U pip


PIP_PACKAGES="matplotlib"
echo "Installing PIP packages: $PIP_PACKAGES"
pip3 install -U $PIP_PACKAGES  || exit 1





echo "Setting up developer mode"
python3 ./setup.py develop || exit 1


# Setting up 'bin' folder
echo ""
echo "chmod"
echo ""
echo "*******************************************************"
chmod -v 755 "$SCRIPTDIR/bin/"* || exit 1
chmod -v 755 "$SCRIPTDIR/venv_cleanup.sh" || exit 1
echo "*******************************************************"

echo ""
echo "Setup finished"
echo ""
