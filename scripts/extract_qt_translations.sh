#!/usr/bin/env bash

set -e

LANGUAGES=$1
TRANSLATIONS_DIR=$2
GUI_DIR=$3

echo "Extracting Qt translations (.ts)..."
for lang in $LANGUAGES; do
  ts_file="$TRANSLATIONS_DIR/$lang.ts"
  if [ ! -f "$ts_file" ]; then
    echo '<?xml version="1.0" encoding="utf-8"?><!DOCTYPE TS><TS version="2.1" language="'"$lang"'"></TS>' > "$ts_file"
  fi
  hatch run pyside6-lupdate $(find "$GUI_DIR" -name '*.py') -ts "$ts_file"
done