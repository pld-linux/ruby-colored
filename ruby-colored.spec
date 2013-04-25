#
# Conditional build:
%bcond_without	tests		# build without tests

%define	gem_name colored
Summary:	Extends ruby string class in order to colorize terminal output
Name:		ruby-%{gem_name}
Version:	1.2
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Source0-md5:	1b1a0f16f7c6ab57d1a2d6de53b13c42
URL:		http://github.com/defunkt/colored
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-minitest
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rubygem extending the ruby string class to include methods that
generates colored terminal output.

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
Documentation for %{name}

%prep
%setup -q -n %{gem_name}-%{version}

%build
%if %{with tests}
testrb -Ilib test/colored_test.rb
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE
%{ruby_vendorlibdir}/colored.rb
