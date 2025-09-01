#!/usr/bin/env sh

set -e

LANGUAGES=$1
LOCALES_DIR=$2
DOMAIN=$3

echo "Updating and compiling Babel translations (.po → .mo)..."
for lang in $LANGUAGES; do \
  po_dir="$LOCALES_DIR/$$lang/LC_MESSAGES"; \
  mkdir -p $$po_dir; \
  po_file="$$po_dir/messages.po"; \
  pot_file="$LOCALES_DIR/$DOMAIN.pot"; \
  if [ -f $$po_file ]; then \
    hatch run pybabel update -i $$pot_file -d $$po_dir -l $$lang; \
  else \
    hatch run pybabel init -i $$pot_file -d $$po_dir -l $$lang; \
  fi; \
  hatch run pybabel compile -d $$po_dir -l $$lang; \
done
