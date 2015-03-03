import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('libraries_copy_from_dataset')
@options.galaxy_instance()
@click.argument("library_id", type=str)
@click.argument("dataset_id", type=str)

@click.option(
    "--folder_id",
    help="id of the folder where to place the uploaded files. If not provided, the root folder will be used",
    type=str
)
@click.option(
    "--message",
    help="message for copying action",
    type=str
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, library_id, dataset_id, folder_id="", message=""):
    """Copy a Galaxy dataset into a library.
    """
    return ctx.gi.libraries.copy_from_dataset(library_id, dataset_id, folder_id=folder_id, message=message)
