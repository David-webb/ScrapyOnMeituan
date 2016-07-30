#!/bin/bash
loginpath = $1
uid = $2
lpwd = $3
if [  loginpath == "" ]
then   
  loginpath = '/home/login.py'
fi
if [ uid == "" ]
  then
  uid = "9120111051"
fi
if [ lpwd == "" ]
then
lpwd = "300059"
fi
python loginpath uid lpwd