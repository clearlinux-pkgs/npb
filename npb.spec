#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : npb
Version  : 3.4.2
Release  : 4
URL      : https://www.nas.nasa.gov/assets/npb/NPB3.4.2.tar.gz
Source0  : https://www.nas.nasa.gov/assets/npb/NPB3.4.2.tar.gz
Source1  : npb-run-omp.sh
Source2  : npb-run-mpi.sh
Summary  : NAS Parallel Benchmarks
Group    : Development/Tools
License  : NASA-1.3
Requires: npb-bin = %{version}-%{release}
Requires: npb-openmpi = %{version}-%{release}
Requires: openmpi
BuildRequires : openmpi
BuildRequires : openmpi-dev
Patch1: suite_def.patch
Patch2: mpi_def.patch
Patch3: omp_def.patch
Patch4: makefile.patch
Patch5: make_common.patch

%description
NAS Parallel Benchmarks Version 3.4.2 (NPB3.4.2)
--------------------------------------------------

%package bin
Summary: bin components for the npb package.
Group: Binaries

%description bin
bin components for the npb package.


%package openmpi
Summary: openmpi components for the npb package.
Group: Default

%description openmpi
openmpi components for the npb package.


%prep
%setup -q -n NPB3.4.2
cd %{_builddir}/NPB3.4.2
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1624411471
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1624411471
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}/usr
install -m 0755 %{_sourcedir}/npb-run-omp.sh %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr
install -m 0755 %{_sourcedir}/npb-run-mpi.sh %{buildroot}/usr/bin

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bt.A.x
/usr/bin/bt.B.x
/usr/bin/bt.C.x
/usr/bin/bt.D.x
/usr/bin/bt.E.x
/usr/bin/bt.S.x
/usr/bin/bt.W.x
/usr/bin/cg.A.x
/usr/bin/cg.B.x
/usr/bin/cg.C.x
/usr/bin/cg.D.x
/usr/bin/cg.E.x
/usr/bin/cg.S.x
/usr/bin/cg.W.x
/usr/bin/ep.A.x
/usr/bin/ep.B.x
/usr/bin/ep.C.x
/usr/bin/ep.D.x
/usr/bin/ep.E.x
/usr/bin/ep.S.x
/usr/bin/ep.W.x
/usr/bin/ft.A.x
/usr/bin/ft.B.x
/usr/bin/ft.C.x
/usr/bin/ft.D.x
/usr/bin/ft.E.x
/usr/bin/ft.S.x
/usr/bin/ft.W.x
/usr/bin/is.A.x
/usr/bin/is.B.x
/usr/bin/is.C.x
/usr/bin/is.S.x
/usr/bin/is.W.x
/usr/bin/lu.A.x
/usr/bin/lu.B.x
/usr/bin/lu.C.x
/usr/bin/lu.D.x
/usr/bin/lu.E.x
/usr/bin/lu.S.x
/usr/bin/lu.W.x
/usr/bin/mg.A.x
/usr/bin/mg.B.x
/usr/bin/mg.C.x
/usr/bin/mg.D.x
/usr/bin/mg.E.x
/usr/bin/mg.S.x
/usr/bin/mg.W.x
/usr/bin/npb-run-mpi.sh
/usr/bin/npb-run-omp.sh
/usr/bin/sp.A.x
/usr/bin/sp.B.x
/usr/bin/sp.C.x
/usr/bin/sp.D.x
/usr/bin/sp.E.x
/usr/bin/sp.S.x
/usr/bin/sp.W.x
/usr/bin/ua.A.x
/usr/bin/ua.B.x
/usr/bin/ua.C.x
/usr/bin/ua.D.x
/usr/bin/ua.S.x
/usr/bin/ua.W.x

%files openmpi
%defattr(-,root,root,-)
/usr/lib64/openmpi/bin/dt.A.x
/usr/lib64/openmpi/bin/dt.B.x
/usr/lib64/openmpi/bin/dt.S.x
/usr/lib64/openmpi/bin/dt.W.x
/usr/lib64/openmpi/bin/is.A.x
/usr/lib64/openmpi/bin/is.B.x
/usr/lib64/openmpi/bin/is.C.x
/usr/lib64/openmpi/bin/is.D.x
/usr/lib64/openmpi/bin/is.E.x
/usr/lib64/openmpi/bin/is.S.x
/usr/lib64/openmpi/bin/is.W.x
