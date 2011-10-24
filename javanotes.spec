Name:       javanotes
Version:    5.1
Release:    4
Summary:    Introduction to Programming Using Java, By David J. Eck

Group:      Development/Java
License:    CC-BY-SA
URL:        http://math.hws.edu/javanotes/
Source0:    http://math.hws.edu/eck/cs124/downloads/%{name}5.tar.bz2
BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:  noarch

%description
The fifth edition of Introduction to Programming Using Java, a free, on-line
textbook on introductory programming, which uses Java as the language of
instruction. This book is directed mainly towards beginning programmers,
although it might also be useful for experienced programmers who want to learn
something about Java. It is certainly not meant to provide complete coverage of
the Java language.

The fifth edition covers Java 5.0 and can also be used with later versions of
Java. You will find many Java applets on the web pages that make up this book,
and many of those applets require Java 5.0 or higher to function. Earlier
editions, which covered earlier versions of Java, are still available; see the
preface for links.

This is the html version, start with index.html in the main directory.

%prep
%setup -q -n %{name}%{version}

%build
# empty but exists to keep rpmlint happy


%install
rm -rf $RPM_BUILD_ROOT
find -type d -exec install -m 755 -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/{} ';'
find -type f -exec install -m 644 {} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/{} ';'

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}-%{version}/


