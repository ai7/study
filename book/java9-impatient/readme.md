# Core Java SE 9

## Overview

This directory contains exercises I did for the
*Core Java SE 9 for the Impatient* book.

## Build

Project can be build using `gradle`, using standard project layout.
- src/main/java
- src/test/java

Each chapter and exercise are in unique packages. This way, class
structure for each exercise are easily visible in IDE.

- ch01/ex01/Answer.java

In answer, static methods are using default visibility, so they are
easily tested.

## Intellij

Open this folder, and Intellij should be able to create a project
based on Gradle files. Make sure gradle wrapper files already exist,
if not, can use "gradle wrapper" command to create it. This way,
Intellij will configure project to use existing wrapper files.

### Lombok

Need to "enable annotation processing", or unittest won't run since I
am using lombok annotations.
