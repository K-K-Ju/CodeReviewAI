T1 = '''[
  {
    "name": ".gitignore",
    "path": ".gitignore",
    "sha": "68851d46cb9a5d45b053ea2d268bd12272c0f9e2",
    "size": 49,
    "url": "https://api.github.com/repos/K-K-Ju/test-str-counter/contents/.gitignore?ref=master",
    "html_url": "https://github.com/K-K-Ju/test-str-counter/blob/master/.gitignore",
    "git_url": "https://api.github.com/repos/K-K-Ju/test-str-counter/git/blobs/68851d46cb9a5d45b053ea2d268bd12272c0f9e2",
    "download_url": "https://raw.githubusercontent.com/K-K-Ju/test-str-counter/master/.gitignore",
    "type": "file",
    "_links": {
      "self": "https://api.github.com/repos/K-K-Ju/test-str-counter/contents/.gitignore?ref=master",
      "git": "https://api.github.com/repos/K-K-Ju/test-str-counter/git/blobs/68851d46cb9a5d45b053ea2d268bd12272c0f9e2",
      "html": "https://github.com/K-K-Ju/test-str-counter/blob/master/.gitignore"
    }
  },
  {
    "name": "README.md",
    "path": "README.md",
    "sha": "90bad3a8677a7234000834f0cb983e4a09e71636",
    "size": 128,
    "url": "https://api.github.com/repos/K-K-Ju/test-str-counter/contents/README.md?ref=master",
    "html_url": "https://github.com/K-K-Ju/test-str-counter/blob/master/README.md",
    "git_url": "https://api.github.com/repos/K-K-Ju/test-str-counter/git/blobs/90bad3a8677a7234000834f0cb983e4a09e71636",
    "download_url": "https://raw.githubusercontent.com/K-K-Ju/test-str-counter/master/README.md",
    "type": "file",
    "_links": {
      "self": "https://api.github.com/repos/K-K-Ju/test-str-counter/contents/README.md?ref=master",
      "git": "https://api.github.com/repos/K-K-Ju/test-str-counter/git/blobs/90bad3a8677a7234000834f0cb983e4a09e71636",
      "html": "https://github.com/K-K-Ju/test-str-counter/blob/master/README.md"
    }
  },
  {
    "name": "pom.xml",
    "path": "pom.xml",
    "sha": "6cc2bb40aa50404cb8ad47945dcb0e997529a754",
    "size": 1299,
    "url": "https://api.github.com/repos/K-K-Ju/test-str-counter/contents/pom.xml?ref=master",
    "html_url": "https://github.com/K-K-Ju/test-str-counter/blob/master/pom.xml",
    "git_url": "https://api.github.com/repos/K-K-Ju/test-str-counter/git/blobs/6cc2bb40aa50404cb8ad47945dcb0e997529a754",
    "download_url": "https://raw.githubusercontent.com/K-K-Ju/test-str-counter/master/pom.xml",
    "type": "file",
    "_links": {
      "self": "https://api.github.com/repos/K-K-Ju/test-str-counter/contents/pom.xml?ref=master",
      "git": "https://api.github.com/repos/K-K-Ju/test-str-counter/git/blobs/6cc2bb40aa50404cb8ad47945dcb0e997529a754",
      "html": "https://github.com/K-K-Ju/test-str-counter/blob/master/pom.xml"
    }
  },
  {
    "name": "src",
    "path": "src",
    "sha": "dfb76fd8a6abca29529478bd541ed7b8810da4dc",
    "size": 0,
    "url": "https://api.github.com/repos/K-K-Ju/test-str-counter/contents/src?ref=master",
    "html_url": "https://github.com/K-K-Ju/test-str-counter/tree/master/src",
    "git_url": "https://api.github.com/repos/K-K-Ju/test-str-counter/git/trees/dfb76fd8a6abca29529478bd541ed7b8810da4dc",
    "download_url": null,
    "type": "dir",
    "_links": {
      "self": "https://api.github.com/repos/K-K-Ju/test-str-counter/contents/src?ref=master",
      "git": "https://api.github.com/repos/K-K-Ju/test-str-counter/git/trees/dfb76fd8a6abca29529478bd541ed7b8810da4dc",
      "html": "https://github.com/K-K-Ju/test-str-counter/tree/master/src"
    }
  }
]'''

T2 = '''pom.xml

<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>ua.testing-str-counter.io</groupId>
  <artifactId>test-str-counter</artifactId>
  <version>1.0-SNAPSHOT</version>
  <packaging>jar</packaging>

  <name>test-str-counter</name>
  <url>http://maven.apache.org</url>

  <properties>
    <java.version>11</java.version>
    <maven.compiler.source>${java.version}</maven.compiler.source>
    <maven.compiler.target>${java.version}</maven.compiler.target>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
  </properties>

  <repositories>
    <repository>
      <id>jitpack.io</id>
      <url>https://jitpack.io</url>
    </repository>
  </repositories>

  <dependencies>

    <dependency>
      <groupId>com.github.K-K-Ju</groupId>
      <artifactId>str-lib</artifactId>
      <version>83322bd319</version>
    </dependency>

  </dependencies>

  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-compiler-plugin</artifactId>
        <version>3.8.0</version>
      </plugin>
    </plugins>
  </build>
</project>


src/main/java/org/example/App.java

package org.example;

import io.str_counter.ua.CharacterCounter;
import io.str_counter.ua.CharacterCounterImpl;

import java.util.List;

public class App{

    private static final CharacterCounter counter = new CharacterCounterImpl();

    public static void main(String[] args) {
        List<String> text = List.of("Suppose you want to show these anonymous users a message \\n" +
                "that says, “Hello guest.” This is a perfect place to use a \\n" +
                "default value with the c:out tag. Just add a default\\n" +
                "attribute, and provide the value you want to print if your \\n" +
                "expression evaluates to null");

        var result = counter.countCharacters(text);

        result.entrySet().forEach(System.out::println);
    }
}


'''