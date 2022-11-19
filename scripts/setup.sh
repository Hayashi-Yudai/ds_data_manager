#!/bin/bash

PROJECT=$1

REPO_ROOT=`cd $(dirname $0)/.. && pwd`

DATA_ROOT=$REPO_ROOT/data/$PROJECT
OUTPUT_ROOT=$REPO_ROOT/outputs/$PROJECT
SOURCE_ROOT=$REPO_ROOT/src/$PROJECT

if [ ! -e $REPO_ROOT/core/config.py ]; then
  echo 'REPO_ROOT = "'$REPO_ROOT'"' > $REPO_ROOT/core/config.py
  echo 'DATA_ROOT = f"{REPO_ROOT}/data"' >> $REPO_ROOT/core/config.py
  echo 'SOURCE_ROOT = f"{REPO_ROOT}/src"' >> $REPO_ROOT/core/config.py
  echo 'OUTPUT_ROOT = f"{REPO_ROOT}/outputs"' >> $REPO_ROOT/core/config.py

  echo "Generate config.py."
else
  REPO_ROOT_SETTING=`cat $REPO_ROOT/core/config.py \
    | grep -E 'REPO_ROOT =' \
    | grep -o '".*"' \
    | grep -o '[^"]*'
  `

  if [ $REPO_ROOT_SETTING != $REPO_ROOT ]; then
    echo 'REPO_ROOT = "'$REPO_ROOT'"' > $REPO_ROOT/core/config.py
    echo 'DATA_ROOT = f"{REPO_ROOT}/data"' >> $REPO_ROOT/core/config.py
    echo 'SOURCE_ROOT = f"{REPO_ROOT}/src"' >> $REPO_ROOT/core/config.py
    echo 'OUTPUT_ROOT = f"{REPO_ROOT}/outputs"' >> $REPO_ROOT/core/config.py

    echo "Re-generate config.py."
  fi
fi

if [ ! -e $DATA_ROOT ]; then
  echo "Create data directory in $PROEJCT_ROOT/data"
  mkdir -p $DATA_ROOT
fi
if [ ! -e $OUTPUT_ROOT ]; then
  echo "Create outputs directory in $PROEJCT_ROOT/outputs"
  mkdir -p $OUTPUT_ROOT
fi
if [ ! -e $SOURCE_ROOT ]; then
  echo "Create source directory in $PROEJCT_ROOT/src"
  mkdir -p $SOURCE_ROOT

  cp $REPO_ROOT/core/resources.py $SOURCE_ROOT
  sed -i -e "s/fawef230rfaw/$PROJECT/g" $SOURCE_ROOT/resources.py
  rm $SOURCE_ROOT/resources.py-e
fi
