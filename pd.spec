Summary:   Real-time patchable audio and multimedia processor.
Name:      pd
Version:   0.50
Release:   0
License:   BSD
Source:    http://msp.ucsd.edu/Software/pd-0.50-0.src.tar.gz


BuildRequires:	gcc
BuildRequires:	cmake
BuildRequires:	gettext-devel
BuildRequires:	libtool

%description
Pd gives you a canvas for patching together modules that analyze, process,
and synthesize sounds, together with a rich palette of real-time control  
and I/O possibilities.  Similar to Max (Cycling74) and JMAX (IRCAM).  A   
related software package named Gem extends Pd's capabilities to include   
graphical rendering.

%prep
%setup -n pd-%{version}-%{release}

%build
./autogen.sh
./configure --disable-alsa --prefix=%{prefix} --mandir=%{_mandir}
make depend 
make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{prefix}/bin
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{prefix}/lib/pd/include
mkdir -p $RPM_BUILD_ROOT%{prefix}/lib/pd/bin

install -m 644 man/* $RPM_BUILD_ROOT%{_mandir}/man1
install -s -m 4755 bin/pd $RPM_BUILD_ROOT%{prefix}/bin/pd
install -s bin/pd-gui bin/pd-watchdog $RPM_BUILD_ROOT%{prefix}/lib/pd/bin/
install -s bin/pdsend bin/pdreceive $RPM_BUILD_ROOT%{prefix}/bin/
install bin/pd.tk $RPM_BUILD_ROOT%{prefix}/lib/pd/bin/
cp -pr doc $RPM_BUILD_ROOT%{prefix}/lib/pd/
cp -pr extra $RPM_BUILD_ROOT%{prefix}/lib/pd/
install README.txt LICENSE.txt $RPM_BUILD_ROOT%{prefix}/lib/pd/
install src/*.h $RPM_BUILD_ROOT%{prefix}/lib/pd/include

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)

%{prefix}/bin/pd
%{prefix}/bin/pdsend
%{prefix}/bin/pdreceive
%{prefix}/lib/pd
%{_mandir}/man1/pd.1.gz
%{_mandir}/man1/pdsend.1.gz
%{_mandir}/man1/pdreceive.1.gz

%changelog
* Sun Oct 06 2019 Ron Olson <tachoknight@gmail.com>
  Ressurected the spec file for packaging in modern Fedora
* Tue Apr 14 2001 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- added %{prefix}, added %{_mandir} so that the man pages go into the
  correct man directory for redhat
- added %{alsa} for automatic detection of the installed alsa library
- decoupled pd release (ie: PATCH2) from the rpm release 
