#! /bin/bash

SCRIPTDIR="$(realpath "$(dirname "${BASH_SOURCE[0]}")")"

# Load further config
source "$SCRIPTDIR/venv_config.sh" || exit 1

#
# Activate environment
#
source "$VENV_DIR/bin/activate" || exit 1