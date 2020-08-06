import pytest

from panoramic.cli.mapper import map_model_from_local, map_model_from_remote
from panoramic.cli.model.client import Model, ModelAttribute
from panoramic.cli.pano_model import PanoModel, PanoModelField


@pytest.fixture
def local_model_fixture():
    yield PanoModel(
        model_name='source_schema1_table',
        data_source='source.schema1.table',
        fields=[
            PanoModelField(uid='source.schema1.table1.id', data_type='str', data_reference='id', field_map=['id'],),
            PanoModelField(
                uid='source.schema1.table1.value', data_type='int', data_reference='value', field_map=['value'],
            ),
        ],
        joins=[],
        identifiers=[],
    )


@pytest.fixture
def remote_model_fixture():
    yield Model(
        name="source_schema1_table",
        fully_qualified_object_name="source.schema1.table",
        attributes=[
            ModelAttribute(
                uid="source.schema1.table1.id",
                column_data_type="str",
                taxon="source.schema1.table1.id",
                identifier=False,
                transformation="id",
            ),
            ModelAttribute(
                uid="source.schema1.table1.id",
                column_data_type="str",
                taxon="id",
                identifier=False,
                transformation="id",
            ),
            ModelAttribute(
                uid="source.schema1.table1.value",
                column_data_type="int",
                taxon="source.schema1.table1.value",
                identifier=False,
                transformation="value",
            ),
            ModelAttribute(
                uid="source.schema1.table1.value",
                column_data_type="int",
                taxon="value",
                identifier=False,
                transformation="value",
            ),
        ],
        joins=[],
        visibility='available',
    )


@pytest.fixture
def local_model_missing_uid_fixture():
    yield PanoModel(
        model_name='source_schema1_table',
        data_source='source.schema1.table',
        fields=[
            PanoModelField(uid='source.schema1.table1.id', data_type='str', data_reference='id', field_map=['id'],),
            PanoModelField(uid=None, data_type='int', data_reference='value', field_map=['value'],),
        ],
        joins=[],
        identifiers=[],
    )


@pytest.fixture
def remote_model_missing_uid_fixture():
    yield Model(
        name="source_schema1_table",
        fully_qualified_object_name="source.schema1.table",
        attributes=[
            ModelAttribute(
                uid="source.schema1.table1.id",
                column_data_type="str",
                taxon="source.schema1.table1.id",
                identifier=False,
                transformation="id",
            ),
            ModelAttribute(
                uid="source.schema1.table1.id",
                column_data_type="str",
                taxon="id",
                identifier=False,
                transformation="id",
            ),
            ModelAttribute(uid=None, column_data_type="int", taxon="value", identifier=False, transformation="value",),
        ],
        joins=[],
        visibility='available',
    )


def test_from_remote_to_local(remote_model_fixture, local_model_fixture):
    expected_local_model = local_model_fixture.to_dict()

    local_model = map_model_from_remote(remote_model_fixture)

    assert local_model.to_dict() == expected_local_model


def test_from_local_to_remote(local_model_fixture, remote_model_fixture):
    expected_remote_model = remote_model_fixture.to_dict()

    remote_model = map_model_from_local(local_model_fixture)

    assert remote_model.to_dict() == expected_remote_model


def test_from_remote_to_local_missing_uid(remote_model_missing_uid_fixture, local_model_missing_uid_fixture):
    expected_local_model = local_model_missing_uid_fixture.to_dict()

    local_model = map_model_from_remote(remote_model_missing_uid_fixture)

    assert local_model.to_dict() == expected_local_model


def test_from_local_to_remote_missing_uid(local_model_missing_uid_fixture, remote_model_missing_uid_fixture):
    expected_remote_model = remote_model_missing_uid_fixture.to_dict()

    remote_model = map_model_from_local(local_model_missing_uid_fixture)

    assert remote_model.to_dict() == expected_remote_model