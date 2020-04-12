from pathlib import Path
from zipfile import *

from os import PathLike
from typing import Union


def build_engine_archive(zip_name: str, source_dir: Union[str, PathLike]):
    src_path = Path(source_dir).expanduser().resolve(strict=True)
    with ZipFile(zip_name, "w", ZIP_DEFLATED) as zf:
        for file in src_path.rglob("*"):
            zf.write(file, file.relative_to(src_path.parent))
