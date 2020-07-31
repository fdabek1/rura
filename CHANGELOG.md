# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.2] - 2020-07-31
### Changed
- Tracker: starting and ending run still happens regardless of if logging or not.

## [0.2.1] - 2020-07-31
### Added
- Ability to read/write JSON files.

## [0.2.0] - 2020-07-04
### Changed
- Source dependencies will only get loaded when they will be used.
- Custom seed for patient split is supported.
- Local mlflow will log under appropriate experiment and run names rather than defaults.
- Simplified metrics computation. 
- Ability to evaluate model against test data.

## [0.1.0] - 2020-XX-XX
### Added
- Initial release.
