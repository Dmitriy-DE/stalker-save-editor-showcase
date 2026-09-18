"""Sanitised illustrative binary-container parser."""

from __future__ import annotations

from dataclasses import dataclass
import struct


@dataclass(frozen=True)
class Header:
    magic: bytes
    version: int
    payload_size: int


def parse_header(data: bytes) -> Header:
    if len(data) < 12:
        raise ValueError("container is too short")

    magic, version, payload_size = struct.unpack_from("<4sII", data, 0)

    if magic not in {b"SAVE", b"GVAS"}:
        raise ValueError("unsupported container")

    if payload_size > len(data) - 12:
        raise ValueError("declared payload exceeds file boundary")

    return Header(magic=magic, version=version, payload_size=payload_size)
