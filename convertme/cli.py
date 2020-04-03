"""Console script for convertme."""
import sys
import click
from convertme import CsvReader, CsvWriter, FimiReader, FimiWriter, BurmeisterReader, BurmeisterWriter, MatlabReader, MatlabWriter, CexReader, CexWriter


@click.command()
@click.option('-if', '--input-format',
              type=click.Choice(['csv', 'fimi', 'cxt', 'mat', 'cex'],
                                case_sensitive=False),
              required=True)
@click.option('-of', '--output-format',
              type=click.Choice(['csv', 'fimi', 'cxt', 'mat', 'cex'],
                                case_sensitive=False),
              required=True)
@click.option('-i', '--input', 'input_',
              #   type=click.File("r"),
              help="Input file, skip it for stdin.")
@click.option('-o', '--output', 'output_',
              #   type=click.File("w"),
              help="Output file, skip it for stdout.")
# Only for csv
@click.option('--input-delimiter',
              type=str, default=',', show_default=True,
              help="(CSV) Delimiter of input.")
@click.option('--output-delimiter',
              type=str, default=',', show_default=True,
              help="(CSV) Delimiter of output.")
@click.option('--objects-col',
              type=int,
              help="(CSV) Index of column with object labels, typically 0, ignored on default.")
@click.option('--attributes-row',
              type=int,
              help="(CSV) Index of row with attribute labels, typically 0, ignored on default.")
@click.option('--true-values',
              type=str,
              help="(CSV) Values which will be count as True, comma separated.")
def main(input_format, output_format, input_, output_, input_delimiter,
         output_delimiter, objects_col, attributes_row, true_values):
    BINARY_FORMATS = ['mat']

    # Fallback to stdin
    if input_ is None:
        input_ = '-'

    # Handle binary reading
    if input_format in BINARY_FORMATS:
        read_mode = 'rb'
    else:
        read_mode = 'r'

    input_ = click.open_file(input_, read_mode)

    # Fallback to stdout
    if output_ is None:
        output_ = '-'

    # Handle binary writing
    if output_format in BINARY_FORMATS:
        write_mode = 'wb'
    else:
        write_mode = 'w'

    output_ = click.open_file(output_, write_mode)

    # Init reader
    if input_format == 'csv':
        if true_values is not None:
            true_values = set([string.strip()
                               for string in true_values.split(',')])

        reader = CsvReader(delimiter=input_delimiter,
                           set_true_values=true_values,
                           objects_col=objects_col,
                           attributes_row=attributes_row)

    elif input_format == 'fimi':
        reader = FimiReader()
    elif input_format == 'cxt':
        reader = BurmeisterReader()
    elif input_format == 'mat':
        reader = MatlabReader()
    elif input_format == 'cex':
        reader = CexReader()

    # Init writer
    if output_format == 'csv':
        writer = CsvWriter(delimiter=output_delimiter)
    elif output_format == 'fimi':
        writer = FimiWriter()
    elif output_format == 'cxt':
        writer = BurmeisterWriter()
    elif output_format == 'mat':
        writer = MatlabWriter()
    elif output_format == 'cex':
        writer = CexWriter()

    # Do the work :)
    writer.write(reader.read(input_), output_)
