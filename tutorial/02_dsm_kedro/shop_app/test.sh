#!/bin/bash
while getopts i:n: flag
do
    case "${flag}" in
        n) app_name=${OPTARG};;
        i) app_index=${OPTARG};;
    esac
done
echo "app_name: $app_name";
echo "app_index: $app_index";