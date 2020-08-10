import distutils.dir_util as dir_util
import filecmp
from collections import namedtuple
from pathlib import Path

import pytest

import projectdiffview.configuration as config
from projectdiffview import folder


@pytest.fixture
def data_folder():
    """Fixture shortcut to the test/data folder."""
    return Path(__file__).parent.joinpath("data")


def test_folder_version(data_folder):
    folder_path = data_folder.joinpath("template")
    assert folder.folder_version(folder_path) == "1.0"


def test_folder_version_no_meta_file(data_folder):
    assert folder.folder_version(data_folder) == "Unknown"


def test_recursively_compare_folders(data_folder):
    """Compare the template folder to the working folder and list out any differences.

    This will fail if the all three: common, working and template don't line up.

    Template should have 3 new items:  mechanical, new_template_file.txt and new_template_folder
    Working should have 3 new items: source_code.c, test and new_file.txt
    The rest should be common and `.keep` should be ignored.

    """

    CommonFile = namedtuple("CommonFile", ["template", "working"])

    template = data_folder.joinpath("template")
    working = data_folder.joinpath("working")
    configuration = config.Configuration()
    dir_cmp = filecmp.dircmp(template, working, ignore=configuration.ignored)
    common_files, template_only, working_only = folder.recursively_compare_folders(dir_cmp)

    assert common_files == [
        CommonFile(template.joinpath(".meta"), working.joinpath(".meta")),
        CommonFile(template.joinpath("README.md"), working.joinpath("README.md")),
        CommonFile(template.joinpath("hardware"), working.joinpath("hardware")),
        CommonFile(template.joinpath("software"), working.joinpath("software"),),
        CommonFile(template.joinpath("hardware/bom"), working.joinpath("hardware/bom"),),
        CommonFile(template.joinpath("hardware/pcb"), working.joinpath("hardware/pcb"),),
        CommonFile(
            template.joinpath("hardware/schematic"), working.joinpath("hardware/schematic"),
        ),
        CommonFile(
            template.joinpath("hardware/bom/project_rev_a.bom"),
            working.joinpath("hardware/bom/project_rev_a.bom"),
        ),
        CommonFile(
            template.joinpath("hardware/pcb/project_rev_a.pcb"),
            working.joinpath("hardware/pcb/project_rev_a.pcb"),
        ),
        CommonFile(
            template.joinpath("hardware/schematic/project_rev_a.prj"),
            working.joinpath("hardware/schematic/project_rev_a.prj"),
        ),
    ]

    template_only = [filename.name for filename in template_only]
    assert sorted(template_only) == sorted(
        ["mechanical", "new_template_file.txt", "new_template_folder",]
    )

    working_only = [filename.name for filename in working_only]
    assert sorted(working_only) == sorted(["source_code.c", "tests",])


def test_get_empty_folders(tmp_path, data_folder):
    """Detect empty folders in the working folder."""
    dir_util.copy_tree(
        str(data_folder.joinpath("working")), str(tmp_path), preserve_symlinks=True, update=True,
    )

    empty1 = tmp_path.joinpath("hardware/empty_folder")
    empty1.mkdir()
    empty2 = tmp_path.joinpath("hardware/bom/empty_folder")
    empty2.mkdir()

    assert folder.get_empty_folders(tmp_path) == [
        empty2,
        empty1,
    ]


def test_get_unchanged_files_no_change(data_folder):
    """Given a list of common files, see which ones have not been updated."""
    CommonFile = namedtuple("CommonFile", ["template", "working"])
    template = data_folder.joinpath("template")
    working = data_folder.joinpath("working")
    files = [
        CommonFile(template.joinpath(".meta"), working.joinpath(".meta")),
        CommonFile(template.joinpath("README.md"), working.joinpath("README.md")),
        CommonFile(template.joinpath("hardware"), working.joinpath("hardware")),
        CommonFile(template.joinpath("software"), working.joinpath("software"),),
        CommonFile(template.joinpath("hardware/bom"), working.joinpath("hardware/bom"),),
        CommonFile(template.joinpath("hardware/pcb"), working.joinpath("hardware/pcb"),),
        CommonFile(
            template.joinpath("hardware/schematic"), working.joinpath("hardware/schematic"),
        ),
        CommonFile(
            template.joinpath("hardware/bom/project_rev_a.bom"),
            working.joinpath("hardware/bom/project_rev_a.bom"),
        ),
        CommonFile(
            template.joinpath("hardware/pcb/project_rev_a.pcb"),
            working.joinpath("hardware/pcb/project_rev_a.pcb"),
        ),
        CommonFile(
            template.joinpath("hardware/schematic/project_rev_a.prj"),
            working.joinpath("hardware/schematic/project_rev_a.prj"),
        ),
    ]
    assert folder.get_unchanged_files(files) == [
        working.joinpath("hardware/bom/project_rev_a.bom"),
        working.joinpath("hardware/pcb/project_rev_a.pcb"),
        working.joinpath("hardware/schematic/project_rev_a.prj"),
    ]


def test_get_unchanged_files_updated_file(data_folder):
    """Repeat the previous test but in a folder that has updates."""
    CommonFile = namedtuple("CommonFile", ["template", "working"])
    template = data_folder.joinpath("template")
    working = data_folder.joinpath("working_with_updates")
    files = [
        CommonFile(template.joinpath(".meta"), working.joinpath(".meta")),
        CommonFile(template.joinpath("README.md"), working.joinpath("README.md")),
        CommonFile(template.joinpath("hardware"), working.joinpath("hardware")),
        CommonFile(template.joinpath("software"), working.joinpath("software"),),
        CommonFile(template.joinpath("hardware/bom"), working.joinpath("hardware/bom"),),
        CommonFile(template.joinpath("hardware/pcb"), working.joinpath("hardware/pcb"),),
        CommonFile(
            template.joinpath("hardware/schematic"), working.joinpath("hardware/schematic"),
        ),
        CommonFile(
            template.joinpath("hardware/bom/project_rev_a.bom"),
            working.joinpath("hardware/bom/project_rev_a.bom"),
        ),
        CommonFile(
            template.joinpath("hardware/pcb/project_rev_a.pcb"),
            working.joinpath("hardware/pcb/project_rev_a.pcb"),
        ),
        CommonFile(
            template.joinpath("hardware/schematic/project_rev_a.prj"),
            working.joinpath("hardware/schematic/project_rev_a.prj"),
        ),
    ]
    assert folder.get_unchanged_files(files) == [
        working.joinpath("hardware/pcb/project_rev_a.pcb"),
    ]
