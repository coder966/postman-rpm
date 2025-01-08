Name:          postman
Version:       11.27.1
Release:       1%{?dist}
Summary:       Postman
License:       Apache 2.0
URL:           https://www.postman.com/
Packager:      Khalid Alharisi <coder966@gmail.com>


Source0:       https://dl.pstmn.io/download/latest/linux_64
Source1:       https://raw.githubusercontent.com/coder966/postman-rpm/master/postman.desktop


BuildRequires: desktop-file-utils
AutoReqProv: no

%define __brp_check_rpaths %{nil}
%define debug_package %{nil}
%global __strip /bin/true
%global __jar_repack %{nil}


%global build_id 11.27.1


%description
Postman




%prep


# Postman/app is the dir inside the tar
%setup -q -n Postman/app


%build



%install


mkdir -p %{buildroot}/opt/%{name}
cp -a * %{buildroot}/opt/%{name}

install -pDm644 icons/icon_128x128.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}




%files
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%dir /opt/%{name}
/opt/%{name}/*




%changelog
* Wed Jan 08 2025 RPM Bot <rpm-bot@coder966.net> - 11.27.1
- Update to 11.27.1

* Thu Dec 19 2024 RPM Bot <rpm-bot@coder966.net> - 11.23.3
- Update to 11.23.3

* Tue Dec 17 2024 RPM Bot <rpm-bot@coder966.net> - 11.23.1
- Update to 11.23.1

* Fri Dec 06 2024 RPM Bot <rpm-bot@coder966.net> - 11.22.0
- Update to 11.22.0

* Tue Nov 26 2024 RPM Bot <rpm-bot@coder966.net> - 11.21.0
- Update to 11.21.0

* Mon Nov 18 2024 RPM Bot <rpm-bot@coder966.net> - 11.20.0
- Update to 11.20.0

* Fri Nov 08 2024 RPM Bot <rpm-bot@coder966.net> - 11.19.0
- Update to 11.19.0

* Wed Oct 23 2024 RPM Bot <rpm-bot@coder966.net> - 11.18.0
- Update to 11.18.0

* Tue Oct 15 2024 RPM Bot <rpm-bot@coder966.net> - 11.17.0
- Update to 11.17.0

* Wed Oct 09 2024 RPM Bot <rpm-bot@coder966.net> - 11.16.0
- Update to 11.16.0

* Tue Oct 01 2024 RPM Bot <rpm-bot@coder966.net> - 11.15.0
- Update to 11.15.0

* Wed Sep 25 2024 RPM Bot <rpm-bot@coder966.net> - 11.14.0
- Update to 11.14.0

* Thu Sep 19 2024 RPM Bot <rpm-bot@coder966.net> - 11.13.0
- Update to 11.13.0

* Wed Sep 11 2024 RPM Bot <rpm-bot@coder966.net> - 11.12.0
- Update to 11.12.0

* Wed Sep 04 2024 RPM Bot <rpm-bot@coder966.net> - 11.11.0
- Update to 11.11.0

* Tue Aug 27 2024 RPM Bot <rpm-bot@coder966.net> - 11.10.0
- Update to 11.10.0

* Fri Aug 23 2024 RPM Bot <rpm-bot@coder966.net> - 11.9.0
- Update to 11.9.0

* Wed Aug 14 2024 RPM Bot <rpm-bot@coder966.net> - 11.8.0
- Update to 11.8.0

* Wed Aug 07 2024 RPM Bot <rpm-bot@coder966.net> - 11.7.0
- Update to 11.7.0

* Wed Jul 31 2024 RPM Bot <rpm-bot@coder966.net> - 11.6.1
- Update to 11.6.1

* Wed Jul 24 2024 RPM Bot <rpm-bot@coder966.net> - 11.5.0
- Update to 11.5.0

* Wed Jul 17 2024 RPM Bot <rpm-bot@coder966.net> - 11.4.0
- Update to 11.4.0

* Fri Jul 12 2024 RPM Bot <rpm-bot@coder966.net> - 11.3.2
- Update to 11.3.2

* Wed Jul 10 2024 RPM Bot <rpm-bot@coder966.net> - 11.3.0
- Update to 11.3.0

* Tue Jun 11 2024 RPM Bot <rpm-bot@coder966.net> - 11.2.0
- Update to 11.2.0

* Wed May 22 2024 RPM Bot <rpm-bot@coder966.net> - 11.1.14
- Update to 11.1.14

* Mon May 13 2024 RPM Bot <rpm-bot@coder966.net> - 11.1.0
- Update to 11.1.0

* Fri May 10 2024 RPM Bot <rpm-bot@coder966.net> - 11.0.12
- Update to 11.0.12

* Tue May 07 2024 RPM Bot <rpm-bot@coder966.net> - 11.0.7
- Update to 11.0.7

* Thu May 02 2024 RPM Bot <rpm-bot@coder966.net> - 11.0.4
- Update to 11.0.4

* Thu Apr 04 2024 RPM Bot <rpm-bot@coder966.net> - 10.24.16
- Update to 10.24.16

* Fri Mar 15 2024 RPM Bot <rpm-bot@coder966.net> - 10.24.3
- Update to 10.24.3

* Mon Mar 11 2024 RPM Bot <rpm-bot@coder966.net> - 10.24.0
- Update to 10.24.0

* Tue Mar 05 2024 RPM Bot <rpm-bot@coder966.net> - 10.23.9
- Update to 10.23.9

* Wed Feb 21 2024 RPM Bot <rpm-bot@coder966.net> - 10.23.5
- Update to 10.23.5

* Mon Feb 12 2024 RPM Bot <rpm-bot@coder966.net> - 10.23.0
- Update to 10.23.0

* Fri Jan 12 2024 RPM Bot <rpm-bot@coder966.net> - 10.22.0
- Update to 10.22.0

* Fri Dec 15 2023 RPM Bot <rpm-bot@coder966.net> - 10.21.0
- Update to 10.21.0

* Thu Nov 09 2023 RPM Bot <rpm-bot@coder966.net> - 10.20.0
- Update to 10.20.0

* Sat Oct 21 2023 RPM Bot <rpm-bot@coder966.net> - 10.19.7
- Update to 10.19.7

* Fri Oct 13 2023 RPM Bot <rpm-bot@coder966.net> - 10.19.0
- Update to 10.19.0

* Tue Oct 03 2023 RPM Bot <rpm-bot@coder966.net> - 10.18.10
- Update to 10.18.10

* Mon Sep 25 2023 RPM Bot <rpm-bot@coder966.net> - 10.18.7
- Update to 10.18.7

* Sat Sep 23 2023 RPM Bot <rpm-bot@coder966.net> - 10.18.6
- Update to 10.18.6

* Wed Sep 20 2023 RPM Bot <rpm-bot@coder966.net> - 10.18.4
- Update to 10.18.4

* Tue Sep 19 2023 RPM Bot <rpm-bot@coder966.net> - 10.18.3
- Update to 10.18.3

* Sat Sep 16 2023 RPM Bot <rpm-bot@coder966.net> - 10.18.2
- Update to 10.18.2

* Fri Sep 15 2023 RPM Bot <rpm-bot@coder966.net> - 10.18.1
- Update to 10.18.1

* Wed Sep 13 2023 RPM Bot <rpm-bot@coder966.net> - 10.17.4
- Update to 10.17.4

* Tue Sep 12 2023 RPM Bot <rpm-bot@coder966.net> - 10.18.0
- Update to 10.18.0

* Fri Aug 25 2023 RPM Bot <rpm-bot@coder966.net> - 10.17.4
- Update to 10.17.4

* Tue Aug 22 2023 RPM Bot <rpm-bot@coder966.net> - 10.17.3
- Update to 10.17.3


* Tue Aug 18 2023 coder966 <coder966@gmail.com> - 10.17.0
- Initial Release
