#!/usr/bin/env bash

set -euxo pipefail

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

#mkdir -p test/testdir/testpost
#touch test/testdir/index.md
#touch test/testdir/testpost/index.md
#touch test/testdir/testpost/post-image.jpg
#touch test/testdir/testpost/post-image.png


BASE_DIR="test"
BASE_DIR="src/content/docs"
for dir in $(find $BASE_DIR/* -type d -maxdepth 0); do
    echo $dir
    for subdir in $(find $dir/* -type d -maxdepth 0); do
        # move all jpg and png files to dir with same name
        for file in $(find $subdir -type f -name *.jpg -o -name *.png); do
            mv $file $dir/
        done
        # move all index.md files to dir with name of parent directory
        for file in $(find $subdir -maxdepth 1 -type f -name index.md); do
            mv $file $(dirname $file).md
            rmdir $subdir
        done
    done
done
