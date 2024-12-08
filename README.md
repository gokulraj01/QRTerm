# QRTerm
QRTerm is a command-line application that generates QR codes. It takes raw/ASCII data as input and outputs the QR code in various formats, including displaying it directly on the screen, saving it to a file, or printing it to the terminal.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/gokulraj01/QRTerm.git
   ```
2. You can use `pip` to directly install the package from the root directory
    ```bash
    pip install .
    ```

## Run locally
Since this is a module, you can use:
```bash
python -m src.qrterm <parameters>
```

## Building qrterm
This project uses Python's standard build tools(`setuptools`).

1. **Build the distribution:**
   ```bash
   python -m build
   ```

2. **Install from the wheel:**
    ```bash
    pip install dist/qrterm-*.whl
    ```

After these steps, the qr command should be available in your terminal.

You can test the installation by running:
```bash
qr --help
```

## Usage

### Options

*   `-o`, `--output <file>`: Output file path. If not specified, the QR code will be printed to the console.
*   `-i`, `--input <file>`: Input file path. If specified, the data will be read from this file.
*   `-s`, `--screen`: Display QR code in full screen.
*   `--gui`: Take the input data from a GUI (default behavior if no input is provided).
*   `<data>`: Data to encode in the QR code (can be provided directly as a command-line argument).


## Examples

**Use the GUI to input data:**
```bash
qr
```

**Encode data from the command line:**
```bash
qr "Hello, world!"
```

**Encode data from a file:**
```bash
qr -i input.txt
```

**Save QR code to a file:**
```bash
qr -o output.png "Hello, world!"
```

**Display QR code in full screen:**
```bash
qr -s "Hello, world!"
```

> Note: `--output` and `--screen` cannot be used together. If no input is provided via `-i`, `--input` or `<data>`, the GUI will automatically launch.