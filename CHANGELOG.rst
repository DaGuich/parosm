Changelog
=========
All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <http://keepachangelog.com/en/1.0.0/>`
and this project adheres to `Semantic Versioning <http://semver.org/spec/v2.0.0.html>`.

[Unreleased]
------------
Added:

-

Changed:

-

Deprecated:

-

Removed:

-

Fixed:

-

Security:

-


[0.2] - 2018-04-22
------------
Added:

- MultiParser as parser for all of the two file types
- Make importing of all "public" classes easier
- Testing

Changed:

- Use MultiParser in osminfo
- Coordinate assignment does not throw TypeError but ValueError

Deprecated:

-

Removed:

- --xml and --pbf arguments of osminfo

Fixed:

-

Security:

-


[0.1] - 2018-04-05
------------
Added:

- OpenStreetMap Basic Types
- License: GPL Version 3
- OSM-XML Parser
- OSM-PBF Parser
- osminfo

Changed:

- usage of defusedxml
