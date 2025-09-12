
##########################################
#            INSTALLATION                #
##########################################
# https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/How-do-I-install-Java-on-Ubuntu
# https://askubuntu.com/questions/740757/switch-between-multiple-java-versions
#List all java versions:
update-java-alternatives --list

#Set java version as default (needs root permissions):
sudo update-java-alternatives --set /path/to/java/version
#...where /path/to/java/version is one of those listed by the previous command (e.g. /usr/lib/jvm/java-7-openjdk-amd64).

#Additional information:
#update-java-alternatives is a convenience tool that uses Debian's (alternatives system)[https://wiki.debian.org/DebianAlternatives] (update-alternatives) to set a bunch of links to the specified java version (e.g. java, javac, ...).

# https://askubuntu.com/a/845300/1166575

sudo update-alternatives --config java # which lists all installed versions with current active one marked and provides dialog to switch:
# use to set $JAVA_HOME from current active version
export JAVA_HOME="$(jrunscript -e 'java.lang.System.out.println(java.lang.System.getProperty("java.home"));')"

# Find Java installation
# Windows - CMD 
for %i in (javac.exe) do @echo.   %~$PATH:i
# Linux 
which java


##########################################
#            RUN / BUILD                 #
##########################################

# ----------------
#   Compile
# ----------------
javac FileName.java 
# Compile all java files (same folder)
javac *.java

# Run
java FileName 

# Class Path to include other jars
java -classpath [lib/..jar]

# multiple jars
java -cp "Test.jar:lib/*" my.package.MainClass
java -cp jar1:jar2:jar3:dir1:. HelloWorld
# windows
java -cp C:/.../jardir1/*;C:/.../jardir2/* class_with_main_method

##########################################
#            MAVEN                       #
##########################################
# install
sudo apt install maven
mvn --version 

# it worked
export JAVA_HOME=/usr/lib/jvm/default-java


# or craate a maven.º
# # https://linuxize.com/post/how-to-install-apache-maven-on-ubuntu-18-04/

# sudo vim /etc/profile.d/maven.sh
export JAVA_HOME=/usr/lib/jvm/default-java
export M2_HOME=/opt/maven
export MAVEN_HOME=/opt/maven
export PATH=${M2_HOME}/bin:${PATH}


# Create a project
mvn archetype:generate -DgroupId=com.mycompany.app -DartifactId=my-app -DarchetypeArtifactId=maven-archetype-quickstart -DarchetypeVersion=1.4 -DinteractiveMode=false


# download dependencies without doing anything else
mvn dependency:resolve
# download a single dependency
mvn dependency:get -Dartifact=groupId:artifactId:version
# clean 
mvn clean javafx:run
# compile 
mvn compile
# build project 
mvn package 
# run project 
java -cp target/my-app-1.0-SNAPSHOT.jar com.mycompany.app.App

# download junit
mvn dependency:get -DremoteRepositories=http://repo1.maven.org/maven2/ \
                   -DgroupId=junit -DartifactId=junit -Dversion=4.8.2 \
                   -Dtransitive=false
# spring
mvn dependency:get -Dartifact=org.springframework:spring-instrument:3.2.3.RELEASE
# maven plugin
mvn org.apache.maven.plugins:maven-dependency-plugin:2.1:get \
    -DrepoUrl=http://download.java.net/maven/2/ \
    -Dartifact=robo-guice:robo-guice:0.4-SNAPSHOT 



# copy command  https://stackoverflow.com/a/65019190/13903942
mvn dependency:copy -Dartifact=<group>:<artifact-name>:<version> -DoutputDirectory=/tmp/my_custom_dir

# -------------
# Maven + Spring Boot
# -------------
./mvnw spring-boot:run 
# Build jar and run 
./mvnw clean package
java -jar target/target-jar.jar

##########################################
#            jshell                      #
##########################################
jshell 
# exit (also CTRL + d)
/exit 
/ex


# With -XX:+UseSerialGC This will perform garbage collection inline with the thread allocating the heap memory instead of a dedicated GC thread(s)

# With -Xss512k This will limit each threads stack memory to 512KB instead of the default 1MB

# With -XX:MaxRAM=72m This will restrict the JVM's calculations for the heap and non heap managed memory to be within the limits of this value.

# In addition to the above JVM options you can also use the following property inside your application.properties file:
# server.tomcat.max-threads = 1 This will limit the number of HTTP request handler threads to 1 (default is 200)


##########################################
#           INSTALL 2                    #
##########################################

# Install Java corretto - Add multiple 3 latest versions
# 1) ======================
#    Update system
# 1) ======================
sudo apt update && sudo apt upgrade -y
# 2) ======================
#    Add Amazon Corretto repository
# 2) ======================
# Import the Amazon Corretto GPG key
wget -O- https://apt.corretto.aws/corretto.key | sudo apt-key add -
# Add the repository
sudo add-apt-repository 'deb https://apt.corretto.aws stable main'
# Update package lists
sudo apt update

# 3) ======================
#    Install the latest 3 versions
# 3) ======================
sudo apt install -y java-17-amazon-corretto-jdk
sudo apt install -y java-21-amazon-corretto-jdk
# sudo apt install -y java-22-amazon-corretto-jdk
sudo apt install -y java-24-amazon-corretto-jdk

# 4) ======================
#    Manage multiple Java versions
# 4) ======================
update-alternatives --list java
# Register alternatives (if not auto-registered):
sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/java-17-amazon-corretto/bin/java 1717
sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/java-21-amazon-corretto/bin/java 2121
sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/java-24-amazon-corretto/bin/java 2424

#  Set default Java to the latest (24)
sudo update-alternatives --config java
sudo update-alternatives --display java

java -version

# ======================
#  Set JAVA_HOME
# ======================
# Find your install dir:
ls -d /usr/lib/jvm/java-24-amazon-corretto


# option 2
# Java version switcher
export JAVA_HOME=/usr/lib/jvm/java-24-amazon-corretto
export PATH="$JAVA_HOME/bin:$PATH"

use_java17() {
  export JAVA_HOME=/usr/lib/jvm/java-17-amazon-corretto
  export PATH="$JAVA_HOME/bin:$PATH"
  java -version
}

use_java21() {
  export JAVA_HOME=/usr/lib/jvm/java-21-amazon-corretto
  export PATH="$JAVA_HOME/bin:$PATH"
  java -version
}

use_java24() {
  export JAVA_HOME=/usr/lib/jvm/java-24-amazon-corretto
  export PATH="$JAVA_HOME/bin:$PATH"
  java -version
}

# ======================
#  Gradle
# ======================
# Create directory for Gradle
sudo mkdir -p /opt/gradle
cd /opt/gradle

# Download Gradle (replace version if newer is out)
sudo wget https://services.gradle.org/distributions/gradle-8.10.2-bin.zip -P /tmp

# Unzip
sudo unzip -d /opt/gradle /tmp/gradle-8.10.2-bin.zip

# Symlink "current" to latest
sudo ln -sfn /opt/gradle/gradle-8.10.2 /opt/gradle/current

## Add gradle to path
export PATH=/opt/gradle/current/bin:$PATH
source ~/.bashrc
gradle --version

# ======================
#  Maven
# ======================
sudo apt install maven
mvn --version