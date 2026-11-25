#!/usr/bin/env python3
"""news-image-20261125: publish the bundled 25 November 2026 news image.

The repository ships entry.png, a 1024x1024 picture summing up the
day's world news. This program copies those exact bytes to the output
directory. It performs no network access, reads no clock and uses no
randomness, so repeated runs always produce the same output.
"""

import hashlib
import os
import struct
import sys
from pathlib import Path

IMAGE_FILENAME = "entry.png"
MAX_IMAGE_BYTES = 1_048_576
DEFAULT_OUTPUT = "/output"
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024

# Accepted file types, keyed by their leading magic bytes.
SIGNATURES = {
    b"\x89PNG\r\n\x1a\n": "PNG",
    b"\xff\xd8\xff": "JPEG",
}


class EntryError(Exception):
    """A problem with the bundled image or the output location."""


def read_bundled_image():
    """Read and validate the bundled image; return (bytes, kind)."""
    image_path = Path(__file__).resolve().parent / IMAGE_FILENAME
    if not image_path.is_file():
        raise EntryError(f"bundled image {IMAGE_FILENAME} is missing")
    payload = image_path.read_bytes()
    if not payload:
        raise EntryError(f"bundled image {IMAGE_FILENAME} is empty")
    if len(payload) > MAX_IMAGE_BYTES:
        raise EntryError(f"bundled image {IMAGE_FILENAME} exceeds 1 MiB")
    kind = next(
        (label for magic, label in SIGNATURES.items()
         if payload.startswith(magic)),
        None,
    )
    if kind is None:
        raise EntryError(f"bundled image {IMAGE_FILENAME} is not PNG or JPEG")
    if kind == "PNG":
        check_png_dimensions(payload)
    digest = hashlib.sha256(payload).hexdigest()[:16]
    print(f"bundled image is {kind}, {len(payload)} bytes, sha256 {digest}")
    return payload, kind


def check_png_dimensions(payload):
    """Confirm a PNG is the required 1024x1024 from its IHDR chunk."""
    if len(payload) < 33 or payload[12:16] != b"IHDR":
        raise EntryError("bundled PNG has no readable IHDR chunk")
    width, height = struct.unpack(">II", payload[16:24])
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        raise EntryError(
            f"bundled PNG is {width}x{height}, expected "
            f"{EXPECTED_WIDTH}x{EXPECTED_HEIGHT}"
        )


def output_directory():
    """Resolve the output directory, creating it when needed."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT))
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        raise EntryError(f"cannot create output directory {out_dir}: {exc}")
    return out_dir


def write_output(payload):
    """Write the image to the output directory and verify the copy."""
    target = output_directory() / IMAGE_FILENAME
    try:
        target.write_bytes(payload)
    except OSError as exc:
        raise EntryError(f"cannot write {target}: {exc}")
    written = target.read_bytes()
    if len(written) != len(payload):
        raise EntryError("output image has the wrong size")
    if hashlib.sha256(written).hexdigest() != hashlib.sha256(payload).hexdigest():
        raise EntryError("output image differs from the bundled image")
    digest = hashlib.sha256(written).hexdigest()[:16]
    print(f"wrote {target} ({len(written)} bytes, sha256 {digest})")


def main():
    try:
        payload, _kind = read_bundled_image()
        write_output(payload)
    except EntryError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
