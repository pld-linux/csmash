Summary:	3D tabletennis game
Summary(pl):	Trójwymiarowy tenis stołowy
Name:		csmash
Version:	0.6.1
Release:	1
License:	GPL
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	http://prdownloads.SourceForge.net/CannonSmash/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://CannonSmash.Sourceforge.net/
BuildRequires:	OpenGL-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix		/usr/X11R6

%description
CannonSmash is a 3D tabletennis game. The goal of this project is to
represent various strategy of tabletennis on computer game.

%description -l pl
CannonSmash to trójwymiarowy tenis stołowy. Celem tego projektu jest
przedstawienie różnych strategii tenisa stołowego w grze komputerowej.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Games,%{_pixmapsdir}}

%{__make} install DESTDIR="$RPM_BUILD_ROOT"
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf AUTHORS CREDITS ChangeLog NEWS README README.en

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS* CREDITS* ChangeLog* NEWS* TODO* README.en*
%lang(jp) %doc README.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/csmash
%{_applnkdir}/Games/*
%{_pixmapsdir}/*
