from click.testing import CliRunner
from convertme.cli import main
import pytest

from pytest import fixture
import os


def test_help():
    runner = CliRunner()

    result = runner.invoke(main, ['--help'])
    assert result.exit_code == 0


TEST_PARAMETERS = "input_file, expected_file, input_format, output_format, input_delimiter, \
                          output_delimiter, objects_col, attributes_row, true_values, read_mode"

INDIRECT = ["input_file", "expected_file"]

PARAMETERS = [('csv1.csv', 'csv1.csv', 'csv', 'csv', None, None, None, None, None, 'r'),
              ('csv2.csv', 'csv1.csv', 'csv', 'csv',
               ';', None, None, None, None, 'r'),
              ('csv1.csv', 'csv2.csv', 'csv', 'csv',
               None, ';', None, None, None, 'r'),
              ('csv2.csv', 'csv2.csv', 'csv', 'csv',
               ';', ';', None, None, None, 'r'),
              ('csv3.csv', 'csv1.csv', 'csv', 'csv',
               None, None, None, 0, None, 'r'),
              ('csv4.csv', 'csv1.csv', 'csv', 'csv',
               None, None, 0, None, None, 'r'),
              ('csv5.csv', 'csv1.csv', 'csv', 'csv', None, None, 0, 0, None, 'r'),
              ('csv6.csv', 'csv1.csv', 'csv', 'csv',
               None, None, None, None, 'reznik_triska', 'r'),
              ('csv7.csv', 'csv1.csv', 'csv', 'csv', None,
               None, None, None, 'reznik_triska, neumi_dotu', 'r'),
              ('csv1.csv', 'fimi1.fimi', 'csv',
               'fimi', None, None, None, None, None, 'r'),
              ('csv1.csv', 'burmeister1.cxt', 'csv',
               'cxt', None, None, None, None, None, 'r'),
              ('mat1.mat', 'csv8.csv', 'mat', 'csv', None, None, None, None, None, 'rb'), ]


@pytest.fixture(scope="function")
def input_file(request):
    return os.path.join(os.path.dirname(
        os.path.realpath(__file__)), 'test_data/', request.param)


@pytest.fixture(scope="function")
def expected_file(request):
    return os.path.join(os.path.dirname(
        os.path.realpath(__file__)), 'test_data/', request.param)


def __append_args(args, input_delimiter, output_delimiter, true_values, attributes_row, objects_col):
    if input_delimiter is not None:
        args.append('--input-delimiter={}'.format(input_delimiter))

    if output_delimiter is not None:
        args.append('--output-delimiter={}'.format(output_delimiter))

    if true_values is not None:
        args.append('--true-values={}'.format(true_values))

    if attributes_row is not None:
        args.append('--attributes-row={}'.format(attributes_row))

    if objects_col is not None:
        args.append('--objects-col={}'.format(objects_col))

    return args


@pytest.mark.parametrize(TEST_PARAMETERS, PARAMETERS, indirect=INDIRECT)
def test_cli_files(input_file, expected_file, input_format, output_format,
                   input_delimiter, output_delimiter, objects_col, attributes_row,
                   true_values, read_mode):

    runner = CliRunner()

    with runner.isolated_filesystem():
        args = ['-i', input_file,
                '-o', 'out',
                '-if={}'.format(input_format),
                '-of={}'.format(output_format)]

        args = __append_args(args, input_delimiter, output_delimiter,
                             true_values, attributes_row, objects_col)

        result = runner.invoke(main, args)

        with open('out', 'r') as f:
            out_lines = f.readlines()

        with open(expected_file, 'r') as f:
            expected_lines = f.readlines()

        assert out_lines == expected_lines
        assert result.exit_code == 0


@pytest.mark.parametrize(TEST_PARAMETERS, PARAMETERS, indirect=INDIRECT)
def test_cli_stdin_stdout(input_file, expected_file, input_format, output_format,
                          input_delimiter, output_delimiter, objects_col, attributes_row,
                          true_values, read_mode):

    runner = CliRunner()

    with runner.isolated_filesystem():
        args = ['-if={}'.format(input_format),
                '-of={}'.format(output_format)]

        args = __append_args(args, input_delimiter, output_delimiter,
                             true_values, attributes_row, objects_col)

        with open(input_file, read_mode) as f:
            if read_mode is 'rb':
                input_string = f.read()
            else:
                input_string = ''.join(f.readlines())

        result = runner.invoke(main, args, input=input_string)

        with open(expected_file, 'r') as f:
            expected_lines = f.readlines()
            expected_output = ''.join(expected_lines)

        assert result.output == expected_output
        assert result.exit_code == 0


@pytest.mark.parametrize(TEST_PARAMETERS, PARAMETERS, indirect=INDIRECT)
def test_cli_stdin(input_file, expected_file, input_format, output_format,
                   input_delimiter, output_delimiter, objects_col, attributes_row,
                   true_values, read_mode):

    runner = CliRunner()

    with runner.isolated_filesystem():
        args = ['-o', 'out',
                '-if={}'.format(input_format),
                '-of={}'.format(output_format)]

        args = __append_args(args, input_delimiter, output_delimiter,
                             true_values, attributes_row, objects_col)

        with open(input_file, read_mode) as f:
            if read_mode is 'rb':
                input_string = f.read()
            else:
                input_string = ''.join(f.readlines())

        result = runner.invoke(main, args, input=input_string)

        with open(expected_file, 'r') as f:
            expected_lines = f.readlines()

        with open('out', 'r') as f:
            out_lines = f.readlines()

        assert expected_lines == out_lines
        assert result.exit_code == 0


@pytest.mark.parametrize(TEST_PARAMETERS, PARAMETERS, indirect=INDIRECT)
def test_cli_stdout(input_file, expected_file, input_format, output_format,
                    input_delimiter, output_delimiter, objects_col, attributes_row,
                    true_values, read_mode):

    runner = CliRunner()

    with runner.isolated_filesystem():
        args = ['-i', input_file,
                '-if={}'.format(input_format),
                '-of={}'.format(output_format)]

        args = __append_args(args, input_delimiter, output_delimiter,
                             true_values, attributes_row, objects_col)

        result = runner.invoke(main, args)

        with open(expected_file, 'r') as f:
            expected_lines = f.readlines()
            expected_output = ''.join(expected_lines)

        assert result.output == expected_output
        assert result.exit_code == 0
