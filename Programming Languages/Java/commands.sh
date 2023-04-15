
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
# run 
mvn clean javafx:run


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


##########################################
#            jshell                      #
##########################################
jshell 
# exit (also CTRL + d)
/exit 
/ex