%define name	alienpool
%define version	0.2.0
%define release	%mkrel 6

Name:		%{name}
Summary:	Arcade-style mix of asteroids and pool
Version:	%{version}
Release:	%{release}
Epoch:		1
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}-16.png
Source2:	%{name}-32.png
Source3:	%{name}-48.png
URL:		http://www.mkorman.org/alienpool/
Group:		Games/Arcade
BuildRoot:	%{_tmppath}/%{name}-buildroot
License:	GPLv2+
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel

%description
Alienpool is a space-shooter that is similar to both asteroids
and pool. Move a spaceship around the screen and shoot at aliens.
Aliens that have been shot bounce around the screen and hit other
aliens.

%prep
%setup -q

%build
%configure --bindir=%{_gamesbindir} --localstatedir=%{_localstatedir}/lib
%make

%install
rm -rf %{buildroot}
%makeinstall_std

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Alien pool
Comment=Arcade-style mix of asteroids and pool
Exec=%{_gamesbindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

%__install -D -m 644 %SOURCE1 %{buildroot}%{_iconsdir}/%{name}.png
%__install -D -m 644 %SOURCE2 %{buildroot}%{_miconsdir}/%{name}.png
%__install -D -m 644 %SOURCE3 %{buildroot}%{_liconsdir}/%{name}.png

%__rm -f %{buildroot}%{_datadir}/pixmaps/alienpool.xpm

%clean
%__rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr(0644,root,root,0755)
%doc README NEWS COPYING AUTHORS
%attr(2755, root, games) %{_gamesbindir}/%{name}
%attr(664, root, games) %{_localstatedir}/lib/games/*
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}/*
%{_mandir}/man6/%{name}.6*
%{_datadir}/pixmaps/%{name}-48.png
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png


%changelog
* Tue Feb 09 2010 Sandro Cazzaniga <kharec@mandriva.org> 1:0.2.0-6mdv2010.1
+ Revision: 503408
- rebuild

* Mon May 25 2009 JÃ©rÃ´me Brenier <incubusss@mandriva.org> 1:0.2.0-5mdv2010.0
+ Revision: 379660
- adapt to localstatedir being /var instead of /var/lib
- fix URL / Source
- delete buildroot before install
- cosmetic changes

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

* Wed Jan 30 2008 Funda Wang <fwang@mandriva.org> 1:0.2.0-2mdv2008.1
+ Revision: 160133
- simplify BR's version
- drop requirement on SDL*

  + Thierry Vignaud <tvignaud@mandriva.com>
    - drop old menu

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1:0.2.0-1mdv2008.1
+ Revision: 135819
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - import alienpool


* Tue Sep 05 2006 Stéphane Téletchéa <steletch@mandriva.org> 1:0.2.0-1mdv2007.0
- Migration to XDG menu structure
- Add mkrel

* Wed Jun 28 2006 Lenny Cartier <lenny@mandriva.com> 0:0.2.0-2mdv2007.0
- rebuild

* Thu Sep 02 2004 David Walluck <walluck@linux-mandrake.com> 0:0.2.0-1mdk
- 0.2.0

* Thu Jun 17 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.1.0-2mdk
- Rebuild

* Sun Feb 15 2004 David Walluck <walluck@linux-mandrake.com> 0:0.1.0-1mdk
- release
