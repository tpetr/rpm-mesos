# To build:
#
# You will need the autoconf and libunwind from http://repo.milford.io and the Oracle JDK.
#
# sudo yum -y install rpmdevtools && rpmdev-setuptree
# sudo yum -y install python26-devel curl-devel libunwind-devel automake autoconf jdk
#
# QA_RPATHS=$[ 0x0002|0x0001 ] rpmbuild -bb ~/rpmbuild/SPECS/mesos.spec

Name:      mesos
Version:   0.14.0
Release:   rc3
Summary:   Apache Mesos Cluster Manager
License:   Apache 2.0
URL:       http://mesos.apache.org/
Group:     Applications/System
Source0:   https://github.com/apache/%{name}/archive/%{version}-%{release}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
Packager:  Tom Petr <tpetr@hubspot.com>
BuildRequires: automake
BuildRequires: autoconf
Requires(pre): libsnappy
AutoReq: no

%description
Apache Mesos is a cluster manager that provides efficient resource isolation and
sharing across distributed applications, or frameworks. It can run Hadoop, MPI,
Hypertable, Spark, and other applications on a dynamically shared pool of nodes.

%prep
%setup -qn %{name}-%{version}-%{release}

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
