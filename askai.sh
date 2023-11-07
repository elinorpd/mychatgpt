#!/bin/bash

# The path to your Python script
python_script_path="./ask-ai.py"

# Function to display usage
usage() {
    echo "Usage: $0 [--model MODEL] [--q QUERY] [--c chat mode]"
    exit 1
}

# Initialize variables for command-line arguments
QUERY=""
CHAT_MODE=""
MODEL=""

# Parse command-line arguments
while [ $# -gt 0 ]; do
    case "$1" in
        --q) QUERY="$2"; shift ;;
        --c) CHAT_MODE="--c";;
        --model) MODEL="--model $2"; shift ;;
        --help) usage ;;
        *) echo "Unknown argument: $1"; usage ;;
    esac
    shift
done

# Construct the final command with arguments to run the Python script
cmd="python3 \"$python_script_path\""

# Append arguments to the command if they are set
if [ ! -z "$MODEL" ]; then
    cmd="$cmd $MODEL"
fi
if [ ! -z "$QUERY" ]; then
    cmd="$cmd --q \"$QUERY\""
fi
if [ ! -z "$CHAT_MODE" ]; then
    cmd="$cmd $CHAT_MODE"
fi

# Run the Python script with the constructed command
eval $cmd

# Exit the script
exit 0
