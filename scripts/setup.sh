#!/bin/bash

PROJECT=$1

REPO_ROOT=`cd $(dirname $0)/.. && pwd`

DATA_ROOT=$REPO_ROOT/data/$PROJECT
OUTPUT_ROOT=$REPO_ROOT/outputs/$PROJECT
SOURCE_ROOT=$REPO_ROOT/src/$PROJECT

if [ ! -e $DATA_ROOT ]; then
  echo "Create data directory in $PROEJCT_ROOT/data"
  mkdir -p $DATA_ROOT
fi
if [ ! -e $OUTPUT_ROOT ]; then
  echo "Create outputs directory in $PROEJCT_ROOT/outputs"
  mkdir -p $OUTPUT_ROOT
fi
if [ ! -e $SOURCE_ROOT]; then
  echo "Create outputs directory in $PROEJCT_ROOT/src"
  mkdir -p $SOURCE_ROOT

  cp $REPO_ROOT/core/download.py $SOURCE_ROOT
  sed -i -e "s/sample/$PROJECT/g" $SOURCE_ROOT/download.py

  # TODO: $PROJECT ごとに.envを自動生成する
fi
