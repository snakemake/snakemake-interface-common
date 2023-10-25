# Changelog

## [1.14.1](https://github.com/snakemake/snakemake-interface-common/compare/v1.14.0...v1.14.1) (2023-10-25)


### Bug Fixes

* improved settings and envvar handling ([0c6eb7d](https://github.com/snakemake/snakemake-interface-common/commit/0c6eb7dfd04776514022471db6ababa43a495122))

## [1.14.0](https://github.com/snakemake/snakemake-interface-common/compare/v1.13.0...v1.14.0) (2023-10-14)


### Features

* add method get_plugin_package_name ([db6ae92](https://github.com/snakemake/snakemake-interface-common/commit/db6ae92f62cc9cbfe8f2bdbb25a6c78dd63824d4))
* add package_name property ([6491cd2](https://github.com/snakemake/snakemake-interface-common/commit/6491cd2266853fe263569b9a931690fc2e0513af))

## [1.13.0](https://github.com/snakemake/snakemake-interface-common/compare/v1.12.0...v1.13.0) (2023-10-13)


### Features

* add is_installed for checking whether a plugin is installed ([cf6f3ab](https://github.com/snakemake/snakemake-interface-common/commit/cf6f3ab5b2104289792228fbb671ffeffaffa31e))
* make collect_plugins public ([ca77b28](https://github.com/snakemake/snakemake-interface-common/commit/ca77b28e88344e010941e3b48090c39462896b6d))

## [1.12.0](https://github.com/snakemake/snakemake-interface-common/compare/v1.11.0...v1.12.0) (2023-10-11)


### Features

* add abstract method for returning example args in test suite ([e84b5cb](https://github.com/snakemake/snakemake-interface-common/commit/e84b5cb1a82c39bc1f004fd00854ee9e290ab40b))

## [1.11.0](https://github.com/snakemake/snakemake-interface-common/compare/v1.10.0...v1.11.0) (2023-10-11)


### Features

* add functionality for converting settings into arguments ([48687f9](https://github.com/snakemake/snakemake-interface-common/commit/48687f99dc5de81679af99134a07e82926fe0393))


### Bug Fixes

* fix handling of plugin settings names ([8007ab4](https://github.com/snakemake/snakemake-interface-common/commit/8007ab46dfdc152630be42c8247aec093033af3c))
* improved handling of tagged settings ([8653e82](https://github.com/snakemake/snakemake-interface-common/commit/8653e824b700247b212f433f8d4aa8d7ad0ecbb8))
* kwargs undefined, likely needs to be kwargs_all ([#25](https://github.com/snakemake/snakemake-interface-common/issues/25)) ([372fb10](https://github.com/snakemake/snakemake-interface-common/commit/372fb106b7985297d8f0d765e690d4d7d2710127))

## [1.10.0](https://github.com/snakemake/snakemake-interface-common/compare/v1.9.2...v1.10.0) (2023-09-27)


### Features

* add method to get registered plugins ([a630f9a](https://github.com/snakemake/snakemake-interface-common/commit/a630f9a1f1fd2a47c8b500523039a6261fc4dae4))


### Bug Fixes

* use hyphen for plugin names ([67797bd](https://github.com/snakemake/snakemake-interface-common/commit/67797bd6a85a589a08931abe37df6f0e45b1bae3))

## [1.9.2](https://github.com/snakemake/snakemake-interface-common/compare/v1.9.1...v1.9.2) (2023-09-26)


### Bug Fixes

* various fixes ([5f0636f](https://github.com/snakemake/snakemake-interface-common/commit/5f0636f16148fc8f4078a53079be1ddc66f44d69))

## [1.9.1](https://github.com/snakemake/snakemake-interface-common/compare/v1.9.0...v1.9.1) (2023-09-26)


### Bug Fixes

* fix TaggedSettings ([44eb317](https://github.com/snakemake/snakemake-interface-common/commit/44eb317e1efa57238818435abc3bcb901b1efcb8))

## [1.9.0](https://github.com/snakemake/snakemake-interface-common/compare/v1.8.0...v1.9.0) (2023-09-26)


### Features

* implemented support for tagged plugin settings ([57bf443](https://github.com/snakemake/snakemake-interface-common/commit/57bf443786c2a94c1eb4c409139e7f86f94c8eae))


### Bug Fixes

* improved error handling for tagged settings ([02c67b3](https://github.com/snakemake/snakemake-interface-common/commit/02c67b3015819ae030fc265fa1e6a8e6ba40e052))

## [1.8.0](https://github.com/snakemake/snakemake-interface-common/compare/v1.7.3...v1.8.0) (2023-09-22)


### Features

* support specification of parse_func in settings field metadata. ([ac3dcb7](https://github.com/snakemake/snakemake-interface-common/commit/ac3dcb7cc46413077d80c428b328ac8e6eb90454))

## [1.7.3](https://github.com/snakemake/snakemake-interface-common/compare/v1.7.2...v1.7.3) (2023-09-22)


### Bug Fixes

* plugin retrieval ([5a92361](https://github.com/snakemake/snakemake-interface-common/commit/5a92361e8d0fed0479ff372d6287453418c42886))

## [1.7.2](https://github.com/snakemake/snakemake-interface-common/compare/v1.7.1...v1.7.2) (2023-09-22)


### Bug Fixes

* add type annotation ([aadc36a](https://github.com/snakemake/snakemake-interface-common/commit/aadc36aa78a4e4c414cabfb52c335334ad851047))
* avoid instantiation of base class by pytest ([bd2d094](https://github.com/snakemake/snakemake-interface-common/commit/bd2d0948021e16bc1ddd4995bc44c894dac12b71))

## [1.7.1](https://github.com/snakemake/snakemake-interface-common/compare/v1.7.0...v1.7.1) (2023-09-21)


### Bug Fixes

* fix base class name ([fc6fab7](https://github.com/snakemake/snakemake-interface-common/commit/fc6fab7fa8224baff17f520d5b2d7a22dca422a5))

## [1.7.0](https://github.com/snakemake/snakemake-interface-common/compare/v1.6.0...v1.7.0) (2023-09-21)


### Features

* add test suite for plugin registries ([36f5b13](https://github.com/snakemake/snakemake-interface-common/commit/36f5b133286ede83c95de1f5238b026fcdef2136))

## [1.6.0](https://github.com/snakemake/snakemake-interface-common/compare/v1.5.0...v1.6.0) (2023-09-21)


### Features

* add helper to retrieve logger singleton ([4cd69e8](https://github.com/snakemake/snakemake-interface-common/commit/4cd69e8521ac8f77c18d4287f5c7025f2aff7d73))

## [1.5.0](https://github.com/snakemake/snakemake-interface-common/compare/v1.4.3...v1.5.0) (2023-09-21)


### Features

* add utils ([34ad602](https://github.com/snakemake/snakemake-interface-common/commit/34ad602bdbeb55f3ba961376365f963dbf25ab77))

## [1.4.3](https://github.com/snakemake/snakemake-interface-common/compare/v1.4.2...v1.4.3) (2023-09-21)


### Bug Fixes

* compatibility with Python 3.7 ([4eb555d](https://github.com/snakemake/snakemake-interface-common/commit/4eb555d30bdb5f20eec3d9d0147639a0b30fbc12))

## [1.4.2](https://github.com/snakemake/snakemake-interface-common/compare/v1.4.1...v1.4.2) (2023-09-21)


### Bug Fixes

* avoid too agressive imports in order to maintain compatibility with older scripts ([4c803d9](https://github.com/snakemake/snakemake-interface-common/commit/4c803d9b0f07feb53eda6faf4786c2b7ec48cc9f))

## [1.4.1](https://github.com/snakemake/snakemake-interface-common/compare/v1.4.0...v1.4.1) (2023-09-19)


### Bug Fixes

* fixed typo in method name ([a3a1f9a](https://github.com/snakemake/snakemake-interface-common/commit/a3a1f9a88b9a0ea72f160aa3a381c18bfc205773))

## [1.4.0](https://github.com/snakemake/snakemake-interface-common/compare/v1.3.3...v1.4.0) (2023-09-19)


### Features

* add generic plugin registry ([#9](https://github.com/snakemake/snakemake-interface-common/issues/9)) ([8fb3349](https://github.com/snakemake/snakemake-interface-common/commit/8fb3349130f4338293c38db7be55695ad5b742d6))


### Bug Fixes

* fix typo in method name when calling _get_spec ([253e984](https://github.com/snakemake/snakemake-interface-common/commit/253e984e6dfd3788bfbf5e2759831d20e98a53d8))

## [1.3.3](https://github.com/snakemake/snakemake-interface-common/compare/v1.3.2...v1.3.3) (2023-09-10)


### Bug Fixes

* improved exception messages ([c4254c0](https://github.com/snakemake/snakemake-interface-common/commit/c4254c04c00e066a9676ad14af9b1a21cd338712))

## [1.3.2](https://github.com/snakemake/snakemake-interface-common/compare/v1.3.1...v1.3.2) (2023-08-28)


### Bug Fixes

* return frozenset from SettingsEnumBase.all() ([a6e20d8](https://github.com/snakemake/snakemake-interface-common/commit/a6e20d8a8677f10c57b4c990c272c61714bccbd4))

## [1.3.1](https://github.com/snakemake/snakemake-interface-common/compare/v1.3.0...v1.3.1) (2023-08-28)


### Bug Fixes

* ensure Python 3.7 compatibility ([6597b9c](https://github.com/snakemake/snakemake-interface-common/commit/6597b9c42a8c09608bd32741fd7615128190a51a))

## [1.3.0](https://github.com/snakemake/snakemake-interface-common/compare/v1.2.0...v1.3.0) (2023-08-25)


### Features

* improve SettingsEnumBase API ([40e9579](https://github.com/snakemake/snakemake-interface-common/commit/40e95792ddf67d16ee49339a09d98e20df961e04))


### Bug Fixes

* fixed settingsEnumBase class ([f8d9edc](https://github.com/snakemake/snakemake-interface-common/commit/f8d9edc0b0aa503e9cb889d28003cfb01528e273))

## [1.2.0](https://github.com/snakemake/snakemake-interface-common/compare/v1.1.0...v1.2.0) (2023-08-25)


### Features

* added SettingsEnumBase ([7e63a01](https://github.com/snakemake/snakemake-interface-common/commit/7e63a01cac77111cdd8e23ccadbcb92812da7efa))

## [1.1.0](https://github.com/snakemake/snakemake-interface-common/compare/v1.0.0...v1.1.0) (2023-08-25)


### Features

* add RuleInterface ([2c89e9b](https://github.com/snakemake/snakemake-interface-common/commit/2c89e9bc5f6e286690e11559e7af5fdbda5be94c))

## 1.0.0 (2023-08-25)


### Miscellaneous Chores

* release 1.0.0 ([89c43d0](https://github.com/snakemake/snakemake-interface-common/commit/89c43d08dc03dc82a77f4b5eb80da24a9fb3a933))
