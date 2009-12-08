#
# TODO:
# fix endless loop on ./configure
# add missing BRs
# make it build and add %files
#
%define     _subver b1
Summary:	XBMC
Name:		xbmc
Version:	9.11
Release:	0.%{_subver}.0.1
License:	GPL v3)
Group:		Applications/Multimedia
Source0:	http://downloads.sourceforge.net/project/xbmc/XBMC%20Source%20Code/pre-release/%{name}-%{version}-%{_subver}.tar.gz
# Source0-md5:	a5fa3c4e3ad5a17b91e444ff9a72986d
URL:		http://xbmc.org
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	avahi-devel
BuildRequires:	bzip2-devel
BuildRequires:	cmake
BuildRequires:	curl-devel
BuildRequires:	dbus-devel
BuildRequires:	enca-devel
BuildRequires:	faac-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	fribidi-devel
BuildRequires:	gawk
BuildRequires:	glew-devel
BuildRequires:	gperf
BuildRequires:	libcdio-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmad-devel
BuildRequires:	libmms-devel
BuildRequires:	libogg-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsmbclient-devel
BuildRequires:	libvorbis-devel
BuildRequires:	openssl-devel
BuildRequires:	openssl-devel
BuildRequires:	pulseaudio-devel
BuildRequires:	pulseaudio-devel
BuildRequires:	sqlite3-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXtst
BuildRequires:	xorg-proto-xineramaproto-devel
BuildRequires:	zip
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q -n %{name}-%{version}-%{_subver}

%build
./bootstrap
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO

%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
