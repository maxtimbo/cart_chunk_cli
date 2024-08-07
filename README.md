# cart_chunk_cli

A command-line interface for [python_cart_chunk](https://github.com/maxtimbo/python_cart_chunk/tree/main).

> [!NOTE]
> Only `title`, `artist`, `cart`, and `category` are currently supported.

## Installation

Clone this repository and install using pip:

```
git clone https://github.com/maxtimbo/cart_chunk_cli.git
pip3 install .
```

## Usage

If the filename is already **CAT**_CART_.wav then you can use the `--from_filename` flag:

```
$ cart_chunk_cli NEW1234.wav --from_filename
```

Use `-v` or `--verbose` to get verbose output.

Additionally, you can supply `cat`, `cart`, `title`, and `artist`:

```
$ cart_chunk_cli Some_random_audio.wav --cat CAT --cart 1234
```

or

```
$ cart_chunk_cli NEW1234.wav --title "News from TV" --artist "John McNewsFace"
```

```
$ cart_chunk_cli --help
Usage: cart_chunk_cli [OPTIONS] FILENAME

Options:
  -v, --verbose    enable verbose mode
  --from_filename  get cat/cart from filename
  --cat TEXT       set category
  --cart TEXT      set cart
  --artist TEXT    set artist
  --title TEXT     set title
  --help           Show this message and exit.
```
