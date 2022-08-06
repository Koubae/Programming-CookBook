
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

# Build

# Run
