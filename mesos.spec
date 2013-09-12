# To build:
#
# You will need the autoconf and libunwind from http://repo.milford.io and the Oracle JDK.
#
# sudo yum -y install rpmdevtools && rpmdev-setuptree
# sudo yum -y install python26-devel curl-devel libunwind-devel automake autoconf jdk
#
# wget https://raw.github.com/nmilford/rpm-mesos/master/mesos.spec -O ~/rpmbuild/SPECS/mesos.spec
# wget http://mirror.tcpdiag.net/apache/incubator/mesos/mesos-0.12.0-incubating/mesos-0.12.0-incubating.tar.gz -O ~/rpmbuild/SOURCES/mesos-0.12.0-incubating.tar.gz
# wget https://raw.github.com/nmilford/rpm-mesos/master/mesos -O ~/rpmbuild/SOURCES/mesos
# wget https://raw.github.com/nmilford/rpm-mesos/master/mesos.nofiles.conf -O ~/rpmbuild/SOURCES/mesos.nofiles.conf
# wget https://raw.github.com/nmilford/rpm-mesos/master/mesos.conf -O ~/rpmbuild/SOURCES/mesos.conf
# wget https://raw.github.com/nmilford/rpm-mesos/master/mesos-master -O ~/rpmbuild/SOURCES/mesos-master
# wget https://raw.github.com/nmilford/rpm-mesos/master/mesos-slave -O ~/rpmbuild/SOURCES/mesos-slave
#
# QA_RPATHS=$[ 0x0002|0x0001 ] rpmbuild -bb ~/rpmbuild/SPECS/mesos.spec

Name:      mesos
Version:   0.14.0
Release:   rc3
Summary:   Apache Mesos Cluster Manager
License:   Apache 2.0
URL:       http://mesos.apache.org/
Group:     Applications/System
Source0:   https://github.com/apache/mesos/archive/0.14.0-rc3.tar.gz
Source1:   mesos
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
Packager:  Tom Petr <tpetr@hubspot.com>
BuildRequires: automake
BuildRequires: autoconf
AutoReq: no

%description
Apache Mesos is a cluster manager that provides efficient resource isolation and
sharing across distributed applications, or frameworks. It can run Hadoop, MPI,
Hypertable, Spark, and other applications on a dynamically shared pool of nodes.

%prep
%setup -n %{name}-%{version}-%{release}

%build
./bootstrap
LIBS="-lsnappy" ./configure --prefix=%{_prefix} --libdir=%{_libdir}
%{__make} %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR="%{buildroot}"

rm -rf %{buildroot}/usr/var/mesos*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/mesos-*
%{_includedir}/mesos/*
%{_libdir}/libmesos*
%{_libexecdir}/mesos/*
%{_sbindir}/*
%{_datadir}/mesos/*
