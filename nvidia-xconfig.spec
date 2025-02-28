Name:           nvidia-xconfig
Version:        570.124.04
Release:        1%{?dist}
Summary:        NVIDIA X configuration file editor
Epoch:          3
License:        GPLv2+
URL:            http://www.nvidia.com/object/unix.html
ExclusiveArch:  x86_64 aarch64

Source0:        https://download.nvidia.com/XFree86/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  libpciaccess-devel
BuildRequires:  m4

Requires:       libnvidia-cfg%{?_isa} >= %{?epoch:%{epoch}:}%{version}
Requires:       xorg-x11-nvidia%{?_isa} >= %{?epoch:%{epoch}:}%{version}

%description
%{name} is a command line tool intended to provide basic control over
configuration options available in the NVIDIA X driver.

%prep
%autosetup -p1
# Remove additional CFLAGS added when enabling DEBUG
sed -i '/+= -O0 -g/d' utils.mk

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{?__global_ldflags}"
make %{?_smp_mflags} \
    DEBUG=1 \
    MANPAGE_GZIP=0 \
    NV_VERBOSE=1 \
    PREFIX=%{_prefix} \
    STRIP_CMD=true

%install
%make_install \
    MANPAGE_GZIP=0 \
    NV_VERBOSE=1 \
    PREFIX=%{_prefix} \
    STRIP_CMD=true

%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Feb 28 2025 Simone Caronni <negativo17@gmail.com> - 3:570.124.04-1
- Update to 570.124.04.

* Fri Jan 31 2025 Simone Caronni <negativo17@gmail.com> - 3:570.86.16-1
- Update to 570.86.16.

* Mon Jan 27 2025 Simone Caronni <negativo17@gmail.com> - 3:570.86.15-1
- Update to 570.86.15.

* Thu Dec 05 2024 Simone Caronni <negativo17@gmail.com> - 3:565.77-1
- Update to 565.77.

* Wed Oct 23 2024 Simone Caronni <negativo17@gmail.com> - 3:565.57.01-1
- Update to 565.57.01.

* Sun Sep 01 2024 Simone Caronni <negativo17@gmail.com> - 3:560.35.03-2
- Add requirement on xorg-x11-nvidia so package gets removed as well in case of
  uninstallation of X.org components.

* Wed Aug 21 2024 Simone Caronni <negativo17@gmail.com> - 3:560.35.03-1
- Update to 560.35.03.

* Tue Aug 06 2024 Simone Caronni <negativo17@gmail.com> - 3:560.31.02-1
- Update to 560.31.02.

* Mon Aug 05 2024 Simone Caronni <negativo17@gmail.com> - 3:560.28.03-1
- Update to 560.28.03.

* Tue Jul 02 2024 Simone Caronni <negativo17@gmail.com> - 3:555.58.02-1
- Update to 555.58.02.
- Require dynamically loaded library libnvidia-cfg.

* Thu Jun 27 2024 Simone Caronni <negativo17@gmail.com> - 3:555.58-1
- Update to 555.58.

* Thu Jun 06 2024 Simone Caronni <negativo17@gmail.com> - 3:555.52.04-1
- Update to 555.52.04.

* Wed May 22 2024 Simone Caronni <negativo17@gmail.com> - 3:555.42.02-1
- Update to 555.42.02.

* Tue Apr 30 2024 Simone Caronni <negativo17@gmail.com> - 3:550.78-2
- Switch to Nvidia provided tarball.

* Fri Apr 26 2024 Simone Caronni <negativo17@gmail.com> - 3:550.78-1
- Update to 550.78.

* Thu Apr 18 2024 Simone Caronni <negativo17@gmail.com> - 3:550.76-1
- Update to 550.76.

* Sun Mar 24 2024 Simone Caronni <negativo17@gmail.com> - 3:550.67-1
- Update to 550.67.

* Sat Mar 09 2024 Simone Caronni <negativo17@gmail.com> - 3:550.54.14-2
- Enable aarch64.

* Sun Mar 03 2024 Simone Caronni <negativo17@gmail.com> - 3:550.54.14-1
- Update to 550.54.14.

* Tue Feb 06 2024 Simone Caronni <negativo17@gmail.com> - 3:550.40.07-1
- Update to 550.40.07.
