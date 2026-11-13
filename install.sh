#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_BASE="${1:-$HOME/.gemini/config/skills}"
DEST_DIR="${TARGET_BASE}/destructive-action-guard"

mkdir -p "$DEST_DIR"
ln -sf "${SCRIPT_DIR}/SKILL.md" "${DEST_DIR}/SKILL.md"
echo "Installed destructive-action-guard -> ${DEST_DIR}/SKILL.md"
