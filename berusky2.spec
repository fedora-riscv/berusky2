Name:           berusky2
Version:        0.9
Release:        2%{?dist}
License:        GPLv2+
Summary:        Sokoban clone
Group:          Amusements/Games
Source:         http://www.anakreon.cz/download/%{name}-%{version}.tar.gz
URL:            http://www.anakreon.cz/en/Berusky2.htm

Requires:       berusky2-data >= 0.7
BuildRequires:  SDL-devel
BuildRequires:  SDL_image-devel
BuildRequires:  gtk2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  freealut-devel
BuildRequires:  openal-soft-devel
BuildRequires:  libvorbis-devel
ExclusiveArch:  %{ix86} x86_64 %{arm}

%description
Berusky 2 is a game that challenges your visual/spatial thinking
and ability to find a way to resolve a logic task. Using five bugs,
you'll go through an adventure full of various puzzles spread across
nine episodes. Individual episodes differ in appearance and difficulty,
which increases throughout the game.

%prep
%setup -q

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
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps
cp -p %{buildroot}/%{_datadir}/%{name}/berusky2.png \
      %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps

desktop-file-install --dir %{buildroot}/%{_datadir}/applications \
                     --add-category X-Fedora %{buildroot}/%{_datadir}/%{name}/berusky2.desktop

# Remove directory that will be owned by data package.
rm -rf %{buildroot}/%{_datadir}/%{name}

%post
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
 %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
 %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%files
%doc _tmpdoc/*
%{_bindir}/berusky2
%{_datadir}/applications/berusky2.desktop
%{_datadir}/icons/hicolor/32x32/apps/berusky2.png
%dir %{_var}/games/%{name}
%{_var}/games/%{name}/*

%changelog
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
