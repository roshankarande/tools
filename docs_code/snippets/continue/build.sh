#!/usr/bin/env bash
set -e

echo "Installing Core extension dependencies..."
pushd core
npm install
popd

echo "Installing GUI extension dependencies..."
pushd gui
npm install
npm run build
popd

echo "Installing VSCode extension dependencies..."
pushd extensions/vscode
npm install
npm run prepackage
npm run package
popd

# ==========================================================

# Install NVM
# Install npm
# Install Node


# npm run prepackage -- --target linux-x64
# npx vsce package --no-dependencies --target linux-x64
# npm run prepackage -- --target win32-x64
# npx vsce package --no-dependencies --target win32-x64

# win32-x64
# win32-arm64
# linux-x64
# linux-arm64
# linux-armhf
# alpine-x64
# darwin-x64
# darwin-arm64

# # armhf stands for "arm hard float", and is the name given to a debian port for arm processors (armv7+) that have hardware floating point support.
