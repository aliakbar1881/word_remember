#!/bin/bash 
#===============================================================================
#
#          FILE: init.sh
# 
#         USAGE: ./init.sh 
# 
#   DESCRIPTION: 
# 		bash file to initialize project environment
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (aliakbar1881), 
#  ORGANIZATION: 
#       CREATED: 09/06/2022 10:46
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error

export PYTHONPATH=${PWD}
echo $PYTHONPATH
echo DONE
