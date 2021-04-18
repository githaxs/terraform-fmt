#!/usr/bin/env bash
tf_fmt() {
    if [[ $1 =~ .*.(tf|tfvars)$ ]]; then
        terraform fmt -no-color -list=false $1
    fi
}

task() {
    foreach_changed_file tf_fmt
}