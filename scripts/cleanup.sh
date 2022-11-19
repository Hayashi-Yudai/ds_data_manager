#!/bin/bash

PROJECT=$1

REPO_ROOT=`cd $(dirname $0)/.. && pwd`

echo $REPO_ROOT

DATA_ROOT=$REPO_ROOT/data/$PROJECT
OUTPUT_ROOT=$REPO_ROOT/outputs/$PROJECT
SOURCE_ROOT=$REPO_ROOT/src/$PROJECT

if [ -e $DATA_ROOT ]; then
  echo "Delete data directory in $PROEJCT_ROOT/data"
  rm -rf $DATA_ROOT
fi
if [ -e $OUTPUT_ROOT ]; then
  echo "Delete outputs directory in $PROEJCT_ROOT/outputs"
  rm -rf $OUTPUT_ROOT
fi
if [ -e $SOURCE_ROOT ]; then
  echo "Delete source directory in $PROEJCT_ROOT/src"
  rm -ri $SOURCE_ROOT
fi
