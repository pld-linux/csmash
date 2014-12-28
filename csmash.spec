Summary:	3D tabletennis game
Summary(pl.UTF-8):	Trójwymiarowy tenis stołowy
Name:		csmash
Version:	0.6.6
Release:	3
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/cannonsmash/%{name}-%{version}.tar.gz
# Source0-md5:	bcf2eddd0f04d58e5dac6d767f41d9af
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-types.patch
URL:		http://CannonSmash.Sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
CannonSmash is a 3D tabletennis game. The goal of this project is to
represent various strategy of tabletennis on computer game.

%description -l pl.UTF-8
CannonSmash to trójwymiarowy tenis stołowy. Celem tego projektu jest
przedstawienie różnych strategii tenisa stołowego w grze komputerowej.

%prep
%setup -q
%patch0 -p1

%build
rm -f acinclude.m4
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake} -i
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README.en
%lang(ja) %doc README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/games/csmash
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
