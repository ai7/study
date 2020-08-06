# Sample Gradle Project

<!-- TOC depthFrom:2 -->

- [1. Overview](#1-overview)
- [2. Create Project](#2-create-project)
    - [2.1. gradle init](#21-gradle-init)
    - [2.2. gitignore](#22-gitignore)
- [3. Add Dependencies](#3-add-dependencies)
    - [3.1. lombok](#31-lombok)
        - [3.1.1. lombok.config](#311-lombokconfig)
    - [3.2. guice](#32-guice)
    - [3.3. jacoco](#33-jacoco)
    - [3.4. spotbugs](#34-spotbugs)
- [4. Run Tasks](#4-run-tasks)
    - [4.1. tasks](#41-tasks)
    - [4.2. checks](#42-checks)
- [5. IntelliJ](#5-intellij)
- [6. Conclusion](#6-conclusion)

<!-- /TOC -->

## 1. Overview

A sample Java Gradle project with essential dependencies for
development.

- lombok: annotations that saves you from writing
  getters/setters/constructors/etc.
- guice: dependency injection framework.
- jacoco: generate code coverage reports.
- spotbugs: static code analysis to find bugs.

Steps for creating this project is outlined below.

## 2. Create Project

### 2.1. gradle init

Run `gradle init` to create an empty project.

```console
$ gradle init

Select type of project to generate:
  1: basic
  2: application
  3: library
  4: Gradle plugin
Enter selection (default: basic) [1..4] 2

Select implementation language:
  1: C++
  2: Groovy
  3: Java
  4: Kotlin
  5: Swift
Enter selection (default: Java) [1..5]

Select build script DSL:
  1: Groovy
  2: Kotlin
Enter selection (default: Groovy) [1..2]

Select test framework:
  1: JUnit 4
  2: TestNG
  3: Spock
  4: JUnit Jupiter
Enter selection (default: JUnit 4) [1..4] 4

Project name (default: java-gradle-sample):

Source package (default: java.gradle.sample): com.sample.gradle

> Task :init
Get more help with your project: https://docs.gradle.org/6.5.1/userguide/tutorial_java_projects.html

BUILD SUCCESSFUL in 55s
2 actionable tasks: 2 executed
```

### 2.2. gitignore

Add the following to the `.gitignore` file Gradle creates:

```
# ignore gradle wrapper files
# https://stackoverflow.com/questions/20348451/why-should-the-gradle-wrapper-be-committed-to-vcs
gradlew
gradlew.bat
gradle

# intellij files
.idea
out
```

## 3. Add Dependencies

Add each relevant dependencies by modifying the `build.gradle` file to
include the entries in the relevant section.

Check each link for most up-to-date version to use, and update the
block accordingly.

### 3.1. lombok

```java
plugins {
    // https://plugins.gradle.org/plugin/io.freefair.lombok
    id "io.freefair.lombok" version "5.1.0"
}

// enable this after the lombok.config file has been generated,
// this prevents your changes from being clobbered.
// generateLombokConfig.enabled = false
```

#### 3.1.1. lombok.config

```
# This file is generated by the 'io.freefair.lombok' Gradle plugin
config.stopBubbling = true

# copy annotation on fields to constructor parameter
lombok.copyableAnnotations += javax.inject.Named
```

### 3.2. guice

```java
dependencies {
    // https://mvnrepository.com/artifact/com.google.inject/guice
    implementation group: 'com.google.inject', name: 'guice', version: '4.2.3'
}
```

Note:
- This is the `dependencies` block, not `plugins`.
- It is `implementation`, not `compile` (which is a warning on Gradle 6.x).

### 3.3. jacoco

```java
plugins {
    // https://docs.gradle.org/current/userguide/jacoco_plugin.html
    id 'jacoco'
}

test {
    finalizedBy jacocoTestReport  // report is always generated after tests run
}

jacocoTestReport {
    dependsOn test  // tests are required to run before generating the report
}
```

### 3.4. spotbugs

```java
plugins {
    // https://plugins.gradle.org/plugin/com.github.spotbugs
    id "com.github.spotbugs" version "4.4.4"
}

// Example to configure HTML report
spotbugsMain {
    reports {
        html {
            enabled = true
            destination = file("$buildDir/reports/spotbugs/main/spotbugs.html")
            stylesheet = 'fancy-hist.xsl'
        }
    }
}
```

## 4. Run Tasks

The project is now ready. You can run various Gradle tasks.

```console
$ gradle

> Task :help

Welcome to Gradle 6.5.1.

To run a build, run gradle <task> ...

To see a list of available tasks, run gradle tasks

To see a list of command-line options, run gradle --help

To see more detail about a task, run gradle help --task <task>

For troubleshooting, visit https://help.gradle.org
```

### 4.1. tasks

Available tasks can be shown with the `tasks` target:

```console
$ gradle tasks

> Task :tasks

------------------------------------------------------------
Tasks runnable from root project
------------------------------------------------------------

Application tasks
-----------------
run - Runs this project as a JVM application

Build tasks                                                                                                                                                           [0/3707]
-----------
assemble - Assembles the outputs of this project.
build - Assembles and tests this project.
buildDependents - Assembles and tests this project and all projects that depend on it.
buildNeeded - Assembles and tests this project and all projects it depends on.
classes - Assembles main classes.
clean - Deletes the build directory.
jar - Assembles a jar archive containing the main classes.
testClasses - Assembles test classes.

Build Setup tasks
-----------------
init - Initializes a new Gradle build.
wrapper - Generates Gradle wrapper files.

Distribution tasks
------------------
assembleDist - Assembles the main distributions
distTar - Bundles the project as a distribution.
distZip - Bundles the project as a distribution.
installDist - Installs the project as a distribution as-is.

Documentation tasks
-------------------
javadoc - Generates Javadoc API documentation for the main source code.

Help tasks
----------
buildEnvironment - Displays all buildscript dependencies declared in root project 'java-sample'.
components - Displays the components produced by root project 'java-sample'. [incubating]
dependencies - Displays all dependencies declared in root project 'java-sample'.
dependencyInsight - Displays the insight into a specific dependency in root project 'java-sample'.
dependentComponents - Displays the dependent components of components in root project 'java-sample'. [incubating]
help - Displays a help message.
model - Displays the configuration model of root project 'java-sample'. [incubating]
outgoingVariants - Displays the outgoing variants of root project 'java-sample'.
projects - Displays the sub-projects of root project 'java-sample'.
properties - Displays the properties of root project 'java-sample'.
tasks - Displays the tasks runnable from root project 'java-sample'.

Lombok tasks
------------
delombok - Runs delombok on the main source-set
delombokTest - Runs delombok on the test source-set
generateLombokConfig

Verification tasks
------------------
check - Runs all checks.
jacocoTestCoverageVerification - Verifies code coverage metrics based on specified rules for the test task.
jacocoTestReport - Generates code coverage report for the test task.
test - Runs the unit tests.

Rules
-----
Pattern: clean<TaskName>: Cleans the output files of a task.
Pattern: build<ConfigurationName>: Assembles the artifacts of a configuration.
Pattern: upload<ConfigurationName>: Assembles and uploads the artifacts belonging to a configuration.

To see all tasks and more detail, run gradle tasks --all

To see more detail about a task, run gradle help --task <task>
```

Notice plugins and dependencies we added have tasks of their own, such as `delombok`.

### 4.2. checks

- JaCoCo coverage report is available in `build/reports/jacoco/test/html/index.html`.

    ![img](https://www.eclemma.org/images/jacocoreport.png)

- SpotBugs report is available in `build/reports/spotbugs/main/spotbugs.html`.

Run `gradle check` to generate these reports.

## 5. IntelliJ

Simply open the folder in IntelliJ. It should automatically recognize
this is a Gradle project, and setup the project accordingly.

There should be a `Gradle` tab on the right side of the IntelliJ
window. You can run the various Gradle tasks, and configure project
settings there.

## 6. Conclusion

We are now ready to develop our awesome java application using all the
fancy tools and support we've added to Gradle.