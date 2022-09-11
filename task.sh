#!/usr/bin/env bash
set -e

run_task() {
    terraform --version
    FILES=$(echo "$1" | grep -E "\.tf$")

    if [ "$FILES" = "" ]; then
        exit 0
    fi
    
    echo "$FILES" | xargs -I {} terraform fmt -no-color -list=false {}

    git diff --quiet
    status=$?
    if [ $status -ne 0 ]; then
        echo '```diff'
        git diff
        echo '```'
        exit 1
    else
        exit 0
    fi
}