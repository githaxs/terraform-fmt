#!/usr/bin/env bash
set -e

run() {
    if [[ $1 =~ .*.tf$ ]]; then
        terraform fmt -no-color -list=false $1
    fi
}

task() {
    echo "Running Terraform Format"

    foreach_changed_file run
}
