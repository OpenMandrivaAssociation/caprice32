Summary:	Amstrad CPC Emulator
Name:		caprice32
Version:	4.2.0
Release:	4
Group:		Emulators
#v2, except for cpc roms, which just are just allowed be distributed
License:	GPLv2
URL:		http://caprice32.sourceforge.net/
Source0:	%{name}-%{version}-src.tar.bz2
Source1:	%{name}.png
#this is the same icon as xcpc, but converted in png
Source2:	%{name}
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(zlib)

%description
CaPriCe32 emulates the Amstrad CPC home computer models 464, 664 and 6128 
faithfully on your PC.
Detailed usage instructions can be found in the included documentation.

%prep
%setup -c -q
perl -pi -e "s|\r\n|\n|g" README.txt

%build
%make -f makefile.unix RELEASE=true

%install
#binary
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 cap32 %{buildroot}%{_bindir}
#wrapper
install -m 755 %{SOURCE2} %{buildroot}%{_bindir}
#roms
install -d -m 755 %{buildroot}%{_datadir}/%{name}/rom
install -m 644 rom/* %{buildroot}%{_datadir}/%{name}/rom/
#config
install -m 644 cap32.cfg %{buildroot}%{_datadir}/%{name}/
#icon
install -d -m 755 %{buildroot}%{_iconsdir}
install -m 644 %{SOURCE1} %{buildroot}%{_iconsdir}/

#xdg menu
install -d -m 755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Version=1.0
Encoding=UTF-8
Name=CaPriCe32
Comment=Amstrad CPC Emulator
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Emulators;Emulator;
EOF

%files
%doc README.txt
%attr(0755,root,root) %{_bindir}/cap32
%attr(0755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_iconsdir}/*
%{_datadir}/applications/mandriva-%{name}.desktop

%changelog
* Wed Aug 03 2011 Andrey Bondrov <abondrov@mandriva.org> 4.2.0-2mdv2012.0
+ Revision: 692924
- Fix debug info extraction error
- Fix BuildRequires
- imported package caprice32


* Sun Jul 29 2007 Guillaume Bedot <littletux@zarb.org> 4.2.0-1plf2008.0
- First PLF package for caprice32
