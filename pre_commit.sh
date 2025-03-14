#!/bin/bash

set -e  # Exit on error
set -o pipefail  # Fail on first error in a pipeline

echo -e "\n\033[1mRunning Static Code Analysis\033[0m\n"

# Step 1: Lock File Check
echo "✅ Checking lock file..."
uv lock --locked || { echo "❌ Lock file check failed"; exit 1; }

# Step 2: Linting with Ruff
echo "✅ Running Ruff linting..."
uvx ruff check . || { echo "❌ Linting failed"; exit 1; }

# Step 3: Formatting with Ruff
echo "✅ Running Ruff formatting..."
uvx ruff format . || { echo "❌ Formatting failed"; exit 1; }

# Step 4: Type Checking with mypy
echo "✅ Running mypy type checks..."
uv run mypy . || { echo "❌ Type checking failed"; exit 1; }

echo "✅ Static Code Analysis completed successfully!"

