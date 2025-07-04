from snakemake_interface_common import at_least_snakemake_version


def test_snakemake_version():
    assert at_least_snakemake_version("8.1.0")
    assert not at_least_snakemake_version("100.0.0")
