$VERSION_TAG="0.14.0-rc3"

mkdir -p $WORKSPACE/SOURCES
if [ ! -e $WORKSPACE/SOURCES/$VERSION_TAG.tar.gz ]; then
    wget https://github.com/apache/mesos/archive/$VERSION_TAG.tar.gz -O $WORKSPACE/SOURCES/$VERSION_TAG.tar.gz
fi

QA_RPATHS=$[ 0x0002|0x0001 ] rpmbuild --define "_topdir $WORKSPACE" -bb $WORKSPACE/mesos.spec