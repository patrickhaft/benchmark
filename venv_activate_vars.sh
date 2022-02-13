#! /bin/bash

if [ "`basename -- "$SHELL"`" != "bash" ]; then
        echo
        echo "These scripts are only compatible to the bash shell"
        echo
        return
fi



#######################################################################
# Setup important directory environment variables #####################
#######################################################################

SCRIPTDIR="$(realpath "$(dirname "${BASH_SOURCE[0]}")")"
export BENCHMARK_ROOT="$SCRIPTDIR"



MULE_BACKDIR="$PWD"

cd "$SCRIPTDIR/bin"
BINDIR="$(pwd)"
cd "$MULE_BACKDIR"

echo "Setting up path '$BINDIR'"

export PATH="$PATH:$BINDIR"


export BENCHMARK_PATH_ORIG="$PATH"

export BENCHMARK_PATH="$PATH"

source "$SCRIPTDIR/venv_activate.sh"
