#!/bin/bash

awk '$4=="PHE" {print $2}' 1HK0.pdb > PHE_atoms.xyz
