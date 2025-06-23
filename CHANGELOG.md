# Changelog

## [1.19.3](https://github.com/snakemake/snakemake-interface-common/compare/v1.19.2...v1.19.3) (2025-06-23)


### Bug Fixes

* relax version checking by allowing non-semver compatible dev version suffixes ([#68](https://github.com/snakemake/snakemake-interface-common/issues/68)) ([91c340f](https://github.com/snakemake/snakemake-interface-common/commit/91c340f0dd2e98e91412370381a23ce23fd0d090))

## [1.19.2](https://github.com/snakemake/snakemake-interface-common/compare/v1.19.1...v1.19.2) (2025-06-23)


### Bug Fixes

* ensure backwards compatibility of type annotations ([#66](https://github.com/snakemake/snakemake-interface-common/issues/66)) ([6ae173d](https://github.com/snakemake/snakemake-interface-common/commit/6ae173d5b8078d25024174f03e6bde7689138011))

## [1.19.1](https://github.com/snakemake/snakemake-interface-common/compare/v1.19.0...v1.19.1) (2025-06-23)


### Bug Fixes

* fix type annotations for compatibility with older python versions ([#64](https://github.com/snakemake/snakemake-interface-common/issues/64)) ([0db57ec](https://github.com/snakemake/snakemake-interface-common/commit/0db57ec6f6e4931045fee4f4d2bff42432692267))

## [1.19.0](https://github.com/snakemake/snakemake-interface-common/compare/v1.18.0...v1.19.0) (2025-06-23)


### Features

* add function to check for minimum snakemake version ([#62](https://github.com/snakemake/snakemake-interface-common/issues/62)) ([7234583](https://github.com/snakemake/snakemake-interface-common/commit/72345832b0a54a0542751e0b363cb6e46e172e9d))

## [1.18.0](https://github.com/snakemake/snakemake-interface-common/compare/v1.17.4...v1.18.0) (2025-03-27)


### Features

* setup pixi, move to src layout, run ruff format once ([#58](https://github.com/snakemake/snakemake-interface-common/issues/58)) ([95d1d8d](https://github.com/snakemake/snakemake-interface-common/commit/95d1d8d0d8780305641eaeef2b58269dc710dcf7))

## [1.17.4](https://github.com/snakemake/snakemake-interface-common/compare/v1.17.3...v1.17.4) (2024-10-04)


### Bug Fixes

* do not check for exactly one plugin in registry tests ([#54](https://github.com/snakemake/snakemake-interface-common/issues/54)) ([755e64e](https://github.com/snakemake/snakemake-interface-common/commit/755e64eb182ffa97f23f3b77566703b61c346dea))
* return str placeholder in settings info if default value of setting is a callable ([#52](https://github.com/snakemake/snakemake-interface-common/issues/52)) ([0f26fe3](https://github.com/snakemake/snakemake-interface-common/commit/0f26fe3bbe9d72f909c19fd9b013bbb48b68c2f6))

## [1.17.3](https://github.com/snakemake/snakemake-interface-common/compare/v1.17.2...v1.17.3) (2024-08-14)


### Bug Fixes

* set CLI arg type to str if parse_func is provided ([#50](https://github.com/snakemake/snakemake-interface-common/issues/50)) ([aca9a5a](https://github.com/snakemake/snakemake-interface-common/commit/aca9a5ac3aa2837fcaecded588a1b6391dc2eeb1))


### Documentation

* insert space between original help message and suffix ([#48](https://github.com/snakemake/snakemake-interface-common/issues/48)) ([93e96ee](https://github.com/snakemake/snakemake-interface-common/commit/93e96eede3d66291e72ac3952a7c933f05b28e88))

## [1.17.2](https://github.com/snakemake/snakemake-interface-common/compare/v1.17.1...v1.17.2) (2024-04-11)


### Bug Fixes

* Add missing name field to InvalidPluginExceptions ([#46](https://github.com/snakemake/snakemake-interface-common/issues/46)) ([4f26d75](https://github.com/snakemake/snakemake-interface-common/commit/4f26d75da09bbad230a1e0f1b0c18fa5db90ca94))
* properly handle missing defaults in plugin settings ([f631c34](https://github.com/snakemake/snakemake-interface-common/commit/f631c34137e2bdd0cb5bfd4aaacd562804e5e15c))

## [1.17.1](https://github.com/snakemake/snakemake-interface-common/compare/v1.17.0...v1.17.1) (2024-02-21)


### Bug Fixes

* fix parsing and error handling for non-str plugin settings ([#43](https://github.com/snakemake/snakemake-interface-common/issues/43)) ([02084c2](https://github.com/snakemake/snakemake-interface-common/commit/02084c2e29a9c1d131eee1cef281973a7a405ec0))

## [1.17.0](https://github.com/snakemake/snakemake-interface-common/compare/v1.16.0...v1.17.0) (2024-02-19)


### Features

* add lutime and lchmod to utils ([6fa0cb5](https://github.com/snakemake/snakemake-interface-common/commit/6fa0cb5693109f5b9d466d843b84a0ef035d27ec))

## [1.16.0](https://github.com/snakemake/snakemake-interface-common/compare/v1.15.4...v1.16.0) (2024-02-15)


### Features

* add path to valid cli arg types ([3856d49](https://github.com/snakemake/snakemake-interface-common/commit/3856d49d49c15ed3dec35f1e9e385dd5d20a1587))

## [1.15.4](https://github.com/snakemake/snakemake-interface-common/compare/v1.15.3...v1.15.4) (2024-02-14)


### Bug Fixes

* do not try to consider bool settings as tagged. This fixes the error TypeError: 'bool' object is not iterable occurring with some plugins. ([49e47ac](https://github.com/snakemake/snakemake-interface-common/commit/49e47ac4352bde97816d08d88f0f9c66fdc64c49))

## [1.15.3](https://github.com/snakemake/snakemake-interface-common/compare/v1.15.2...v1.15.3) (2024-02-02)


### Bug Fixes

* print details of exception group errors ([6f8e289](https://github.com/snakemake/snakemake-interface-common/commit/6f8e2890a68198c67b5cbf2a17befce65931c6dd))

## [1.15.2](https://github.com/snakemake/snakemake-interface-common/compare/v1.15.1...v1.15.2) (2024-01-23)


### Bug Fixes

* better error message for missing plugin args ([d233f4f](https://github.com/snakemake/snakemake-interface-common/commit/d233f4fadd91a74829b45163f72a84debe9d77f8))
* properly handle tagged storage if only default settings are provided ([f59aa18](https://github.com/snakemake/snakemake-interface-common/commit/f59aa18c2dee0b16700bfb44a49ba33477e222fa))

## [1.15.1](https://github.com/snakemake/snakemake-interface-common/compare/v1.15.0...v1.15.1) (2024-01-15)


### Bug Fixes

* do not set metavar in case of boolean CLI args (aka flags) ([#35](https://github.com/snakemake/snakemake-interface-common/issues/35)) ([c0fb61a](https://github.com/snakemake/snakemake-interface-common/commit/c0fb61a7f3b74b5778e8da3d612d41afcc280a5c))

## [1.15.0](https://github.com/snakemake/snakemake-interface-common/compare/v1.14.5...v1.15.0) (2023-12-08)


### Features

* allow skipping of items when calling all method of SettingsEnumBase. ([01776e8](https://github.com/snakemake/snakemake-interface-common/commit/01776e8436249b93f9acc483e1adbcb279084166))


### Bug Fixes

* fix lints ([3d83d91](https://github.com/snakemake/snakemake-interface-common/commit/3d83d9187690f330dd4f050b311e215714ffd3fb))

## [1.14.5](https://github.com/snakemake/snakemake-interface-common/compare/v1.14.4...v1.14.5) (2023-12-06)


### Bug Fixes

* return envvar name in settings info ([68627b2](https://github.com/snakemake/snakemake-interface-common/commit/68627b2cce65d5b57b142cc7f3aebb9fdc7f0c42))

## [1.14.4](https://github.com/snakemake/snakemake-interface-common/compare/v1.14.3...v1.14.4) (2023-11-27)


### Bug Fixes

* return empty settings info if plugin does not have a settings class ([b59fbff](https://github.com/snakemake/snakemake-interface-common/commit/b59fbffc8555bd93bf0f616243a6423c763ee437))

## [1.14.3](https://github.com/snakemake/snakemake-interface-common/compare/v1.14.2...v1.14.3) (2023-11-17)


### Bug Fixes

* return empty TaggedSettings if plugin does not provide any settings but is taggable. ([ec6cc70](https://github.com/snakemake/snakemake-interface-common/commit/ec6cc709f85b56819e9a79f8f4c0c320433b4f03))

## [1.14.2](https://github.com/snakemake/snakemake-interface-common/compare/v1.14.1...v1.14.2) (2023-11-02)


### Bug Fixes

* fix bug in settings retrieval in the non-tagged case ([5b0ab9b](https://github.com/snakemake/snakemake-interface-common/commit/5b0ab9b3e6e8484288bb4a3fa59ccaaf0b57db91))

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
