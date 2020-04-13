# Core Java SE 9

## Overview

This directory contains exercises I did for the
*Core Java SE 9 for the Impatient* book.

## Build

Project can be build using `gradle`, using standard project layout.

## Intellij

Open this folder, and Intellij should be able to create a project
based on Gradle files. Make sure gradle wrapper files already exist,
if not, can use "gradle wrapper" command to create it. This way,
Intellij will configure project to use existing wrapper files.

### Lombok

Need to "enable annotation processing", or unittest won't run since I
am using lombok annotations.
