#!/bin/sh
ls -l
echo Running on $1

tar xzf  tcl8.4.11.tar.gz
ls -l tcl8.4.11

mv tcl8.4.11/library library
mkdir ns-2.29
mv ns ns-2.29/
ls -l
pwd
cd ns-2.29
./ns ../NetworkPerformancetry.tcl


hostname

