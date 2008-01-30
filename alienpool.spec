%define name	alienpool
%define version	0.2.0
%define release	%mkrel 2

Name:		%{name}
Summary:	Arcade-style mix of asteroids and pool
Version:	%{version}
Release:	%{release}
Epoch:		1
Source0:	http://mike.taequin.org/alienpool/%{name}-%{version}.tar.bz2
Source1:	%{name}-16.png
Source2:	%{name}-32.png
Source3:	%{name}-48.png
URL:		http://mike.taequin.org/alienpool/
Group:		Games/Arcade
BuildRoot:	%{_tmppath}/%{name}-buildroot
License:	GPLv2+
BuildRequires:	SDL1.2-devel
BuildRequires:	SDL_image1.2-devel
BuildRequires:	SDL_mixer1.2-devel
BuildRequires:	SDL_ttf-devel >= 0:2.0

%description
Alienpool is a space-shooter that is similar to both asteroids
and pool. Move a spaceship around the screen and shoot at aliens.
Aliens that have been shot bounce around the screen and hit other
aliens.

%prep
%setup -q

%build
%configure --bindir=%{_gamesbindir}
%make

%install
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Alien pool
Comment=Arcade-style mix of asteroids and pool
Exec=%{_gamesbindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

%__install -D -m 644 %SOURCE1 $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
%__install -D -m 644 %SOURCE2 $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
%__install -D -m 644 %SOURCE3 $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%__rm -f $RPM_BUILD_ROOT%{_datadir}/pixmaps/alienpool.xpm

%clean
%__rm -rf $RPM_BUILD_ROOT

%post
%{update_menus}

%postun
%{clean_menus}

%files
%defattr(0644,root,root,0755)
%doc README NEWS COPYING AUTHORS
%attr(2755, root, games) %{_gamesbindir}/%{name}
%attr(664, root, games) %{_localstatedir}/games/*
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}/*
%{_mandir}/man6/%{name}.6*
%{_datadir}/pixmaps/%{name}-48.png
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
