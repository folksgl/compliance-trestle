# -*- mode:python; coding:utf-8 -*-

# Copyright (c) 2021 IBM Corp. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for the drawio model."""

import pathlib

import pytest

from trestle.core.draw_io import DrawIO
from trestle.core.markdown_validator import MarkdownValidator


def test_directory_instead_file() -> None:
    """Test that exceptions are raised on a bad file."""
    pass


def test_missing_file() -> None:
    """Test that exceptions are raised on a missing file."""
    pass


@pytest.mark.parametrize(
    'file_path, metadata_exists, metadata_valid',
    [
        (pathlib.Path('tests/data/drawio/single_tab_bad_metadata_extra_fields_compressed.drawio'), True, False),
        (pathlib.Path('tests/data/drawio/single_tab_bad_metadata_missing_fields_compressed.drawio'), True, False),
        (pathlib.Path('tests/data/drawio/single_tab_metadata_compressed.drawio'), True, True),
        (pathlib.Path('tests/data/drawio/single_tab_no_metadata_compressed.drawio'), False, False),
        (pathlib.Path('tests/data/drawio/single_tab_no_metadata_uncompressed.drawio'), False, False),
        (pathlib.Path('tests/data/drawio/two_tabs_metadata_compressed.drawio'), True, True),
        (pathlib.Path('tests/data/drawio/two_tabs_metadata_second_tab_compressed.drawio'), True, False)
    ]
)
def test_valid_drawio(file_path: pathlib.Path, metadata_exists: bool, metadata_valid: bool) -> None:
    """Run various scenarios with a valid drawio and various metadata status."""
    expected_metadata_flat = {
        'test': 'value', 'nested.test': 'value', 'nested.nested.test': 'value', 'nested.extra': 'value'
    }
    draw_io = DrawIO(file_path)
    metadata = draw_io.get_metadata()
    md = False
    for tab_md in metadata:
        if not tab_md == {}:
            md = True
    assert metadata_exists == md
    md_first = metadata[0]
    val_status = MarkdownValidator.compare_keys(expected_metadata_flat, md_first)
    assert val_status == metadata_valid


@pytest.mark.parametrize('bad_file_name', [pathlib.Path('')])
def test_bad_drawio_files(bad_file_name: pathlib.Path) -> None:
    """This tests that exceptions are properly thrown on bad drawio files."""
    pass
