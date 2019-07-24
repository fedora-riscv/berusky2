Name:           berusky2
Version:        0.10
Release:        21%{?dist}
License:        GPLv2+
Summary:        Sokoban clone
Source:         http://www.anakreon.cz/download/%{name}-%{version}.tar.gz
Source1:        berusky2.appdata.xml
Source2:        berusky2.png
Patch0:         berusky2-anim-crash.patch
Patch1:         berusky2-gcc6.patch
Patch2:         berusky2-gcc7.patch
Patch3:         berusky2-mmalloc.patch
URL:            http://www.anakreon.cz/en/Berusky2.htm

Requires:       berusky2-data >= 0.9
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  SDL-devel
BuildRequires:  SDL_image-devel
BuildRequires:  gtk2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  freealut-devel
BuildRequires:  openal-soft-devel
BuildRequires:  libvorbis-devel
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 %{mips}

%description
Berusky 2 is a game that challenges your visual/spatial thinking
and ability to find a way to resolve a logic task. Using five bugs,
you'll go through an adventure full of various puzzles spread across
nine episodes. Individual episodes differ in appearance and difficulty,
which increases throughout the game.

%prep
%setup -q
%patch0 -p1 -b .anim-crash
%patch1 -p1 -b .gcc
%patch2 -p1 -b .gcc7
%patch3 -p1 -b .mmalloc

%build
%configure CFLAGS="$RPM_OPT_FLAGS"

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

# Move documentation so it can get installed to the right place.
mkdir _tmpdoc
mv %{buildroot}%{_usr}/doc/%{name}/* _tmpdoc/
rm -f _tmpdoc/INSTALL

# Install ini file
mkdir -p %{buildroot}%{_var}/games/%{name}
install -pm 644 %{buildroot}/%{_datadir}/%{name}/berusky3d.ini \
                %{buildroot}%{_var}/games/%{name}

# Install icon and desktop file
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps

desktop-file-install --dir %{buildroot}/%{_datadir}/applications \
                     --add-category X-Fedora %{buildroot}/%{_datadir}/%{name}/berusky2.desktop

# Remove directory that will be owned by data package.
rm -rf %{buildroot}/%{_datadir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata/
cp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/appdata/

%files
%doc _tmpdoc/*
%{_bindir}/berusky2
%{_datadir}/applications/berusky2.desktop
%{_datadir}/icons/hicolor/128x128/apps/berusky2.png
%{_datadir}/appdata/berusky2.appdata.xml
%dir %{_var}/games/%{name}
%{_var}/games/%{name}/*

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.10-17
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 12 2017 Michal Toman <mtoman@fedoraproject.org> 0.10-14
- Enable on MIPS

* Fri Jun 30 2017 Martin Stransky <stransky@redhat.com> 0.10-13
- gcc7 build fix
- mmalloc link patch

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 14 2016 Martin Stransky <stransky@redhat.com> 0.10-11
- gcc6 build fix

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Martin Stransky <stransky@redhat.com> 0.10-9
- fixes more animation crashes (water, teleports, lifts)

* Wed Dec 30 2015 Martin Stransky <stransky@redhat.com> 0.10-8
- fixes animation crashes

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.10-6
- Rebuilt for GCC 5 C++11 ABI change

* Fri Nov 7 2014 Martin Stransky <stransky@redhat.com> 0.10-5
- Added appdata file

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.10-3
- Build on aarch64

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Jan 18 2014 Martin Stransky <stransky@redhat.com> 0.10-1
- Updated to 0.10

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 24 2013 Martin Stransky <stransky@redhat.com> 0.9-1
- Updated to 0.9

* Sun Dec 16 2012 Martin Stransky <stransky@redhat.com> 0.8-2
- Updated to 0.8

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May  2 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.7-2
- Build on ARM too

* Wed Mar 28 2012 Martin Stransky <stransky@redhat.com> 0.7-1
- Updated to 0.7

* Mon Mar 5 2012 Martin Stransky <stransky@redhat.com> 0.6.1-1
- Updated to 0.6.1

* Sun Mar 4 2012 Martin Stransky <stransky@redhat.com> 0.6-1
- Updated to 0.6

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Sep 7 2011 Martin Stransky <stransky@redhat.com> 0.5-1
- Updated to 0.5

* Tue Aug 30 2011 Martin Stransky <stransky@redhat.com> 0.4-1
- new upstream version
- spec clean-up (by Richard Shaw)

* Mon Aug 22 2011 Martin Stransky <stransky@redhat.com> 0.3-3
- spec polished

* Mon Aug 15 2011 Martin Stransky <stransky@redhat.com> 0.3-2
- fixed ini file location

* Mon Aug 15 2011 Martin Stransky <stransky@redhat.com> 0.3-1
- initial build
