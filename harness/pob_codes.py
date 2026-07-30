#!/usr/bin/env python3
"""Encode/decode Path of Building import codes.

A PoB import code is base64url( zlib( build XML ) ).

Usage:
  pob_codes.py encode build.xml            # prints import code
  pob_codes.py decode CODE_OR_FILE         # prints XML
"""
import base64
import sys
import zlib
from pathlib import Path


def encode(xml_bytes: bytes) -> str:
    return base64.urlsafe_b64encode(zlib.compress(xml_bytes, 9)).decode("ascii")


def decode(code: str) -> bytes:
    return zlib.decompress(base64.urlsafe_b64decode(code.strip()))


def main() -> None:
    if len(sys.argv) != 3 or sys.argv[1] not in ("encode", "decode"):
        sys.exit(__doc__)
    mode, arg = sys.argv[1], sys.argv[2]
    if mode == "encode":
        print(encode(Path(arg).read_bytes()))
    else:
        code = Path(arg).read_text() if Path(arg).exists() else arg
        sys.stdout.write(decode(code).decode("utf-8"))


if __name__ == "__main__":
    main()
