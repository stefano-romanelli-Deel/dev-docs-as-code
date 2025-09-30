#!/usr/bin/env bash
set -e

VALE_VERSION="3.8.0"
OS=$(uname -s | tr '[:upper:]' '[:lower:]')
ARCH=$(uname -m)

if [ "$ARCH" = "x86_64" ]; then
  ARCH="64-bit"
elif [ "$ARCH" = "arm64" ] || [ "$ARCH" = "aarch64" ]; then
  ARCH="arm64"
fi

# Map uname output to Vale release names
if [ "$OS" = "darwin" ]; then
  OS="macOS"
elif [ "$OS" = "linux" ]; then
  OS="Linux"
else
  echo "Unsupported OS: $OS"
  exit 1
fi

URL="https://github.com/errata-ai/vale/releases/download/v${VALE_VERSION}/vale_${VALE_VERSION}_${OS}_${ARCH}.tar.gz"

mkdir -p tools/vale
curl -sSL "$URL" | tar -xz -C tools/vale
