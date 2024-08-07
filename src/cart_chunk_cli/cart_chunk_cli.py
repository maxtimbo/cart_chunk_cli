import click
import shutil
from pathlib import Path

from cart_chunk import CartChunk, NewCart


class VerbosePrint:
    def __init__(self, verbose: bool):
        self.verbose = verbose

    def vprint(self, msg: str):
        if self.verbose:
            click.echo(msg)

@click.command()
@click.option('-v', '--verbose', is_flag=True, help='enable verbose mode')
@click.option('--from_filename', is_flag=True, help='get cat/cart from filename')
@click.option('--cat', help="set category")
@click.option('--cart', help="set cart")
@click.option('--artist', help="set artist")
@click.option('--title', help="set title")
@click.argument('filename')
def cli(filename,
        verbose,
        from_filename,
        cat,
        cart,
        artist,
        title):
    msg = VerbosePrint(verbose)

    ffile = Path(filename).resolve()
    copy = Path(ffile.parent, ffile.name + "_COPY")

    wav = CartChunk(ffile)

    new_wav = NewCart(copy)

    tags = []

    if from_filename:
        ffonly = ffile.stem
        lengths = [3, 4]
        results = []
        start = 0
        for size in lengths:
            results.append(ffonly[start : start + size])
            start += size

        tags.append(("cat", results[0]))
        new_wav.category = results[0]

        tags.append(("cart", results[1]))
        new_wav.cart = results[1]
    else:
        if cat is not None:
            tags.append(("cat", cat))
            new_wav.category = cat
        if cart is not None:
            tags.append(("cart", cart))
            new_wav.cart = cart

    if artist is not None:
        tags.append(("artist", artist))
        new_wav.artist = artist

    if title is not None:
        tags.append(("title", title))
        new_wav.title = title

    msg.vprint(f"creating file {copy} with cart chunk tags:")
    for tag in tags:
        msg.vprint(f"{tag[0]}:\t\t{tag[1]}")

    new_file = wav.write_copy(new_wav)
    msg.vprint(f"file saved as {new_file}")
