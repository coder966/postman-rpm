Name:          postman
Version:       11.54.0
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


%global build_id 11.54.0


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
* Mon Jul 14 2025 RPM Bot <rpm-bot@coder966.net> - 11.54.0
- Update to 11.54.0

* Sat Jul 12 2025 RPM Bot <rpm-bot@coder966.net> - 11.53.5
- Update to 11.53.5

* Fri Jul 11 2025 RPM Bot <rpm-bot@coder966.net> - 11.53.4
- Update to 11.53.4

* Wed Jul 09 2025 RPM Bot <rpm-bot@coder966.net> - 11.53.0
- Update to 11.53.0

* Sat Jul 05 2025 RPM Bot <rpm-bot@coder966.net> - 11.52.5
- Update to 11.52.5

* Fri Jul 04 2025 RPM Bot <rpm-bot@coder966.net> - 11.52.4
- Update to 11.52.4

* Sat Jun 28 2025 RPM Bot <rpm-bot@coder966.net> - 11.51.5
- Update to 11.51.5

* Fri Jun 20 2025 RPM Bot <rpm-bot@coder966.net> - 11.50.5
- Update to 11.50.5

* Thu Jun 19 2025 RPM Bot <rpm-bot@coder966.net> - 11.50.2
- Update to 11.50.2

* Tue Jun 17 2025 RPM Bot <rpm-bot@coder966.net> - 11.50.1
- Update to 11.50.1

* Fri Jun 13 2025 RPM Bot <rpm-bot@coder966.net> - 11.49.4
- Update to 11.49.4

* Wed Jun 11 2025 RPM Bot <rpm-bot@coder966.net> - 11.49.1
- Update to 11.49.1

* Mon Jun 09 2025 RPM Bot <rpm-bot@coder966.net> - 11.49.0
- Update to 11.49.0

* Fri Jun 06 2025 RPM Bot <rpm-bot@coder966.net> - 11.48.5
- Update to 11.48.5

* Thu Jun 05 2025 RPM Bot <rpm-bot@coder966.net> - 11.48.4
- Update to 11.48.4

* Wed Jun 04 2025 RPM Bot <rpm-bot@coder966.net> - 11.48.2
- Update to 11.48.2

* Mon Jun 02 2025 RPM Bot <rpm-bot@coder966.net> - 11.48.0
- Update to 11.48.0

* Fri May 30 2025 RPM Bot <rpm-bot@coder966.net> - 11.47.4
- Update to 11.47.4

* Tue May 27 2025 RPM Bot <rpm-bot@coder966.net> - 11.47.1
- Update to 11.47.1

* Fri May 23 2025 RPM Bot <rpm-bot@coder966.net> - 11.46.6
- Update to 11.46.6

* Tue May 20 2025 RPM Bot <rpm-bot@coder966.net> - 11.46.2
- Update to 11.46.2

* Mon May 19 2025 RPM Bot <rpm-bot@coder966.net> - 11.46.1
- Update to 11.46.1

* Fri May 16 2025 RPM Bot <rpm-bot@coder966.net> - 11.45.6
- Update to 11.45.6

* Thu May 15 2025 RPM Bot <rpm-bot@coder966.net> - 11.45.3
- Update to 11.45.3

* Mon May 12 2025 RPM Bot <rpm-bot@coder966.net> - 11.45.0
- Update to 11.45.0

* Mon May 05 2025 RPM Bot <rpm-bot@coder966.net> - 11.44.0
- Update to 11.44.0

* Fri May 02 2025 RPM Bot <rpm-bot@coder966.net> - 11.43.4
- Update to 11.43.4

* Tue Apr 29 2025 RPM Bot <rpm-bot@coder966.net> - 11.43.2
- Update to 11.43.2

* Sat Apr 26 2025 RPM Bot <rpm-bot@coder966.net> - 11.42.5
- Update to 11.42.5

* Thu Apr 24 2025 RPM Bot <rpm-bot@coder966.net> - 11.42.4
- Update to 11.42.4

* Wed Apr 23 2025 RPM Bot <rpm-bot@coder966.net> - 11.42.3
- Update to 11.42.3

* Thu Apr 17 2025 RPM Bot <rpm-bot@coder966.net> - 11.41.4
- Update to 11.41.4

* Wed Apr 16 2025 RPM Bot <rpm-bot@coder966.net> - 11.41.2
- Update to 11.41.2

* Sat Apr 12 2025 RPM Bot <rpm-bot@coder966.net> - 11.40.6
- Update to 11.40.6

