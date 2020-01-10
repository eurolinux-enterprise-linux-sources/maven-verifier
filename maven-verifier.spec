Name:           maven-verifier
Version:        1.4
Release:        6%{?dist}
Summary:        Maven verifier
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-verifier
Source0:        http://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
# Forwarded upstream, see MSHARED-284
Patch1:         0001-Update-to-maven-shared-utils-0.3.patch

BuildArch:      noarch

BuildRequires:  java-devel
BuildRequires:  maven-local
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-shared-utils

Obsoletes:      maven-shared-verifier < %{version}-%{release}
Provides:       maven-shared-verifier = %{version}-%{release}

%description
Provides a test harness for Maven integration tests.

This is a replacement package for maven-shared-verifier

%package javadoc
Group:          Documentation
Summary:        Javadoc for %{name}
    
%description javadoc
API documentation for %{name}.


%prep
%setup -q
%patch1 -p1

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE


%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.4-6
- Mass rebuild 2013-12-27

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-5
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Fri Apr 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-4
- Update to maven-shared-utils 0.3

* Fri Feb 08 2013 Tomas Radej <tradej@redhat.com> - 1.4-3
- Building the new way

* Thu Jan 24 2013 Tomas Radej <tradej@redhat.com> - 1.4-2
- Added BuildRequires on maven-shared-utils

* Wed Jan 16 2013 Tomas Radej <tradej@redhat.com> - 1.4-1
- Initial version

