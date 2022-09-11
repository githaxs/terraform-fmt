#!/usr/bin/env bats
source ./task.sh

@test "githaxs task" {
  #git clone --branch demo git@github.com:githaxs/demo.git /tmp/test
  dir=$(mktemp -d)
  git clone --branch GabeL7r-patch-9 git@github.com:githaxs/test.git $dir
  cd $dir
  FILES=$(git diff --name-only 35ca47667b HEAD)
  run run_task "$FILES"

  rm -rf /tmp/test
  echo "$status"
  echo "$output"
  [ "$status" -eq 1 ]
}

@test "returns success if no files changed" {
  dir=$(mktemp -d)
  cd $dir
  run run_task ""

  echo "$status"
  echo "$output"
  [ "$status" -eq 0 ]
}