from unittest.mock import ANY, call, patch

import pytest

from panoramic.cli.command import scan


@pytest.fixture
def mock_refresher():
    with patch('panoramic.cli.command.Refresher') as mock_scanner:
        yield mock_scanner()


@pytest.fixture
def mock_scanner():
    with patch('panoramic.cli.command.Scanner') as mock_scanner:
        yield mock_scanner()


@patch('panoramic.cli.command.write')
def test_scan(mock_write, mock_scanner, mock_refresher):
    mock_scanner.scan_tables.return_value = [{'table_schema': 'source.schema1', 'table_name': 'table1'}]
    mock_scanner.scan_columns.return_value = [
        {'table_schema': 'schema1', 'table_name': 'table1', 'column_name': 'id'},
        {'table_schema': 'schema1', 'table_name': 'table1', 'column_name': 'value'},
    ]

    scan('test-source', 'test-filter')

    assert mock_refresher.refresh_table.mock_calls == [call('schema1.table1')]
    assert mock_write.mock_calls == [call(ANY)]


@patch('panoramic.cli.command.write')
def test_scan_single_table_error(mock_write, mock_scanner, mock_refresher):
    mock_scanner.scan_tables.return_value = [{'table_schema': 'source.schema1', 'table_name': 'table1'}]
    mock_scanner.scan_columns.return_value = [
        {'table_schema': 'schema1', 'table_name': 'table1', 'column_name': 'id'},
        {'table_schema': 'schema1', 'table_name': 'table1', 'column_name': 'value'},
    ]
    mock_refresher.refresh_table.side_effect == [Exception('test'), None]

    scan('test-source', 'test-filter')

    assert mock_write.mock_calls == [call(ANY)]
