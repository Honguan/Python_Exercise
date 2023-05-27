from pathlib import Path
import tempfile
import tarfile
import os

import zstandard  
# pip install zstandard



def extract_zst(archive: Path, out_path: Path):
    
    if zstandard is None:
        raise ImportError("pip install zstandard")

    archive = Path(archive).expanduser()
    out_path = Path(out_path).expanduser().resolve()
    # need .resolve() in case intermediate relative dir doesn't exist

    dctx = zstandard.ZstdDecompressor()

    with tempfile.TemporaryFile(suffix=".tar") as ofh:
        with archive.open("rb") as ifh:
            dctx.copy_stream(ifh, ofh)
        ofh.seek(0)
        with tarfile.open(fileobj=ofh) as z:
            z.extractall(out_path)

# Input the archive file path and output directory path
archive_file = input(r"Enter the path to the .zst file: ")
output_dir = input(r"Enter the output directory path: ")

# Extract the .zst file
extract_zst(archive_file, output_dir)