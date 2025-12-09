#!/bin/bash

# Load SESSION_ID from .env
set -a && source .env && set +a

year=2025
day=$((10#$1))
dir="./$(printf "%02d" $day)"

mkdir -p "$dir"
curl -s -o "$dir/input.txt" -H "Cookie: session=$SESSION_ID" "https://adventofcode.com/$year/day/$day/input"