* Thu Apr 10 2025 RPM Bot <rpm-bot@coder966.net> - 11.40.4
- Update to 11.40.4

* Tue Apr 08 2025 RPM Bot <rpm-bot@coder966.net> - 11.40.1
- Update to 11.40.1

* Mon Apr 07 2025 RPM Bot <rpm-bot@coder966.net> - 11.40.0
- Update to 11.40.0

* Fri Apr 04 2025 RPM Bot <rpm-bot@coder966.net> - 11.39.5
- Update to 11.39.5

* Wed Apr 02 2025 RPM Bot <rpm-bot@coder966.net> - 11.39.2
- Update to 11.39.2

* Fri Mar 28 2025 RPM Bot <rpm-bot@coder966.net> - 11.38.5
- Update to 11.38.5

* Fri Mar 21 2025 RPM Bot <rpm-bot@coder966.net> - 11.37.5
- Update to 11.37.5

* Thu Mar 20 2025 RPM Bot <rpm-bot@coder966.net> - 11.37.3
- Update to 11.37.3

* Tue Mar 18 2025 RPM Bot <rpm-bot@coder966.net> - 11.37.1
- Update to 11.37.1

* Fri Mar 14 2025 RPM Bot <rpm-bot@coder966.net> - 11.36.6
- Update to 11.36.6

* Thu Mar 13 2025 RPM Bot <rpm-bot@coder966.net> - 11.36.3
- Update to 11.36.3

* Tue Mar 11 2025 RPM Bot <rpm-bot@coder966.net> - 11.36.1
- Update to 11.36.1

* Mon Mar 10 2025 RPM Bot <rpm-bot@coder966.net> - 11.36.0
- Update to 11.36.0

* Fri Mar 07 2025 RPM Bot <rpm-bot@coder966.net> - 11.35.4
- Update to 11.35.4

* Wed Mar 05 2025 RPM Bot <rpm-bot@coder966.net> - 11.35.2
- Update to 11.35.2

* Mon Mar 03 2025 RPM Bot <rpm-bot@coder966.net> - 11.35.0
- Update to 11.35.0

* Fri Feb 28 2025 RPM Bot <rpm-bot@coder966.net> - 11.34.5
- Update to 11.34.5

* Thu Feb 27 2025 RPM Bot <rpm-bot@coder966.net> - 11.34.4
- Update to 11.34.4

* Wed Feb 26 2025 RPM Bot <rpm-bot@coder966.net> - 11.34.3
- Update to 11.34.3

* Thu Feb 20 2025 RPM Bot <rpm-bot@coder966.net> - 11.33.4
- Update to 11.33.4

* Mon Feb 17 2025 RPM Bot <rpm-bot@coder966.net> - 11.33.0
- Update to 11.33.0

* Wed Feb 12 2025 RPM Bot <rpm-bot@coder966.net> - 11.32.2
- Update to 11.32.2

* Tue Feb 11 2025 RPM Bot <rpm-bot@coder966.net> - 11.32.1
- Update to 11.32.1

* Mon Feb 10 2025 RPM Bot <rpm-bot@coder966.net> - 11.31.4
- Update to 11.31.4

* Thu Feb 06 2025 RPM Bot <rpm-bot@coder966.net> - 11.31.3
- Update to 11.31.3

* Mon Feb 03 2025 RPM Bot <rpm-bot@coder966.net> - 11.31.0
- Update to 11.31.0

* Fri Jan 31 2025 RPM Bot <rpm-bot@coder966.net> - 11.30.4
- Update to 11.30.4

* Thu Jan 30 2025 RPM Bot <rpm-bot@coder966.net> - 11.30.3
- Update to 11.30.3

* Tue Jan 28 2025 RPM Bot <rpm-bot@coder966.net> - 11.30.1
- Update to 11.30.1

* Fri Jan 24 2025 RPM Bot <rpm-bot@coder966.net> - 11.29.5
- Update to 11.29.5

* Thu Jan 23 2025 RPM Bot <rpm-bot@coder966.net> - 11.29.3
- Update to 11.29.3

* Sat Jan 18 2025 RPM Bot <rpm-bot@coder966.net> - 11.28.4
- Update to 11.28.4

* Thu Jan 16 2025 RPM Bot <rpm-bot@coder966.net> - 11.28.3
- Update to 11.28.3

* Thu Jan 09 2025 RPM Bot <rpm-bot@coder966.net> - 11.27.3
- Update to 11.27.3

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
